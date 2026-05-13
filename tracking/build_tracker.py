# -*- coding: utf-8 -*-
"""Generate master-tracker.csv and per-brand CSVs from checklist data."""
from __future__ import annotations

import csv
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MASTER = ROOT / "master-tracker.csv"
BY_BRAND = ROOT / "by-brand"

# (workstream, brand, task_id, task, priority)
# priority: CRITICAL | HIGH | MEDIUM | LOW
ROWS: list[tuple[str, str, str, str, str]] = []

# Persisted completion (survives `py build_tracker.py`). (Status, Evidence_Link, Notes)
TASK_COMPLETION: dict[str, tuple[str, str, str]] = {
    "U-LEG-01": ("Done", "https://github.com/scalekorpau-cmd", "Terms published site-wide; footer + /terms.html per repo."),
    "U-LEG-02": ("Done", "https://github.com/scalekorpau-cmd", "Privacy published site-wide; footer + /privacy.html per repo."),
    "U-LEG-03": ("Done", "https://github.com/scalekorpau-cmd", "Cookies published site-wide; footer + /cookies.html per repo."),
    "U-LEG-08": ("Done", "https://github.com/scalekorpau-cmd/scalekorp-web", "Banner + /disclaimer.html + footer link + contact page."),
    "SK-02": ("Done", "https://github.com/scalekorpau-cmd/scalekorp-web", "M&A / licensing disclaimer prominent site-wide."),
}

def add(ws: str, brand: str, tid: str, task: str, pri: str) -> None:
    ROWS.append((ws, brand, tid, task, pri))


# --- Part 2: Universal (ALL) ---
u = "universal"
add(u, "ALL", "U-LEG-01", "Terms & Conditions published on every website", "CRITICAL")
add(u, "ALL", "U-LEG-02", "Privacy Policy published on every website", "CRITICAL")
add(u, "ALL", "U-LEG-03", "Cookies Policy published on every website", "CRITICAL")
add(u, "ALL", "U-LEG-04", "Service agreements drafted for every brand (where applicable)", "CRITICAL")
add(u, "ALL", "U-LEG-05", "Cancellation policy published (where applicable)", "HIGH")
add(u, "ALL", "U-LEG-06", "ABN displayed in footer of every website", "CRITICAL")
add(u, "ALL", "U-LEG-07", "Professional email signatures (logo, disclaimer; ABN if required) all team", "HIGH")
add(u, "ALL", "U-LEG-08", "M&A disclaimer (not licensed broker) on ScaleKorp", "CRITICAL")
add(u, "ALL", "U-TRU-01", "$20M PL insurance certificate downloadable per relevant brand", "HIGH")
add(u, "ALL", "U-TRU-02", "Police cleared / insured verification graphics on each website", "HIGH")
add(u, "ALL", "U-TRU-03", "WA Heights certified badge where applicable (DailyClean, Solar, Gutters)", "HIGH")
add(u, "ALL", "U-TRU-04", "Professional photography (team, ops, equipment, dashboards) all brands", "HIGH")
add(u, "ALL", "U-TRU-05", "Branded uniforms consistent per brand", "HIGH")
add(u, "ALL", "U-TRU-06", "Capability statement PDF per brand", "HIGH")
add(u, "ALL", "U-TRU-07", "Service brochure PDF per brand", "HIGH")
add(u, "ALL", "U-TRU-08", "Parent watermark / line on materials (Part of Daily Group etc.)", "HIGH")
add(u, "ALL", "U-TEC-01", "SSL (HTTPS) active all domains", "CRITICAL")
add(u, "ALL", "U-TEC-02", "Google Analytics 4 installed all websites", "HIGH")
add(u, "ALL", "U-TEC-03", "Google Search Console verified all domains", "HIGH")
add(u, "ALL", "U-TEC-04", "Uptime monitoring active all domains", "MEDIUM")
add(u, "ALL", "U-TEC-05", "Hosting backup redundancy confirmed all domains", "HIGH")
add(u, "ALL", "U-TEC-06", "Zoho Mail (or chosen) professional email all domains", "CRITICAL")
add(u, "ALL", "U-TEC-07", "No consumer Gmail for brand-facing comms", "CRITICAL")
add(u, "ALL", "U-TEC-08", "Remove default mobile signature (Sent from my iPhone) on brand devices", "LOW")
add(u, "ALL", "U-COM-01", "Dedicated phone routing / IVR (or documented interim)", "HIGH")
add(u, "ALL", "U-COM-02", "Professional voicemail scripts per brand", "HIGH")
add(u, "ALL", "U-COM-03", "Auto-response emails for each contact form", "HIGH")
add(u, "ALL", "U-COM-04", "CRM pipelines (GoHighLevel) per brand", "HIGH")
add(u, "ALL", "U-COM-05", "Lead response SLA documented (max 24h)", "HIGH")
add(u, "ALL", "U-COM-06", "Lead SLA tested with dummy submission every brand", "CRITICAL")
add(u, "ALL", "U-COM-07", "Crisis response protocol (complaints, reviews, outage)", "HIGH")
add(u, "ALL", "U-TST-01", "Test every phone on every website", "CRITICAL")
add(u, "ALL", "U-TST-02", "Test every phone on Google Business Profile", "CRITICAL")
add(u, "ALL", "U-TST-03", "Test every phone on social profiles", "HIGH")
add(u, "ALL", "U-TST-04", "Test every contact form → GHL → notification", "CRITICAL")
add(u, "ALL", "U-TST-05", "Test key mailboxes (admin@, support@, etc.)", "CRITICAL")
add(u, "ALL", "U-TST-06", "Verify all automated responses", "HIGH")

