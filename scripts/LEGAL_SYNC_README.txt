Multi-repo legal file sync (semi-automatic)
===========================================

What this does
---------------
For each repository listed in repos-legal-manifest.json, Sync-LegalToRepos.ps1:
  1. Shallow-clones the repo under %TEMP%\daily-group-legal-sync\<id> (or pulls if already there)
  2. Reads TERMS / PRIVACY / COOKIES templates from ..\01-universal-standards\legal\
  3. Replaces [PLACEHOLDERS] using the "placeholders" object for that repo
  4. Writes terms.html, privacy.html, cookies.html into relativeTarget (default: public/)
  5. Commits and pushes to the branch you set (usually main)

What it does NOT do
-------------------
- It does not log in to GitHub for you or accept passwords in chat.
- It cannot add React/Next "page.tsx" routes for every stack. For App Router sites, set "skip": true
  and add pages in that repo (see TradesBook pattern), or extend the script.

Authentication (do once on this PC)
------------------------------------
Option A — GitHub CLI (recommended):
  winget install GitHub.cli
  gh auth login
  (use browser / device flow — never paste your password here)

Option B — Git credential manager + SSH remotes (git@github.com:...)

Then run:
  powershell -ExecutionPolicy Bypass -File C:\Users\DELL\daily-group-pre-launch\scripts\Sync-LegalToRepos.ps1

First run creates repos-legal-manifest.json from repos-legal-manifest.example.json if missing.
Copy the example entry for each real repo, set gitUrl, placeholders, "skip": false.

Placeholder keys (must match templates)
----------------------------------------
  BRAND_DISPLAY_NAME, WEBSITE_URL, LEGAL_ENTITY_NAME, ABN, DATE_DD_MONTH_YYYY,
  PRIVACY_EMAIL, CONTACT_EMAIL, CONTACT_PHONE, POSTAL_ADDRESS

If a repo has no public/ folder, set "relativeTarget" to an existing static-served folder or mark "skip": true.

Optional: Export-LegalHtml.ps1
--------------------------------
Not required for sync (substitution happens in the sync script). Use a small script or manual copy
if you want a single-folder HTML preview outside Git.
