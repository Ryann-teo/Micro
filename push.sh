#!/usr/bin/env bash
# Initialise (or update) the local git repo and push to GitHub.
# Run this from the Website/ folder.

set -euo pipefail

REPO="https://github.com/Ryann-teo/Micro.git"
BRANCH="main"

if [ ! -d ".git" ]; then
  git init
  git branch -M "$BRANCH"
  git remote add origin "$REPO" || true
else
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "$REPO"
  fi
fi

git add -A
git commit -m "Core Micro study guide (Phase 1: 173 concept stubs with intuition)" || echo "No changes to commit."

# Push. May prompt for GitHub credentials or use cached gh CLI token.
git push -u origin "$BRANCH"

echo ""
echo "Done."
echo "Open https://github.com/Ryann-teo/Micro/settings/pages and set Source to:"
echo "  Branch: main  /  Folder: / (root)"
echo "The live site will then be at https://ryann-teo.github.io/Micro/"
