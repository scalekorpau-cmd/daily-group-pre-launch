GitHub "drive" — control outside Cursor updates
================================================

Why this exists
---------------
When Cursor or another .exe updates, PATH, embedded terminals, or gh sessions can
feel "broken." These scripts use:

  - Windows Git Credential Manager (HTTPS) and/or
  - GH_TOKEN / GITHUB_TOKEN in **User** environment variables (survives most app updates)

They do **not** depend on Cursor's chat UI.

Setup (once)
-------------
1. Install Git for Windows (includes Git Credential Manager).
2. Install GitHub CLI: winget install GitHub.cli
3. Authenticate once in a normal PowerShell window (not only inside Cursor):
     gh auth login
   Or set a classic PAT with `repo` scope as user env var:
     GITHUB_TOKEN=ghp_...

4. Optional: add to User PATH (Environment Variables):
     C:\Program Files\GitHub CLI

Usage
------
Dot-source the script so functions load into your session:

  . C:\Users\DELL\daily-group-pre-launch\scripts\GitHub-Drive.ps1

Then run commands below. You can also create a **Desktop shortcut** that runs:

  powershell -NoExit -Command "& 'C:\Users\DELL\daily-group-pre-launch\scripts\GitHub-Drive.ps1'"

(Adjust path if you moved the repo.)

Cursor integration (light touch)
---------------------------------
- **.cursor/rules** in each repo: "For GitHub operations, prefer scripts/GitHub-Drive.ps1"
- **Tasks** (.vscode/tasks.json): task "Git: Push" that runs pwsh with the push function

This gives "one prompt" inside Cursor via a **task name**, not a bar above chat.

Official alternatives
---------------------
- **github.com** — full control, always works.
- **GitHub Mobile app** — merges, notifications.
- **GitHub CLI** `gh` — same API as the website, scriptable forever.
