#!/usr/bin/env python3
"""Add ABCs-focused Acute Management as first section for all topics missing it."""

import json, sys

CONTENT_PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"
SYMPTOMS_PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/Symptoms.json"

# ── New Acute Management sections for content.json topics ──

acute_sections = {
    "LVAD Emergencies": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — assess patency; if GCS <8 or unable to protect airway → intubate",
            "!!Breathing!! — SpO2, RR, auscultate; apply supplemental O2 if hypoxic",
            "!!Circulation!! — !!DO NOT rely on NIBP or pulse ox!! — LVAD pts may have no palpable pulse & no SpO2 reading",
            "!!Auscultate for LVAD hum!! — continuous hum = device running; absent hum = pump failure → EMERGENCY",
            "!!Check MAP via arterial line or manual Doppler BP!! — target MAP 70-80 mmHg",
            "Obtain LVAD parameters: speed (RPM), flow, pulsatility index, power",
            "!!If unresponsive w/ no LVAD hum: start CPR!! — chest compressions ARE safe in LVAD pts (risk of dislodgement is theoretical)",
            "IV access (avoid left arm if driveline on left); labs, ECG, CXR",
            "!!Contact LVAD coordinator & CT surgery immediately!! — they should be involved in ALL LVAD emergencies"
        ]
    },
    "Sepsis & Septic Shock": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — assess patency; intubate if GCS <8, unable to protect airway, or respiratory failure",
            "!!Breathing!! — SpO2, RR; supplemental O2; if hypoxic → HFNC or NIPPV; intubate if refractory",
            "!!Circulation!! — 2 large-bore IVs; !!30 mL/kg crystalloid (LR preferred) within first 3 hrs!!",
            "!!If MAP <65 after fluid resuscitation → start norepinephrine!! (can start peripherally while awaiting central access)",
            "!!Measure lactate!! — repeat if initial >2 mmol/L; target ≥10% clearance at 6 hrs",
            "!!Blood cultures × 2 sites (4 bottles) BEFORE antibiotics!! — do NOT delay abx >45 min for cultures",
            "!!Broad-spectrum antibiotics within 1 hour of recognition!! — each hour delay ↑ mortality by ~4%",
            "POC glucose, BMP, CBC, coags, CXR, UA",
            "Source identification — lung, urine, abdomen, skin/soft tissue, lines",
            "If refractory shock on norepinephrine: add vasopressin 0.04 units/min; consider stress-dose hydrocortisone 50 mg IV q6h"
        ]
    },
    "Acute Kidney Injury": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — assess patency; severe uremia or volume overload can cause AMS or pulmonary edema → may need intubation",
            "!!Breathing!! — SpO2, RR; if pulmonary edema (crackles, ↑ WOB) → sit upright, O2, consider NIPPV or IV furosemide",
            "!!Circulation!! — assess volume status: hypovolemic (pre-renal) vs euvolemic vs hypervolemic (cardiorenal)",
            "!!Check K+!! — hyperkalemia is the most immediately life-threatening complication → ECG, treat if K+ >5.5 or EKG changes",
            "If hyperkalemia w/ EKG changes: !!calcium gluconate 3 g IV!! → insulin 10 units + D50 → albuterol nebs",
            "Foley catheter — r/o urinary obstruction (post-renal); check bladder volume w/ bladder scan or POCUS",
            "If hypovolemic: IV crystalloid bolus; if hypervolemic: hold fluids, consider diuresis",
            "!!Urgent dialysis indications (AEIOU)!!: Acidosis (refractory), Electrolytes (refractory hyperK), Ingestion (toxic), Overload (refractory pulmonary edema), Uremia (encephalopathy, pericarditis, bleeding)",
            "Hold nephrotoxins — NSAIDs, ACEi/ARBs, aminoglycosides, contrast; dose-adjust renally cleared meds"
        ]
    },
    "Massive GI Bleed": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if massive hematemesis, AMS, or inability to protect airway → !!intubate early!! (blood in airway = aspiration risk)",
            "!!Breathing!! — SpO2, supplemental O2; monitor for aspiration",
            "!!Circulation!! — 2 large-bore IVs (≥16G) or IO access; start NS/LR wide open",
            "!!Activate massive transfusion protocol (MTP)!! if hemodynamically unstable or ongoing brisk hemorrhage",
            "Transfuse pRBCs immediately — do NOT wait for type & cross if actively hemorrhaging; use O-neg or uncrossmatched",
            "Target 1:1:1 ratio (pRBCs : FFP : platelets) per MTP",
            "!!Assess hemodynamic status!! — tachycardia, hypotension, AMS = !!shock!! → aggressive resuscitation",
            "Reverse anticoagulation if applicable — see Anticoagulation Reversal topic",
            "GI consult for emergent endoscopy (upper); IR consult if unable to scope or massive ongoing hemorrhage",
            "Keep pt NPO; place NG tube if upper GI bleed suspected (guides timing of endoscopy)"
        ]
    },
    "Diabetic Ketoacidosis (DKA)": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if GCS <8 or unable to protect airway → intubate; !!CAUTION: Kussmaul respirations are compensatory!! — if intubating, match high RR & tidal volume to avoid worsening acidosis",
            "!!Breathing!! — SpO2, RR; Kussmaul breathing (deep, rapid) is expected compensatory mechanism — do NOT suppress w/ sedation",
            "!!Circulation!! — 2 large-bore IVs; !!NS 1-1.5 L/hr for first 1-2 hrs!! (avg deficit 5-9 L); reassess volume status then switch to 250-500 mL/hr",
            "!!Check K+ BEFORE starting insulin!! — if K+ <3.3, replete K+ FIRST (insulin drives K+ intracellularly → fatal hypokalemia)",
            "If K+ ≥3.3: start !!regular insulin 0.1 units/kg/hr IV infusion!! (or 0.14 units/kg/hr w/o bolus)",
            "!!Monitor glucose q1h, BMP q2-4h!! — when glucose <200-250, add D5 to IVF & ↓ insulin to 0.02-0.05 units/kg/hr",
            "Replete K+ aggressively — add 20-40 mEq KCl per liter of IVF; target K+ 4-5 mEq/L",
            "!!Do NOT give bicarb!! unless pH <6.9 (worsens intracellular acidosis & hypokalemia)",
            "!!Do NOT stop insulin until anion gap closes!! — not based on glucose alone",
            "Search for precipitant: infection (#1), medication non-compliance, new-onset DM, MI, pancreatitis"
        ]
    },
    "Massive Hemorrhage / MTP": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if AMS, massive hematemesis, or hemodynamic collapse → intubate early; RSI w/ hemodynamically neutral agents (ketamine, avoid propofol in shock)",
            "!!Breathing!! — SpO2, supplemental O2; monitor for aspiration if upper GI source",
            "!!Circulation!! — !!2 large-bore IVs (≥16G), IO, or rapid infuser access!!; start crystalloid wide open while blood products prepared",
            "!!Activate MTP immediately!! — do NOT wait for labs to confirm hemorrhage if clinical picture is clear",
            "Transfuse O-neg or uncrossmatched pRBCs while type & cross pending",
            "!!Goal 1:1:1 ratio!! (pRBCs : FFP : platelets); give TXA 1 g IV over 10 min w/in first 3 hrs of hemorrhage",
            "!!Assess & treat the lethal triad!!: hypothermia (warm fluids, blankets), acidosis (resuscitate, limit crystalloid), coagulopathy (blood products, TXA, factor replacement)",
            "Identify source & achieve source control — surgical consult, GI for endoscopy, IR for embolization, OB for postpartum hemorrhage",
            "!!Permissive hypotension!!: target SBP 80-90 mmHg until source control achieved (except in TBI — target SBP >100)"
        ]
    },
    "Anticoagulation Reversal": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — assess patency; if intracranial hemorrhage w/ ↓ GCS → intubate for airway protection",
            "!!Breathing!! — SpO2; if massive hemoptysis or pulmonary hemorrhage → intubate, position bleeding side down",
            "!!Circulation!! — 2 large-bore IVs; IV crystalloid; type & cross; activate MTP if life-threatening hemorrhage",
            "!!Identify the anticoagulant!! — warfarin, heparin, enoxaparin, rivaroxaban, apixaban, dabigatran, etc.",
            "!!STAT labs!!: INR/PT, PTT, fibrinogen, CBC w/ platelets, type & screen",
            "!!Hold ALL anticoagulants & antiplatelets immediately!!",
            "For !!warfarin!!: 4-factor PCC (Kcentra) 25-50 units/kg IV + vitamin K 10 mg IV (PCC works in minutes; vitamin K takes 6-24 hrs)",
            "For !!dabigatran!!: idarucizumab (Praxbind) 5 g IV",
            "For !!rivaroxaban/apixaban!!: andexanet alfa (Andexxa) or 4-factor PCC 50 units/kg if andexanet unavailable",
            "For !!heparin!!: protamine sulfate 1 mg per 100 units heparin given in last 2-3 hrs (max 50 mg)",
            "!!Do NOT delay reversal for labs!! if life-threatening hemorrhage — give empiric reversal based on known agent"
        ]
    }
}

