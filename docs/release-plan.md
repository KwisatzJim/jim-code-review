# First public release — approved publication record

Approved repository: `KwisatzJim/jim-code-review`, public.
Approved tag: `v0.1.0`.
License: MIT, copyright 2026 KwisatzJim. Applied at the repository root and inside the standalone skill folder.

This is a standalone Codex skill package. Public plugin-directory submission is outside this release.

## Publication contents

Include the skill folder, README, attribution, installation/usage/maintenance documentation, synthetic fixtures, witness scripts, and recorded evaluation results. Historical setup paths are sanitized placeholders; they are not installation requirements.

Exclude Finder metadata, Python caches, virtual environments, local release archives, and the original working request `projecplan.md`. The publication archive uses an explicit file inventory. Review the inventory before publishing.

## Release description

jim-code-review 0.1.0 introduces a reusable Codex code-review workflow with five perspectives: correctness, security, architecture, performance/reliability, and platform compatibility.

It supports Git changes, selected files/directories, and read-only GitHub pull-request review when tools are available. Markdown rules combine shared guidance with relevant language/framework and project context. Reports prioritize actionable findings, identify triggers and evidence, and challenge speculative warnings. Source changes and publishing comments require a separate request.

Included guidance covers Rust, Swift/SwiftUI, JavaScript/TypeScript/React, Python, Tauri 2, SQLite, and shell scripting. Linux/macOS installation and usage instructions are included.

A fresh-context validation found five planted defects and raised no findings against five safe examples. All ten executable ground-truth checks passed. This was one small synthetic run, not an accuracy guarantee or evidence that the skill improves upon the underlying model. Runtime/native UI and broad platform coverage remain limited. See the recorded evaluation reports for scope and evidence.

The design credits Asterinas's aster-code-review. Instructions and synthetic examples were independently authored; no Asterinas scripts or source fixtures are included.

## Approval and verification

The user approved the public repository, version 0.1.0, and MIT license on 2026-11-03. The approved publication process includes creating the repository, pushing the versioned source, and uploading a release archive and checksums. Check live GitHub state to verify publication; this document alone is not proof of a successful upload.
