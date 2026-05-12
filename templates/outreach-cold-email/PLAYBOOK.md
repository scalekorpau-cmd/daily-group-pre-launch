# Cold outreach & growth — playbook (Daily Group ecosystem)

Use this **after launch** when websites and core forms are stable. Adapt per brand; get **commercial + legal** review before high-volume sends.

---

## 1. Where cold email *fits* (and where it usually does not)

| Motion | Typical brands | Notes |
| :--- | :--- | :--- |
| **B2B outbound** (ICP list, LinkedIn + email) | ScaleKorp, VATasker, TradesBook, Vantix (strict compliance), Daily / Kaltos / Arkos **parent** for partnerships | Personalise; low volume; clear opt-out. |
| **Local demand gen** (GBP, local SEO, referrals, review asks) | DailyClean, PowerBath, Outreach Clean, DueClean, Saxum, Solar Cleanse, Gutters Cleanse | Usually **not** consumer cold email at scale; focus **local** channels. |
| **Newsletter / nurture** (inbound opted-in) | All | Opt-in proof stored; unsubscribe on every send. |

**Australian context:** commercial email is heavily regulated. Treat this playbook as **operational**, not legal advice — confirm obligations (e.g. **Spam Act**, privacy, industry rules) with your adviser before scaling.

---

## 2. Minimum technical bar (before any cold send)

- **SPF, DKIM, DMARC** aligned on the **sending domain** (not a random Gmail).
- **Dedicated sending** subdomain optional but recommended for reputation (`news.brand.com.au`).
- **Bounce handling** + **suppression** in GHL (and a master export weekly).

---

## 3. Suppression & ethics (non-negotiable)

- Global **do-not-contact** list (internal + GHL).
- Honour **unsubscribe** and **bounces** immediately.
- No misleading subject lines; identify the business clearly.

---

## 4. Recommended sequence skeleton (B2B)

1. **Touch 0 (optional):** LinkedIn connection note (no pitch wall).
2. **Touch 1:** Short email — problem hypothesis + one proof point + soft CTA.
3. **Touch 2 (5–7 days):** Different angle — insight, checklist, or micro-case.
4. **Touch 3 (7–10 days):** Break-up or “permission to close” — polite exit.

Use placeholders only: `{{FirstName}}`, `{{Company}}`, `{{OneLineProof}}` — never fabricate metrics.

---

## 5. What to store in Git (safe)

- Playbooks, **templates** (no real prospect data).
- **ICP definitions**, messaging pillars, objection lists.
- **GHL field map** and pipeline naming conventions.

## 6. What *not* to store in Git

- Raw prospect CSVs with emails (use **private** CRM + vault).
- Purchased lists without documented consent model.

---

## 7. Metrics (post-launch review ties in)

- Sends, delivered, replies, meetings, pipeline **by brand** and **by sequence version**.
- Compare to existing **PL-*** post-launch metrics in the tracker.
