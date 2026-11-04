# Maintenance and acceptance

Keep improvements small and evidence-based. After a confirmed bug or false positive, record the reviewed revision, minimal trigger, finding, disposition, and evidence in a new local evaluation result. Exclude credentials, user data, private source, and identifying information. Prefer synthetic examples reproducing the same failure mechanism. Do not overwrite old results or silently rewrite historical run hashes.

For a guideline change, explain which failure it addresses and obtain approval. Add the smallest useful example and a correct counterpart, run the witness checks, then compare review decisions on the same cases plus an unseen example. Do not automatically rewrite the skill. Record the exact skill fingerprint and model identifier when available; model changes can affect results independently of guidelines.

The [evaluation procedure](../evaluations/README.md) provides commands, case labels, comparison instructions, and blind-run guidance. The first run was author-visible. A subsequent [independent-context run](../evaluations/results/2026-11-03-independent-summary.md) found five of five planted defects and raised no findings against five safe examples, including a new pagination pair. This is one small blind run, not a general accuracy benchmark. The synthetic witnesses cover Python/SQLite/JavaScript, not every supported technology. Git scope checks exercise commands, not Codex discovery or every review decision.

## Validation status

As of 2026-11-03:

- Package entry point, five shared perspectives, relevant language/framework guides, and external project rules are present.
- Usage covers all requested modes, including file/directory and read-only GitHub PR review. These two newly added modes are instruction-based and not independently behavior-tested.
- Recorded synthetic checks include 6 Python witnesses, 2 JavaScript witnesses, and 1 disposable Git scope test.
- Local link, metadata-presence, and unfinished-template checks passed. Ruby’s YAML parser also successfully parsed the skill frontmatter and UI metadata. The bundled `quick_validate.py` could not run because the available Python lacks PyYAML. These limited checks are not a replacement for YAML parsing or discovery testing. No dependency was installed to resolve this.

When PyYAML is available in a chosen development environment, run the bundled skill-creator's `scripts/quick_validate.py` against `skills/jim-code-review`. This validator is a development tool and not a runtime dependency of the review skill. Do not invent a validator installation path on another machine; locate its actual bundled skill first.

The initial deliverables are packaged for reuse, with the limitations above. The standalone 0.1.0 release is approved for publication under MIT. Packaging as a public plugin and further automated multi-agent evaluations remain separate decisions. Attribution is recorded in [ATTRIBUTION.md](../ATTRIBUTION.md); no upstream scripts or source fixtures are distributed here.
