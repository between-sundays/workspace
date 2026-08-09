#!/bin/bash
# Between Sundays — belt, braces and a third pair of braces.
#   1. GitHub                     — offsite, live (between-sundays/workspace + /state)
#   2. Local mirrors              — full clones, every ref, restorable with `git clone`
#   3. Dated bundles              — one file per repo per day, independent of git's object store
# Nothing here deletes anything except bundles older than the retention window.
set -uo pipefail
BK="$HOME/Backups/bts"
LOG="$BK/backup.log"
TOKEN=$(cat "$HOME/.config/bts-workspace/github-token" 2>/dev/null)
KEEP_DAYS=45
mkdir -p "$BK/mirrors" "$BK/bundles" "$BK/keys"
say(){ echo "$(date '+%Y-%m-%d %H:%M:%S') $*" | tee -a "$LOG"; }
DAY=$(date '+%Y-%m-%d')
ok=0; fail=0
for REPO in workspace state; do
  URL="https://x-access-token:${TOKEN}@github.com/between-sundays/${REPO}.git"
  M="$BK/mirrors/${REPO}.git"
  if [ -d "$M" ]; then
    git --git-dir="$M" remote set-url origin "$URL" 2>/dev/null
    git --git-dir="$M" remote update --prune >/dev/null 2>&1 \
      && { say "mirror updated: $REPO"; ok=$((ok+1)); } \
      || { say "MIRROR FAILED: $REPO"; fail=$((fail+1)); continue; }
  else
    git clone --mirror "$URL" "$M" >/dev/null 2>&1 \
      && { say "mirror created: $REPO"; ok=$((ok+1)); } \
      || { say "MIRROR CLONE FAILED: $REPO"; fail=$((fail+1)); continue; }
  fi
  B="$BK/bundles/${REPO}-${DAY}.bundle"
  git --git-dir="$M" bundle create "$B" --all >/dev/null 2>&1 \
    && say "bundle: $(basename "$B") ($(du -h "$B" | cut -f1))" \
    || say "BUNDLE FAILED: $REPO"
done
# The agent keys and PAT are not in git and cannot be regenerated from it.
cp -p "$HOME/.config/bts-workspace/agent-keys.json" "$BK/keys/agent-keys.json" 2>/dev/null
cp -p "$HOME/.config/bts-workspace/github-token"    "$BK/keys/github-token"    2>/dev/null
chmod -R 700 "$BK/keys" 2>/dev/null
find "$BK/bundles" -name '*.bundle' -mtime +$KEEP_DAYS -delete 2>/dev/null
say "done — $ok mirrors ok, $fail failed, $(ls "$BK/bundles" | wc -l | tr -d ' ') bundles, $(du -sh "$BK" | cut -f1) total"
[ "$fail" -gt 0 ] && exit 1 || exit 0
