# Using jim-code-review

After discovery, enter these prompts in Codex, not in your shell. Before discovery, supply the absolute `SKILL.md` path as described in [installation](installation.md). The skill is editor-independent and works with different editor workflows.

| Scope | Prompt |
| --- | --- |
| All uncommitted changes | Use $jim-code-review to review all my uncommitted changes. |
| Staged only | Use $jim-code-review to review only my staged changes. |
| Latest commit | Use $jim-code-review to review the latest commit. |
| Specified commit | Use $jim-code-review to review commit abc1234. |
| Endpoint difference | Use $jim-code-review to review abc1234..def5678. |
| Changes since branch divergence | Use $jim-code-review to review main...HEAD. |
| Whole file | Use $jim-code-review to review the entire file src/saveQueue.ts. |
| Directory | Use $jim-code-review to review src-tauri/src, excluding generated files. |
| GitHub PR | Use $jim-code-review to review https://github.com/OWNER/REPO/pull/123 and return findings here without posting. |

Replace example revisions/paths/URLs with real ones. “All uncommitted” includes the final tracked working-tree state and relevant nonignored untracked files; it does not separately review a staged version later overwritten in the editor. Staged mode uses the index snapshot. `A..B` compares endpoint trees; `A...B` compares the merge base to B. Detailed semantics and coverage limits are in [review modes](../skills/jim-code-review/references/review-modes.md).

PR mode requires available read access. Missing access or truncated patches must be disclosed; posting comments is not part of a review. File/directory mode examines selected current source even without Git. Both modes are newly documented in Phase 5 and have not received independent behavioral evaluation.

## Project-aware review

Applicable `AGENTS.md` instructions and existing architecture/tests are discovered selectively. Optionally provide a `.code-review.md` in the reviewed repository, or supply an external profile explicitly. Creating a repository configuration file is separate work; reviews do not create it automatically.

Example with repository-specific guidance:

> Use $jim-code-review to review the latest commit in /absolute/path/to/repository. Use that repository's .code-review.md as additional project guidance. Recheck its assumptions at the reviewed revision. Do not modify source files.

See the [profile template and precedence](../skills/jim-code-review/references/project-rules.md) before adding project rules.

## Results and fixes

Findings identify severity, location, trigger, evidence, and a recommended correction. They distinguish static reasoning from executed checks. “No actionable findings” means no defects were established within the stated coverage, not a guarantee. Verification gaps stay separate from confirmed findings.

To save a report, explicitly request its destination. Otherwise results stay in chat. To fix one finding, say “Fix the first finding only, explain the change, and run focused verification.” That authorizes the scoped correction; the skill waits for your feedback before another fix. Reviews never automatically install dependencies, change source/Git state, or publish results.

See the [controlled review](../evaluations/results/2026-11-02-controlled-review.md) for a synthetic example of the reporting behavior and its limits.
