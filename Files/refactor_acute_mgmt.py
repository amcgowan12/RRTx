#!/usr/bin/env python3
"""
Refactor Acute Management sections across all topics in content.json and Symptoms.json.
Keep only ABCs/primary stability assessment items; move everything else to Management.
"""

import json
import re
import sys
import os
import copy

BASE = os.path.dirname(os.path.abspath(__file__))
CONTENT_PATH = os.path.join(BASE, "Rapid Response", "Data", "content.json")
SYMPTOMS_PATH = os.path.join(BASE, "Rapid Response", "Data", "Symptoms.json")

# ---------------------------------------------------------------------------
# Classification patterns: items matching ANY of these stay in Acute Management
# ---------------------------------------------------------------------------
KEEP_PATTERNS = [
    # ABCs core
    re.compile(r'!!Airway!!', re.I),
    re.compile(r'!!Breathing!!', re.I),
    re.compile(r'!!Circulation!!', re.I),
    re.compile(r'\bABCs?\b'),
    re.compile(r'\bairway\b', re.I),
    re.compile(r'\bintubat', re.I),
    re.compile(r'\bcricothyrotomy', re.I),
    re.compile(r'\bGCS\b'),
    re.compile(r'\bmental status\b', re.I),
    re.compile(r'\baltered\b', re.I),
    re.compile(r'\bAMS\b'),
    re.compile(r'\bconsciou', re.I),
    re.compile(r'\bunresponsive\b', re.I),

    # Vitals and monitoring
    re.compile(r'\bSpO2\b', re.I),
    re.compile(r'\bpulse ox', re.I),
    re.compile(r'\bBP\b'),
    re.compile(r'\bblood pressure\b', re.I),
    re.compile(r'\bvital', re.I),
    re.compile(r'\btelemetry\b', re.I),
    re.compile(r'\bcardiac monitor', re.I),
    re.compile(r'\bmonitor\b', re.I),
    re.compile(r'\bEtCO2\b', re.I),

    # Oxygen / ventilation escalation
    re.compile(r'\bO2\b'),
    re.compile(r'\boxygen\b', re.I),
    re.compile(r'\bNRB\b'),
    re.compile(r'\bHFNC\b'),
    re.compile(r'\bBiPAP\b', re.I),
    re.compile(r'\bCPAP\b'),
    re.compile(r'\bNIPPV\b', re.I),
    re.compile(r'\bhigh.flow\b', re.I),
    re.compile(r'\bvent(ilat|ilation)\b', re.I),
    re.compile(r'\bhypox', re.I),

    # Emergency procedures
    re.compile(r'\bCPR\b'),
    re.compile(r'\bcardioversion\b', re.I),
    re.compile(r'\bdefibrillat', re.I),
    re.compile(r'\bpacing\b', re.I),
    re.compile(r'\bpericardiocentesis\b', re.I),
    re.compile(r'\bchest (tube|decompress)', re.I),
    re.compile(r'\bneedle decompress', re.I),
    re.compile(r'\bthoracotomy\b', re.I),
    re.compile(r'\bchest compress', re.I),

    # IV access
    re.compile(r'\bIV access\b', re.I),
    re.compile(r'\blarge.bore\b', re.I),
    re.compile(r'\bIV\b.*\baccess\b', re.I),
    re.compile(r'\bIO\b.*\baccess\b', re.I),
    re.compile(r'\b2\s*large\b', re.I),

    # Escalation calls
    re.compile(r'\bcall\b.*\b(ICU|anesth|surgery|cardiology|neurosurg|neuro|pulmonol|GI|ENT|IR|interventional|CT surg|LVAD|coordinator|transplant|poison|tox|MHAUS|RT)\b', re.I),
    re.compile(r'\bCall\b.*\bRT\b'),
    re.compile(r'\bnotify\b', re.I),
    re.compile(r'\bcode\b.*\b(blue|status|team|stroke)\b', re.I),
    re.compile(r'\bactivate\b.*\b(code|rapid|stroke|STEMI|MTP|trauma)\b', re.I),
    re.compile(r'\bcontact\b.*\b(ICU|anesth|surgery|cardiology|neurosurg|specialist|coordinator|ECMO)\b', re.I),
    re.compile(r'\btransfer\b.*\bICU\b', re.I),
    re.compile(r'\bcall code stroke\b', re.I),

    # Immediate reversals / antidotes
    re.compile(r'\bnaloxone\b', re.I),
    re.compile(r'\bdextrose\b', re.I),
    re.compile(r'\bD50\b'),
    re.compile(r'\bD10\b'),
    re.compile(r'\bMTP\b'),
    re.compile(r'\breversal\b', re.I),
    re.compile(r'\breverse\b.*\banticoag', re.I),

    # Assessment / look
    re.compile(r'\bhow do they look\b', re.I),
    re.compile(r'\bassess\b', re.I),
    re.compile(r'\bperfus', re.I),
    re.compile(r'\bshock\b', re.I),
    re.compile(r'\bhemodynamic', re.I),
    re.compile(r'\bunstable\b', re.I),
    re.compile(r'\bstab(le|ility)\b', re.I),
    re.compile(r'\brespiratory\s+(distress|failure|arrest)\b', re.I),
    re.compile(r'\bcardiac arrest\b', re.I),
    re.compile(r'\bcoding\b', re.I),
    re.compile(r'\bperi.?arrest\b', re.I),
    re.compile(r'\bcrash', re.I),

    # Positioning
    re.compile(r'\bTrendelenburg\b', re.I),
    re.compile(r'\bbleeding\s+side\s+down\b', re.I),
    re.compile(r'\bHOB\b'),
    re.compile(r'\bhead\s+of\s+bed\b', re.I),
    re.compile(r'\bposition\b.*\b(comfort|upright|supine|lateral|left)\b', re.I),
    re.compile(r'\blegs?\s+elevat', re.I),

    # Stop offending agent / remove trigger
    re.compile(r'\bstop\b.*\b(med|agent|drug|infusion|offend|serotonerg|causative|trigger|transfusion|ALL)\b', re.I),
    re.compile(r'\bStop ALL\b', re.I),
    re.compile(r'\bremove\b.*\b(trigger|cause|offend|source)\b', re.I),
    re.compile(r'\bdiscontinue\b', re.I),

    # Resuscitation / fluid bolus (in stabilization context)
    re.compile(r'\bresuscitat', re.I),
    re.compile(r'\bbolus\b.*\b(NS|normal saline|LR|lactated|fluid|crystalloid)\b', re.I),
    re.compile(r'\b(NS|LR|fluid)\b.*\bbolus\b', re.I),
    re.compile(r'\bfluid\b.*\b(resus|challeng)\b', re.I),
    re.compile(r'\bIV\s+fluid\b', re.I),

    # Epinephrine IM (anaphylaxis = immediate stabilization)
    re.compile(r'\bepinephrine\b.*\bIM\b', re.I),
    re.compile(r'\bIM\b.*\bepinephrine\b', re.I),
    re.compile(r'\bepi\b.*\b0\.3\b', re.I),

    # Glucose check / NPO
    re.compile(r'\bPOC\s+glucose\b', re.I),
    re.compile(r'\bfingerstick\b', re.I),
    re.compile(r'\bglucose\b.*\bASAP\b', re.I),
    re.compile(r'\bNPO\b'),
    re.compile(r'\bmake\s+NPO\b', re.I),

    # Suction / airway adjuncts
    re.compile(r'\bsuction\b', re.I),
    re.compile(r'\bjaw\s*thrust\b', re.I),
    re.compile(r'\bchin\s*lift\b', re.I),
    re.compile(r'\boral\s*airway\b', re.I),
    re.compile(r'\bnasal\s*airway\b', re.I),

    # EKG / ECG (initial assessment tool)
    re.compile(r'\bE[CK]G\b'),
    re.compile(r'\b12.lead\b', re.I),

    # Type and screen / crossmatch (preparing for hemorrhage)
    re.compile(r'\btype\s*(and|&)\s*(screen|cross)', re.I),
    re.compile(r'\bcrossmatch\b', re.I),

    # Hemorrhage control
    re.compile(r'\btourniquet\b', re.I),
    re.compile(r'\bdirect\s+pressure\b', re.I),
    re.compile(r'\bbleeding\b.*\bcontrol\b', re.I),
    re.compile(r'\bcontrol\b.*\bbleeding\b', re.I),

    # CXR (initial stabilization imaging)
    re.compile(r'\bCXR\b'),
    re.compile(r'\bchest\s*(x-?ray|film)\b', re.I),

    # LVAD specific ABCs
    re.compile(r'\bLVAD\s+hum\b', re.I),
    re.compile(r'\bpump\s+(fail|stop)\b', re.I),

    # Heimlich / foreign body
    re.compile(r'\bHeimlich\b', re.I),
    re.compile(r'\babdominal\s+thrust\b', re.I),
    re.compile(r'\bforeign\s+body\b', re.I),

    # Labs (stat initial labs are part of primary assessment)
    re.compile(r'\bstat\b.*\b(labs?|CBC|BMP|ABG|lactate|troponin|VBG)\b', re.I),
    re.compile(r'\b(labs?|CBC|BMP|ABG|lactate|troponin)\b.*\bstat\b', re.I),
    re.compile(r'\bpoint.of.care\b', re.I),

    # Don't/avoid (safety warnings during stabilization)
    re.compile(r'\bavoid\b.*\b(positive pressure|succinylcholine|agitat)\b', re.I),
    re.compile(r'\bdo\s+NOT\b', re.I),

    # Red flags / emergent workup triggers
    re.compile(r'\bred\s+flag', re.I),
    re.compile(r'\bemergent\b', re.I),

    # Cooling / temperature (immediate intervention)
    re.compile(r'\bcool(ing)?\b.*\b(blanket|measure|ice|active)\b', re.I),
    re.compile(r'\btemp(erature)?\b.*\b>\s*\d', re.I),

    # Seizure acute
    re.compile(r'\bseizure\b.*\b(protect|safety|active)\b', re.I),
    re.compile(r'\bprotect\b.*\b(airway|head)\b', re.I),

    # TTE / bedside echo (immediate diagnostic)
    re.compile(r'\bTTE\b'),
    re.compile(r'\bbedside\b.*\b(echo|ultrasound|US)\b', re.I),
    re.compile(r'\bPOCUS\b', re.I),
    re.compile(r'\bFAST\b'),
]


