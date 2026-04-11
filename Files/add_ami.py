#!/usr/bin/env python3
"""Add Acute Mesenteric Ischemia to GI / Hepatology in content.json."""

import json, sys

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

with open(PATH, "r") as f:
    data = json.load(f)

ami_topic = {
    "title": "Acute Mesenteric Ischemia",
    "subtitle": "Arterial embolism, thrombosis, venous thrombosis, NOMI — pain out of proportion to exam, CTA, heparin, surgery",
    "sections": [
        {
            "title": "Acute Management",
            "type": "steps",
            "items": [
                "!!Airway!! — assess patency; if AMS from shock or severe sepsis → intubate",
                "!!Breathing!! — SpO2, RR; tachypnea may be compensatory for metabolic acidosis (lactic acidosis from ischemic bowel)",
                "!!Circulation!! — 2 large-bore IVs; !!aggressive IV crystalloid resuscitation!! — pts are often profoundly volume-depleted",
                "!!If hypotensive: minimize vasopressors if possible!! — vasoconstrictors worsen mesenteric ischemia; use lowest effective dose if required",
                "!!Start heparin immediately once dx suspected!! — UFH bolus 80 units/kg IV → 18 units/kg/hr infusion (target aPTT 1.5-2.5× normal)",
                "!!Broad-spectrum antibiotics!! — bacterial translocation from ischemic gut; pip-tazo 4.5 g IV or meropenem 1 g IV if septic",
                "!!STAT CTA abdomen/pelvis (arterial + venous phase)!! — diagnostic study of choice (sensitivity ~94%, specificity ~95%)",
                "!!Emergent surgical consult!! — vascular surgery + general surgery + IR; do NOT delay for labs if clinical suspicion is high",
                "NPO, NG tube if vomiting/distension, Foley for UOP monitoring",
                "IV opioid analgesia — do NOT withhold pain control; fentanyl or morphine titrated to effect"
            ]
        },
        {
            "title": "Chart Check / History",
            "type": "bullets",
            "items": [
                "!!Atrial fibrillation!! — #1 risk factor for SMA embolism; check if on anticoagulation",
                "Cardiac hx — recent MI (mural thrombus), cardiomyopathy, prosthetic valves, endocarditis, ventricular aneurysm",
                "Vascular hx — PAD, prior arterial thrombosis, aortic disease",
                "Prior episodes of postprandial pain, food fear (sitophobia), weight loss → suggests chronic mesenteric ischemia (→ acute-on-chronic thrombosis)",
                "Hypercoagulable state — prior DVT/PE, Factor V Leiden, protein C/S deficiency, malignancy, OCP use",
                "Recent surgery — esp cardiac bypass (NOMI risk)",
                "ICU pt on vasopressors or w/ low cardiac output → think NOMI",
                "Anticoagulant use — type, compliance, last dose",
                "Cirrhosis / portal HTN — risk for mesenteric venous thrombosis"
            ]
        },
        {
            "title": "Exam",
            "type": "keyValue",
            "pairs": [
                {"key": "!!Classic finding!!", "value": "!!Pain out of proportion to physical exam!! — severe pain w/ benign-appearing, soft, non-tender abdomen (early)"},
                {"key": "Vitals", "value": "Tachycardia (often earliest sign); hypotension (late — suggests necrosis/sepsis); tachypnea (metabolic acidosis compensation); fever (late)"},
                {"key": "Abdomen — early", "value": "Soft, minimal tenderness, non-distended — !!deceptively benign exam despite severe pain!!"},
                {"key": "Abdomen — late", "value": "!!Peritoneal signs!! (guarding, rigidity, rebound) = bowel necrosis has likely already occurred — ominous & late finding"},
                {"key": "Bowel sounds", "value": "May be hyperactive early → absent late (ileus from necrosis)"},
                {"key": "Rectal", "value": "Heme-positive stool or frankly bloody (\"currant jelly\" stools = mucosal sloughing) — present in ~25%"},
                {"key": "General", "value": "Rapid gut emptying (forceful diarrhea) early; AMS, mottled skin, cool extremities if in shock"}
            ]
        },
        {
            "title": "Definitions",
            "type": "keyValue",
            "pairs": [
                {"key": "Acute mesenteric ischemia", "value": "Inadequate blood flow to intestines → ischemia → infarction → necrosis if untreated; !!mortality 60-80%!! overall"},
                {"key": "SMA embolism (~50%)", "value": "Thrombus lodges in SMA (usually at branch points); most common type; classically from AFib or cardiac source"},
                {"key": "SMA thrombosis (~15-25%)", "value": "Progressive atherosclerotic narrowing; often hx of chronic mesenteric ischemia; highest mortality (70-100%)"},
                {"key": "NOMI (~20%)", "value": "Non-occlusive mesenteric ischemia — low-flow state (shock, CHF, vasopressors) w/o mechanical obstruction; occurs in critically ill pts"},
                {"key": "Mesenteric venous thrombosis (~5-15%)", "value": "SMV thrombosis — most insidious onset; best prognosis (20-50% mortality); associated w/ hypercoagulable states"},
                {"key": "Ischemic colitis", "value": "Most common form of intestinal ischemia (80-85%); typically watershed areas (splenic flexure, rectosigmoid); usually self-limited"}
            ]
        },
        {
            "title": "Etiology / DDx",
            "type": "keyValue",
            "pairs": [
                {"key": "Arterial embolism", "value": "AFib, recent MI, prosthetic valves, endocarditis, ventricular aneurysm, cardiomyopathy"},
                {"key": "Arterial thrombosis", "value": "Atherosclerosis, chronic mesenteric ischemia, PAD, aortic disease/dissection"},
                {"key": "Venous thrombosis", "value": "Hypercoagulable states, malignancy, cirrhosis/portal HTN, pancreatitis, recent surgery, OCP use"},
                {"key": "NOMI", "value": "Shock (any type), CHF w/ ↓ CO, vasopressor use, cardiac bypass surgery, hemodialysis, sepsis"},
                {"key": "DDx — acute abdomen", "value": "Bowel obstruction (SBO/LBO), perforated viscus, pancreatitis, ruptured AAA, volvulus, acute cholecystitis"},
                {"key": "DDx — vascular", "value": "Aortic dissection w/ mesenteric malperfusion, renal infarction, splenic infarction"},
                {"key": "DDx — other", "value": "Ischemic colitis (usually less severe, self-limited), C. diff colitis, IBD flare, acute diverticulitis"}
            ]
        },
        {
            "title": "Labs & Orders",
            "type": "bullets",
            "items": [
                "!!Lactate!! — ↑ as ischemia progresses; !!normal lactate does NOT rule out AMI!! (can be normal early)",
                "CBC — leukocytosis w/ left shift (WBC often >15,000)",
                "BMP — metabolic acidosis (AG), ↑ BUN/Cr (prerenal from dehydration)",
                "ABG/VBG — base deficit correlates w/ severity; lactic acidosis",
                "D-dimer — elevated (sensitive but nonspecific; !!high negative predictive value!!)",
                "Phosphate — !!hyperphosphatemia!! (released from ischemic bowel mucosa — relatively specific)",
                "LDH — ↑ (nonspecific tissue necrosis marker)",
                "Amylase — may be ↑ (confuses w/ pancreatitis)",
                "LFTs — AST/ALT may ↑ if portal/hepatic flow affected",
                "Coags (PT/INR, aPTT) — baseline before heparin; DIC screen",
                "Type & screen — prepare for possible surgery",
                "Blood cultures if septic",
                "!!CTA abdomen/pelvis (arterial + venous phase)!! — study of choice; sensitivity ~94%, specificity ~95%",
                "Plain abdominal XR — often normal early; late: thumbprinting, pneumatosis intestinalis, portal venous gas, free air"
            ]
        },
        {
            "title": "Medications",
            "type": "drugTable",
            "drugs": [
                {
                    "name": "Heparin (UFH)",
                    "dose": "80 units/kg IV bolus (max 5,000 units) → 18 units/kg/hr infusion (max 1,000 units/hr)",
                    "route": "IV",
                    "contraindications": "Active hemorrhage, HIT, recent surgery (relative)",
                    "notes": "!!Start immediately once dx suspected!! — even if surgery planned, heparinize first. Target aPTT 1.5-2.5× normal (60-80 sec)"
                },
                {
                    "name": "Piperacillin-Tazobactam",
                    "dose": "4.5 g IV q6h",
                    "route": "IV",
                    "contraindications": "PCN allergy",
                    "notes": "Covers gram-negatives + anaerobes — bacterial translocation from ischemic gut. Start empirically"
                },
                {
                    "name": "Meropenem",
                    "dose": "1 g IV q8h",
                    "route": "IV",
                    "contraindications": "Carbapenem allergy",
                    "notes": "For critically ill / septic pts or if high resistance risk; alternative to pip-tazo"
                },
                {
                    "name": "Fentanyl",
                    "dose": "25-100 mcg IV q30-60 min PRN; or infusion 25-100 mcg/hr",
                    "route": "IV",
                    "contraindications": "Resp depression (monitor closely)",
                    "notes": "For analgesia — !!do NOT withhold pain control!!; hemodynamically neutral (preferred over morphine in hypotension)"
                },
                {
                    "name": "Papaverine (via IR catheter)",
                    "dose": "30-60 mg/hr continuous intra-arterial infusion via SMA catheter",
                    "route": "Intra-arterial",
                    "contraindications": "Recent stroke/MI (relative), glaucoma",
                    "notes": "Mesenteric vasodilator — used for arterial embolism & NOMI; administered via IR catheter directly into SMA"
                },
                {
                    "name": "Norepinephrine (if shock)",
                    "dose": "0.1-0.5 mcg/kg/min IV; use lowest effective dose",
                    "route": "IV",
                    "contraindications": "!!Worsens mesenteric ischemia!! — use only if necessary",
                    "notes": "Vasopressors worsen mesenteric perfusion; minimize dose; avoid pure alpha-agonists (phenylephrine) if possible"
                }
            ]
        },
        {
            "title": "Surgical / IR Interventions",
            "type": "keyValue",
            "pairs": [
                {"key": "Arterial embolism", "value": "Surgical embolectomy (mainstay) or catheter-directed tPA thrombolysis (IR); resect necrotic bowel; !!second-look laparotomy at 24-48 hrs!!"},
                {"key": "Arterial thrombosis", "value": "Angioplasty ± stenting (IR) or surgical bypass/endarterectomy; bowel resection if necrosis"},
                {"key": "Venous thrombosis", "value": "!!Anticoagulation alone is sufficient in ~95%!!; catheter-directed thrombolysis if worsening; surgery only for peritonitis/necrosis"},
                {"key": "NOMI", "value": "Transcatheter vasodilator infusion (papaverine) via SMA catheter; treat underlying cause (optimize CO, d/c vasoconstrictors); bowel resection if necrosis"},
                {"key": "Second-look laparotomy", "value": "!!Planned re-exploration at 24-48 hrs!! — standard after revascularization to reassess bowel viability; do not skip"},
                {"key": "!!Peritoneal signs = OR!!", "value": "If peritonitis present → emergent laparotomy for bowel resection; do not delay for further workup"}
            ]
        },
        {
            "title": "Ongoing Management & Pearls",
            "type": "bullets",
            "items": [
                "!!Pain out of proportion to exam is the hallmark!! — severe pain w/ soft, non-tender abdomen early; by the time peritoneal signs develop, necrosis has occurred",
                "!!Normal lactate does NOT rule out AMI!! — can be normal early; serial lactates are more useful than a single value",
                "!!Mortality is 60-80%!! — directly linked to time-to-dx & time-to-revascularization; every hour of delay ↑ mortality",
                "!!Think AMI in any pt w/ AFib + acute abdominal pain!! — SMA embolism is the most common type (~50%)",
                "!!Vasopressors worsen mesenteric ischemia!! — minimize dose; avoid phenylephrine (pure alpha); use norepinephrine at lowest effective dose",
                "NOMI occurs in !!critically ill ICU pts!! — no mechanical obstruction; caused by low-flow states + vasopressors; easy to miss",
                "MVT has the best prognosis (20-50% mortality) & most insidious onset — anticoagulation alone is sufficient in ~95%",
                "Hyperphosphatemia is a relatively specific lab marker — released from ischemic bowel mucosa",
                "!!Second-look laparotomy at 24-48 hrs is standard!! — do not skip; bowel that appeared viable initially may have infarcted"
            ]
        },
        {
            "title": "RECAP Template",
            "type": "bullets",
            "items": [
                "**R**ecognize — severe abdominal pain out of proportion to exam; AFib + abdominal pain; critically ill pt w/ abdominal pain on pressors",
                "**E**valuate — CTA abdomen/pelvis (arterial + venous), lactate, CBC, BMP, coags, phosphate, D-dimer",
                "**C**ritical actions — heparin immediately, broad-spectrum abx, aggressive IVF, emergent surgical/IR consult, minimize vasopressors",
                "**A**ssess response — pain improving? Lactate clearing? Peritoneal signs developing? Need for OR?",
                "**P**lan — ICU admission, vascular surgery + general surgery + IR; second-look laparotomy at 24-48 hrs; long-term anticoagulation (esp MVT)"
            ]
        },
        {
            "title": "Disposition",
            "type": "keyValue",
            "pairs": [
                {"key": "!!ICU — all pts!!", "value": "All AMI pts require ICU-level care; hemodynamic monitoring, anticoagulation, serial exams, serial lactates"},
                {"key": "Emergent OR", "value": "Peritoneal signs, free air, clinical deterioration despite resuscitation → emergent laparotomy"},
                {"key": "IR suite", "value": "Catheter-directed thrombolysis (embolism), angioplasty/stenting (thrombosis), papaverine infusion (NOMI)"},
                {"key": "Consults", "value": "!!Vascular surgery, general surgery, AND IR!! — all three should be involved early"},
                {"key": "Post-op", "value": "!!Second-look laparotomy at 24-48 hrs!! — standard of care after revascularization"},
                {"key": "Long-term", "value": "MVT: 6-12 months anticoagulation (consider lifelong if hypercoagulable state); arterial: address underlying cardiac source (AFib anticoagulation, etc.)"}
            ]
        }
    ]
}

# Find GI / Hepatology and append
found = False
for system in data:
    if "GI" in system["name"] or "Hepatology" in system["name"]:
        system["topics"].append(ami_topic)
        found = True
        print(f"✅ Added 'Acute Mesenteric Ischemia' to '{system['name']}' ({len(system['topics'])} topics now)")
        for t in system["topics"]:
            print(f"   - {t['title']} ({len(t['sections'])} sections)")
        break

if not found:
    print("❌ GI / Hepatology system not found!")
    sys.exit(1)

total = sum(len(s["topics"]) for s in data)
print(f"   Total topics: {total}")

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("✅ content.json written successfully")

with open(PATH, "r") as f:
    json.load(f)
print("✅ JSON validation passed")
