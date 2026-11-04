# Tauri 2

Load when changes cross the webview/native boundary or affect Tauri configuration and packaging. Read manifests, command registration, capability files, plugin configuration, and actual callers selectively.

- Trace frontend-controlled command arguments into native operations. Check validation and authorization where the privileged action occurs; do not assume a UI confirmation alone restricts command callers.
- Verify the actual capability/permission model for the command or plugin before declaring access allowed or denied. Do not assume plugin permissions automatically govern every custom command.
- Keep secrets out of command responses, frontend state, logs, and exception strings. Check the platform credential backend and its failure behavior.
- Trace blocking native work, shared application state, cancellation, and reentrant commands against the runtime and existing coordination. Establish the harmful overlap rather than flagging every synchronous command.
- Review webview navigation/content policy, external openers, filesystem access, and packaging only for implemented operations and supported targets. Browser-only development cannot prove native command behavior.
