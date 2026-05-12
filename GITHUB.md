# Cloud copy (GitHub)

This folder is the **Daily Group pre-launch workspace**: trackers, brand runbooks, legal templates, scripts, and reference data.

- **Primary tracker:** `tracking/master-tracker.csv` (and `tracking/by-brand/*.csv` generated from it).
- **How to work:** see `README.txt` at the root of this repo.

`_incoming/` (signed PDFs, evidence screenshots) is **gitignored** — use secure storage for those; everything else here is intended to live in this repository on GitHub.

**AI tooling (all brands):** `01-universal-standards/communication/CLAUDE_VS_GENSPARK_ROUTING.md` and `templates/ai-task-routing/PER_BRAND_APPLICABILITY.md`. Regenerate CSVs after `build_tracker.py` edits: `py tracking\build_tracker.py`.

**Post-launch growth / outbound:** `22-post-launch-growth-outreach/` and `templates/outreach-cold-email/` (playbook + sequences + GHL field map).
