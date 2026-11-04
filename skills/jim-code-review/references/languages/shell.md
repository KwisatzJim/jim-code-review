# Shell scripting

Load for scripts or changes that construct shell commands. Identify the actual interpreter from the shebang or invocation: Fish, POSIX shell, Bash, and Zsh syntax are not interchangeable.

- Trace whitespace, wildcard characters, leading dashes, newlines, and hostile text through expansions and argument boundaries. Check quoting and option termination without assuming every unquoted value is exploitable.
- Inspect pipeline and command failure handling under the selected interpreter. Do not prescribe `set -e` or `pipefail` as a universal fix; demonstrate the failure that is ignored.
- Check temporary-file ownership, symlinks, cleanup, and destructive path construction. Prove the wrong target can be reached before reporting data loss.
- For macOS/Linux support, verify the utility and option actually used; do not assume GNU-only flags exist on both. Check executable availability and interpreter version against declared prerequisites.
- Never run an installation, cleanup, or deployment script just to review it. Read its commands and use isolated fixtures if execution is separately safe and authorized.
