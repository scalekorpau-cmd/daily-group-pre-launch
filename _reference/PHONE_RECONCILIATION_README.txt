Step 2 — Phone & address reconciliation (automated + manual)
==============================================================

Canonical values (edit once, then propagate everywhere)
---------------------------------------------------------
File: phone-reconciliation-canonical.csv
  One row per brand: Display_Phone, tel_link, Office vs Service area text.

Work-through checklist (mark Status in Excel)
---------------------------------------------
File: phone-reconciliation-channels-checklist.csv

Homepage automated scrape
-------------------------
  py C:\Users\DELL\daily-group-pre-launch\_reference\audit_homepage_phones.py
Output: phone-audit-homepage-scrape.csv

Ops decision (May 2026)
-------------------------
Outreach Clean and Saxum Works both use the fleet public line (08) 6384 5466 and the Greater Perth
service area line (not St Georges). Update live websites, GBP, and social to match if any still show 6189.

Limits: SPA sites may show NO_PHONE_FOUND; SSL/DNS failures need manual check.

Email signatures: regenerate after matrix changes
  py C:\Users\DELL\email-signatures\build_signatures.py
