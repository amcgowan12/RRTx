#!/usr/bin/env python3
"""Add Myasthenic Crisis (Neurology) and Ventricular Tachycardia (Cardiovascular) to content.json."""

import json, sys

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

with open(PATH, "r") as f:
    data = json.load(f)

# ── 1. MYASTHENIC CRISIS ──
myasthenic_crisis = {
    "title": "Myasthenic Crisis",
    "subtitle": "Acute respiratory failure in MG — PLEX vs IVIG, intubation strategy, medication pitfalls",
    "sections": [
        {
            "title": "Acute Management",
            "type": "steps",
            "items": [
                "!!Assess respiratory status immediately!! — FVC, NIF, SpO2, capnography, work of breathing",
                "!!Intubation triggers!!: FVC <20 mL/kg (or <1 L), NIF weaker than -30 cmH2O, ↑ pCO2, inability to handle secretions, bulbar dysfunction w/ aspiration risk",
                "Favor !!elective over emergent intubation!! — trial BiPAP as bridge is acceptable",
                "If RSI needed: !!rocuronium at HALF dose!! (0.5-0.6 mg/kg) — MG pts are hypersensitive to non-depolarizing agents",
                "Have !!sugammadex!! available (2-4 mg/kg for reversal, 16 mg/kg for immediate reversal)",
                "If succinylcholine needed: !!DOUBLE the dose!! (1.5-2 mg/kg) — MG pts are resistant to depolarizing agents",
                "!!Discontinue pyridostigmine if intubated!! — ↑ secretions, complicates vent management; restart near extubation",
                "Identify & treat precipitant — infection (#1 trigger), medication changes, surgery, stress",
                "!!Review medication list!! — stop MG-exacerbating drugs (aminoglycosides, fluoroquinolones, beta-blockers, Mg, phenytoin)",
                "Early neurology consultation"
            ]
        },
        {
            "title": "Chart Check / History",
            "type": "bullets",
            "items": [
                "Known MG diagnosis? Duration? Antibody status (AChR vs MuSK)?",
                "Current medications — pyridostigmine dose, immunosuppressants, steroids",
                "Recent medication changes — steroids can cause transient worsening in ~50% of pts when initiated",
                "Recent infection — respiratory infection is #1 trigger; aspiration pneumonitis #2",
                "Recent surgery or anesthesia",
                "!!Medications that worsen MG!!: aminoglycosides, fluoroquinolones, macrolides, beta-blockers, CCBs, procainamide, lithium, phenytoin, magnesium, iodinated contrast",
                "Prior crisis episodes? Prior intubations? PLEX vs IVIG hx — which worked better?",
                "Thymoma hx — present in 10-15% of MG pts",
                "~20% of crises represent the !!initial MG presentation!! — consider in new-onset resp failure w/ weakness"
            ]
        },
        {
            "title": "Exam",
            "type": "keyValue",
            "pairs": [
                {"key": "Respiratory", "value": "Tachypnea, shallow breathing, pausing mid-sentence, weak cough, paradoxical breathing, orthopnea"},
                {"key": "Eyes", "value": "!!Ptosis!! (unilateral or bilateral), diplopia — present in >80% eventually; fatigable on sustained upgaze"},
                {"key": "Bulbar", "value": "Dysarthria, dysphonia (nasal voice), dysphagia, pooling secretions, weak palate elevation"},
                {"key": "Motor", "value": "Proximal > distal weakness; neck extensor weakness (\"dropped head\" sign); fatigable — worsens w/ repetition"},
                {"key": "Reflexes", "value": "!!Normal!! — distinguishes from GBS (areflexia) and Lambert-Eaton (depressed)"},
                {"key": "Sensation", "value": "!!Normal!! — if abnormal, consider alternative dx"},
                {"key": "Autonomic", "value": "!!Normal!! — distinguishes from GBS (dysautonomia) and botulism"},
                {"key": "Bedside tests", "value": "Ice pack test (↓ ptosis by ≥2 mm after 2 min ice on eyelid); single breath count <20 = resp compromise; prolonged upgaze test"}
            ]
        },
        {
            "title": "Definitions",
            "type": "keyValue",
            "pairs": [
                {"key": "Myasthenia gravis", "value": "Autoimmune disorder of the NMJ — autoantibodies against AChR (80-90%) or MuSK; weakness worsens w/ activity, improves w/ rest"},
                {"key": "Myasthenic crisis", "value": "MG exacerbation severe enough to require mechanical ventilation or airway protection; occurs in 15-20% of MG pts, most w/in first 2 yrs of dx"},
                {"key": "Cholinergic crisis", "value": "Excessive anticholinesterase medication → weakness + SLUDGE sx (miosis, ↑ secretions, fasciculations); rare w/ modern dosing"},
                {"key": "Myasthenic vs cholinergic", "value": "Myasthenic: normal pupils, minimal secretions, no fasciculations; Cholinergic: miosis, ↑↑ secretions, fasciculations"},
                {"key": "FVC", "value": "Forced vital capacity — normal ≥60 mL/kg; !!<20 mL/kg = impending resp failure!!"},
                {"key": "NIF", "value": "Negative inspiratory force — normal -80 to -100 cmH₂O; !!weaker than -30 cmH₂O = significant weakness!!"}
            ]
        },
        {
            "title": "Etiology / DDx",
            "type": "keyValue",
            "pairs": [
                {"key": "Crisis triggers", "value": "Infection (#1, >30-40%), medication changes, surgery/anesthesia, steroid initiation, stress, heat, ~50% no identifiable trigger"},
                {"key": "DDx — NMJ disorders", "value": "Lambert-Eaton (proximal leg weakness, improves w/ repetition, ↓ reflexes, associated w/ SCLC), botulism (descending paralysis, dilated pupils)"},
                {"key": "DDx — motor neuron", "value": "ALS (upper + lower motor neuron signs, fasciculations, no fatigability)"},
                {"key": "DDx — peripheral nerve", "value": "GBS (ascending paralysis, areflexia, CSF albuminocytologic dissociation, autonomic dysfunction)"},
                {"key": "DDx — other", "value": "Organophosphate toxicity (SLUDGE, miosis), stroke, MS, CNS lesion"}
            ]
        },
        {
            "title": "Labs & Orders",
            "type": "bullets",
            "items": [
                "!!Serial FVC & NIF!! — q2h minimum; most important monitoring parameters",
                "Continuous capnography — best early indicator of resp deterioration",
                "ABG/VBG — assess ventilatory status (pCO₂ >45 = concerning)",
                "CBC, BMP — electrolytes, infection markers",
                "CXR — aspiration, pneumonia (most common trigger)",
                "Blood & urine cultures if infection suspected",
                "AChR antibodies (positive in 80-90% of generalized MG; may be negative in ocular-only or MuSK-positive)",
                "MuSK antibodies — check if AChR negative",
                "TSH — thyroid disease association",
                "CT chest — thymoma evaluation if not previously done",
                "Continuous telemetry & pulse oximetry"
            ]
        },
        {
            "title": "Medications",
            "type": "drugTable",
            "drugs": [
                {
                    "name": "IVIG",
                    "dose": "0.4 g/kg/day × 5 days (total 2 g/kg)",
                    "route": "IV",
                    "contraindications": "Renal failure, IgA deficiency (anaphylaxis risk)",
                    "notes": "!!Disease-modifying!! — effect lasts 30-45 days; onset slower than PLEX (days to weeks). Easier to administer (peripheral IV ok)"
                },
                {
                    "name": "Plasmapheresis (PLEX)",
                    "dose": "5 exchanges over 10-14 days",
                    "route": "Central venous access required",
                    "contraindications": "Sepsis, hemodynamic instability, coagulopathy",
                    "notes": "!!Fastest onset!! — improvement by 2nd-3rd session; effect lasts 15-20 days. Preferred if rapid response needed"
                },
                {
                    "name": "Pyridostigmine",
                    "dose": "30-60 mg PO q4-6h (max 90 mg q4h); IV: 2-3 mg (1/30th PO dose)",
                    "route": "PO / IV",
                    "contraindications": "Cholinergic crisis, mechanical ileus",
                    "notes": "Symptomatic tx only — does not alter disease course. !!Discontinue if pt is intubated!! (↑ secretions). Restart near extubation"
                },
                {
                    "name": "Rocuronium (if RSI needed)",
                    "dose": "!!0.5-0.6 mg/kg!! (HALF standard dose)",
                    "route": "IV",
                    "contraindications": "Avoid if possible; MG pts are hypersensitive",
                    "notes": "MG pts need !!half the dose!! of non-depolarizing agents. Have sugammadex 2-4 mg/kg available for reversal"
                },
                {
                    "name": "Sugammadex",
                    "dose": "2-4 mg/kg for reversal; 16 mg/kg for immediate reversal",
                    "route": "IV",
                    "contraindications": "Severe renal impairment (limited data)",
                    "notes": "!!Keep available during intubation!! — reverses rocuronium. Critical safety net in MG intubation"
                }
            ]
        },
        {
            "title": "Ongoing Management & Pearls",
            "type": "bullets",
            "items": [
                "!!Reflexes & sensation are NORMAL in MG!! — if abnormal, reconsider dx (GBS, Lambert-Eaton, botulism)",
                "!!Do NOT rely on SpO2 alone!! — it is a LATE indicator of resp failure; FVC & NIF are far more sensitive",
                "!!Steroid initiation can transiently worsen MG in ~50% of pts!! — generally defer until after PLEX/IVIG started & pt stabilized",
                "PLEX is faster onset but requires central access; IVIG is easier to administer but slower onset — both are equally effective",
                "!!~20% of crises are the initial MG presentation!! — consider in unexplained resp failure w/ weakness & normal reflexes",
                "Ice pack test is quick bedside test: ice on closed eyelid × 2 min → ↓ ptosis by ≥2 mm = positive for MG",
                "!!Avoid Mg infusions!! — magnesium worsens NMJ transmission & can precipitate crisis",
                "Thymectomy is definitive tx for thymoma & may benefit non-thymoma MG — not an acute intervention"
            ]
        },
        {
            "title": "RECAP Template",
            "type": "bullets",
            "items": [
                "**R**ecognize — worsening weakness, bulbar sx, resp distress in known or suspected MG pt",
                "**E**valuate — serial FVC & NIF (q2h), capnography, bulbar function, identify trigger (infection, meds, surgery)",
                "**C**ritical actions — secure airway early (half-dose rocuronium + sugammadex available), stop offending meds, initiate PLEX or IVIG",
                "**A**ssess response — FVC trending up? Strength improving? Secretions manageable?",
                "**P**lan — ICU admission, neurology consult, PLEX vs IVIG completion, extubation planning, thymoma workup"
            ]
        },
        {
            "title": "Disposition",
            "type": "keyValue",
            "pairs": [
                {"key": "ICU / Neuro-ICU", "value": "Any respiratory failure or impending failure (FVC <20 mL/kg, NIF weaker than -30), intubated, rapidly declining parameters, significant bulbar dysfunction"},
                {"key": "Floor / step-down", "value": "MG exacerbation w/o respiratory failure, requiring PLEX/IVIG, stable respiratory monitoring"},
                {"key": "Discharge (w/ close neuro f/u)", "value": "Known MG w/ mild exacerbation, stable FVC/NIF, adequate PO intake, offending med identified & stopped"},
                {"key": "Consults", "value": "!!Neurology!! (early & always), Pulmonology if intubated, CT surgery if thymoma identified"}
            ]
        }
    ]
}

