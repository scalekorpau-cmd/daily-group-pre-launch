# -*- coding: utf-8 -*-
"""Fetch homepage HTML and extract phone-like strings; compare to canonical category."""
from __future__ import annotations

import csv
import re
import ssl
import urllib.error
import urllib.request
from pathlib import Path

OUT = Path(__file__).resolve().parent / "phone-audit-homepage-scrape.csv"

# Brand -> (url, category: dailyclean | cleaning_fleet | corporate_hq)
SITES: list[tuple[str, str, str]] = [
    ("DailyClean", "https://dailyclean.com.au", "dailyclean"),
    ("PowerBath", "https://powerbath.com.au", "cleaning_fleet"),
    ("Outreach Clean", "https://outreachclean.com.au", "cleaning_fleet"),
    ("DueClean", "https://dueclean.com.au", "cleaning_fleet"),
    ("Cleanse Group", "https://cleansegroup.com.au", "cleaning_fleet"),
    ("Solar Cleanse", "https://solarcleanse.com.au", "cleaning_fleet"),
    ("Gutters Cleanse", "https://gutterscleanse.com.au", "cleaning_fleet"),
    ("Daily Group", "https://thedailygroup.com.au", "corporate_hq"),
    ("Kaltos Group", "https://kaltosgroup.com.au", "corporate_hq"),
    ("Arkos Group", "https://arkosgroup.com.au", "corporate_hq"),
    ("Vantix Capital", "https://vantixcapital.com.au", "corporate_hq"),
    ("VATasker", "https://vatasker.com", "corporate_hq"),
    ("ScaleKorp", "https://scalekorp.com", "corporate_hq"),
    ("TradesBook", "https://tradesbook.com.au", "corporate_hq"),
    ("Saxum Works", "https://saxumworks.com.au", "cleaning_fleet"),
    ("Kaltos Projects", "https://kaltosprojects.com.au", "corporate_hq"),
    ("DailyReset", "https://dailyreset.com.au", "corporate_hq"),
    ("Stratis Civil", "https://stratiscivil.com.au", "corporate_hq"),
    ("Stratis Landscape", "https://stratislandscape.com.au", "corporate_hq"),
    ("DueClean preview", "https://sienna-wolverine-539565.hostingersite.com", "cleaning_fleet"),
    ("ScaleKorp preview", "https://tan-caribou-397506.hostingersite.com", "corporate_hq"),
]

EXPECTED = {
    "dailyclean": {"digits": {"61861894913", "0861894913", "861894913"}, "label": "+61 8 6189 4913"},
    "cleaning_fleet": {"digits": {"61863845466", "0863845466", "863845466"}, "label": "(08) 6384 5466"},
    "corporate_hq": {"digits": {"61861894913", "0861894913", "861894913"}, "label": "+61 8 6189 4913"},
}


def normalize_digits(s: str) -> set[str]:
    d = re.sub(r"\D", "", s)
    out = set()
    if not d:
        return out
    out.add(d)
    if d.startswith("61") and len(d) >= 10:
        out.add("0" + d[2:])
    if d.startswith("0"):
        out.add("61" + d[1:])
    return out


def extract_phones(html: str) -> list[str]:
    # Broad patterns for AU numbers in pages
    patterns = [
        r"\+61[\s\-]?\d(?:[\d\s\-]{7,20})",
        r"\(?08\)?[\s\-]?\d{4}[\s\-]?\d{3,4}",
        r"tel:\+?61\d+",
        r"tel:08\d+",
    ]
    found: set[str] = set()
    for p in patterns:
        for m in re.findall(p, html, flags=re.I):
            found.add(m.strip())
    return sorted(found, key=len)[:25]


def fetch(url: str, timeout: int = 25) -> tuple[int, str]:
    ctx = ssl.create_default_context()
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "DailyGroupPhoneAudit/1.0 (internal reconciliation)"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout, context=ctx) as r:
            code = r.getcode()
            body = r.read().decode("utf-8", errors="ignore")
            return code, body
    except urllib.error.HTTPError as e:
        return e.code, (e.read() or b"").decode("utf-8", errors="ignore")
    except Exception as e:
        return -1, str(e)


def classify_match(found_strings: list[str], category: str) -> tuple[str, str]:
    exp = EXPECTED[category]
    all_digits: set[str] = set()
    for s in found_strings:
        all_digits |= normalize_digits(s)
    hits = sorted(all_digits & exp["digits"])
    wrong = sorted(all_digits - exp["digits"])
    if not found_strings or not all_digits:
        return "NO_PHONE_FOUND", "No obvious phone pattern in HTML (check client-rendered content manually)."
    if hits and not wrong:
        return "OK", f"Found expected bucket digit forms: {hits}"
    if hits and wrong:
        return "MIXED", f"Expected-like {hits} but also other digit blobs {wrong} — review page."
    return "REVIEW", f"Digit forms found {sorted(all_digits)[:12]} — compare to expected {exp['label']}"


def main() -> None:
    rows = []
    for brand, url, cat in SITES:
        code, body = fetch(url)
        if code == 200:
            phones = extract_phones(body)
            match, note = classify_match(phones, cat)
        else:
            phones = []
            match = "HTTP_FAIL"
            note = (body[:500] if isinstance(body, str) else str(body))[:500]
        rows.append(
            {
                "Brand": brand,
                "URL": url,
                "Category": cat,
                "Expected_phone": EXPECTED[cat]["label"],
                "HTTP": str(code),
                "Phones_snippet": " | ".join(phones[:8]),
                "Match": match,
                "Notes": note,
            }
        )

    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(
            f,
            fieldnames=["Brand", "URL", "Category", "Expected_phone", "HTTP", "Phones_snippet", "Match", "Notes"],
        )
        w.writeheader()
        w.writerows(rows)

    print(f"Wrote {OUT} ({len(rows)} rows)")


if __name__ == "__main__":
    main()
