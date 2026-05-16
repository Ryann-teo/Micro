@echo off
REM Push the Core Micro website to https://github.com/Ryann-teo/Micro.git
REM Double-click this file, or run it from cmd.exe in this folder.

setlocal

REM Move into the folder this script lives in
cd /d "%~dp0"

set REPO=https://github.com/Ryann-teo/Micro.git
set BRANCH=main

echo.
echo === Core Micro website push ===
echo Folder:  %CD%
echo Remote:  %REPO%
echo Branch:  %BRANCH%
echo.

REM Check git is installed
where git >nul 2>nul
if errorlevel 1 (
  echo ERROR: git is not on PATH. Install Git for Windows from https://git-scm.com/download/win then re-run.
  pause
  exit /b 1
)

REM Init repo if needed
if not exist ".git" (
  echo Initialising new git repo...
  git init
  git branch -M %BRANCH%
)

REM Add or update remote
git remote get-url origin >nul 2>nul
if errorlevel 1 (
  echo Adding remote origin...
  git remote add origin %REPO%
) else (
  echo Updating remote origin...
  git remote set-url origin %REPO%
)

REM Stage everything
echo.
echo Staging files...
git add -A

REM Commit (allow empty so re-runs do not error out)
echo Committing...
git commit -m "Core Micro study guide: 173 concept stubs, 8 topics, 6 question type pages" 2>nul
if errorlevel 1 (
  echo No new changes to commit. Continuing to push in case the remote is behind.
)

REM Push. If the remote already has a default branch (e.g. an empty README on main),
REM the first push may need --force on a fresh repo. We try a normal push first.
echo.
echo Pushing to %BRANCH%...
git push -u origin %BRANCH%
if errorlevel 1 (
  echo.
  echo Plain push failed. This usually means the remote already has commits.
  echo Trying force push to overwrite the remote with this build...
  git push -u origin %BRANCH% --force
)

if errorlevel 1 (
  echo.
  echo Push failed. Common causes:
  echo   1. You are not logged into GitHub. Run: git config --global credential.helper manager-core
  echo   2. The repo does not exist. Create it at https://github.com/new (name: Micro, public).
  echo   3. Your account does not have push access to Ryann-teo/Micro.
  pause
  exit /b 1
)

echo.
echo === Push complete ===
echo.
echo Next: enable GitHub Pages.
echo   1. Open https://github.com/Ryann-teo/Micro/settings/pages
echo   2. Source: Deploy from a branch
echo   3. Branch: main, Folder: / (root)
echo   4. Save. Site will be live in 1-2 minutes at:
echo      https://ryann-teo.github.io/Micro/
echo.
pause