# ── 2. VENTRICULAR TACHYCARDIA ──
vt_topic = {
    "title": "Ventricular Tachycardia",
    "subtitle": "Wide complex tachycardia — assume VT until proven otherwise; procainamide, amiodarone, cardioversion",
    "sections": [
        {
            "title": "Acute Management",
            "type": "steps",
            "items": [
                "!!Pulseless VT → defibrillation!! — unsynchronized 200J biphasic; begin CPR per ACLS",
                "!!Unstable w/ pulse → synchronized cardioversion!! — 100-200J; sedate if conscious & time permits",
                "If !!stable monomorphic VT!!: procainamide 20-50 mg/min IV (max 17 mg/kg or 1 g) — first-line (PROCAMIO trial)",
                "Alternative for stable VT (esp w/ acute MI or ↓ EF): amiodarone 150 mg IV over 10 min",
                "If !!polymorphic VT / torsades!!: !!Mg 2 g IV!! + unsynchronized defibrillation if deteriorating + stop ALL QT-prolonging drugs",
                "If !!irregular WCT!! (possible AFib w/ WPW): !!do NOT give AV nodal blockers!! → procainamide or cardioversion",
                "Check & correct K+ (goal >4.0) and Mg2+ (goal >2.0) immediately",
                "12-lead EKG (compare to prior); troponin, BMP, digoxin level if applicable",
                "If very wide QRS (>200 ms) w/ rate <120 → think !!hyperkalemia!! → calcium, insulin/D50, bicarb",
                "If sodium channel blocker toxicity (TCA, cocaine): !!sodium bicarbonate 1-2 mEq/kg IV!!"
            ]
        },
        {
            "title": "Chart Check / History",
            "type": "bullets",
            "items": [
                "!!Cardiac hx!! — prior MI (scar-mediated VT), cardiomyopathy, CHF, EF, valvular disease",
                "Prior arrhythmia hx — VT episodes, ICD, ablation",
                "ICD present? (may see shocks or failed shocks → interrogate device)",
                "Medications — QT-prolonging drugs, digoxin, antiarrhythmics, beta-blockers",
                "Electrolyte hx — renal disease, diuretics (hypoK, hypoMg)",
                "Ischemia risk factors — known CAD, recent chest pain, prior PCI/CABG",
                "Toxicologic — TCA, cocaine, digoxin",
                "Family hx — sudden cardiac death, long QT, Brugada, HCM, ARVC",
                "Symptoms — palpitations, syncope/presyncope, chest pain, SOB, AMS"
            ]
        },
        {
            "title": "Exam",
            "type": "keyValue",
            "pairs": [
                {"key": "Vitals", "value": "HR typically >120 bpm; BP may be normal (stable VT) or ↓↓ (unstable); if HR <120 w/ wide QRS → think hyperkalemia or AIVR"},
                {"key": "!!Stability assessment!!", "value": "Hypotension, AMS, chest pain, signs of shock, acute HF → !!unstable = immediate cardioversion!!"},
                {"key": "CV", "value": "Regular tachycardia; !!cannon A waves in JVP!! (AV dissociation — pathognomonic for VT); variable S1 intensity"},
                {"key": "Lungs", "value": "Crackles if acute pulmonary edema from ↓ cardiac output"},
                {"key": "Neuro", "value": "AMS from hypoperfusion; syncope hx"},
                {"key": "Extremities", "value": "Cool, mottled if cardiogenic shock; check for ICD pocket (left anterior chest)"}
            ]
        },
        {
            "title": "Definitions",
            "type": "keyValue",
            "pairs": [
                {"key": "Ventricular tachycardia", "value": "≥3 consecutive wide QRS complexes (>120 ms) originating from the ventricles at rate >120 bpm"},
                {"key": "Monomorphic VT", "value": "Uniform QRS morphology — single re-entrant circuit (often scar-related post-MI)"},
                {"key": "Polymorphic VT", "value": "Varying QRS morphology — includes torsades de pointes (twisting of the points around baseline)"},
                {"key": "Torsades de pointes", "value": "Polymorphic VT in setting of !!prolonged QT!! — classic sinusoidal twisting pattern; tx: Mg, overdrive pacing, stop QT-prolonging drugs"},
                {"key": "NSVT", "value": "Non-sustained VT — <30 sec duration; still requires workup for structural heart disease"},
                {"key": "Sustained VT", "value": ">30 sec duration or causes hemodynamic compromise before 30 sec"},
                {"key": "Electrical storm", "value": "!!≥3 episodes of sustained VT w/in 24 hrs!! — requires escalated therapy, EP consult, consider overdrive pacing or ablation"},
                {"key": "Wide complex tachycardia", "value": "QRS ≥120 ms during tachycardia; !!80% is VT!! (>90% if known cardiac disease) — assume VT until proven otherwise"}
            ]
        },
        {
            "title": "EKG Features Favoring VT",
            "type": "keyValue",
            "pairs": [
                {"key": "!!AV dissociation!!", "value": "P waves & QRS complexes march independently — !!pathognomonic for VT!!"},
                {"key": "Fusion beats", "value": "Hybrid morphology (simultaneous ventricular + supraventricular activation) — strongly favors VT"},
                {"key": "Capture beats", "value": "Narrow QRS complex intermixed — atrial impulse \"captures\" ventricle during VT — strongly favors VT"},
                {"key": "Concordance", "value": "All precordial leads (V1-V6) showing same QRS direction (all positive or all negative) — favors VT"},
                {"key": "Extreme axis deviation", "value": "\"Northwest axis\" (negative in I and aVF) — VT"},
                {"key": "Very wide QRS", "value": ">160 ms = more likely VT; >200 ms = think hyperkalemia or Na channel blocker toxicity"},
                {"key": "Brugada criteria", "value": "Absence of RS complex in all precordial leads; RS interval >100 ms; AV dissociation; morphology criteria in V1/V6"},
                {"key": "!!If uncertain: treat as VT!!", "value": "Treating VT as SVT can be !!fatal!!; treating SVT as VT is rarely harmful"}
            ]
        },
        {
            "title": "Etiology / DDx",
            "type": "keyValue",
            "pairs": [
                {"key": "Structural heart disease", "value": "Prior MI w/ scar (most common), dilated cardiomyopathy, HCM, ARVC, valvular disease"},
                {"key": "Ischemia", "value": "Acute MI or unstable angina — VT may be presenting rhythm"},
                {"key": "Electrolyte", "value": "!!Hyperkalemia!! (very wide, rate <120), hypokalemia, hypomagnesemia"},
                {"key": "Toxicologic", "value": "Digoxin toxicity (bidirectional VT is classic), TCA OD, cocaine, QT-prolonging drugs → torsades"},
                {"key": "DDx — regular WCT", "value": "SVT w/ aberrancy (pre-existing or rate-related BBB), aflutter w/ BBB, sinus tach w/ BBB, antidromic AVRT (WPW)"},
                {"key": "DDx — irregular WCT", "value": "AFib w/ BBB, AFib w/ WPW (!!avoid AV nodal blockers!!), polymorphic VT / torsades"},
                {"key": "Other", "value": "Severe acidosis, acute HF, Brugada syndrome, long QT syndrome, catecholaminergic polymorphic VT"}
            ]
        },
        {
            "title": "Labs & Orders",
            "type": "bullets",
            "items": [
                "!!12-lead EKG!! — compare to prior; look for AV dissociation, concordance, fusion/capture beats",
                "BMP — !!K+ and Mg2+!! critically important; correct immediately if abnormal",
                "Troponin — acute ischemia may be the trigger",
                "Digoxin level if on digoxin (toxicity = bidirectional VT, accelerated junctional rhythm)",
                "ABG/VBG — metabolic acidosis can perpetuate VT",
                "CBC",
                "Continuous cardiac monitoring (!!mandatory!!)",
                "Toxicology screen if clinical suspicion (TCA, cocaine)",
                "CXR — cardiomegaly, pulmonary edema",
                "TTE — assess EF, wall motion abnormalities, structural disease (often deferred until after acute stabilization)"
            ]
        },
        {
            "title": "Medications",
            "type": "drugTable",
            "drugs": [
                {
                    "name": "Procainamide",
                    "dose": "20-50 mg/min IV until suppressed; max 17 mg/kg or 1 g total; maintenance 1-4 mg/min",
                    "route": "IV",
                    "contraindications": "Prolonged QT, CHF, renal failure",
                    "notes": "!!First-line for stable monomorphic VT!! (PROCAMIO trial: 67% termination vs 38% for amiodarone). Monitor QRS width & BP during infusion"
                },
                {
                    "name": "Amiodarone",
                    "dose": "150 mg IV over 10 min → 1 mg/min × 6 hrs (360 mg) → 0.5 mg/min × 18 hrs (540 mg)",
                    "route": "IV",
                    "contraindications": "Severe sinus node disease, 2nd/3rd degree block w/o pacer, cardiogenic shock",
                    "notes": "Preferred if !!acute MI or ↓ EF!!. Slower onset than procainamide. Total 24-hr dose ~1050 mg"
                },
                {
                    "name": "Lidocaine",
                    "dose": "1-1.5 mg/kg IV bolus; may repeat 0.5-0.75 mg/kg q5-10 min (max 3 mg/kg); infusion 1-4 mg/min",
                    "route": "IV",
                    "contraindications": "Hepatic failure, high-degree AV block",
                    "notes": "Alternative for ischemia-related VT; fewer hemodynamic effects than procainamide. ↓ dose in liver disease & elderly"
                },
                {
                    "name": "Magnesium sulfate",
                    "dose": "2 g IV over 5-10 min; may repeat once",
                    "route": "IV",
                    "contraindications": "Renal failure (monitor levels), myasthenia gravis",
                    "notes": "!!First-line for torsades de pointes!!; also replete if Mg <2.0 in any VT"
                },
                {
                    "name": "Adenosine (diagnostic)",
                    "dose": "6 mg rapid IV push → 12 mg if no response",
                    "route": "IV (rapid push)",
                    "contraindications": "!!Do NOT use for irregular WCT!! (AFib w/ WPW → VF risk)",
                    "notes": "Diagnostic trial for regular monomorphic WCT — will NOT terminate VT but may unmask underlying SVT. Safe to give in stable patient"
                },
                {
                    "name": "Sodium bicarbonate",
                    "dose": "1-2 mEq/kg IV bolus",
                    "route": "IV",
                    "contraindications": "Metabolic alkalosis",
                    "notes": "For Na channel blocker toxicity (TCA, cocaine) causing wide QRS; also for hyperkalemia w/ VT"
                }
            ]
        },
        {
            "title": "Ongoing Management & Pearls",
            "type": "bullets",
            "items": [
                "!!Assume wide complex tachycardia is VT until proven otherwise!! — 80% of WCT is VT (>90% w/ known cardiac disease)",
                "!!Treating VT as SVT can be fatal; treating SVT as VT is rarely harmful!! — when in doubt, treat as VT",
                "!!Do NOT give AV nodal blockers for irregular WCT!! (adenosine, diltiazem, digoxin, beta-blockers) — can cause VF in WPW",
                "Procainamide > amiodarone for stable VT (PROCAMIO trial) unless acute MI or ↓ EF (then amiodarone preferred)",
                "Very wide QRS (>200 ms) w/ rate <120 bpm → think !!hyperkalemia!! before VT — give calcium first",
                "!!Cannon A waves in JVP = AV dissociation = VT!! — quick bedside exam finding",
                "Bidirectional VT (alternating QRS axis) is classic for !!digoxin toxicity!! — check level, give DigiFab",
                "Electrical storm (≥3 VT episodes in 24 hrs): escalate to overdrive pacing, deep sedation, EP consult, consider ablation",
                "!!Admit ALL VT patients!! — even if successfully cardioverted; high recurrence risk + need for structural workup + ICD evaluation"
            ]
        },
        {
            "title": "RECAP Template",
            "type": "bullets",
            "items": [
                "**R**ecognize — wide complex tachycardia on monitor/EKG → assume VT; assess pulse & stability",
                "**E**valuate — 12-lead EKG (AV dissociation, concordance, fusion beats), K+/Mg2+, troponin, stability",
                "**C**ritical actions — cardiovert if unstable; procainamide or amiodarone if stable; Mg for torsades; correct electrolytes",
                "**A**ssess response — rhythm converted? Hemodynamics stable? Recurrence? Underlying cause identified?",
                "**P**lan — admit ALL VT pts; cardiology/EP consult; ICD evaluation; address underlying cause (ischemia, electrolytes, toxin)"
            ]
        },
        {
            "title": "Disposition",
            "type": "keyValue",
            "pairs": [
                {"key": "!!Admit ALL VT patients!!", "value": "Even if successfully converted — high recurrence risk; inpatient structural workup + ICD evaluation required"},
                {"key": "ICU / telemetry", "value": "All sustained VT, cardioversion/defibrillation required, electrical storm, VT w/ hemodynamic compromise, ongoing antiarrhythmic infusion"},
                {"key": "Cardiology / EP consult", "value": "All sustained VT; electrical storm; ICD evaluation; catheter ablation consideration for recurrent VT"},
                {"key": "!!Electrical storm!!", "value": "EP consult urgently; consider overdrive pacing, deep sedation (propofol/intubation), catheter ablation"},
                {"key": "!!Never discharge VT!!", "value": "No pt w/ VT should be discharged from ED — even w/ successful rhythm conversion"}
            ]
        }
    ]
}

# Insert Myasthenic Crisis into Neurology
for system in data:
    if system["name"] == "Neurology":
        system["topics"].append(myasthenic_crisis)
        print(f"✅ Added 'Myasthenic Crisis' to Neurology ({len(system['topics'])} topics now)")
        break

# Insert VT into Cardiovascular (after SVT)
for system in data:
    if system["name"] == "Cardiovascular":
        # Find SVT index and insert after it
        for i, topic in enumerate(system["topics"]):
            if "SVT" in topic["title"]:
                system["topics"].insert(i + 1, vt_topic)
                print(f"✅ Added 'Ventricular Tachycardia' to Cardiovascular at position {i + 1} ({len(system['topics'])} topics now)")
                break
        break

total = sum(len(s["topics"]) for s in data)
print(f"   Total topics: {total}")

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ content.json written successfully")

with open(PATH, "r") as f:
    json.load(f)
print("✅ JSON validation passed")