# --- AI tooling (Claude vs Genspark) — see 01-universal-standards/communication/ + templates/ai-task-routing/ ---
add(u, "ALL", "U-AI-01", "AI production routing adopted (Claude: web/forms/HTML vs Genspark: PDFs/print/visuals)", "HIGH")
add(u, "ALL", "U-AI-02", "Per-brand AI applicability matrix reviewed and owners assigned", "HIGH")
add(u, "ALL", "U-AI-03", "Master case study HTML template (Claude) with brand token slots for reuse", "MEDIUM")
add(u, "ALL", "U-AI-04", "Master newsletter HTML template (Claude) with brand token slots", "LOW")

# --- Part 3: Parents ---
def parent(prefix: str, brand: str, items: list[tuple[str, str, str]]) -> None:
    for tid, task, pri in items:
        add("parent", brand, f"{prefix}-{tid}", task, pri)

parent("DG", "Daily Group", [
    ("01", "Website live: homepage, about, contact", "CRITICAL"),
    ("02", "Our Brands page: all subsidiaries logos + links", "CRITICAL"),
    ("03", "Ecosystem diagram (visual hierarchy)", "CRITICAL"),
    ("04", "Footer: no parent line (top of hierarchy)", "CRITICAL"),
    ("05", "Contact: phone + address match approved matrix", "CRITICAL"),
    ("06", "LinkedIn Company Page created", "CRITICAL"),
    ("07", "Google Business Profile optimised", "HIGH"),
])
parent("KG", "Kaltos Group", [
    ("01", "Website live: homepage, about, contact", "CRITICAL"),
    ("02", "Our Divisions page (Projects + Facility Management)", "CRITICAL"),
    ("03", "Footer: Part of Daily Group", "CRITICAL"),
    ("04", "LinkedIn Company Page created", "CRITICAL"),
    ("05", "Google Business Profile optimised", "HIGH"),
])
parent("AG", "Arkos Group", [
    ("01", "Website live: homepage, about, contact", "CRITICAL"),
    ("02", "Our Brands page (ScaleKorp, VATasker, TradesBook, etc.)", "CRITICAL"),
    ("03", "Footer: Part of Daily Group", "CRITICAL"),
    ("04", "LinkedIn Company Page created", "CRITICAL"),
    ("05", "Google Business Profile optimised", "HIGH"),
])
parent("VX", "Vantix Capital", [
    ("01", "Website live: homepage, about, contact", "CRITICAL"),
    ("02", "Investment philosophy page", "CRITICAL"),
    ("03", "Confidential inquiry form for business sellers", "CRITICAL"),
    ("04", "Footer: Part of Daily Group", "CRITICAL"),
    ("05", "LinkedIn Company Page created", "CRITICAL"),
    ("06", "Google Business Profile optimised", "HIGH"),
])

# --- Part 4: Kaltos operations ---
def ops(prefix: str, brand: str, items: list[tuple[str, str, str]]) -> None:
    for tid, task, pri in items:
        add("operations", brand, f"{prefix}-{tid}", task, pri)

