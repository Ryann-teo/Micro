#!/usr/bin/env bash
# Rebuild the Core Micro website from concepts_data.py + phase2_content.py,
# then push the changes to GitHub.
#
# Use this after editing either data file.

set -euo pipefail

REPO="https://github.com/Ryann-teo/Micro.git"
BRANCH="main"

# Move to the folder this script lives in
cd "$(dirname "${BASH_SOURCE[0]}")"

echo ""
echo "=== Core Micro website update ==="
echo "Folder:  $(pwd)"
echo ""

# Check Python
if ! command -v python3 >/dev/null 2>&1; then
  if command -v python >/dev/null 2>&1; then
    PY=python
  else
    echo "ERROR: python3 not found on PATH." >&2
    exit 1
  fi
else
  PY=python3
fi

# Check git
if ! command -v git >/dev/null 2>&1; then
  echo "ERROR: git not found on PATH. Install Git from https://git-scm.com/." >&2
  exit 1
fi

# 1. Rebuild
echo "Step 1: rebuilding index.html and assets..."
"$PY" build_site.py

# 2. Init or update git repo
if [ ! -d ".git" ]; then
  echo ""
  echo "Step 2: initialising git repo..."
  git init
  git branch -M "$BRANCH"
  git remote add origin "$REPO" || true
else
  echo ""
  echo "Step 2: existing git repo found, syncing remote..."
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "$REPO"
  else
    git remote set-url origin "$REPO"
  fi
fi

# 3. Stage + commit + push
echo ""
echo "Step 3: staging changes..."
git add -A

if git diff --cached --quiet; then
  echo "No changes to commit. Skipping push."
  exit 0
fi

COMMIT_MSG="Update Core Micro study guide ($(date -u +%Y-%m-%d))"
git commit -m "$COMMIT_MSG"

echo ""
echo "Step 4: pushing to $BRANCH..."
if ! git push -u origin "$BRANCH"; then
  echo ""
  echo "Plain push failed. Retrying with --force (overwrite remote)..."
  git push -u origin "$BRANCH" --force
fi

echo ""
echo "=== Update complete ==="
echo ""
echo "Live site: https://ryann-teo.github.io/Micro/"
echo "If GitHub Pages is not yet enabled, go to:"
echo "  https://github.com/Ryann-teo/Micro/settings/pages"
echo "and set Source = Branch: main, Folder: / (root)."
