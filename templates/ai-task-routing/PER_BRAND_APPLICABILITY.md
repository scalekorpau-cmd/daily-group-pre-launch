# Per-brand applicability — Claude vs Genspark

**Legend:** **Y** = include in brand backlog · **—** = not applicable · **Later** = after core launch

**Claude** = HTML/CSS/JS + GHL where relevant. **Genspark** = PDF / print / visual design.

Active brands align with `tracking/build_tracker.py` social / launch set.

---

## Matrix (active brands)

| Brand | Discovery / consult form (Claude) | Asset / site / audit form (Claude) | VA intake (Claude) | Capability PDF (Genspark) | Brochures PDF (Genspark) | Proposal PDF (Genspark) | Case study web (Claude) | Case study PDF (Genspark) | Newsletter HTML (Claude) |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| Daily Group | Later | — | — | Y | — | — | Later | Later | Later |
| Kaltos Group | Later | — | — | Y | — | — | Later | Later | Later |
| Arkos Group | Later | — | — | Y | — | — | Later | Later | Later |
| Vantix Capital | Y | — | — | Y | — | Later | Y | Later | Later |
| DailyClean | Later | Y | — | Y | Y | — | Y | Later | Later |
| PowerBath | Later | Y | — | Y | Y | — | Y | Later | Later |
| Outreach Clean | Later | Y | — | Y | Later | — | Y | Later | Later |
| DueClean | Y | Y | — | Y | Later | — | Later | Later | Later |
| Saxum Works | Later | Y | — | Y | Later | — | Y | Later | Later |
| Cleanse Group | — | — | — | Y | — | — | Later | Later | Later |
| Solar Cleanse | Later | Y | — | Y | Later | — | Y | Later | Later |
| Gutters Cleanse | Later | Y | — | Y | Later | — | Y | Later | Later |
| VATasker | Y | — | Y | Y | Later | — | Y | Later | Later |
| ScaleKorp | Y | — | — | Y | Later | Y | Y | Later | Later |
| TradesBook | Later | — | — | Later | Later | — | Later | Later | Later |

---

## Notes

- **Discovery / consult:** highest for **ScaleKorp**, **Vantix**, **VATasker**, **DueClean** (Discovery Audit narrative); parent sites can use a lighter “partnership inquiry” later.
- **Asset / site / audit:** field brands (DailyClean, PowerBath, Outreach, DueClean, Saxum, Solar, Gutters) — match existing tracker wording (forms → GHL).
- **VA intake:** **VATasker** client intake + separate talent pipeline (tracker already has both forms).
- **Capability / brochures / proposal:** many rows already exist as trust/comms tasks (`U-TRU-06`, `U-TRU-07`, ScaleKorp exec summary / proposal story); this matrix ties them to **Genspark** as the default production tool.
- **Case study web:** **Claude** for embeddable site sections; **Genspark** optional for leave-behind PDF.
- **Newsletter:** one **Claude** master HTML with brand tokens; roll out Later unless email is already live.

Update this table when a brand’s go-to-market changes; keep evidence links in `tracking/master-tracker.csv` after `python tracking/build_tracker.py`. **Post-launch outbound tasks (GO-*)** live in the separate repo **daily-group-post-launch** (`tracking/TASKS.csv`).
