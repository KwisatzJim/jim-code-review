#!/usr/bin/env python3
"""Execute independent-run ground truth, outside the reviewer's visible fixture."""
import importlib.util
import json
from pathlib import Path
import sqlite3
import subprocess
import sys

sys.dont_write_bytecode = True
root = Path(sys.argv[1]).resolve()
results = []

def module(filename):
    spec = importlib.util.spec_from_file_location(filename.replace('.', '_'), root / filename)
    loaded = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(loaded)
    return loaded

def check(case, assertion):
    assertion()
    results.append({'case': case, 'witness_passed': True})

def expect(actual, expected):
    assert actual == expected, (actual, expected)

def database():
    db = sqlite3.connect(':memory:')
    db.executescript("CREATE TABLE notes(id INTEGER PRIMARY KEY,title TEXT); INSERT INTO notes VALUES(1,'one'),(2,'two');")
    return db

for filename, expected in [('module_14.py', []), ('module_46.py', [(1,), (2,)])]:
    db = database()
    try:
        check(filename, lambda: expect(module(filename).apply(db, "' OR 1=1 --"), expected))
    finally:
        db.close()

for filename, expected in [('module_27.py', ['first', 'second']), ('module_52.py', ['second'])]:
    fn = module(filename).apply
    fn('first')
    check(filename, lambda: expect(fn('second'), expected))

for filename, expected in [('module_31.py', [('one',), ('two',)]), ('module_68.py', [('new',), ('two',)])]:
    db = database()
    try:
        db.execute("CREATE TRIGGER reject_two BEFORE UPDATE ON notes WHEN old.id=2 BEGIN SELECT RAISE(ABORT,'injected failure'); END")
        try:
            module(filename).apply(db, 'new')
        except sqlite3.IntegrityError:
            pass
        else:
            raise AssertionError('Expected injected update failure')
        check(filename, lambda: expect(db.execute('SELECT title FROM notes ORDER BY id').fetchall(), expected))
    finally:
        db.close()

script = '''
import assert from 'node:assert/strict';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
const root=process.argv[1];
const results=[];
const submitted={id:1,content:'old',modified_at:1};
const saved={...submitted,modified_at:2};
const current={id:1,content:'new',modified_at:1};
for(const [name,expected] of [['module_19.mjs','new'],['module_73.mjs','old']]) {
 const {apply}=await import(pathToFileURL(path.join(root,name)));
 assert.equal(apply(current,submitted,saved).content,expected);
 results.push({case:name,witness_passed:true});
}
for(const [name,expected] of [['module_84.mjs',3],['module_95.mjs',0]]) {
 const {apply}=await import(pathToFileURL(path.join(root,name)));
 assert.equal(apply([1,2,3],0).length,expected);
 assert.deepEqual(apply([1,2,3],2),[1,2]);
 assert.deepEqual(apply([1,2,3],null),[1,2,3]);
 results.push({case:name,witness_passed:true});
}
console.log(JSON.stringify(results));
'''
completed = subprocess.run(['node', '--input-type=module', '-e', script, str(root)], capture_output=True, text=True, check=True, timeout=20)
results.extend(json.loads(completed.stdout))
print(json.dumps({'checks': results, 'passed': len(results), 'total': 10}, indent=2))
