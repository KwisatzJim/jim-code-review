#!/usr/bin/env python3
"""Verify fixture ground truth, NOT model accuracy. Python standard library only."""
import importlib.util
from pathlib import Path
import sqlite3
import unittest

spec = importlib.util.spec_from_file_location('cases', Path(__file__).parent / 'cases/python_cases.py')
cases = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cases)


class Witnesses(unittest.TestCase):
    def test_mutable_default_exposes_previous_call(self):
        cases.append_label.__defaults__[0].clear()
        cases.append_label('first')
        self.assertEqual(cases.append_label('second'), ['first', 'second'])

    def test_safe_default_is_independent(self):
        cases.append_label_safe('first')
        self.assertEqual(cases.append_label_safe('second'), ['second'])

    def pair(self, function):
        with cases.fixture() as db:
            db.execute("CREATE TRIGGER reject_two BEFORE UPDATE ON notes WHEN old.id=2 "
                       "BEGIN SELECT RAISE(ABORT,'fixture failure'); END")
            with self.assertRaises(sqlite3.IntegrityError):
                function(db, 'new')
            result = db.execute('SELECT title FROM notes ORDER BY id').fetchall()
        db.close()
        return result

    def test_split_commits_leave_partial_update(self):
        self.assertEqual(self.pair(cases.rename_pair), [('new',), ('two',)])

    def test_transaction_rolls_back_pair(self):
        self.assertEqual(self.pair(cases.rename_pair_safe), [('one',), ('two',)])

    def test_interpolated_query_changes_predicate(self):
        db = cases.fixture()
        try:
            self.assertEqual(cases.lookup(db, "' OR 1=1 --"), [(1,), (2,)])
        finally:
            db.close()

    def test_bound_query_keeps_input_literal(self):
        db = cases.fixture()
        try:
            self.assertEqual(cases.lookup_safe(db, "' OR 1=1 --"), [])
        finally:
            db.close()


if __name__ == '__main__':
    unittest.main(verbosity=2)
