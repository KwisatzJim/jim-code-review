# Controlled review — 2026-11-02

## Scope and method

Targets: the eight named synthetic functions in `evaluations/cases/python_cases.py` and `evaluations/cases/save_cases.mjs`, including their explicit behavior contracts. Shared, Python, SQLite, and JavaScript guidance was applied. This is a source-level self-check in the skill-authoring session, with known answers visible, not an independent Codex invocation or an end-to-end Git review. Model identifier/settings were not exposed to this run. No source fixes were applied.

Four actionable defects match the four known buggy cases. None of the four safe counterparts warranted a finding within the stated fixture contracts. No known defect was missed in this self-check. Those counts do not establish an unbiased precision/recall estimate.

## Findings

### Medium — Calls unexpectedly share labels (PY-DEFAULT)

Location: `cases/python_cases.py:5`.

Problem/trigger: call `append_label('first')`, then `append_label('second')`, omitting the list both times. The second call returns both labels despite the documented independent-call behavior. The default list is retained between calls.

Evidence: the Python witness executed this sequence and observed `['first', 'second']`. Correction: use an omitted-value sentinel and create a list per call, as in the safe counterpart. Guidance: Python shared mutable defaults. Medium reflects incorrect cross-call results; no application-level security impact is assumed.

### Medium — Failure leaves half the rename committed (DB-ATOMIC)

Location: `cases/python_cases.py:22`.

Problem/trigger: the first update commits, then updating row 2 fails. The function promises both rows change or neither does, but row 1 stays renamed.

Evidence: an in-memory SQLite trigger rejected the second update. The witness observed `('new', 'two')`; the transaction counterpart retained `('one', 'two')`. Correction: enclose both updates in one transaction, rolling back on failure. Guidance: SQLite all-or-nothing operations.

### Medium — A title can change the lookup predicate (DB-QUERY)

Location: `cases/python_cases.py:36`.

Problem/trigger: a title containing `' OR 1=1 --` becomes SQL syntax rather than an exact title. This returns both rows. Ordinary quotes can also cause a query error.

Evidence: the in-memory witness returned IDs 1 and 2 for that input, while the bound version returned none. Correction: bind the title parameter. Guidance: SQLite query construction and Python external-input tracing. Medium reflects the demonstrated lookup failure; the fixture does not establish a sensitive multi-user system or justify an invented High-severity exposure claim.

### Medium — Save acknowledgment discards a newer edit (JS-STALE)

Location: `cases/save_cases.mjs:3`.

Problem/trigger: a save was submitted with text `old`; the user types `new` before the save response arrives. Returning the whole saved snapshot replaces the newer editor value with `old`.

Evidence: the Node witness observed `old` from the unsafe function and `new` from the guarded counterpart. Correction: acknowledge only a matching submitted version, preserving newer state. Guidance: asynchronous state identity/version checks. Medium reflects the demonstrated stale replacement without assuming a full persistence or account model.

## Safe cases and rejected warnings

- A fresh list for each omitted argument prevents cross-call state leakage.
- The SQLite transaction context rolls back the pair after the injected failure.
- Bound SQL handles the attack-shaped title as literal data; no injection finding is justified.
- Guarded acknowledgment retains changed editor text and updates the timestamp for unchanged text. Do not invent a multi-field contract absent from the tiny fixture.

## Executed checks

- Python witness suite: 6/6 passed.
- Node witness suite: 2/2 passed.
- Git scope test: 1/1 passed, covering index/working-tree separation, untracked discovery, unborn HEAD, root commit, historical content, and endpoint versus merge-base differences. Read queries left fixture HEAD/index/status unchanged. Fixture setup intentionally created commits/branches only in a temporary repository.

No Rust/Swift/Tauri tests, fresh-context model evaluation, performance benchmark, or real application interaction was performed. The corpus is small and known-answer; future blind and holdout cases are needed to assess review accuracy.
