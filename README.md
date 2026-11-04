# jim-code-review

A reusable Codex skill for project-aware, evidence-based code review. One structured review uses five perspectives: correctness, security, architecture, performance/reliability, and platform compatibility. It challenges candidate findings before reporting them and leaves source files unchanged unless a fix is requested.

Start with [installation for Linux/macOS](docs/installation.md), then [usage examples](docs/usage.md). The skill entry point is [SKILL.md](skills/jim-code-review/SKILL.md). You can invoke it by absolute path before installing anything.

## Included

- Git uncommitted/staged/commit/range review, whole-file/directory review, and GitHub PR review when read tools are available.
- Selectively loaded Rust, Swift/SwiftUI, TypeScript/JavaScript/React, Python, Tauri 2, SQLite, and shell guidance.
- Simple Markdown [project rules](skills/jim-code-review/references/project-rules.md) for repository-specific guidance.
- A small [evaluation corpus](evaluations/README.md), recorded [controlled results](evaluations/results/2026-11-02-controlled-review.md).
- [Maintenance and validation status](docs/maintenance.md) and [attribution](ATTRIBUTION.md).

No runtime scripts, paid APIs, cloud service, or dependencies beyond the coding agent and scope-appropriate access are required. Git is needed for Git modes; Python/Node are only needed for optional evaluation checks. Zed, Vim, and Fish work without special integration.

## Current limits

The first evaluation was a known-answer self-check. A subsequent [fresh-context blind run](evaluations/results/2026-11-03-independent-summary.md) found all five planted bugs with no findings against five safe cases; this small run is not a broad accuracy guarantee. File/directory and PR instructions have not been independently evaluated. Both metadata files passed YAML parsing; the bundled Python skill validator remains unavailable without PyYAML.

## License

[MIT License](LICENSE), copyright 2026 KwisatzJim. See [attribution](ATTRIBUTION.md) for the upstream design inspiration.
