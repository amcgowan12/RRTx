#!/usr/bin/env python3
"""Add Fever / New Infection topic to Sepsis / Infectious in content.json."""

import json, sys

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

with open(PATH, "r") as f:
    data = json.load(f)

new_topic = {
    "title": "Fever / New Infection",
    "subtitle": "Workup of new fever — infectious vs non-infectious etiologies, febrile neutropenia, MRSA risk factors",
    "sections": [
        {
            "title": "Acute Management",
            "type": "steps",
            "items": [
                "Assess vitals — is pt in !!shock!!? (tachycardia, hypotension, AMS, mottled skin)",
                "If septic: activate !!Hour-1 Bundle!! — cultures, broad abx, 30 mL/kg IVF, lactate, vasopressors if needed",
                "Identify any known infectious disease or immunocompromised state",
                "Is pt currently receiving antibiotics? (breakthrough fever = inadequate coverage or new source)",
                "!!Check ANC!! — if <500/mm³ → !!febrile neutropenia is a medical emergency!! → immediate broad-spectrum abx",
                "Obtain !!blood cultures from 2 sites (4 bottles total) BEFORE starting antimicrobials!!",
                "If pt looks septic: do not wait for workup results — start wide-spectrum abx immediately",
                "If pt is immunocompetent, not sick-appearing, & no obvious source: antibiotics may be held until workup results return",
                "Remove/change lines or catheters if possible — send tips for culture (removing infected line is often sufficient)"
            ]
        },
        {
            "title": "Chart Check / History",
            "type": "bullets",
            "items": [
                "Recent hospitalization or surgery — HAP, wound infection, line infection risk",
                "Current antibiotics — what spectrum? Duration? Breakthrough fever?",
                "Immunosuppression — chemotherapy, transplant, chronic steroids, HIV, biologics",
                "Indwelling devices — central line, Foley catheter, prosthetic joints/valves, VP shunt",
                "Recent procedures — LP, bronchoscopy, surgery, intubation",
                "Travel hx, sick contacts, animal exposures",
                "MRSA risk factors: recent hospitalization/abx, HIV, IVDU/needle sharing, MSM, hemodialysis, incarceration, long-term care facility, military service, shared sports equipment",
                "Medication changes — drug fever is a dx of exclusion",
                "DVT/PE risk factors — thrombosis can cause fever"
            ]
        },
        {
            "title": "Exam",
            "type": "keyValue",
            "pairs": [
                {"key": "Vitals", "value": "Fever >38.0°C (>100.4°F) oral; !!expected ↑ HR ~16 bpm per °C!! above baseline"},
                {"key": "General", "value": "Toxic-appearing? Rigors? Diaphoresis? AMS?"},
                {"key": "Skin", "value": "Wound erythema/drainage, cellulitis, decubitus ulcers, rashes, petechiae, line-site erythema/purulence"},
                {"key": "Lungs", "value": "Crackles, ↓ breath sounds, consolidation — pneumonia (esp if on ventilator)"},
                {"key": "Abdomen", "value": "Tenderness, distension, peritoneal signs — abscess, C. diff colitis, peritonitis"},
                {"key": "GU", "value": "CVA tenderness (pyelonephritis), suprapubic tenderness; !!simple UTI should NOT cause fever!! — think pyelo/urosepsis"},
                {"key": "Neuro", "value": "Nuchal rigidity, photophobia, focal deficits — meningitis/encephalitis/brain abscess"},
                {"key": "Lines/devices", "value": "Erythema, purulence, or tenderness at catheter sites; check all indwelling devices"},
                {"key": "Joints", "value": "Swelling, warmth, effusion — septic arthritis, prosthetic joint infection"},
                {"key": "!!Rectal exam!!", "value": "!!Do NOT take rectal temp in neutropenic pts!! — risk of bacteremia from mucosal disruption"}
            ]
        },
        {
            "title": "Definitions",
            "type": "keyValue",
            "pairs": [
                {"key": "Fever", "value": ">38.0°C (>100.4°F) oral. Single oral temp ≥38.3°C or sustained ≥38.0°C over 1 hr"},
                {"key": "Febrile neutropenia", "value": "!!Medical emergency!!: fever + ANC <500/mm³ (or <1000 & expected to ↓ to <500). Start broad abx w/in 60 min"},
                {"key": "Bacteremia", "value": "Bacteria in bloodstream; may be transient (procedural) or sustained (endocarditis, line infection)"},
                {"key": "Drug fever", "value": "Fever caused by medication — dx of exclusion; common culprits: abx, heparin, anticonvulsants (carbamazepine, phenytoin, phenobarbital), allopurinol, clozapine"},
                {"key": "Post-op fever", "value": "Common in first 48-72 hrs — often non-infectious (atelectasis, inflammatory response); !!dx of exclusion!! — still workup infectious causes"},
                {"key": "MRSA", "value": "Methicillin-resistant Staph aureus — consider empiric vancomycin if risk factors present"}
            ]
        },
        {
            "title": "Etiology / DDx",
            "type": "keyValue",
            "pairs": [
                {"key": "!!#1 Infectious!! (most common)", "value": "Always consider first; non-infectious causes are dx of exclusion"},
                {"key": "Pneumonia", "value": "CAP, HAP (>48 hrs hospitalization), aspiration — ↑ risk if on ventilator"},
                {"key": "Urinary", "value": "Pyelonephritis / urosepsis — esp w/ indwelling catheter; !!simple UTI should NOT cause fever!!"},
                {"key": "Abdominal", "value": "Abscess, wound infection, pancreatitis, C. diff colitis, peritonitis"},
                {"key": "Line / device infection", "value": "Central line, PICC, catheter, prosthetic joint/valve, VP shunt"},
                {"key": "Other infectious", "value": "Endocarditis, meningitis, osteomyelitis, septic arthritis, skin/soft tissue infection"},
                {"key": "Thrombosis", "value": "DVT, PE — can present w/ fever alone"},
                {"key": "Inflammation w/o infection", "value": "Hematoma, gout/pseudogout, autoimmune disease flare, pancreatitis"},
                {"key": "Medication", "value": "Drug fever — antimicrobials, heparin, anticonvulsants, allopurinol, clozapine, etc."},
                {"key": "Other non-infectious", "value": "Serotonin syndrome, neuroleptic malignant syndrome, malignant hyperthermia, thyroid storm, adrenal insufficiency, transfusion reaction"},
                {"key": "Post-op fever", "value": "Dx of exclusion — common in first 48-72 hrs; still must r/o surgical site infection, PE, atelectasis"}
            ]
        },
        {
            "title": "Labs & Orders",
            "type": "bullets",
            "items": [
                "!!Blood cultures from 2 sites (4 bottles total)!! — obtain BEFORE starting abx",
                "CBC w/ differential — trend WBC; !!check ANC!! (febrile neutropenia if <500)",
                "BMP — lytes, creatinine, glucose",
                "Lactate — ↑ in sepsis (>2 mmol/L = concern; >4 mmol/L = severe)",
                "CXR — pneumonia screening",
                "Urinalysis + urine culture — esp if catheter in place",
                "Sputum culture if productive cough or intubated",
                "Use clinical judgment for additional workup based on suspected source:",
                "  • Wound/decubitus swab if wound erythema or drainage",
                "  • LP if meningitis in differential (fever + AMS + nuchal rigidity)",
                "  • C. diff toxin if diarrhea (esp after recent abx)",
                "  • LFTs if hepatobiliary source suspected",
                "  • Procalcitonin — may help distinguish bacterial vs viral (>0.5 ng/mL suggests bacterial)",
                "  • Blood smear if travel hx (malaria)",
                "  • CT abdomen/pelvis if intra-abdominal source suspected"
            ]
        },
        {
            "title": "Medications",
            "type": "drugTable",
            "drugs": [
                {
                    "name": "Acetaminophen",
                    "dose": "650 mg PO/PR q4h PRN or 1 g IV q6h",
                    "route": "PO / PR / IV",
                    "contraindications": "Liver disease, APAP allergy",
                    "notes": "For comfort; !!note: antipyretics make trending temp difficult!! — use judiciously if monitoring fever curve"
                },
                {
                    "name": "Vancomycin",
                    "dose": "15-20 mg/kg IV q8-12h (adjust for renal function); load 25-30 mg/kg for severe infection",
                    "route": "IV",
                    "contraindications": "Monitor troughs/AUC",
                    "notes": "Add if MRSA risk factors, line infection, skin/soft tissue, or severe sepsis w/ unknown source"
                },
                {
                    "name": "Piperacillin-Tazobactam",
                    "dose": "4.5 g IV q6h (extended infusion over 4 hrs preferred)",
                    "route": "IV",
                    "contraindications": "PCN allergy (cross-reactivity low but assess severity)",
                    "notes": "Broad-spectrum — covers gram-positives, gram-negatives, anaerobes. !!First-line for febrile neutropenia!!"
                },
                {
                    "name": "Ceftriaxone",
                    "dose": "1-2 g IV q24h",
                    "route": "IV",
                    "contraindications": "Severe cephalosporin allergy",
                    "notes": "Good empiric choice for CAP, UTI/pyelo, unknown source in immunocompetent pt"
                },
                {
                    "name": "Meropenem",
                    "dose": "1-2 g IV q8h",
                    "route": "IV",
                    "contraindications": "Carbapenem allergy; caution w/ valproic acid (↓ levels)",
                    "notes": "Reserve for high-resistance risk, ESBL organisms, or failure of pip-tazo"
                },
                {
                    "name": "Micafungin",
                    "dose": "100 mg IV q24h",
                    "route": "IV",
                    "contraindications": "Echinocandin allergy",
                    "notes": "Add empiric antifungal if persistent fever despite broad abx in neutropenic pt (>4-7 days)"
                }
            ]
        },
        {
            "title": "Ongoing Management & Pearls",
            "type": "bullets",
            "items": [
                "!!#1 cause of fever is infectious!! — non-infectious causes are a dx of exclusion",
                "!!Simple UTI should NOT cause fever!! — if febrile w/ positive UA, think pyelonephritis or urosepsis",
                "!!Febrile neutropenia (ANC <500) is a medical emergency!! — broad abx w/in 60 min, do NOT take rectal temp",
                "!!Remove/change suspicious lines & catheters!! — send tips for culture; removing the infected line is often enough",
                "If immunocompetent, not sick-appearing, & no obvious source → may hold abx until culture results return",
                "If pt looks septic → do not delay — pan-culture & start wide-spectrum abx; ensure good IV access & bolus NS PRN",
                "Drug fever: suspect if fever persists despite adequate abx coverage & negative workup — trial drug withdrawal",
                "Post-op fever in first 48 hrs is often non-infectious but !!must still rule out surgical site infection, PE, aspiration!!",
                "Antipyretics (APAP) provide comfort but obscure fever curve — use judiciously when trending temp matters",
                "Abx selection should be based on institution's antibiogram & local resistance patterns",
                "!!Severe sepsis / septic shock: see Sepsis & Septic Shock topic for full Hour-1 Bundle & vasopressor management!!"
            ]
        },
        {
            "title": "RECAP Template",
            "type": "bullets",
            "items": [
                "**R**ecognize — fever >38.0°C; is pt septic? Check ANC for neutropenia",
                "**E**valuate — full exam looking for source; lines, wounds, lungs, abdomen, GU, neuro",
                "**C**ritical actions — cultures BEFORE abx; broad abx if septic/neutropenic; remove suspect lines",
                "**A**ssess response — fever trending? Cultures growing? WBC trending? Hemodynamics stable?",
                "**P**lan — narrow abx based on culture data; address source control; ID consult if complex"
            ]
        },
        {
            "title": "Disposition",
            "type": "keyValue",
            "pairs": [
                {"key": "ICU", "value": "Septic shock, febrile neutropenia w/ hemodynamic instability, resp failure, AMS"},
                {"key": "Floor / step-down", "value": "Stable pt w/ identified source on appropriate abx; febrile neutropenia w/o instability"},
                {"key": "Source control", "value": "Surgical consult for abscess drainage, wound debridement; IR for percutaneous drainage"},
                {"key": "Consults", "value": "ID for complex infections, resistant organisms, immunocompromised pts; Surgery/IR for source control"},
                {"key": "F/u cultures", "value": "Repeat blood cultures 48-72 hrs if bacteremia to document clearance; daily until negative for S. aureus bacteremia"}
            ]
        }
    ]
}

# Find Sepsis / Infectious system and insert the new topic right after Sepsis & Septic Shock
found = False
for system in data:
    if system["name"] == "Sepsis / Infectious":
        # Insert after the first topic (Sepsis & Septic Shock)
        insert_idx = 1  # After Sepsis & Septic Shock
        system["topics"].insert(insert_idx, new_topic)
        found = True
        print(f"✅ Added 'Fever / New Infection' to Sepsis / Infectious at position {insert_idx}")
        print(f"   Sepsis / Infectious now has {len(system['topics'])} topics:")
        for t in system["topics"]:
            print(f"   - {t['title']} ({len(t['sections'])} sections)")
        break

if not found:
    print("❌ Sepsis / Infectious system not found!")
    sys.exit(1)

total = sum(len(s["topics"]) for s in data)
print(f"   Total topics across all systems: {total}")

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ content.json written successfully")

# Validate
with open(PATH, "r") as f:
    json.load(f)
print("✅ JSON validation passed")