# ── New Acute Management sections for Symptoms.json topics ──

symptom_sections = {
    "Hemoptysis": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if massive hemoptysis (>100-600 mL/24h): !!intubate early!! w/ largest ETT possible; death is from asphyxiation, NOT exsanguination",
            "!!Position pt w/ BLEEDING side down!! — protects contralateral lung from aspiration of blood",
            "!!Breathing!! — supplemental O2, continuous SpO2; suction airway as needed",
            "!!Circulation!! — 2 large-bore IVs, type & screen; if massive → activate MTP",
            "Call interventional pulmonology AND IR simultaneously for massive hemoptysis",
            "If intubating: consider selective intubation of unaffected bronchus or use bronchial blocker",
            "!!Reverse anticoagulation!! immediately if on blood thinners",
            "CXR and CT chest w/ contrast to identify source"
        ]
    },
    "Headache": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if GCS <8 or rapidly declining consciousness → intubate; consider ↑ ICP (avoid succinylcholine if possible)",
            "!!Breathing!! — SpO2, supplemental O2; if ↑ ICP suspected → target PaCO2 35-40 (brief hyperventilation to 30-35 only if herniating)",
            "!!Circulation!! — IV access; BP assessment — !!SBP >220 or DBP >120 w/ HA = hypertensive emergency!!",
            "!!Red flags → emergent workup!!: sudden \"thunderclap\" onset, worst HA of life, focal neuro deficits, fever + meningismus, ↓ LOC, anticoagulation, immunocompromised, age >50 w/ new HA",
            "If thunderclap HA: !!STAT non-contrast head CT!! → if negative → LP for xanthochromia (r/o SAH)",
            "If focal deficits: consider stroke alert (CT, CTA)",
            "If fever + nuchal rigidity: empiric meningitis tx BEFORE LP (vanc + ceftriaxone + dexamethasone)",
            "If signs of ↑ ICP/herniation: HOB 30°, mannitol 1 g/kg IV or hypertonic saline 23.4% 30 mL, neurosurgery STAT"
        ]
    },
    "Abdominal Pain": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — assess patency; if AMS or active vomiting w/ aspiration risk → position laterally, suction, consider intubation",
            "!!Breathing!! — SpO2, RR; peritonitis or distension can impair diaphragm excursion → ↓ tidal volumes",
            "!!Circulation!! — 2 large-bore IVs; !!assess for shock!! (tachycardia, hypotension, AMS, pallor) → aggressive IVF resuscitation",
            "If peritoneal signs (rigid abdomen, rebound, guarding): !!surgical consult STAT!! — do NOT delay for imaging",
            "If hemodynamically unstable + abdominal pain: think ruptured AAA, ruptured ectopic, massive GI bleed, splenic rupture → emergent imaging/OR",
            "Analgesics — IV morphine or fentanyl for pain control (does NOT mask surgical findings in modern practice)",
            "NPO if surgical abdomen suspected",
            "STAT labs: CBC, BMP, lipase, LFTs, lactate, coags, UA, pregnancy test (all women of reproductive age)"
        ]
    },
    "Nausea & Vomiting": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if ↓ LOC or persistent vomiting → position laterally to prevent aspiration; suction PRN",
            "!!Breathing!! — SpO2; assess for aspiration pneumonitis (tachypnea, crackles, hypoxia after vomiting episode)",
            "!!Circulation!! — IV access; assess hydration status (tachycardia, dry mucous membranes, ↓ UOP, orthostatic hypotension)",
            "IV crystalloid bolus (NS or LR) if signs of dehydration or ↓ PO intake",
            "!!Check K+, Mg2+, glucose!! — vomiting causes hypokalemia & metabolic alkalosis; correct immediately",
            "Antiemetic: ondansetron 4 mg IV (!!check QTc first — avoid if QTc >500 ms!!)",
            "Evaluate for surgical emergency: SBO (distension, obstipation), appendicitis, pancreatitis",
            "!!Red flags!!: bilious emesis (obstruction), hematemesis (GI bleed), projectile (↑ ICP), severe abdominal pain (surgical abdomen)"
        ]
    },
    "Edema": {
        "title": "Acute Management",
        "type": "steps",
        "items": [
            "!!Airway!! — if anasarca w/ upper airway edema or angioedema → assess for stridor, prepare for advanced airway",
            "!!Breathing!! — SpO2, RR; !!pulmonary edema!!: sit upright, O2, NIPPV (BiPAP/CPAP); IV furosemide if volume overloaded",
            "!!Circulation!! — BP, HR; assess for decompensated heart failure (JVD, crackles, S3, hepatojugular reflux)",
            "!!If acute pulmonary edema!!: furosemide 40-80 mg IV (or 2.5× home PO dose); nitroglycerin if SBP >100; BiPAP",
            "If hypotensive + edema: consider cardiogenic shock (poor forward flow) → inotropes, NOT more diuretics",
            "Assess for DVT if unilateral leg edema (asymmetric, painful, warm) → Doppler US urgently",
            "Check BMP (renal function, K+), albumin, BNP/NT-proBNP, UA (proteinuria → nephrotic syndrome)",
            "Determine etiology: cardiac (CHF), hepatic (cirrhosis/ascites), renal (nephrotic/nephritic), venous (DVT), medication-related"
        ]
    }
}

