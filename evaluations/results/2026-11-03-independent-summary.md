# Independent validation — 2026-11-03

The reviewer found all five known defects, missed none, and raised no findings against the five safe examples. All ten ground-truth witnesses passed. No skill changes were made.

## Method

A fresh subagent was created with `fork_turns=none`, so it did not inherit the development conversation, prior self-check, or answer key. Its request supplied only the copied skill path and a disposable repository containing ten uncommitted modules, repository instructions, and behavior contracts. It was told to read only that repository and skill, make no changes, install nothing, contact no services, and not delegate.

Files and functions used neutral names. The reviewer was not given the expected number, locations, or types of findings. The prewritten answer key remained outside its permitted scope. This separation was instruction-based; a separate operating-system filesystem sandbox was not established. The reviewer inherited the parent model; its exact identifier/settings were not exposed. This tests independent context, not a different model family.

The corpus included four defective/safe pairs adapted from earlier examples (Python mutable defaults, SQLite transactions and query parameters, and JavaScript delayed save acknowledgment). A new pair tested explicit zero pagination limits versus default limits. That holdout was new to the skill's evaluation corpus, not evidence that the model had never encountered the programming pattern before.

The reviewer report was preserved before scoring. The parent matched the reported causes and triggers against the prewritten answer key and independently executed witness checks. This was manual semantic scoring, not a count based on matching prose or headings.

## Results

| Measure | Result |
| --- | --- |
| Known defective modules | 5 |
| Correctly identified defects | 5 |
| Missed known defects | 0 |
| Safe modules | 5 |
| Safe modules incorrectly flagged | 0 |
| Unmatched findings needing further triage | 0 |
| New holdout defect found | 1 of 1 |
| New holdout safe case incorrectly flagged | 0 of 1 |
| Ground-truth witness checks | 10 of 10 passed |

The five findings were: committed partial database updates, stale save responses replacing newer text, interpolated SQL changing a lookup predicate, shared mutable default state, and zero limits being replaced by a nonzero default.

Two findings were rated High, whereas analogous earlier self-check findings were Medium. Severity was not scored because no application-level impact baseline was predefined for these small utilities. Finding detection was consistent; severity calibration remains an area for a future real-world evaluation. The evidence does not justify automatically editing the skill.

## Artifacts and repeatability

- [Raw reviewer output](2026-11-03-independent-raw.md)
- [Scored results and skill/target hashes](2026-11-03-independent-run.json)
- [Pre-review setup and answer key](2026-11-03-independent-setup.json)
- [Witness execution results](2026-11-03-independent-witnesses.json)
- [Archived target contracts](../independent-01/target/README.md)

Run the witnesses against the archived targets from the project root:

```sh
python3 evaluations/verify_independent.py evaluations/independent-01/target
```

These checks reproduce the expected behaviors, including intentional failures; passing them is not a claim that every target is correct. They use in-memory SQLite and pure JavaScript functions, do not install dependencies, and disable Python bytecode output. The scripts do not perform another model review.

To repeat the blind review, prepare a fresh disposable Git repository with the archived README and AGENTS committed first, and the ten neutral modules as untracked additions. Supply only that repository and the skill to a fresh reviewer; do not supply this summary, answer key, witness script, or prior report. Save its output before scoring. The temporary path and Git commit in the original setup file document the original execution; the archived targets and hashes survive temporary-directory cleanup.

## Verification and limits

Parent witnesses ran with Python 3.15.2 and Node 26.13.0. The reviewer also reported focused executions. Minimum supported runtime versions were not separately exercised. Target hashes, copied skill hashes, original skill hashes, fixture HEAD, tracked diff, index diff, and untracked-file inventory were checked after the review; all remained consistent with the setup.

This is one reviewer execution over tiny synthetic modules, with parent-authored contracts and parent scoring. It provides no statistical accuracy guarantee, no comparison against Codex without the skill, and no measured improvement attributable to the skill. Rust, Swift, Tauri, PR mode, native interfaces, platform packaging, and large-repository review remain outside this run. No project source or skill guideline was changed as a result.