ops("DC", "DailyClean", [
    ("01", "Client logos displayed with documented permission", "CRITICAL"),
    ("02", "Minimum 3 case studies with measurable outcomes", "CRITICAL"),
    ("03", "Trust badges: $20M PL, WA Heights, police cleared", "CRITICAL"),
    ("04", "Footer: A Kaltos Group company | Part of Daily Group", "CRITICAL"),
    ("05", "Primary phone prominent all pages (match matrix)", "CRITICAL"),
    ("06", "Asset Assessment form → GHL working", "CRITICAL"),
    ("07", "Before/after gallery ≥10 real images (not stock)", "CRITICAL"),
    ("08", "AS 1851-2012 compliance certification visible (if claimed)", "CRITICAL"),
    ("09", "Our Process page (checklist, QA, reporting)", "CRITICAL"),
    ("10", "Quality Assurance page", "CRITICAL"),
    ("11", "Safety & Compliance page", "CRITICAL"),
    ("12", "Industries We Serve page", "CRITICAL"),
    ("13", "Team uniforms navy/silver consistent", "CRITICAL"),
    ("14", "LinkedIn + 10 posts scheduled", "CRITICAL"),
    ("15", "Google Business Profile fully optimised", "HIGH"),
    ("16", "Review request automation configured", "HIGH"),
    ("17", "First 20 reviews target plan", "HIGH"),
    ("18", "Service-area SEO Yanchep to Mandurah", "HIGH"),
    ("19", "Commercial capability statement PDF", "HIGH"),
    ("20", "Residential brochure PDF", "HIGH"),
    ("21", "Vehicle branding all fleet", "HIGH"),
    ("22", "Daily Performance Report template (digital)", "MEDIUM"),
    ("23", "Certificate of Currency downloadable", "MEDIUM"),
])
ops("PB", "PowerBath", [
    ("01", "Footer: A Kaltos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Trust badges: $20M PL, police cleared, environmental compliance", "CRITICAL"),
    ("03", "Before/after gallery ≥10 images", "CRITICAL"),
    ("04", "Service pages: commercial/industrial, residential, graffiti, sealing", "CRITICAL"),
    ("05", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("06", "Contact / site assessment form → GHL", "CRITICAL"),
    ("07", "LinkedIn + 5 posts scheduled", "CRITICAL"),
    ("08", "Google Business Profile optimised", "HIGH"),
    ("09", "Review request automation", "HIGH"),
    ("10", "Capability statement PDF commercial", "HIGH"),
    ("11", "Before/after video walkthrough", "MEDIUM"),
    ("12", "Certificate of Currency downloadable", "MEDIUM"),
])
ops("OR", "Outreach Clean", [
    ("01", "Footer: A Kaltos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Trust badges: $20M PL, police cleared, WA Heights", "CRITICAL"),
    ("03", "Service pages: windows, high-level dusting, estate detail, flyscreen", "CRITICAL"),
    ("04", "Service area page (luxury suburbs)", "CRITICAL"),
    ("05", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("06", "Contact / property assessment form → GHL", "CRITICAL"),
    ("07", "Before/after gallery ≥10 images", "CRITICAL"),
    ("08", "Instagram Business + 10 posts scheduled", "CRITICAL"),
    ("09", "LinkedIn Company minimal", "CRITICAL"),
    ("10", "Google Business Profile select suburbs", "HIGH"),
    ("11", "Review request automation", "HIGH"),
    ("12", "Property Presentation Assessment template", "MEDIUM"),
    ("13", "Digital condition report template", "MEDIUM"),
])
ops("DU", "DueClean", [
    ("01", "Footer: A Kaltos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Trust badges: $20M PL, police cleared", "CRITICAL"),
    ("03", "Subscription tiers explained (Residential/Commercial/Builder Guardian)", "CRITICAL"),
    ("04", "Discovery Audit process explained", "CRITICAL"),
    ("05", "Asset Health Portal preview / mockup", "CRITICAL"),
    ("06", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("07", "Contact / Discovery Audit form → GHL", "CRITICAL"),
    ("08", "What's included per tier + deep/annual cycles", "CRITICAL"),
    ("09", "Optional add-ons listed (bins, garden, laundry, etc.)", "CRITICAL"),
    ("10", "Plain English cadence explanation", "CRITICAL"),
    ("11", "LinkedIn + 5 posts scheduled", "CRITICAL"),
    ("12", "Google Business Profile optimised", "HIGH"),
    ("13", "Review request automation", "HIGH"),
    ("14", "Welcome Kit PDF new subscribers", "MEDIUM"),
    ("15", "Asset Health Portal onboarding guide", "MEDIUM"),
])
ops("SX", "Saxum Works", [
    ("01", "Footer: A Kaltos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Trust badges: $20M PL, licensed & insured, police cleared", "CRITICAL"),
    ("03", "Service pages: brick/block, limestone, rendering, outdoor masonry", "CRITICAL"),
    ("04", "For Builders dedicated page", "CRITICAL"),
    ("05", "For Homeowners dedicated page", "CRITICAL"),
    ("06", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("07", "Contact / site consultation form → GHL", "CRITICAL"),
    ("08", "Before/after gallery ≥10 images", "CRITICAL"),
    ("09", "LinkedIn + 5 posts scheduled", "CRITICAL"),
    ("10", "Google Business Profile optimised", "HIGH"),
    ("11", "Review request automation", "HIGH"),
    ("12", "Capability statement PDF for builders", "MEDIUM"),
])

# --- Part 5: Cleanse ---
def cleanse(prefix: str, brand: str, items: list[tuple[str, str, str]]) -> None:
    for tid, task, pri in items:
        add("cleanse", brand, f"{prefix}-{tid}", task, pri)

cleanse("CG", "Cleanse Group", [
    ("01", "Footer: A Kaltos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Our Brands page: Solar Cleanse + Gutters Cleanse links", "CRITICAL"),
    ("03", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("04", "LinkedIn Company Page", "CRITICAL"),
    ("05", "Google Business Profile optimised", "HIGH"),
])
cleanse("SC", "Solar Cleanse", [
    ("01", "Footer: A Cleanse Group company | Part of Kaltos Group | Daily Group", "CRITICAL"),
    ("02", "Trust badges: $20M PL, WA Heights, 0-TDS deionised", "CRITICAL"),
    ("03", "Service pages: residential, commercial fleet, bird-proofing, health checks", "CRITICAL"),
    ("04", "0-TDS / hard water educational content", "CRITICAL"),
    ("05", "Before/after performance gallery ≥10", "CRITICAL"),
    ("06", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("07", "Contact / asset assessment form → GHL", "CRITICAL"),
    ("08", "Why Deionized Water page", "CRITICAL"),
    ("09", "LinkedIn + 5 posts scheduled", "CRITICAL"),
    ("10", "Google Business Profile optimised", "HIGH"),
    ("11", "Review request automation", "HIGH"),
    ("12", "Solar Performance & Condition Report template PDF", "MEDIUM"),
    ("13", "Bird-proofing add-on pricing guide", "MEDIUM"),
])
cleanse("GC", "Gutters Cleanse", [
    ("01", "Footer: A Cleanse Group company | Part of Kaltos Group | Daily Group", "CRITICAL"),
    ("02", "Trust badges: $20M PL, WA Heights, industrial vacuum", "CRITICAL"),
    ("03", "Service tiers: maintenance, infrastructure, restoration documented", "CRITICAL"),
    ("04", "BAL-rated gutter guards explained", "CRITICAL"),
    ("05", "Before/after gallery ≥10", "CRITICAL"),
    ("06", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("07", "Contact / site assessment form → GHL", "CRITICAL"),
    ("08", "LinkedIn + 5 posts scheduled", "CRITICAL"),
    ("09", "Google Business Profile optimised", "HIGH"),
    ("10", "Review request automation", "HIGH"),
    ("11", "Gutter & Drainage Condition Audit template PDF", "MEDIUM"),
    ("12", "Gutter guard vs plastic mesh comparison page", "MEDIUM"),
    ("13", "Seasonal urgency messaging (fire/storm)", "MEDIUM"),
])

# --- Part 6: Arkos digital ---
def digital(prefix: str, brand: str, items: list[tuple[str, str, str]]) -> None:
    for tid, task, pri in items:
        add("digital", brand, f"{prefix}-{tid}", task, pri)

digital("VT", "VATasker", [
    ("01", "Footer: An Arkos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Trust badges: pre-vetted talent, 30-day replacement", "CRITICAL"),
    ("03", "Service categories: admin, sales, ops, CS, social, bookkeeping VA", "CRITICAL"),
    ("04", "How We Recruit / Vetting Manifesto page", "CRITICAL"),
    ("05", "Training Standards page", "CRITICAL"),
    ("06", "Security & Confidentiality page (NDA, data, access)", "CRITICAL"),
    ("07", "Client intake form → GHL", "CRITICAL"),
    ("08", "VA talent pool application form", "CRITICAL"),
    ("09", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("10", "Pricing tiers — ranges only", "CRITICAL"),
    ("11", "Remove cheap VA language; institutional positioning", "CRITICAL"),
    ("12", "LinkedIn + 10 thought leadership posts scheduled", "CRITICAL"),
    ("13", "Google Business Profile optimised", "HIGH"),
    ("14", "Review request automation", "HIGH"),
    ("15", "Employee Handbook PDF per VA placed", "HIGH"),
    ("16", "Client Portal mockup / branded dashboard", "HIGH"),
    ("17", "Discovery questionnaire", "MEDIUM"),
    ("18", "Client onboarding SOP", "MEDIUM"),
    ("19", "Role matching framework", "MEDIUM"),
    ("20", "30-day onboarding plan", "MEDIUM"),
    ("21", "Reporting templates (KPIs, hours, tasks)", "MEDIUM"),
])
digital("TB", "TradesBook", [
    ("01", "Footer: An Arkos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "Website live or roadmap page: digitalisation & automation positioning", "CRITICAL"),
    ("03", "Primary contact form → GHL (or interim)", "HIGH"),
    ("04", "LinkedIn Company Page + 3 starter posts", "HIGH"),
    ("05", "Google Business Profile (if applicable) or service-area note", "MEDIUM"),
])
digital("SK", "ScaleKorp", [
    ("01", "Footer: An Arkos Group company | Part of Daily Group", "CRITICAL"),
    ("02", "M&A disclaimer prominent (not licensed broker)", "CRITICAL"),
    ("03", "5-Tier model explained with visuals", "CRITICAL"),
    ("04", "Scale Framework / 5-Pillar diagram", "CRITICAL"),
    ("05", "Minimum 3 case studies (anonymised OK)", "CRITICAL"),
    ("06", "For Whom section (trades, cleaning, FM, etc.)", "CRITICAL"),
    ("07", "Discovery call calendar (Calendly/GHL)", "CRITICAL"),
    ("08", "Primary phone prominent (match matrix)", "CRITICAL"),
    ("09", "Contact / discovery form → GHL", "CRITICAL"),
    ("10", "Our Backing section (Arkos → Kaltos → Daily)", "CRITICAL"),
    ("11", "LinkedIn + 10 thought leadership posts scheduled", "CRITICAL"),
    ("12", "ROI calculator tool", "HIGH"),
    ("13", "Strategic partner network listed", "HIGH"),
    ("14", "Minimum 3 whitepapers / industry guides", "HIGH"),
    ("15", "Methodology naming legal check (ScaleOS etc.)", "HIGH"),
    ("16", "Executive Summary template PDF", "MEDIUM"),
    ("17", "Discovery framework documented", "MEDIUM"),
    ("18", "Qualification criteria", "MEDIUM"),
    ("19", "Strategic assessment process", "MEDIUM"),
    ("20", "Audit process documentation", "MEDIUM"),
    ("21", "Quarterly business review structure", "MEDIUM"),
])

# --- Part 7: Cross-brand ---
x = "cross-brand"
add(x, "ALL", "X-01", "Same footer structure pattern across all live sites", "HIGH")
add(x, "ALL", "X-02", "Similar typography tokens across sites", "HIGH")
add(x, "ALL", "X-03", "Consistent naming logic (Daily / Cleanse / Kaltos / Arkos)", "MEDIUM")
add(x, "ALL", "X-04", "Parent reference on every brand footer", "CRITICAL")
add(x, "ALL", "X-05", "Daily Group site complete with ecosystem diagram", "CRITICAL")
add(x, "ALL", "X-06", "LinkedIn company pages cross-linked where appropriate", "MEDIUM")
add(x, "ALL", "X-07", "All GBP verified and optimised", "HIGH")
add(x, "ALL", "X-08", "Google Alerts for all brand names", "LOW")

# --- Part 8: Social (per brand rows) ---
s = "social-gbp"
social_brands = [
    "Daily Group", "Kaltos Group", "Arkos Group", "DailyClean", "PowerBath", "Outreach Clean",
    "DueClean", "Cleanse Group", "Solar Cleanse", "Gutters Cleanse", "VATasker", "ScaleKorp",
    "TradesBook", "Saxum Works", "Vantix Capital",
]
for i, b in enumerate(social_brands, 1):
    add(s, b, f"SOC-{i:02d}", f"LinkedIn/IG/FB as per matrix: profile + cover + bio live", "HIGH")

# --- Part 9–12: Launch & post ---
add("launch-week", "ALL", "LW-01", "Day -21 to -14: parent brands critical tasks + phone tests", "CRITICAL")
add("launch-week", "ALL", "LW-02", "Day -14 to -7: operations brands critical + form tests", "CRITICAL")
add("launch-week", "ALL", "LW-03", "Day -7 to -3: Cleanse + Saxum + digital brands critical", "CRITICAL")
add("launch-week", "ALL", "LW-04", "Day -5: legal review complete all brands", "CRITICAL")
add("launch-week", "ALL", "LW-05", "Day -3: LinkedIn first posts + team training", "HIGH")
add("launch-week", "ALL", "LW-06", "Day -2: GBP optimised + SLA live test", "HIGH")
add("launch-week", "ALL", "LW-07", "Day -1: internal announcement + site walkthrough", "HIGH")
add("launch-week", "ALL", "LW-08", "Day 0: ecosystem launch post all channels", "CRITICAL")
add("launch-week", "ALL", "LW-09", "Day +1: email database (DailyClean-only if that remains policy)", "HIGH")
add("emergency", "ALL", "EM-01", "Hosting emergency contact list all domains", "CRITICAL")
add("emergency", "ALL", "EM-02", "Developer on-call documented", "HIGH")
add("emergency", "ALL", "EM-03", "Crisis response script final", "HIGH")
add("emergency", "ALL", "EM-04", "Backup Google Form per brand", "HIGH")
add("emergency", "ALL", "EM-05", "Phone forwarding fallback if IVR fails", "HIGH")
add("post-launch", "ALL", "PL-01", "30-day: lead response time vs target", "HIGH")
add("post-launch", "ALL", "PL-02", "30-day: form conversion rate", "HIGH")
add("post-launch", "ALL", "PL-03", "30-day: discovery call bookings (ScaleKorp/VATasker)", "HIGH")
add("post-launch", "ALL", "PL-04", "30-day: asset assessment requests (DailyClean)", "HIGH")
add("post-launch", "ALL", "PL-05", "30-day: GBP views trend", "MEDIUM")
add("post-launch", "ALL", "PL-06", "30-day: LinkedIn engagement trend", "MEDIUM")
add("post-launch", "ALL", "PL-07", "30-day: combined web traffic vs target", "HIGH")
add("post-launch", "ALL", "PL-08", "30-day: first 20 reviews progress service brands", "HIGH")


def slug(brand: str) -> str:
    return (
        brand.lower()
        .replace(" ", "-")
        .replace("group", "group")
    )


def main() -> None:
    BY_BRAND.mkdir(parents=True, exist_ok=True)
    header = ["Workstream", "Brand", "Task_ID", "Task", "Priority", "Owner", "Status", "Due_Date", "Evidence_Link", "Notes"]

    with MASTER.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(header)
        for ws, brand, tid, task, pri in ROWS:
            owner, status, due, evidence, notes = ("TBD", "TODO", "", "", "")
            if tid in TASK_COMPLETION:
                status, evidence, notes = TASK_COMPLETION[tid]
            w.writerow([ws, brand, tid, task, pri, owner, status, due, evidence, notes])

    by_brand: dict[str, list] = defaultdict(list)
    for row in ROWS:
        by_brand[row[1]].append(row)

    for brand, rows in sorted(by_brand.items()):
        fn = BY_BRAND / f"{slug(brand)}.csv"
        with fn.open("w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(header)
            for ws, br, tid, task, pri in rows:
                owner, status, due, evidence, notes = ("TBD", "TODO", "", "", "")
                if tid in TASK_COMPLETION:
                    status, evidence, notes = TASK_COMPLETION[tid]
                w.writerow([ws, br, tid, task, pri, owner, status, due, evidence, notes])

    print(f"Wrote {MASTER} ({len(ROWS)} tasks)")
    print(f"Wrote {len(by_brand)} files in {BY_BRAND}")


if __name__ == "__main__":
    main()
