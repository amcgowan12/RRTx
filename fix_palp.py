#!/usr/bin/env python3
"""Expand Palpitations topic in Symptoms.json to standard subsection format."""

import json, sys

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/Symptoms.json"

with open(PATH, "r") as f:
    data = json.load(f)

expanded_topic = {
    "title": "Palpitations",
    "subtitle": "Approach to arrhythmia and rate/rhythm abnormalities",
    "sections": [
        {
            "title": "Acute Management",
            "type": "steps",
            "items": [
                "!!Assess hemodynamic stability!! — BP, mental status, perfusion, chest pain, SOB",
                "If !!unstable + tachycardia!! → synchronized cardioversion (sedate if possible)",
                "If !!unstable + bradycardia!! → atropine 0.5-1 mg IV + transcutaneous pacing",
                "Get !!12-lead EKG immediately!! — do NOT treat based on monitor strip alone",
                "IV access, continuous telemetry, pulse oximetry",
                "If stable: proceed w/ systematic evaluation — hx, exam, labs, EKG interpretation",
                "Check POC glucose, K+, Mg2+ — correct immediately if abnormal"
            ]
        },
        {
            "title": "Chart Check / History",
            "type": "bullets",
            "items": [
                "Onset — sudden vs gradual? Duration? Intermittent vs sustained?",
                "Character — fast, slow, regular, irregular, \"skipping\" (ectopy), \"fluttering\" (SVT/AFib)",
                "Associated sx — chest pain, SOB, lightheadedness, syncope/presyncope, diaphoresis",
                "Triggers — exertion, caffeine, alcohol, stress, position change, Valsalva terminates it?",
                "Prior episodes — prior arrhythmia dx? Cardioversion hx? Ablation?",
                "Cardiac hx — structural heart disease, CHF, valve disease, CAD, cardiomyopathy",
                "Medications — digoxin, beta-blockers, calcium channel blockers, antiarrhythmics, QT-prolonging drugs",
                "Stimulants — caffeine, cocaine, amphetamines, energy drinks, pseudoephedrine, theophylline",
                "Thyroid disease — hyper/hypothyroid, recent thyroid medication changes",
                "Recent illness — fever, dehydration, anemia, PE risk factors",
                "Family hx — sudden cardiac death, WPW, long QT, Brugada, HCM"
            ]
        },
        {
            "title": "Exam",
            "type": "keyValue",
            "pairs": [
                {"key": "Vitals", "value": "HR (rate, regularity), BP (hypotension?), RR, SpO2, temp (fever → ↑ HR)"},
                {"key": "General", "value": "Diaphoretic, anxious, ill-appearing? Hemodynamically stable?"},
                {"key": "CV", "value": "Regular vs irregular rhythm, murmurs (valvular disease, HCM), S3 (CHF), JVD (R heart failure, PE)"},
                {"key": "Lungs", "value": "Crackles (pulmonary edema), wheezing, clear (reassuring)"},
                {"key": "Neck", "value": "Thyromegaly, JVD, cannon A waves (AV dissociation → complete heart block or VT)"},
                {"key": "Extremities", "value": "Peripheral edema, cool/mottled (poor perfusion), asymmetric leg swelling (DVT → PE)"},
                {"key": "Neuro", "value": "AMS (hypoperfusion), tremor (thyrotoxicosis), focal deficits (thromboembolism from AFib)"}
            ]
        },
        {
            "title": "Definitions",
            "type": "keyValue",
            "pairs": [
                {"key": "Palpitations", "value": "Subjective awareness of heartbeat — may be fast, slow, irregular, or \"pounding\"; NOT always arrhythmia"},
                {"key": "Narrow complex tachycardia", "value": "QRS <120 ms — supraventricular origin (sinus tach, SVT, AFib, aflutter, MAT)"},
                {"key": "Wide complex tachycardia", "value": "QRS ≥120 ms — assume !!VT until proven otherwise!! (also: SVT w/ aberrancy, pre-excitation, paced rhythm)"},
                {"key": "SVT", "value": "Supraventricular tachycardia — regular, narrow complex, 150-250 bpm; AVNRT is most common type"},
                {"key": "WPW", "value": "Wolff-Parkinson-White — accessory pathway; delta waves + short PR on baseline EKG; !!avoid AV nodal blockers in AFib + WPW!!"},
                {"key": "QTc prolongation", "value": ">500 ms = ↑ risk of torsades de pointes; check drug list, electrolytes"}
            ]
        },
        {
            "title": "EKG-Based Differential",
            "type": "keyValue",
            "pairs": [
                {
                    "key": "Irregularly irregular, no P waves",
                    "value": "AFib → rate control vs cardioversion",
                    "topicLink": "AFib / Flutter with RVR"
                },
                {
                    "key": "Regular rate ~150, sawtooth waves",
                    "value": "Atrial flutter 2:1 → rate control"
                },
                {
                    "key": "Wide complex, regular, fast",
                    "value": "!!VT until proven otherwise!! → amiodarone or cardioversion"
                },
                {
                    "key": "Narrow complex, regular, fast (150-250 bpm)",
                    "value": "SVT (AVNRT/AVRT) → vagal maneuvers, adenosine",
                    "topicLink": "SVT (Supraventricular Tachycardia)"
                },
                {
                    "key": "Irregular, 3+ P-wave morphologies",
                    "value": "MAT → treat underlying cause (COPD, hypoxia, hypomagnesemia)"
                },
                {
                    "key": "Regular, slow, P-QRS dissociation",
                    "value": "Complete heart block → pacing",
                    "topicLink": "Bradycardia"
                },
                {
                    "key": "Delta waves, short PR",
                    "value": "WPW — !!avoid AV nodal blockers!! (digoxin, CCB, adenosine) if in AFib"
                },
                {
                    "key": "Sinus tach (P before every QRS, regular, 100-150)",
                    "value": "NOT a primary arrhythmia — find the underlying cause (pain, fever, hypovolemia, PE, sepsis, anxiety)"
                },
                {
                    "key": "Frequent PACs/PVCs",
                    "value": "Usually benign; treat underlying cause; if symptomatic or PVC burden >10% → cardiology f/u"
                },
                {
                    "key": "Polymorphic VT w/ long QT",
                    "value": "!!Torsades de pointes!! → Mg 2 g IV, overdrive pacing; stop QT-prolonging drugs"
                }
            ]
        },
        {
            "title": "Etiology / DDx",
            "type": "keyValue",
            "pairs": [
                {"key": "Cardiac — arrhythmia", "value": "AFib/flutter, SVT, VT, WPW, sick sinus syndrome, heart block, PACs, PVCs"},
                {"key": "Cardiac — structural", "value": "Valvular disease (mitral), HCM, cardiomyopathy, myocarditis, pericarditis"},
                {"key": "Metabolic / electrolyte", "value": "!!Hypokalemia!!, hypomagnesemia, hypocalcemia, hyperthyroidism, hypoglycemia"},
                {"key": "Medications / drugs", "value": "Stimulants (caffeine, cocaine, amphetamines), theophylline, pseudoephedrine, digoxin toxicity, QT-prolonging drugs"},
                {"key": "Volume / hemodynamic", "value": "Dehydration, anemia, hemorrhage, PE, sepsis — sinus tach as compensatory response"},
                {"key": "Endocrine", "value": "Hyperthyroidism / thyroid storm, pheochromocytoma"},
                {"key": "Psychiatric", "value": "Panic attack, anxiety — dx of exclusion after cardiac causes r/o"},
                {"key": "!!Red flags!!", "value": "Syncope w/ palpitations, exertional palpitations, family hx sudden cardiac death, structural heart disease, wide complex tachycardia"}
            ]
        },
        {
            "title": "Labs & Orders",
            "type": "bullets",
            "items": [
                "!!12-lead EKG!! — cornerstone of evaluation; compare to prior EKG if available",
                "BMP — K+, Mg2+ (correct if low; both ↑ arrhythmia risk)",
                "CBC — anemia can cause sinus tachycardia",
                "TSH — hyperthyroidism is treatable & common cause",
                "Troponin — if chest pain or concern for ischemia-driven arrhythmia",
                "Digoxin level — if on digoxin (toxicity causes multiple arrhythmia types)",
                "BNP/NT-proBNP — if concern for heart failure",
                "D-dimer / CTA — if PE suspected (sinus tach + pleuritic pain + leg swelling)",
                "Review medication list for QT-prolonging drugs (www.crediblemeds.org)",
                "TTE — if new arrhythmia, suspected structural heart disease, or unexplained",
                "Continuous telemetry monitoring",
                "Holter or event monitor if intermittent & no acute arrhythmia captured on EKG"
            ]
        },
        {
            "title": "Medications",
            "type": "drugTable",
            "drugs": [
                {
                    "name": "Adenosine",
                    "dose": "6 mg rapid IV push → 12 mg if no response → 12 mg; use proximal IV + rapid saline flush",
                    "route": "IV (rapid push)",
                    "contraindications": "!!AFib w/ WPW!! (can cause VF), 2nd/3rd degree heart block, asthma (relative)",
                    "notes": "Diagnostic & therapeutic for SVT (AVNRT/AVRT). Warn pt: transient chest tightness, flushing. Half-life ~10 sec"
                },
                {
                    "name": "Metoprolol",
                    "dose": "5 mg IV over 2 min; may repeat q5 min × 3 doses; then 25-50 mg PO q6h",
                    "route": "IV / PO",
                    "contraindications": "Acute decompensated CHF, 2nd/3rd degree block, severe bradycardia, cocaine use, WPW",
                    "notes": "Rate control for AFib/flutter, SVT refractory to adenosine, sinus tach from thyrotoxicosis"
                },
                {
                    "name": "Diltiazem",
                    "dose": "0.25 mg/kg IV over 2 min (typically 15-20 mg); may repeat 0.35 mg/kg; then infusion 5-15 mg/hr",
                    "route": "IV",
                    "contraindications": "!!WPW + AFib!!, HFrEF, hypotension, 2nd/3rd degree block",
                    "notes": "Rate control for AFib/flutter. Effective if BB contraindicated or insufficient"
                },
                {
                    "name": "Amiodarone",
                    "dose": "150 mg IV over 10 min → 1 mg/min × 6 hrs → 0.5 mg/min × 18 hrs",
                    "route": "IV",
                    "contraindications": "Severe sinus node disease, 2nd/3rd degree block w/o pacer, cardiogenic shock",
                    "notes": "For !!stable wide complex tachycardia (VT)!! or rate/rhythm control in AFib. Safe in structural heart disease"
                },
                {
                    "name": "Magnesium sulfate",
                    "dose": "2 g IV over 15 min",
                    "route": "IV",
                    "contraindications": "Renal failure (monitor levels), myasthenia gravis",
                    "notes": "!!First-line for torsades de pointes!!; also replete if Mg <2.0 (↑ arrhythmia risk)"
                },
                {
                    "name": "Atropine",
                    "dose": "0.5-1 mg IV q3-5 min; max 3 mg",
                    "route": "IV",
                    "contraindications": "Glaucoma (relative), may worsen ischemia",
                    "notes": "For symptomatic bradycardia. Temporizing — prepare for pacing if no response"
                }
            ]
        },
        {
            "title": "Ongoing Management & Pearls",
            "type": "bullets",
            "items": [
                "!!Sinus tachycardia is NOT a primary arrhythmia!! — always find the underlying cause (sepsis, PE, hypovolemia, pain, anxiety)",
                "!!Wide complex tachycardia = VT until proven otherwise!! — treating VT as SVT can be fatal",
                "!!AFib + WPW: avoid AV nodal blockers!! (adenosine, diltiazem, digoxin, metoprolol) → can cause VF; use procainamide or cardioversion",
                "Check K+ & Mg2+ early — both hypokalemia & hypomagnesemia are easily correctable arrhythmia causes",
                "Regular rate exactly ~150 bpm → think aflutter 2:1 (may need to unmask w/ adenosine to see flutter waves)",
                "Panic attacks / anxiety are a dx of exclusion — always r/o cardiac causes first",
                "If palpitations + syncope or family hx of sudden death → high-risk; requires inpatient workup + cardiology consult",
                "Digoxin toxicity can cause almost ANY arrhythmia — always check level if pt is on digoxin",
                "Caffeine, energy drinks, cocaine, amphetamines are common precipitants — ask specifically"
            ]
        },
        {
            "title": "RECAP Template",
            "type": "bullets",
            "items": [
                "**R**ecognize — palpitations w/ hemodynamic assessment; EKG rhythm identification",
                "**E**valuate — 12-lead EKG, K+/Mg2+, TSH, troponin; stable vs unstable?",
                "**C**ritical actions — cardiovert if unstable; adenosine for SVT; amiodarone for stable VT; correct electrolytes",
                "**A**ssess response — rhythm converted? Rate controlled? Hemodynamics stable? Symptoms resolved?",
                "**P**lan — telemetry monitoring, cardiology consult if new arrhythmia or structural disease, outpt Holter if intermittent"
            ]
        },
        {
            "title": "Disposition",
            "type": "keyValue",
            "pairs": [
                {"key": "ICU / step-down", "value": "Hemodynamic instability, VT, wide complex tachycardia, cardioversion required, new heart block, torsades"},
                {"key": "Telemetry floor", "value": "New AFib, controlled SVT, recurrent symptomatic arrhythmia, new structural findings on TTE"},
                {"key": "Outpt / discharge", "value": "Benign PACs/PVCs, sinus tach w/ identified & treated cause, known AFib w/ adequate rate control, normal workup"},
                {"key": "Cardiology consult", "value": "New arrhythmia, syncope w/ palpitations, structural heart disease, WPW, wide complex tachycardia, family hx sudden death"},
                {"key": "Follow-up", "value": "Holter/event monitor for intermittent sx, outpt TTE if not done inpatient, medication titration"}
            ]
        }
    ]
}

# Find Palpitations and replace
found = False
for system in data:
    for i, topic in enumerate(system["topics"]):
        if topic["title"] == "Palpitations":
            system["topics"][i] = expanded_topic
            found = True
            print(f"✅ Replaced Palpitations in '{system['name']}'")
            print(f"   Old: 3 sections → New: {len(expanded_topic['sections'])} sections")
            for s in expanded_topic["sections"]:
                print(f"   - {s['title']}")
            break
    if found:
        break

if not found:
    print("❌ Palpitations topic not found!")
    sys.exit(1)

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Symptoms.json written successfully")

# Validate
with open(PATH, "r") as f:
    json.load(f)
print("✅ JSON validation passed")
