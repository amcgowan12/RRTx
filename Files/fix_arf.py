#!/usr/bin/env python3
"""Replace Acute Respiratory Failure with comprehensive version using standard sections."""

import json

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

with open(PATH, "r") as f:
    data = json.load(f)

new_topic = {
    "title": "Acute Respiratory Failure",
    "subtitle": "Hypoxic & hypercapnic — O2 escalation, NIPPV, intubation indications, vent settings",
    "sections": [
        {
            "title": "Acute Management",
            "type": "steps",
            "items": [
                "!!Airway!! — is the airway patent? Look, listen, feel; suction if secretions/blood; jaw thrust if obstructed; call for airway help early",
                "!!Breathing!! — RR, SpO2, work of breathing, accessory muscle use, paradoxical breathing, ability to speak in full sentences",
                "!!Start O2 immediately!! — NRB 15 L/min if in distress; titrate down once stable; do NOT withhold O2 while figuring out the cause",
                "!!Circulation!! — HR, BP, perfusion; tachycardia is common (compensatory); hypotension suggests tension PTX, massive PE, or cardiogenic shock",
                "Attach continuous pulse oximetry + cardiac monitor",
                "!!Rapid O2 escalation if NRB insufficient!!: HFNC (up to 60 L/min, FiO2 up to 100%) → BiPAP/CPAP → intubation",
                "!!If GCS <8, absent gag, or unable to protect airway → intubate!!",
                "!!If SpO2 <88% despite HFNC/NIPPV → intubate!!",
                "Obtain ABG/VBG — determines hypoxic vs hypercapnic vs mixed failure",
                "POC glucose, 12-lead ECG, portable CXR — order simultaneously while stabilizing"
            ]
        },
        {
            "title": "Chart Check / History",
            "type": "bullets",
            "items": [
                "Onset — sudden (PE, PTX, aspiration, flash pulm edema) vs gradual (COPD, CHF, pneumonia)",
                "Baseline lung disease — COPD, asthma, ILD, OSA; baseline O2 requirements? Home BiPAP/CPAP?",
                "Cardiac hx — CHF (EF?), valvular disease, recent MI, orthopnea, PND",
                "Recent intubation or extubation — post-extubation stridor, laryngeal edema",
                "Infection signs — fever, cough, sputum (pneumonia, COVID, influenza)",
                "VTE risk — immobility, surgery, cancer, DVT hx, pregnancy, OCP (PE)",
                "Medications — sedatives, opioids (resp depression), beta-blockers, neuromuscular agents",
                "Neuromuscular disease — MG, GBS, ALS, spinal cord injury (diaphragm weakness)",
                "Trauma — rib fractures (flail chest), PTX, hemothorax, pulmonary contusion",
                "Allergies / anaphylaxis — bronchospasm, angioedema",
                "Code status / goals of care — !!clarify before intubation if possible!!"
            ]
        },
        {
            "title": "Exam",
            "type": "keyValue",
            "pairs": [
                {"key": "Vitals", "value": "SpO2 <90% on RA or PaO2 <60 mmHg = hypoxic failure; RR >30 or <8; tachycardia (compensatory); hypotension (tension PTX, PE, shock)"},
                {"key": "General", "value": "Tripoding, accessory muscle use, nasal flaring, diaphoresis = severe; can't speak in full sentences = impending failure; !!silent chest in asthma = ominous!!"},
                {"key": "Airway", "value": "Stridor (upper obstruction — croup, angioedema, FB, post-extubation), drooling, muffled voice"},
                {"key": "Lungs — crackles b/l", "value": "Pulmonary edema (CHF), pneumonia, ARDS, aspiration"},
                {"key": "Lungs — wheezing", "value": "Asthma, COPD, bronchospasm, anaphylaxis; !!absent wheezing in severe asthma = poor air movement!!"},
                {"key": "Lungs — ↓ breath sounds unilateral", "value": "!!Pneumothorax!! (± tracheal deviation), large pleural effusion, mainstem intubation"},
                {"key": "Lungs — clear", "value": "PE (clear lungs + hypoxia), neuromuscular weakness, metabolic acidosis (Kussmaul breathing)"},
                {"key": "CV", "value": "JVD + crackles = CHF; JVD + ↓ BS + tracheal deviation = tension PTX; JVD + clear lungs = PE or tamponade"},
                {"key": "Extremities", "value": "Unilateral leg swelling (DVT → PE), b/l edema (CHF), cyanosis (severe hypoxia)"},
                {"key": "Neuro", "value": "AMS from hypoxia or hypercapnia (CO2 narcosis); asterixis (CO2 retention); ↓ NIF in NM disease"}
            ]
        },
        {
            "title": "Etiology / DDx",
            "type": "keyValue",
            "pairs": [
                {"key": "!!Type 1 — Hypoxemic!! (PaO2 <60)", "value": "Failure of oxygenation; ↓ PaO2 w/ normal or ↓ PaCO2 (initially); A-a gradient usually elevated"},
                {"key": "Pulmonary edema", "value": "Cardiogenic (CHF, flash pulm edema, valvular) or non-cardiogenic (ARDS, neurogenic)"},
                {"key": "Pneumonia", "value": "CAP, HAP, VAP, aspiration; viral (COVID, influenza); opportunistic if immunocompromised"},
                {"key": "PE", "value": "Clear lungs + hypoxia + tachycardia + risk factors; massive PE = hypotension"},
                {"key": "Pneumothorax", "value": "Spontaneous, traumatic, iatrogenic; tension PTX = hypotension + tracheal deviation → !!needle decompression!!"},
                {"key": "ARDS", "value": "B/l infiltrates, PaO2/FiO2 <300, not fully explained by cardiac failure; common triggers: sepsis, aspiration, pneumonia, pancreatitis, transfusion (TRALI)"},
                {"key": "!!Type 2 — Hypercapnic!! (PaCO2 >45)", "value": "Failure of ventilation; ↑ PaCO2 ± ↓ PaO2; pH ↓ if acute"},
                {"key": "COPD exacerbation", "value": "Most common cause of hypercapnic failure; wheezing, prolonged expiration, ↑ work of breathing"},
                {"key": "Asthma (severe)", "value": "Status asthmaticus — wheezing → silent chest = ominous; ↑ PaCO2 in asthma = impending arrest"},
                {"key": "Neuromuscular", "value": "MG crisis, GBS, ALS, spinal cord injury, OD (opioids, benzos) — ↓ respiratory drive or muscle weakness"},
                {"key": "Obesity hypoventilation", "value": "BMI >30 + daytime hypercapnia; often overlaps w/ OSA; worsens during sleep/sedation"},
                {"key": "Upper airway obstruction", "value": "Angioedema, anaphylaxis, FB aspiration, croup, epiglottitis, Ludwig angina, post-extubation laryngeal edema"}
            ]
        },
        {
            "title": "Labs & Orders",
            "type": "bullets",
            "items": [
                "!!ABG/VBG!! — defines type: PaO2 <60 = hypoxic; PaCO2 >45 = hypercapnic; calculate A-a gradient & P/F ratio",
                "!!Portable CXR!! — infiltrates (pneumonia, edema, ARDS), PTX, effusion, cardiomegaly",
                "12-lead ECG — RV strain (PE), ischemia (ACS causing flash pulm edema), dysrhythmia",
                "BNP/NT-proBNP — differentiates cardiogenic (CHF) from pulmonary cause (BNP >500 pg/mL suggests CHF)",
                "CBC — ↑ WBC (infection), anemia (↓ O2 carrying capacity)",
                "BMP — electrolytes, renal function, anion gap (metabolic acidosis)",
                "Troponin — if ACS or massive PE suspected",
                "Lactate — tissue hypoperfusion, shock",
                "D-dimer — if PE suspected (age-adjusted: age × 10 for pts >50)",
                "Procalcitonin — bacterial vs viral (>0.5 suggests bacterial; useful in COPD exacerbation abx decision)",
                "!!POCUS!! — B-lines (pulmonary edema), lung sliding (PTX), IVC (volume status), cardiac function (EF, RV dilation)",
                "CTA chest — if PE suspected & pt can tolerate",
                "Sputum culture — if pneumonia, intubated, or immunocompromised"
            ]
        },
        {
            "title": "O2 Escalation & Ventilation Strategy",
            "type": "keyValue",
            "pairs": [
                {"key": "Nasal cannula", "value": "1-6 L/min (FiO2 ~24-44%); for mild hypoxia; comfortable, allows eating/talking"},
                {"key": "Simple face mask", "value": "6-10 L/min (FiO2 ~40-60%); minimum 5 L/min to prevent CO2 rebreathing"},
                {"key": "Non-rebreather (NRB)", "value": "10-15 L/min (FiO2 ~70-90%); reservoir bag must stay inflated; first-line for acute distress"},
                {"key": "HFNC", "value": "Up to 60 L/min, FiO2 up to 100%; provides PEEP effect (~1 cmH2O per 10 L/min); humidified; tolerated well; !!first-line for hypoxic failure if NRB insufficient!!"},
                {"key": "CPAP", "value": "Continuous positive pressure; !!first-line for acute cardiogenic pulmonary edema!!; ↑ FRC, ↓ preload/afterload, ↓ work of breathing"},
                {"key": "BiPAP", "value": "IPAP + EPAP; !!first-line for COPD exacerbation w/ hypercapnia!!; typical start: IPAP 10-12, EPAP 5; titrate IPAP for ventilation (CO2), EPAP for oxygenation"},
                {"key": "!!Intubation indications!!", "value": "GCS <8, unable to protect airway, SpO2 <88% despite max non-invasive support, pH <7.25 w/ rising PaCO2 despite BiPAP, respiratory fatigue, hemodynamic instability"},
                {"key": "Post-intubation vent settings", "value": "AC mode; TV 6-8 mL/kg IBW (!!6 mL/kg if ARDS!!); RR 14-18; FiO2 100% initially → titrate to SpO2 92-96%; PEEP 5 → titrate using ARDSNet table if ARDS"}
            ]
        },
        {
            "title": "Medications",
            "type": "drugTable",
            "drugs": [
                {
                    "name": "Albuterol",
                    "dose": "2.5 mg neb q20 min × 3 or continuous neb; MDI 4-8 puffs q20 min",
                    "route": "Neb / MDI",
                    "contraindications": "Tachyarrhythmias (relative)",
                    "notes": "For bronchospasm (asthma, COPD, anaphylaxis). Continuous nebs for severe. Add ipratropium 0.5 mg for COPD"
                },
                {
                    "name": "Methylprednisolone",
                    "dose": "125 mg IV (asthma/COPD); or prednisone 40-60 mg PO",
                    "route": "IV / PO",
                    "contraindications": "Active fungal infection (relative)",
                    "notes": "For asthma/COPD exacerbation; onset 4-6 hrs; give early. 5-day course typically sufficient"
                },
                {
                    "name": "Furosemide",
                    "dose": "40-80 mg IV (or 2.5× home PO dose); may repeat or start infusion 5-20 mg/hr",
                    "route": "IV",
                    "contraindications": "Hypovolemia, severe hypokalemia",
                    "notes": "For cardiogenic pulmonary edema; onset 5-15 min IV. Monitor K+, Mg2+, UOP"
                },
                {
                    "name": "Nitroglycerin",
                    "dose": "0.4 mg SL q5 min × 3; or infusion 5-200 mcg/min IV",
                    "route": "SL / IV",
                    "contraindications": "SBP <100, PDE5 inhibitor use, severe aortic stenosis",
                    "notes": "For flash pulmonary edema w/ HTN; ↓ preload + afterload; very effective in hypertensive pulm edema"
                },
                {
                    "name": "Epinephrine",
                    "dose": "0.3-0.5 mg IM (1:1000) q5-15 min for anaphylaxis; neb 2.25% racemic epi for stridor",
                    "route": "IM / Neb",
                    "contraindications": "None absolute in anaphylaxis",
                    "notes": "!!First-line for anaphylaxis w/ bronchospasm!!; racemic epi for croup/post-extubation stridor"
                },
                {
                    "name": "Ketamine (RSI)",
                    "dose": "1-2 mg/kg IV push",
                    "route": "IV",
                    "contraindications": "Severe HTN, ↑ ICP (relative)",
                    "notes": "Preferred induction agent for asthma/bronchospasm (bronchodilator); hemodynamically stable; dissociative dose"
                },
                {
                    "name": "Rocuronium (RSI)",
                    "dose": "1.2 mg/kg IV",
                    "route": "IV",
                    "contraindications": "MG (use half dose + sugammadex available)",
                    "notes": "Paralytic for RSI; onset 45-60 sec; reversible w/ sugammadex. Preferred over succinylcholine in most cases"
                },
                {
                    "name": "Magnesium sulfate",
                    "dose": "2 g IV over 20 min",
                    "route": "IV",
                    "contraindications": "Renal failure (monitor levels), MG",
                    "notes": "Adjunct for severe asthma refractory to albuterol + steroids; bronchodilator via smooth muscle relaxation"
                }
            ]
        },
        {
            "title": "Ongoing Management & Pearls",
            "type": "bullets",
            "items": [
                "!!Do NOT withhold O2 in COPD!! — hypoxia kills faster than CO2 retention; target SpO2 88-92% in known CO2 retainers, but treat hypoxia first",
                "!!Silent chest in asthma = near-arrest!! — no air movement; if PaCO2 is normal or rising in acute asthma = !!impending respiratory arrest!!",
                "!!Clear lungs + hypoxia!! = think PE, NM weakness, or metabolic acidosis (Kussmaul breathing)",
                "!!BiPAP for COPD, CPAP for CHF!! — BiPAP provides pressure support to ↓ WOB & blow off CO2; CPAP ↓ preload/afterload in CHF",
                "HFNC is well-tolerated & provides ~1 cmH2O PEEP per 10 L/min — good bridge therapy; better tolerated than NIPPV in many pts",
                "!!Post-intubation hypotension!! — consider tension PTX (bilateral breath sounds?), auto-PEEP (disconnect vent briefly), ↓ preload from positive pressure, sedation-induced vasodilation",
                "!!Lung-protective ventilation for ARDS!!: TV 6 mL/kg IBW, plateau pressure <30 cmH2O, PEEP per ARDSNet table, permissive hypercapnia OK",
                "!!In asthma/COPD intubation!!: low RR (8-12), long expiratory time (I:E 1:4-5), watch for auto-PEEP (breath stacking); disconnect vent if hemodynamic collapse",
                "POCUS is faster than CXR — B-lines (edema), lung sliding (PTX), IVC (volume), EF (cardiac function); can guide management in real-time",
                "!!Clarify code status / goals of care before intubation when possible!! — this conversation is essential"
            ]
        }
    ]
}

# Find and replace
found = False
for system in data:
    for i, topic in enumerate(system["topics"]):
        if topic["title"] == "Acute Respiratory Failure":
            system["topics"][i] = new_topic
            found = True
            print(f"✅ Replaced 'Acute Respiratory Failure' in '{system['name']}'")
            print(f"   Old: 3 sections → New: {len(new_topic['sections'])} sections")
            for s in new_topic["sections"]:
                print(f"   - {s['title']}")
            break
    if found:
        break

if not found:
    print("❌ Acute Respiratory Failure not found!")

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
print("✅ content.json written")

with open(PATH, "r") as f:
    json.load(f)
print("✅ JSON validation passed")
