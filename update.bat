@echo off
REM Rebuild the Core Micro website from concepts_data.py + phase2_content.py
REM and push the changes to GitHub. Double-click or run from cmd.exe in this folder.

setlocal

cd /d "%~dp0"

set REPO=https://github.com/Ryann-teo/Micro.git
set BRANCH=main

echo.
echo === Core Micro website update ===
echo Folder:  %CD%
echo.

REM Detect Python
where python >nul 2>nul
if errorlevel 1 (
  where python3 >nul 2>nul
  if errorlevel 1 (
    echo ERROR: Python not found on PATH. Install Python from https://www.python.org/.
    pause
    exit /b 1
  )
  set PY=python3
) else (
  set PY=python
)

REM Check git
where git >nul 2>nul
if errorlevel 1 (
  echo ERROR: git is not on PATH. Install Git for Windows from https://git-scm.com/download/win.
  pause
  exit /b 1
)

REM Step 1: rebuild
echo Step 1: rebuilding index.html and assets...
%PY% build_site.py
if errorlevel 1 (
  echo Build failed. See errors above.
  pause
  exit /b 1
)

REM Step 2: init/update git
if not exist ".git" (
  echo.
  echo Step 2: initialising git repo...
  git init
  git branch -M %BRANCH%
  git remote add origin %REPO%
) else (
  echo.
  echo Step 2: syncing remote...
  git remote get-url origin >nul 2>nul
  if errorlevel 1 (
    git remote add origin %REPO%
  ) else (
    git remote set-url origin %REPO%
  )
)

REM Step 3: commit
echo.
echo Step 3: staging and committing...
git add -A

set TS=%date%
git commit -m "Update Core Micro study guide (%TS%)" 2>nul
if errorlevel 1 (
  echo No new changes to commit. Continuing to push in case the remote is behind.
)

REM Step 4: push
echo.
echo Step 4: pushing to %BRANCH%...
git push -u origin %BRANCH%
if errorlevel 1 (
  echo.
  echo Plain push failed. Trying force push...
  git push -u origin %BRANCH% --force
)

if errorlevel 1 (
  echo.
  echo Push failed. See git output above.
  pause
  exit /b 1
)

echo.
echo === Update complete ===
echo Live site: https://ryann-teo.github.io/Micro/
echo.
pause