def classify_item(text):
    """Return 'keep' if item is ABCs/primary stability, 'move' if disease-specific."""
    for pattern in KEEP_PATTERNS:
        if pattern.search(text):
            return 'keep'
    return 'move'


def get_items(section):
    """Get the list of items from a section regardless of type."""
    stype = section.get("type", "")
    if stype in ("steps", "bullets"):
        return section.get("items", section.get("steps", []))
    return []


def set_items(section, items):
    """Set items back on the section."""
    stype = section.get("type", "")
    if "items" in section:
        section["items"] = items
    elif "steps" in section:
        section["steps"] = items
    elif stype == "steps":
        section["steps"] = items
    elif stype == "bullets":
        section["items"] = items


def find_insert_index(sections):
    """Find the best index to insert a new Management section."""
    acute_idx = None
    etiology_idx = None
    definitions_idx = None
    exam_idx = None
    orders_idx = None
    ongoing_idx = None
    existing_mgmt_idx = None

    for i, sec in enumerate(sections):
        title = sec.get("title", "").strip()
        title_lower = title.lower()
        if title == "Acute Management":
            acute_idx = i
        elif "etiology" in title_lower or "ddx" in title_lower:
            etiology_idx = i
        elif title_lower == "definitions":
            definitions_idx = i
        elif title_lower == "exam":
            exam_idx = i
        elif title_lower == "orders":
            orders_idx = i
        elif "ongoing" in title_lower and "management" in title_lower:
            ongoing_idx = i
        elif title_lower == "management":
            existing_mgmt_idx = i

    # If there's already a Management section, insert right before it
    if existing_mgmt_idx is not None:
        return existing_mgmt_idx

    # Insert after Etiology/DDx if present
    if etiology_idx is not None:
        return etiology_idx + 1

    # Insert after Definitions
    if definitions_idx is not None:
        return definitions_idx + 1

    # Insert after Exam
    if exam_idx is not None:
        return exam_idx + 1

    # Insert before Ongoing Management
    if ongoing_idx is not None:
        return ongoing_idx

    # Insert before Orders
    if orders_idx is not None:
        return orders_idx

    # Fallback: right after Acute Management
    if acute_idx is not None:
        return acute_idx + 1

    return 1


