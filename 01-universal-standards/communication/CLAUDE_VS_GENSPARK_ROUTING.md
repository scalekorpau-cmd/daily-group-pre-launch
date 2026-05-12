# Claude vs Genspark — which AI for which task?

Institutional guidance for **Daily Group** active brands. Use with `templates/ai-task-routing/PER_BRAND_APPLICABILITY.md` (who needs what).

---

## Short answer

**Both — for different outputs.**

| AI | Best for | Output |
| :--- | :--- | :--- |
| **Claude (code / web)** | HTML/CSS/JS, web forms, GHL-connected pages, email HTML | Web pages, forms, interactive templates |
| **Genspark (design)** | Graphic design, print, branding | Logos, brochures, social graphics, PDFs |

---

## Category B — task breakdown

| Task | Claude | Genspark | Recommended |
| :--- | :---: | :---: | :--- |
| One-page capability statement | Can do HTML web version | Better print-ready PDF | **Genspark** (PDF) |
| Service brochures | Basic HTML layout | Best print-ready | **Genspark** |
| Case study template | HTML for site | Optional polished PDF | **Claude** (web); **Genspark** (PDF if needed) |
| Proposal template (e.g. ScaleKorp) | HTML/interactive possible | Polished client PDF | **Genspark** (PDF) |
| Discovery call form | Best | Not suited | **Claude** |
| Asset assessment form | Best | Not suited | **Claude** |
| VA client intake form | Best | Not suited | **Claude** |
| Newsletter email template | Email HTML | Visual design | **Either** (Claude for code; Genspark for layout mock) |

---

## Claude — best for

| Type | Examples | Why |
| :--- | :--- | :--- |
| Web forms | Discovery call, asset assessment, VA intake | Interactive, validates input, posts to GoHighLevel |
| HTML templates | Case study layout, email shell | Drop into site or ESP |
| Clickable prototypes | Proposal preview in browser | Client reviews online |

**Output:** web-ready HTML/CSS/JS (not print-proof).

---

## Genspark — best for

| Type | Examples | Why |
| :--- | :--- | :--- |
| Print-ready PDFs | Capability statement, brochures, proposals | Layout, typography, brand polish |
| Logos & branding | Visual identity | Design-first |
| Social graphics | LinkedIn banners, post templates | Channel-specific sizing |
| One-pagers | Investor-facing one-pager | Branded PDF |

**Output:** PDF, PNG, JPG, SVG — not production web code.

---

## Hybrid (best of both)

| Step | Action |
| :--- | :--- |
| 1 | Genspark: visual / PDF template |
| 2 | Claude: convert to HTML **only if** you need the same story on the web |
| 3 | Or ship Genspark PDF only for email / print / sales |

**Example — proposal:** Genspark PDF to clients; add Claude web version only if you want an online preview.

**Example — intake:** Claude form → GHL; add Genspark only if you need a branded printable PDF companion.

---

## Quick decision

| Need | Use |
| :--- | :--- |
| Web form that collects leads | **Claude** |
| Branded PDF to send or print | **Genspark** |
| Printable brochure | **Genspark** |
| Newsletter (HTML in ESP) | **Claude** (code); optional Genspark for visual mock |
| Case study on the website | **Claude** |
| Case study as download PDF | **Genspark** |

---

## Priority stack (default order)

| Task | Tool | Priority |
| :--- | :--- | :--- |
| Discovery / consult web form | **Claude** | High (where sales motion exists) |
| Asset / site / audit web form | **Claude** | High (field / assessment brands) |
| VA client intake web form | **Claude** | High (VATasker) |
| One-page capability PDF | **Genspark** | High |
| Proposal template PDF | **Genspark** | High (ScaleKorp; others if used) |
| Service brochures PDF | **Genspark** | Medium |
| Case study | **Claude** (web) + **Genspark** (PDF) optional | Medium |
| Newsletter HTML | **Claude** | Low |

**Rule of thumb:** Claude builds **functional** web surfaces and GHL wiring. Genspark builds **designed** PDF and visual assets.

---

## Related files in this repo

- `templates/ai-task-routing/PER_BRAND_APPLICABILITY.md` — row per active brand: what applies (Y / — / Later).
- Tracker: universal tasks `U-AI-01` … (see `tracking/build_tracker.py`).
