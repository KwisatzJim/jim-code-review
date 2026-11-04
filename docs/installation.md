# Install for Linux or macOS

The skill is a folder of instructions; it does not run a background service. Codex and access to the code are required. Git is required for Git review modes. Python and Node are needed only to run the optional evaluation scripts. Zed, Vim, and Fish require no special integration.

## First try: no installation

Ask Codex to read the actual absolute entry-point path. Replace the example paths with your local paths:

> Use the jim-code-review skill at /absolute/path/to/jim-code-review/skills/jim-code-review/SKILL.md to review all uncommitted changes in /absolute/path/to/repository. Return findings here and do not change files.

Replace both the skill and target repository paths. This works without claiming automatic skill discovery has been verified.

## Install once for all your repositories

Current [official skill documentation](https://learn.chatgpt.com/docs/build-skills) lists `~/.agents/skills` for user-wide discovery and supports symlinked folders. Instructions were checked on 2026-11-03. Some bundled creator/installer guidance still uses `~/.codex/skills`; use one discovered installation rather than duplicating both. Check your installed Codex's discovery if it differs from current documentation.

Keep the project at a stable location. Run the following in Fish, Bash, or Zsh, replacing the source path with this project's location on that machine:

```sh
mkdir -p "$HOME/.agents/skills"
ln -s "/absolute/path/to/jim-code-review/skills/jim-code-review" "$HOME/.agents/skills/jim-code-review"
```

Before running it, check whether `~/.agents/skills/jim-code-review` already exists. If it does, inspect its target/content and preserve it; do not add `-f` or overwrite an existing installation. No `sudo` is needed. The source volume must be mounted for a symlink to work.

A symlink is a directory entry pointing to the source folder: approved edits to this project become available through that link. For a separate installation instead, copy the whole `jim-code-review` folder, including references and `agents`, into the user skills directory. A copied installation must be updated deliberately; do not keep a second discovered copy with the same name.

## Verify discovery

Start a new Codex chat/session. In CLI or an IDE extension, use `/skills` or type `$` to select `jim-code-review`; in the desktop Skills view, look for Jim Code Review. If it is absent, restart Codex and verify the link resolves to a folder containing `SKILL.md`. Check the installed version's skill paths and disabled-skill configuration before changing settings. Exact-path invocation above remains available for troubleshooting.

Try a small review and verify it identifies the intended scope and loads the actual skill. Merely creating a symlink does not prove Codex discovered it. Automatic selection remains enabled by default; explicit `$jim-code-review` prompts give a clear invocation.

## Repository-local alternative

For a team-owned installation, place the complete skill folder at `<repository>/.agents/skills/jim-code-review/`. This changes that repository and should be a deliberate project decision. Team installations should use portable checked-in content rather than a link to your personal disk. Avoid duplicate user/repository skill names.

## Updates and removal

For a symlink, review edits in the source project, run relevant checks, then open a new session and confirm discovery. For a copy, review changes before replacing the installed folder and preserve the previous copy outside discovered locations if rollback is needed.

To remove a symlink installation, inspect it with `ls -ld "$HOME/.agents/skills/jim-code-review"`; only if it is the intended symlink, run `unlink "$HOME/.agents/skills/jim-code-review"`. That removes the link, not the source folder. Do not use this instruction for a copied directory. Restart Codex if its discovery view remains stale.
