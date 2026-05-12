Universal institutional standards (all brands)
----------------------------------------------
Use the subfolders as follows:

legal/
  Draft or final Terms, Privacy, Cookies, cancellation policies. Filename pattern:
  BRANDNAME-document-v1.pdf or .docx

trust-assets/
  Insurance COI PDFs, badge graphics, capability statement drafts, brochure PDFs.

technical-infrastructure/
  DNS exports, SSL check screenshots, GA4 property IDs, Search Console property list,
  uptime monitor links, backup policy notes.

communication/
  IVR scripts, voicemail scripts, auto-reply email HTML, CRM pipeline naming conventions,
  lead SLA doc, crisis comms draft.
  AI tool routing (which deliverables use Claude vs Genspark): see
  communication/CLAUDE_VS_GENSPARK_ROUTING.md
  Per-brand matrix: ../templates/ai-task-routing/PER_BRAND_APPLICABILITY.md

testing/
  Test logs: form submissions, phone tests, email deliverability (SPF/DKIM/DMARC),
  with date and tester initials in the filename.

When a task is done, add a row or update Status in ..\tracking\master-tracker.csv and drop
evidence into ..\_incoming\evidence-screenshots or brand folder as appropriate.