def process_topic(topic, dry_run=False):
    """Process a single topic. Returns (changed, log_lines)."""
    title = topic.get("title", "Unknown")
    sections = topic.get("sections", [])
    log = []

    # Find Acute Management section
    acute_idx = None
    for i, sec in enumerate(sections):
        if sec.get("title", "").strip() == "Acute Management":
            acute_idx = i
            break

    if acute_idx is None:
        return False, [f"  [{title}] No Acute Management section found — skipped"]

    acute_sec = sections[acute_idx]
    stype = acute_sec.get("type", "")

    # Only process steps/bullets types
    if stype not in ("steps", "bullets"):
        return False, [f"  [{title}] Acute Management is type '{stype}' — skipped"]

    items = get_items(acute_sec)
    if not items:
        return False, [f"  [{title}] Acute Management has no items — skipped"]

    # Classify each item
    keep_items = []
    move_items = []
    for item in items:
        classification = classify_item(item)
        if classification == 'keep':
            keep_items.append(item)
        else:
            move_items.append(item)

    # Safety: keep at least 3 items
    while len(keep_items) < 3 and move_items:
        keep_items.append(move_items.pop(0))

    # Nothing to move?
    if not move_items:
        log.append(f"  [{title}] All {len(items)} items classified as ABCs — no changes")
        return False, log

    log.append(f"  [{title}] {len(keep_items)} kept, {len(move_items)} moved")
    for item in keep_items:
        log.append(f"    KEEP: {item[:80]}{'...' if len(item) > 80 else ''}")
    for item in move_items:
        log.append(f"    MOVE: {item[:80]}{'...' if len(item) > 80 else ''}")

    if dry_run:
        return True, log

    # Update Acute Management section
    set_items(acute_sec, keep_items)

    # Find or create Management section for moved items
    # Check if a Management section already exists
    mgmt_idx = None
    for i, sec in enumerate(sections):
        t = sec.get("title", "").strip().lower()
        if t == "management":
            mgmt_idx = i
            break

    if mgmt_idx is not None:
        mgmt_sec = sections[mgmt_idx]
        mgmt_type = mgmt_sec.get("type", "")

        if mgmt_type in ("steps", "bullets"):
            # Compatible type — prepend moved items
            existing = get_items(mgmt_sec)
            set_items(mgmt_sec, move_items + existing)
            log.append(f"    → Prepended {len(move_items)} items to existing Management ({mgmt_type})")
        else:
            # Incompatible type (keyValue, drugTable) — create new steps section before it
            new_sec = {
                "title": "Management",
                "type": "steps",
                "steps": move_items
            }
            # Rename the existing one so we don't have duplicate titles
            sections[mgmt_idx]["title"] = "Management Details"
            sections.insert(mgmt_idx, new_sec)
            log.append(f"    → Created new Management (steps) before existing Management ({mgmt_type}, renamed to 'Management Details')")
    else:
        # No Management section — create one
        insert_idx = find_insert_index(sections)
        new_sec = {
            "title": "Management",
            "type": "steps",
            "steps": move_items
        }
        sections.insert(insert_idx, new_sec)
        log.append(f"    → Created new Management section at index {insert_idx}")

    return True, log


