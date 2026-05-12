Daily Group — Pre-launch workspace
==================================

Root path:
  C:\Users\DELL\daily-group-pre-launch\

How to use
----------
1. Work top-down: finish 01-universal-standards first (legal, trust, technical, comms, testing).
2. For each brand folder (06–15), store drafts, PDFs, screenshots, and completed evidence under that brand only.
   Legal page HTML templates (lawyer review required): 01-universal-standards\legal\*.html
3. Update tracking\master-tracker.csv as tasks move (Notepad, Excel, or Google Sheets import).
   Source of truth for the full grid: py tracking\build_tracker.py (regenerates master + by-brand).
   To regenerate all rows from the checklist script after edits:
     py C:\Users\DELL\daily-group-pre-launch\tracking\build_tracker.py
   Per-brand slices: tracking\by-brand\*.csv
4. Put final signed legal PDFs and certificates in _incoming\legal-signed-pdfs and _incoming\evidence-screenshots.

Related work already on this machine
--------------------------------------
- Email signatures (generated HTML): C:\Users\DELL\email-signatures\
  Regenerate signatures: py C:\Users\DELL\email-signatures\build_signatures.py

Folder map (quick)
------------------
01-universal-standards   Policies, insurance, DNS/email, forms testing — applies to all brands
02–05                    Parent / pillar sites (Daily, Kaltos, Arkos, Vantix)
06–10                    Kaltos operations brands
11–13                    Cleanse Group + solar + gutters
14–15                    Arkos digital (VATasker, ScaleKorp)
16                       Cross-brand consistency (footers, typography, ecosystem page)
17                       Social + Google Business Profile packs
18                       Launch week timeline (runbooks)
19                       Launch day emergency kit (contacts, backups)
20                       Post-launch 30-day metrics review
templates                Reusable outlines (legal placeholders, GHL field specs, scripts)
                           + ai-task-routing/ (Claude vs Genspark per-brand matrix)
_reference               Source-of-truth notes (phones, addresses) — reconcile with live sites
tracking                 master-tracker.csv + optional exports in by-brand\

Next step (recommended)
-------------------------
Open tracking\master-tracker.csv and start filling Owner + Due Date for every row with Status=TODO.
Then open 01-universal-standards\legal and add your lawyer’s versions when ready.
