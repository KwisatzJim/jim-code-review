# SQLite

Load when changes affect database reads, writes, schema, backup, or restore, regardless of host language.

- Trace operations that must succeed together through transaction boundaries and rollback. A single-statement write need not gain an extra transaction without a demonstrated requirement.
- Check row identity, affected-row handling, uniqueness, and relationships. Parameter binding protects values; dynamically constructed identifiers require a separately established trusted source.
- Review schema initialization/migrations against existing user databases and supported versions. Do not treat a fresh-database test as evidence that upgrades preserve data.
- Check concurrent writers, busy/error handling, and read-modify-write sequences with a concrete interleaving. Verify connection settings and application coordination before recommending a locking mode.
- For backup/restore, inspect snapshot consistency, validation, live companion files, partial failure, overwrite policy, and retained recovery copies. Never test against the user's live database.
- Verify SQLite/library-specific behavior from its actual version and documentation when a finding depends on it. Missing indexes require a realistic query/workload consequence, not a generic demand.