# ── Process content.json ──
with open(CONTENT_PATH, "r") as f:
    content = json.load(f)

content_fixed = 0
for system in content:
    for topic in system["topics"]:
        if topic["title"] in acute_sections:
            new_section = acute_sections[topic["title"]]
            topic["sections"].insert(0, new_section)
            content_fixed += 1
            print(f"✅ [content.json] Added Acute Management to '{topic['title']}' (now {len(topic['sections'])} sections)")

with open(CONTENT_PATH, "w") as f:
    json.dump(content, f, indent=2, ensure_ascii=False)

print(f"\n   Fixed {content_fixed} topics in content.json")

# ── Process Symptoms.json ──
with open(SYMPTOMS_PATH, "r") as f:
    symptoms = json.load(f)

symptom_fixed = 0
for system in symptoms:
    for topic in system["topics"]:
        if topic["title"] in symptom_sections:
            new_section = symptom_sections[topic["title"]]
            topic["sections"].insert(0, new_section)
            symptom_fixed += 1
            print(f"✅ [Symptoms.json] Added Acute Management to '{topic['title']}' (now {len(topic['sections'])} sections)")

with open(SYMPTOMS_PATH, "w") as f:
    json.dump(symptoms, f, indent=2, ensure_ascii=False)

print(f"\n   Fixed {symptom_fixed} topics in Symptoms.json")
print(f"   Total fixed: {content_fixed + symptom_fixed}")

# ── Validate both files ──
with open(CONTENT_PATH, "r") as f:
    json.load(f)
print("✅ content.json validation passed")

with open(SYMPTOMS_PATH, "r") as f:
    json.load(f)
print("✅ Symptoms.json validation passed")