def process_file(filepath, dry_run=False):
    """Process all topics in a JSON file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    total_changed = 0
    total_topics = 0
    all_logs = []
    filename = os.path.basename(filepath)
    all_logs.append(f"\n{'='*60}")
    all_logs.append(f"Processing: {filename}")
    all_logs.append(f"{'='*60}")

    for system in data:
        system_name = system.get("name", "Unknown")
        all_logs.append(f"\n--- {system_name} ---")

        for topic in system.get("topics", []):
            total_topics += 1
            changed, logs = process_topic(topic, dry_run=dry_run)
            all_logs.extend(logs)
            if changed:
                total_changed += 1

    all_logs.append(f"\n  TOTAL: {total_changed}/{total_topics} topics modified")

    if not dry_run:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        all_logs.append(f"  Written to: {filepath}")

    return all_logs


def main():
    dry_run = '--dry-run' in sys.argv
    mode = "DRY RUN" if dry_run else "LIVE"
    print(f"\n=== Acute Management Refactor ({mode}) ===\n")

    logs = []
    for path in [CONTENT_PATH, SYMPTOMS_PATH]:
        if os.path.exists(path):
            logs.extend(process_file(path, dry_run=dry_run))
        else:
            logs.append(f"\nFile not found: {path}")

    for line in logs:
        print(line)

    if not dry_run:
        # Validate
        print("\n--- Validation ---")
        for path in [CONTENT_PATH, SYMPTOMS_PATH]:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"  ✓ {os.path.basename(path)} — valid JSON")
            except json.JSONDecodeError as e:
                print(f"  ✗ {os.path.basename(path)} — INVALID: {e}")


if __name__ == "__main__":
    main()
