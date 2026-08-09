# Backups — where everything lives, and how to get it back

Three independent copies, one of them offsite, verified by actually restoring.

| # | Copy | Where | Refreshed |
|---|---|---|---|
| 1 | **GitHub** (offsite) | `between-sundays/workspace` (public) · `between-sundays/state` (private) | every push |
| 2 | **Local mirrors** | `~/Backups/bts/mirrors/*.git` — full clones, every branch and tag | hourly |
| 3 | **Dated bundles** | `~/Backups/bts/bundles/<repo>-YYYY-MM-DD.bundle` — one self-contained file per repo per day, 45-day retention | hourly |

Plus `~/Backups/bts/keys/` — the agent keys and the GitHub token, which are **not
in git** and cannot be regenerated from it. That directory is `chmod 700`.

## It runs itself

A user LaunchAgent, `com.betweensundays.backup`, runs `tools/backup.sh` **every
hour and at login**. Log: `~/Backups/bts/backup.log`.

```bash
launchctl list | grep betweensundays          # is it loaded?
tail -20 ~/Backups/bts/backup.log             # what did it do?
~/Projects/bts-workspace/tools/backup.sh      # run it right now
```

To stop it: `launchctl unload ~/Library/LaunchAgents/com.betweensundays.backup.plist`

## Getting it back

From a bundle — a single file, no server, no network:

```bash
git clone ~/Backups/bts/bundles/workspace-2026-08-09.bundle recovered
```

From a mirror:

```bash
git clone ~/Backups/bts/mirrors/workspace.git recovered
```

**This was tested, not assumed** — the state bundle was cloned back and returned
all 98 commits and every file.

## What is deliberately *not* covered

- Vercel needs nothing backed up; it rebuilds from GitHub on every push.
- The environment variables (`AGENT_KEYS`, `GITHUB_TOKEN`, `STATE_REPO`) live in
  Vercel and in `~/.config/bts-workspace/`. Copy 3 covers the second.
- Bundles older than 45 days are pruned. Mirrors keep full history forever.
