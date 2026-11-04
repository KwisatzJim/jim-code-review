# Lightweight review evaluation

This corpus contains synthetic examples only. No user notes, credentials, or private application source is stored in shared fixtures. Python 3 and Node.js are needed for the witness checks; Git is needed for scope checks. No package installation or external API is required.

## Two different kinds of evidence

The witness scripts execute known buggy and safe examples to verify ground truth. A passing witness for buggy code means the defect was reproduced, not that the code is correct. The Git test verifies documented scope commands in a disposable repository; it is not an end-to-end Codex test.

The review reports record the agent's judgments. The first run was a same-session, author-visible self-check, not a blind evaluation. Do not interpret its counts as an independent accuracy estimate. No separate model, subagent, or unattended launcher was used.

## Run the deterministic checks

From the project root:

```sh
PYTHONDONTWRITEBYTECODE=1 python3 evaluations/verify_cases.py
node --test evaluations/verify_save.mjs
PYTHONDONTWRITEBYTECODE=1 python3 evaluations/verify_git_scopes.py
```

The Python witnesses use in-memory SQLite. The Git check creates and deletes a temporary repository, including fixture commits and branch checkouts; it does not change this workspace's Git state. Neither script accesses real app data. Node's built-in test runner executes only the supplied synthetic functions.

## Repeatable review procedure

1. Record a new run ID, date, exact model identifier if available (otherwise “not exposed”), skill file hashes, runtime versions, and review scope. Keep old reports instead of overwriting them.
2. For a less biased run, use a fresh Codex chat that has not seen `expected.json`, witness scripts, or earlier results. Supply the skill and only the target functions with their behavior contracts. Prepare them as uncommitted additions in a disposable Git repository if exercising Git mode. Keep the answer key outside that repository. Separate defective/safe functions and rename them neutrally when doing blind runs so names do not reveal labels.
3. Ask: “Use $jim-code-review to review all uncommitted changes in this disposable fixture repository. Report actionable findings only. Do not modify files or read outside the repository except the supplied skill.” Save the raw review before revealing the answer key. No extra AI execution is required for ordinary skill use; this procedure is for explicit evaluation.
4. Compare each finding semantically against `expected.json`: match the cause and trigger, not wording. Count known bugs found, known bugs missed, safe cases falsely flagged, and unrelated findings separately. Treat an unexpected finding as a candidate requiring validation, not automatically a false positive.
5. Run witnesses and validate disputed findings. Record confirmed bugs, refuted candidates, and remaining uncertainty. For a new case, use a small synthetic reproducer rather than copying private source.
6. Compare only runs with comparable scope/model/settings. Propose guideline changes supported by misses or false positives; obtain approval before changing guidelines, then repeat the same cases plus a fresh holdout example. Never auto-rewrite the skill.

The initial cases cover Python shared defaults, SQLite atomicity and parameter binding, and JavaScript save acknowledgments. Rust, Swift, Tauri, packaging, concurrency, full React behavior, and large-repository recall are not covered by this small corpus. Add cases in response to evidence rather than assuming these examples establish broad reliability.

## Independent run

A fresh-context reviewer subsequently reviewed ten neutrally named modules without receiving the answer key. It found all five planted bugs and flagged none of the five safe cases, including a new zero-limit pagination pair. This is one small blind run, not a broad accuracy guarantee or a comparison against reviewing without the skill.

See the [method, results, and limits](results/2026-11-03-independent-summary.md). The raw report, prewritten key, archived targets, witness results, and hashes are preserved. Reproduce its deterministic ground truth with:

```sh
python3 evaluations/verify_independent.py evaluations/independent-01/target
```
