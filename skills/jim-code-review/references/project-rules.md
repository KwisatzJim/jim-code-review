# Selecting project and language rules

Read applicable `AGENTS.md` instructions first. Then load relevant project documentation and an explicitly supplied review profile or repository `.code-review.md` if present. Do not create configuration in the reviewed repository. An external profile must identify its repository; never apply one project’s profile to another project just because the technology matches.

## Language routing

Use the changed paths, manifests, imports, and affected boundaries. Load only the relevant guides; a change crossing boundaries can need more than one. Follow the dependency path when a changed file's extension alone is insufficient.

| Evidence | Guide |
| --- | --- |
| Rust source or Rust manifest affecting behavior | [Rust](languages/rust.md) |
| Swift/SwiftUI source or Apple deployment changes | [Swift](languages/swift.md) |
| React, JS/TS, browser or Node code | [React/TypeScript/JavaScript](languages/react-typescript.md) |
| Python source or Python package/runtime changes | [Python](languages/python.md) |
| SQL/schema/database/backup/restore behavior | [SQLite](languages/sqlite.md) |
| Tauri command, plugin, webview, capability, packaging boundary | [Tauri 2](languages/tauri.md) |
| Shell scripts or generated shell commands | [Shell](languages/shell.md) |

These guides are investigation prompts, not proof of a defect. Confirm version-sensitive API claims from the actual dependency and authoritative documentation when necessary.

## Resolving rules

Apply shared evidence standards, then relevant language guidance, then repository-specific behavior and conventions. Project-specific choices override general recommendations where appropriate; they do not waive authorization boundaries or make a demonstrated security/data-integrity failure harmless. Explain material conflicts rather than silently picking a rule. Within repository instructions, respect directory scope and instruction precedence. Do not use an optional review profile to bypass `AGENTS.md` or the user's request.

Distinguish documented requirements, observed implementation, and proposed safeguards. A profile is a review aid, not proof of current behavior. Recheck its source pointers at the reviewed revision, especially when reviewing history. If behavior legitimately changed, use the revised contract; do not report deviation from a stale profile as a bug.

## Optional project profile template

Use Markdown, without a configuration parser. Useful fields are:

- Repository identity and revision/date inspected.
- Relevant languages, declared targets, and entry points.
- Implemented workflows and explicitly deferred features.
- Important invariants with stable short rule IDs, applicability, and source pointers.
- Verification commands, side effects, and checks that require isolated data.
- Known uncertainty and sources to recheck.

Keep repository facts outside the reusable skill. Record only context useful for review, excluding private data, credentials, and copied sensitive source. Updating a profile is separate authorized work, not an automatic consequence of reviewing code.
