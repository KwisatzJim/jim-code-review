# React, TypeScript, and JavaScript

Load for frontend or JavaScript/TypeScript changes. Inspect framework versions and whether code runs in a browser, native webview, or Node environment.

- Trace asynchronous results against the identity and version of the state they modify. Check rapid edits, selection changes, repeated submissions, and out-of-order responses for lost updates or wrong-item changes.
- Examine effects, subscriptions, and cleanup for a demonstrated stale closure, duplicate side effect, or leak. Missing memoization and dependency-array differences are investigation leads, not automatic bugs.
- Types do not validate external JSON, IPC responses, or stored data at runtime. Trace untrusted or malformed values to a concrete consumer and failure; do not require duplicate validation of already-validated internal values.
- Check error paths and optimistic updates: a failed save must not silently appear durable or overwrite newer edits. Verify rollback uses the correct state version.
- For rendering and URLs, establish which content is controlled externally and what sanitization, escaping, navigation, or fetch behavior the actual renderer provides. Do not report injection based solely on a string containing markup.
