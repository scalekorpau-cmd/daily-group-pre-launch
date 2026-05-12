Post-launch growth, cold outreach, and sales motion (all brands)
================================================================

Purpose
-------
After sites and core GHL are live, this pack holds **non-website** artefacts:
sequences, ICP notes, suppression rules, LinkedIn SOPs, and **per-brand**
decisions about *whether* cold outreach fits the brand (B2B vs local consumer).

Primary templates live in:
  ..\templates\outreach-cold-email\

Do not store purchased lists or personal data in **public** GitHub repos.
Use **private** repos and/or encrypted storage for anything sensitive.

How to use
----------
1. Read templates\outreach-cold-email\PLAYBOOK.md (policy + rhythm).
2. Fill ICP + offer one-pagers per B2B brand in this folder (Markdown or PDF links).
3. Wire GHL: pipelines, tags, unsubscribe, webhooks — mirror field names in
   templates\outreach-cold-email\GHL_FIELD_MAP.txt
4. Mark tracker rows GO-* as you complete them (see tracking\build_tracker.py).

Evidence
--------
Screenshots of DNS (SPF/DKIM/DMARC), sample sends, and suppression exports live in
..\_incoming\evidence-screenshots\ with dated filenames.
