#!/usr/bin/env python3
"""Add 5 toxidrome topics to Toxicology in content.json."""

import json, sys

PATH = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

with open(PATH, "r") as f:
    data = json.load(f)

new_topics = [
    # ── 1. CHOLINERGIC TOXIDROME ──
    {
        "title": "Cholinergic Toxidrome",
        "subtitle": "Organophosphates, nerve agents, carbamates — SLUDGE, atropine, pralidoxime",
        "sections": [
            {
                "title": "Acute Management",
                "type": "steps",
                "items": [
                    "!!Determine exposure route!! — dermal, inhalational, or ingestion; initiate decontamination immediately",
                    "!!Full PPE for all providers!! — remove all pt clothing, copious water irrigation for dermal exposure",
                    "Secure airway early — !!bronchorrhea & bronchospasm are primary killers!!",
                    "Suction copious secretions; prepare for intubation if resp distress",
                    "!!Atropine 2 mg IV!! — double dose q3-5 min until secretions dry (may need 10-100+ mg in severe cases)",
                    "Titrate atropine to !!drying of pulmonary secretions!! — NOT pupil size, NOT heart rate",
                    "!!Pralidoxime (2-PAM) 1-2 g IV over 15-30 min!! → then 500 mg/hr infusion",
                    "Give 2-PAM as early as possible — ineffective after enzyme \"aging\" (irreversible binding)",
                    "Benzodiazepines for seizures: diazepam 5-10 mg IV",
                    "!!Avoid succinylcholine!! — causes prolonged paralysis (depressed pseudocholinesterase)"
                ]
            },
            {
                "title": "Chart Check / History",
                "type": "bullets",
                "items": [
                    "Occupation — farming, pesticide application, industrial chemical exposure",
                    "Exposure type — organophosphate insecticide, carbamate, nerve agent",
                    "Route — dermal, ingestion, inhalation",
                    "Time since exposure — determines likelihood of enzyme aging",
                    "Intentional vs accidental — suicide attempt common in developing countries",
                    "Specific agent if known — aging time varies (soman: minutes; malathion: ~3.7 hrs; diethyl compounds: >30 hrs)",
                    "Pre-hospital tx — was atropine given? How much?",
                    "Coexposures — solvents, other pesticides"
                ]
            },
            {
                "title": "Exam",
                "type": "keyValue",
                "pairs": [
                    {"key": "Vitals pattern", "value": "HR variable (bradycardia from muscarinic, tachycardia from nicotinic); BP ↑ or variable; RR ↑; temp normal or ↓"},
                    {"key": "Pupils", "value": "!!Miosis!! (pinpoint) — classic muscarinic finding"},
                    {"key": "Respiratory", "value": "!!Bronchorrhea!! (copious secretions), bronchospasm, wheezing, ↑ work of breathing — primary cause of death"},
                    {"key": "Skin", "value": "!!Diaphoresis!! — profuse sweating; may see chemical odor (garlic-like w/ organophosphates)"},
                    {"key": "GI", "value": "Hyperactive bowel sounds, cramping, diarrhea, emesis, salivation"},
                    {"key": "Neuro", "value": "Fasciculations (nicotinic), weakness, altered mental status, seizures"},
                    {"key": "GU", "value": "Urinary incontinence"},
                    {"key": "Eyes", "value": "Lacrimation, miosis, blurred vision"}
                ]
            },
            {
                "title": "Definitions",
                "type": "keyValue",
                "pairs": [
                    {"key": "SLUDGE(M)", "value": "**S**alivation, **L**acrimation, **U**rination, **D**iarrhea, **G**I cramping, **E**mesis, **M**iosis — muscarinic effects mnemonic"},
                    {"key": "DUMBELS", "value": "**D**iarrhea/**D**iaphoresis, **U**rination, **M**iosis, **B**radycardia/**B**ronchorrhea/**B**ronchospasm, **E**mesis, **L**acrimation, **S**alivation"},
                    {"key": "Nicotinic effects", "value": "Mydriasis, tachycardia, weakness, fasciculations, hypertension — can mask classic muscarinic presentation"},
                    {"key": "Enzyme aging", "value": "Irreversible binding of organophosphate to acetylcholinesterase — once aged, 2-PAM is ineffective; timing varies by agent"},
                    {"key": "Intermediate syndrome", "value": "Proximal muscle weakness & respiratory failure occurring 24-96 hrs post-exposure; !!monitor 48-96 hrs after severe exposure!!"}
                ]
            },
            {
                "title": "Etiology / DDx",
                "type": "keyValue",
                "pairs": [
                    {"key": "Organophosphates", "value": "Malathion, parathion, chlorpyrifos, diazinon — agricultural insecticides"},
                    {"key": "Nerve agents", "value": "Sarin, soman, tabun, VX, Novichok — chemical warfare agents"},
                    {"key": "Carbamates", "value": "Aldicarb, carbaryl — similar presentation but reversible (no aging); 2-PAM still indicated"},
                    {"key": "Medications", "value": "Neostigmine, pyridostigmine, edrophonium, echothiophate — cholinesterase inhibitors"},
                    {"key": "Muscarine mushrooms", "value": "Inocybe, Clitocybe species — muscarinic sx w/o nicotinic effects"},
                    {"key": "DDx — other miosis + secretions", "value": "Opioid toxicity (miosis but no secretions/fasciculations), nicotine toxicity, serotonin syndrome (more diaphoresis/clonus)"}
                ]
            },
            {
                "title": "Labs & Orders",
                "type": "bullets",
                "items": [
                    "POC glucose",
                    "CBC — leukocytosis common",
                    "BMP — monitor K+, renal function",
                    "VBG/ABG — resp failure, acidosis assessment",
                    "Lipase — pancreatitis reported",
                    "ECG — QTc prolongation correlates w/ severity; dysrhythmias",
                    "CXR — pulmonary edema in severe cases",
                    "RBC acetylcholinesterase (confirmatory but results delayed)",
                    "Plasma butyrylcholinesterase / pseudocholinesterase (faster but less specific)",
                    "Continuous cardiac monitoring, continuous pulse oximetry"
                ]
            },
            {
                "title": "Medications",
                "type": "drugTable",
                "drugs": [
                    {
                        "name": "Atropine",
                        "dose": "2 mg IV; !!double dose q3-5 min!! until secretions dry; may need 10-100+ mg/24h",
                        "route": "IV",
                        "contraindications": "None in true cholinergic crisis",
                        "notes": "!!Titrate to drying of pulmonary secretions!! — NOT pupil size. Start infusion once stabilized (10-20% of loading dose/hr)"
                    },
                    {
                        "name": "Pralidoxime (2-PAM)",
                        "dose": "1-2 g IV over 15-30 min → 500 mg/hr infusion; peds: 20-50 mg/kg → 5-10 mg/kg/hr",
                        "route": "IV",
                        "contraindications": "Ineffective after enzyme aging",
                        "notes": "!!Give ASAP!! — must administer before aging occurs. Reverses nicotinic effects (weakness, fasciculations). Continue infusion ≥24 hrs"
                    },
                    {
                        "name": "Diazepam",
                        "dose": "5-10 mg IV; peds 0.2-0.5 mg/kg",
                        "route": "IV",
                        "contraindications": "Resp depression (secure airway first)",
                        "notes": "For seizures — organophosphate seizures are cholinergic, not epileptic; benzos are first-line"
                    },
                    {
                        "name": "Glycopyrrolate",
                        "dose": "0.1-0.2 mg IV",
                        "route": "IV",
                        "contraindications": "Does not cross BBB",
                        "notes": "Alternative to atropine for peripheral muscarinic sx only; does NOT treat CNS effects or seizures"
                    }
                ]
            },
            {
                "title": "Ongoing Management & Pearls",
                "type": "bullets",
                "items": [
                    "!!Nicotinic effects (tachycardia, HTN, mydriasis) can mask classic muscarinic presentation!! — do not exclude dx based on absence of miosis alone",
                    "Atropine drip: once secretions controlled, start continuous infusion at 10-20% of total loading dose per hour",
                    "Monitor for !!intermediate syndrome!! — proximal weakness & resp failure at 24-96 hrs",
                    "Lipophilic agents (fenthion, chlorfenthion) may cause delayed or prolonged toxicity — observe 24+ hrs",
                    "!!Avoid succinylcholine for RSI!! — depressed pseudocholinesterase causes prolonged paralysis; use rocuronium",
                    "Decontaminate early — double-glove providers; remove & bag all pt clothing",
                    "2-PAM is most effective w/in first 24-48 hrs but may still help later — do not withhold based on time alone"
                ]
            },
            {
                "title": "RECAP Template",
                "type": "bullets",
                "items": [
                    "**R**ecognize — SLUDGE/DUMBELS presentation + exposure hx (pesticide, chemical agent)",
                    "**E**valuate — secretion burden, resp status, fasciculations, need for airway",
                    "**C**ritical actions — atropine titrated to dry secretions, 2-PAM early, benzos for seizures",
                    "**A**ssess response — are secretions drying? Resp status improving? Fasciculations resolving?",
                    "**P**lan — ICU admission, atropine infusion, 2-PAM infusion, monitor for intermediate syndrome 48-96 hrs"
                ]
            },
            {
                "title": "Disposition",
                "type": "keyValue",
                "pairs": [
                    {"key": "ICU", "value": "Atropine infusion, intubated, hemodynamic instability, seizures, AMS, significant exposure"},
                    {"key": "Observation", "value": "Minimal exposure, asymptomatic — observe 6-12 hrs (24 hrs for lipophilic agents)"},
                    {"key": "Consults", "value": "Toxicology (early), ICU, Psychiatry if intentional ingestion"},
                    {"key": "!!Do not discharge early!!", "value": "Intermediate syndrome at 24-96 hrs; lipophilic agents cause delayed toxicity; recurrence after 2-PAM wears off"}
                ]
            }
        ]
    },

    # ── 2. ANTICHOLINERGIC TOXIDROME ──
    {
        "title": "Anticholinergic Toxidrome",
        "subtitle": "Antihistamines, TCAs, antipsychotics — hot, dry, flushed, delirious — physostigmine",
        "sections": [
            {
                "title": "Acute Management",
                "type": "steps",
                "items": [
                    "!!Immediate ECG!! — QRS widening suggests TCA ingestion → changes entire management",
                    "If QRS >100 ms: !!sodium bicarbonate 2 mEq/kg IV bolus!! → bicarb infusion",
                    "Benzodiazepines first-line for agitation: lorazepam 2-4 mg IV q5-15 min PRN",
                    "Active cooling for hyperthermia — agitation → heat generation → anhydrosis prevents cooling",
                    "Foley catheter for urinary retention",
                    "Consider physostigmine 0.5-1 mg IV slow push over 5 min (!!only if NO concern for TCA!!)",
                    "!!Avoid physostigmine if: QRS >100 ms, suspected TCA, seizure hx, bradycardia/AV block!!",
                    "Monitor on continuous cardiac telemetry",
                    "Activated charcoal 1 g/kg PO if w/in 1-2 hrs of ingestion & airway protected"
                ]
            },
            {
                "title": "Chart Check / History",
                "type": "bullets",
                "items": [
                    "Medication list — antihistamines, TCAs, antipsychotics, muscle relaxants, bladder antispasmodics",
                    "OTC medications — diphenhydramine (Benadryl) is most common cause",
                    "Intentional vs accidental ingestion",
                    "Amount ingested & time since ingestion",
                    "Psychiatric hx — suicidal ideation, prior OD attempts",
                    "Plant/mushroom exposure — jimson weed (Datura), deadly nightshade",
                    "Eye drop use — atropine, cyclopentolate, tropicamide",
                    "Co-ingestants — esp acetaminophen, aspirin"
                ]
            },
            {
                "title": "Exam",
                "type": "keyValue",
                "pairs": [
                    {"key": "Vitals pattern", "value": "HR ↑↑ (120-160 typical); BP ↑; RR normal or ↓; temp ↑ (anhydrotic hyperthermia)"},
                    {"key": "Pupils", "value": "!!Mydriasis!! — dilated, nonreactive; may be delayed 12-24 hrs"},
                    {"key": "Skin", "value": "!!Hot, dry, flushed!! — \"red as a beet, dry as a bone, hot as a hare\""},
                    {"key": "Neuro", "value": "!!Delirium, agitation, hallucinations!! — \"mad as a hatter\"; dysarthria, mumbling, picking at air"},
                    {"key": "GI", "value": "Decreased/absent bowel sounds, ileus"},
                    {"key": "GU", "value": "Urinary retention — \"full as a flask\""},
                    {"key": "CV", "value": "Sinus tachycardia; !!if QRS wide → suspect TCA!!"},
                    {"key": "!!KEY distinction!!", "value": "Anticholinergic = !!DRY!! skin vs sympathomimetic = !!WET!! (diaphoretic). Both have mydriasis + tachycardia"}
                ]
            },
            {
                "title": "Definitions",
                "type": "keyValue",
                "pairs": [
                    {"key": "Classic mnemonic", "value": "\"Blind as a bat\" (mydriasis), \"Mad as a hatter\" (delirium), \"Red as a beet\" (flushed), \"Hot as a hare\" (hyperthermia), \"Dry as a bone\" (anhidrosis), \"Full as a flask\" (urinary retention)"},
                    {"key": "Anticholinergic", "value": "Blockade of muscarinic acetylcholine receptors → loss of parasympathetic tone → sympathetic dominance"},
                    {"key": "Physostigmine", "value": "Reversible acetylcholinesterase inhibitor — crosses BBB → reverses both central (delirium) & peripheral (tachycardia, mydriasis) effects"},
                    {"key": "Sodium channel blockade", "value": "TCAs block fast sodium channels → QRS widening, right axis deviation, Brugada pattern — treat w/ sodium bicarbonate"}
                ]
            },
            {
                "title": "Etiology / DDx",
                "type": "keyValue",
                "pairs": [
                    {"key": "Antihistamines", "value": "!!Diphenhydramine!! (most common), hydroxyzine, promethazine, doxylamine"},
                    {"key": "TCAs", "value": "Amitriptyline, nortriptyline, imipramine, desipramine — !!most dangerous!! (sodium channel blockade + seizures)"},
                    {"key": "Antipsychotics", "value": "Chlorpromazine, quetiapine, olanzapine"},
                    {"key": "Muscle relaxants", "value": "Cyclobenzaprine (structurally similar to TCA), orphenadrine"},
                    {"key": "Bladder antispasmodics", "value": "Oxybutynin, tolterodine, hyoscyamine"},
                    {"key": "Anti-Parkinsonian", "value": "Benztropine, trihexyphenidyl"},
                    {"key": "Plants", "value": "Jimson weed (Datura stramonium), deadly nightshade (Atropa belladonna)"},
                    {"key": "DDx", "value": "Sympathomimetic (wet vs dry skin), serotonin syndrome (clonus, hyperreflexia), NMS (rigidity, ↑ CK), thyroid storm, heat stroke"}
                ]
            },
            {
                "title": "Labs & Orders",
                "type": "bullets",
                "items": [
                    "!!ECG!! — sinus tach; QRS >100 ms → TCA; QTc prolongation",
                    "POC glucose",
                    "Acetaminophen & salicylate levels (!!mandatory co-ingestion screen!!)",
                    "BMP",
                    "CPK if prolonged agitation (rhabdomyolysis)",
                    "Urinalysis",
                    "UDS (limited utility — detects many anticholinergic agents poorly)",
                    "Continuous cardiac monitoring"
                ]
            },
            {
                "title": "Medications",
                "type": "drugTable",
                "drugs": [
                    {
                        "name": "Lorazepam",
                        "dose": "2-4 mg IV q5-15 min PRN agitation",
                        "route": "IV",
                        "contraindications": "Resp depression (ensure airway control)",
                        "notes": "!!First-line for agitation!! — controls muscular heat generation, prevents hyperthermia"
                    },
                    {
                        "name": "Physostigmine",
                        "dose": "0.5-1 mg IV slowly over 5 min; may repeat q20 min up to 2 mg total in first hr",
                        "route": "IV",
                        "contraindications": "!!TCA ingestion, QRS >100 ms, bradycardia, AV block, seizure hx, unknown OD!!",
                        "notes": "Reverses central & peripheral effects. If needing >3 doses in 6 hrs, consider infusion 1 mg/hr. Duration shorter than most ingested agents → rebound risk"
                    },
                    {
                        "name": "Sodium bicarbonate",
                        "dose": "2 mEq/kg IV bolus → infusion 150 mEq in 1L D5W at 250 mL/hr",
                        "route": "IV",
                        "contraindications": "Metabolic alkalosis",
                        "notes": "!!For QRS >100 ms (TCA sodium channel blockade)!! — goal QRS <120 ms. Can give serial boluses"
                    },
                    {
                        "name": "Activated charcoal",
                        "dose": "1 g/kg PO (max 50 g)",
                        "route": "PO",
                        "contraindications": "Unprotected airway, ileus, bowel obstruction",
                        "notes": "Most effective w/in 1-2 hrs of ingestion; anticholinergics delay gastric emptying → may still be effective later"
                    }
                ]
            },
            {
                "title": "Ongoing Management & Pearls",
                "type": "bullets",
                "items": [
                    "!!Anticholinergic = DRY; sympathomimetic = WET!! — check axillae for moisture (key distinguishing exam finding)",
                    "!!If physostigmine causes seizures: benzos will be INEFFECTIVE!! — use phenobarbital or propofol",
                    "Avoid Class IA/IC antiarrhythmics (procainamide, flecainide) if TCA suspected",
                    "Plant ingestions (jimson weed) may have very delayed absorption due to ↓ GI motility — observe 24-48 hrs",
                    "Mydriasis may persist 12-24 hrs after other sx resolve — do not use pupil size to judge resolution",
                    "Diphenhydramine is dose-dependent: mild anticholinergic at low doses → QRS widening, seizures, rhabdomyolysis at high doses",
                    "!!Always check ECG before giving physostigmine!! — QRS >100 ms = contraindication"
                ]
            },
            {
                "title": "RECAP Template",
                "type": "bullets",
                "items": [
                    "**R**ecognize — hot, dry, flushed, delirious + mydriasis + tachycardia (\"blind, mad, red, hot, dry, full\")",
                    "**E**valuate — ECG for QRS width (TCA?), core temp, agitation severity, urinary retention",
                    "**C**ritical actions — ECG first, benzos for agitation, bicarb if QRS wide, physostigmine if safe",
                    "**A**ssess response — is delirium improving? QRS narrowing? Temp ↓?",
                    "**P**lan — cardiac monitoring, admit all physostigmine recipients, psychiatry consult if intentional"
                ]
            },
            {
                "title": "Disposition",
                "type": "keyValue",
                "pairs": [
                    {"key": "Discharge", "value": "After 6-hr observation if mild sx resolved completely"},
                    {"key": "Extended observation", "value": "24-48 hrs for long-acting agents or plant ingestions (delayed absorption from ileus)"},
                    {"key": "Admit", "value": "All physostigmine recipients (shorter half-life than ingested agents → rebound toxicity risk)"},
                    {"key": "ICU", "value": "QRS widening, seizures, hemodynamic instability, refractory agitation, hyperthermia >40°C"},
                    {"key": "Consults", "value": "Toxicology, Psychiatry if intentional OD"}
                ]
            }
        ]
    },

    # ── 3. SYMPATHOMIMETIC TOXIDROME ──
    {
        "title": "Sympathomimetic Toxidrome",
        "subtitle": "Cocaine, amphetamines, MDMA, bath salts — agitation, diaphoresis, hyperthermia",
        "sections": [
            {
                "title": "Acute Management",
                "type": "steps",
                "items": [
                    "!!Benzodiazepines are first-line for EVERYTHING!! — agitation, HTN, tachycardia, hyperthermia, seizures",
                    "Lorazepam 2-4 mg IV or diazepam 5-10 mg IV q5-10 min — may require very large cumulative doses",
                    "!!Check core temp!! — hyperthermia >41°C (106°F) is life-threatening → aggressive cooling",
                    "Active cooling: ice packs to axillae/groin, evaporative cooling, cooling blankets",
                    "If temp >41°C & refractory to benzos: !!intubate + paralyze (rocuronium)!! to stop heat generation",
                    "!!No beta-blockers!! — unopposed alpha stimulation → severe HTN + coronary vasospasm (esp w/ cocaine)",
                    "For refractory HTN after adequate benzos: nicardipine 5-15 mg/hr or phentolamine 2.5-5 mg IV",
                    "IV crystalloid bolus — pts are volume-depleted from diaphoresis + agitation",
                    "!!Avoid haloperidol as first-line!! — ↓ seizure threshold, may worsen hyperthermia",
                    "!!Avoid antipyretics!! (APAP/ibuprofen) — hyperthermia is from muscular activity, not hypothalamic set-point"
                ]
            },
            {
                "title": "Chart Check / History",
                "type": "bullets",
                "items": [
                    "Substance used — cocaine, methamphetamine, MDMA, bath salts, Adderall, ephedrine",
                    "Route — smoked, snorted, IV, oral",
                    "Time of last use & amount",
                    "Co-ingestants — alcohol, opioids, benzodiazepines",
                    "Chest pain? (acute coronary syndrome, aortic dissection risk w/ cocaine)",
                    "Headache? (intracranial hemorrhage risk)",
                    "Prior substance use — chronic vs naive (tolerance affects presentation)",
                    "Psychiatric hx — stimulant-induced psychosis, prior OD"
                ]
            },
            {
                "title": "Exam",
                "type": "keyValue",
                "pairs": [
                    {"key": "Vitals pattern", "value": "HR ↑↑; BP ↑↑; RR ↑; temp ↑ (can be severely elevated)"},
                    {"key": "Pupils", "value": "!!Mydriasis!! (dilated)"},
                    {"key": "Skin", "value": "!!Diaphoretic!! (WET) — key distinction from anticholinergic (dry)"},
                    {"key": "Neuro", "value": "Agitation, psychosis, paranoia, tremor, hyperreflexia, clonus, seizures"},
                    {"key": "CV", "value": "Tachycardia, hypertension; chest pain → r/o ACS, aortic dissection"},
                    {"key": "MSK", "value": "Muscle rigidity, rhabdomyolysis"},
                    {"key": "!!KEY distinction!!", "value": "Sympathomimetic = !!WET!! (diaphoretic) + agitated + mydriatic; Anticholinergic = !!DRY!! + delirious + mydriatic"}
                ]
            },
            {
                "title": "Etiology / DDx",
                "type": "keyValue",
                "pairs": [
                    {"key": "Cocaine", "value": "Smoked/snorted/IV — short acting (30-60 min); risk of ACS, aortic dissection, intracranial hemorrhage"},
                    {"key": "Amphetamines", "value": "Methamphetamine, dextroamphetamine, lisdexamfetamine — longer duration (hours)"},
                    {"key": "MDMA / Ecstasy", "value": "Also causes hyponatremia (SIADH) & serotonin syndrome overlap"},
                    {"key": "Synthetic cathinones", "value": "\"Bath salts\" (mephedrone, MDPV) — extreme agitation, rhabdomyolysis (63% incidence)"},
                    {"key": "Others", "value": "Ephedrine, pseudoephedrine, caffeine (massive OD), theophylline, PCP (mixed)"},
                    {"key": "DDx", "value": "Serotonin syndrome (clonus/hyperreflexia prominent), thyroid storm, pheochromocytoma, anticholinergic (dry vs wet), NMS, heat stroke"}
                ]
            },
            {
                "title": "Labs & Orders",
                "type": "bullets",
                "items": [
                    "POC glucose",
                    "BMP — renal function, electrolytes (hyponatremia w/ MDMA)",
                    "!!CPK!! — rhabdomyolysis screening (bath salts 63%, amphetamines 40%, cocaine 33%)",
                    "UA w/ myoglobin",
                    "ECG — QTc prolongation, QRS widening, ischemic changes, dysrhythmias",
                    "Troponin if chest pain or ECG changes",
                    "VBG/ABG",
                    "Coags/DIC panel if severe hyperthermia",
                    "UDS (limited — may miss synthetic agents)",
                    "Acetaminophen & salicylate levels",
                    "Head CT if focal neuro findings, severe HA, or AMS (hemorrhage, stroke)"
                ]
            },
            {
                "title": "Medications",
                "type": "drugTable",
                "drugs": [
                    {
                        "name": "Lorazepam",
                        "dose": "2-4 mg IV q5-10 min; may need very large cumulative doses (50-100+ mg)",
                        "route": "IV",
                        "contraindications": "Resp depression at high doses (airway management)",
                        "notes": "!!First-line for everything!! — agitation, HTN, tachycardia, seizures, hyperthermia. Treats the underlying cause"
                    },
                    {
                        "name": "Nicardipine",
                        "dose": "5-15 mg/hr IV infusion",
                        "route": "IV",
                        "contraindications": "Severe aortic stenosis",
                        "notes": "For refractory HTN after adequate benzodiazepines. Safe w/ cocaine (no beta-blockade)"
                    },
                    {
                        "name": "Phentolamine",
                        "dose": "2.5-5 mg IV bolus; may repeat q5-15 min",
                        "route": "IV",
                        "contraindications": "Hypotension",
                        "notes": "Alpha-blocker — for refractory HTN esp cocaine-associated. Addresses unopposed alpha stimulation"
                    },
                    {
                        "name": "Nitroglycerin",
                        "dose": "0.4 mg SL or 5-200 mcg/min IV infusion",
                        "route": "SL / IV",
                        "contraindications": "Hypotension, PDE5 inhibitor use",
                        "notes": "For cocaine-associated ACS — coronary vasodilator"
                    },
                    {
                        "name": "IV Crystalloid",
                        "dose": "1-2 L bolus → target UOP 200-300 mL/hr if rhabdomyolysis",
                        "route": "IV",
                        "contraindications": "Volume overload / CHF",
                        "notes": "Aggressive hydration for rhabdomyolysis prevention + volume depletion from diaphoresis"
                    }
                ]
            },
            {
                "title": "Ongoing Management & Pearls",
                "type": "bullets",
                "items": [
                    "!!No beta-blockers!! — labetalol, metoprolol, propranolol all contraindicated w/ cocaine (unopposed alpha → HTN crisis, coronary vasospasm)",
                    "!!No succinylcholine!! — hyperkalemia risk from rhabdomyolysis",
                    "!!No antipyretics!! — hyperthermia is from muscular heat generation, not febrile response",
                    "Rhabdomyolysis is VERY common — check CPK on all sympathomimetic presentations",
                    "Cocaine chest pain: benzos + NTG + aspirin; avoid beta-blockers; cath lab if STEMI",
                    "MDMA can cause severe hyponatremia (SIADH + excessive free water intake) → seizures",
                    "Bath salts / synthetic cathinones cause most severe agitation & highest rhabdomyolysis rates",
                    "Body packers (swallowed cocaine): whole-bowel irrigation; surgical consult if packet rupture suspected"
                ]
            },
            {
                "title": "RECAP Template",
                "type": "bullets",
                "items": [
                    "**R**ecognize — agitated, diaphoretic, mydriatic, tachycardic, hypertensive (WET + agitated)",
                    "**E**valuate — core temp, ECG, CPK, troponin if chest pain, head CT if focal findings",
                    "**C**ritical actions — benzos early & aggressively, active cooling, IV fluids, avoid beta-blockers",
                    "**A**ssess response — is agitation controlled? Temp ↓? BP improving? CPK trending?",
                    "**P**lan — serial CPK/renal monitoring, rhabdo protocol if CPK ↑, cardiac monitoring, psychiatry consult"
                ]
            },
            {
                "title": "Disposition",
                "type": "keyValue",
                "pairs": [
                    {"key": "Discharge", "value": "Mild intoxication, asymptomatic after 4-6 hrs, normal labs, normal ECG"},
                    {"key": "Observation/Admit", "value": "Persistent tachycardia/HTN, chest pain, rhabdomyolysis (CPK >5000), renal insufficiency, persistent AMS"},
                    {"key": "ICU", "value": "Seizures, severe hyperthermia (>40°C), significant rhabdomyolysis, ACS, intracranial hemorrhage, hemodynamic instability"},
                    {"key": "Consults", "value": "Toxicology, Cardiology if ACS, Neurosurgery if ICH, Psychiatry for intentional OD/psychosis/SUD assessment"}
                ]
            }
        ]
    },

    # ── 4. SYMPATHOLYTIC TOXIDROME ──
    {
        "title": "Sympatholytic Toxidrome",
        "subtitle": "Clonidine, beta-blockers, CCBs — bradycardia, hypotension, ↓ LOC — high-dose insulin, glucagon",
        "sections": [
            {
                "title": "Acute Management",
                "type": "steps",
                "items": [
                    "!!Identify the agent class!! — clonidine vs beta-blocker vs CCB (tx differs significantly)",
                    "IV access, continuous cardiac monitoring, 12-lead ECG",
                    "IV crystalloid bolus 20 mL/kg for hypotension",
                    "Atropine 0.5-1 mg IV for symptomatic bradycardia (often ineffective in severe BB/CCB OD)",
                    "!!For beta-blocker OD: glucagon 5 mg IV bolus!! → 2-5 mg/hr infusion",
                    "!!For CCB OD: high-dose insulin (HDI) 1 unit/kg bolus + D50!! → 0.5-1 unit/kg/hr infusion (start early — 30-60 min to full effect)",
                    "IV calcium chloride 1-3 g (or calcium gluconate 3-9 g) for CCB OD",
                    "Vasopressors: norepinephrine or epinephrine if fluid-refractory hypotension",
                    "For clonidine: trial of naloxone 0.4-2 mg IV (may require high doses up to 10 mg)",
                    "!!Contact ECMO center early!! for massive BB/CCB ingestions w/ refractory shock"
                ]
            },
            {
                "title": "Chart Check / History",
                "type": "bullets",
                "items": [
                    "!!Which agent?!! — specific drug, dose, formulation (immediate-release vs sustained-release)",
                    "Time of ingestion — sustained-release CCBs have delayed, prolonged toxicity",
                    "Amount ingested — single pill can kill in pediatric clonidine ingestion",
                    "Intentional vs accidental",
                    "Concurrent medications — digoxin (synergistic bradycardia), other antihypertensives",
                    "Cardiac hx — baseline conduction disease, CHF, pacemaker",
                    "Renal/hepatic function — affects drug clearance",
                    "Prior hx of similar ingestion"
                ]
            },
            {
                "title": "Exam",
                "type": "keyValue",
                "pairs": [
                    {"key": "Vitals pattern", "value": "HR ↓ (bradycardia); BP ↓ (hypotension); RR ↓ (esp clonidine); temp normal or ↓"},
                    {"key": "Pupils", "value": "Normal or !!miosis!! (esp clonidine — mimics opioid OD)"},
                    {"key": "Neuro", "value": "↓ LOC, sedation, lethargy → coma (esp clonidine); clonidine can closely mimic opioid OD"},
                    {"key": "CV", "value": "Bradycardia, hypotension, AV blocks (verapamil/diltiazem), wide QRS (propranolol)"},
                    {"key": "Skin", "value": "Dry, cool, pale"},
                    {"key": "Respiratory", "value": "↓ RR, periodic apnea, Cheyne-Stokes (clonidine)"},
                    {"key": "!!Glucose clue!!", "value": "!!Hypoglycemia = beta-blocker!!; !!hyperglycemia = CCB!! — critical distinguishing feature when agent unknown"}
                ]
            },
            {
                "title": "Definitions",
                "type": "keyValue",
                "pairs": [
                    {"key": "Sympatholytic", "value": "Agents that ↓ sympathetic nervous system activity → bradycardia, hypotension, ↓ consciousness"},
                    {"key": "High-dose insulin (HDI)", "value": "Euglycemic therapy: insulin ↑ inotropy independent of beta-receptors; !!most effective tx for CCB OD!! — start early as 30-60 min to full effect"},
                    {"key": "Glucagon", "value": "Bypasses beta-receptor blockade via Gs protein activation → ↑ cAMP → ↑ inotropy & chronotropy; !!first-line for beta-blocker OD!!"},
                    {"key": "Dihydropyridine CCBs", "value": "Amlodipine, nifedipine — primarily vasodilation → hypotension w/ reflex tachycardia (may NOT have bradycardia)"},
                    {"key": "Non-dihydropyridine CCBs", "value": "Verapamil, diltiazem — negative chronotropy + inotropy → bradycardia, AV block, ↓ cardiac output"}
                ]
            },
            {
                "title": "Etiology / DDx",
                "type": "keyValue",
                "pairs": [
                    {"key": "Central alpha-2 agonists", "value": "!!Clonidine!!, guanfacine, dexmedetomidine, tizanidine, methyldopa — mimic opioid OD (miosis + CNS depression + resp depression)"},
                    {"key": "Beta-blockers", "value": "!!Propranolol!! (most dangerous — lipophilic, Na channel blockade → QRS widening, seizures); !!sotalol!! (QT prolongation, TdP); metoprolol, atenolol, carvedilol"},
                    {"key": "Calcium channel blockers", "value": "!!Verapamil!! (most dangerous CCB in OD); diltiazem; amlodipine, nifedipine (dihydropyridines)"},
                    {"key": "DDx — bradycardia + hypotension", "value": "Opioid OD (responds to naloxone), digoxin toxicity (bidirectional VT, hyperkalemia), cholinergic toxidrome (SLUDGE), hypothyroidism, hyperkalemia, sepsis"}
                ]
            },
            {
                "title": "Labs & Orders",
                "type": "bullets",
                "items": [
                    "!!ECG!! — bradycardia, AV blocks, QRS widening (propranolol), QT prolongation (sotalol)",
                    "!!POC glucose!! — hypoglycemia → beta-blocker; hyperglycemia → CCB (!!key distinguishing feature!!)",
                    "BMP — electrolytes, renal function, calcium",
                    "Serum lactate — tissue hypoperfusion marker",
                    "Digoxin level (if applicable — often co-prescribed)",
                    "Acetaminophen & salicylate levels",
                    "VBG — assess perfusion, acid-base status",
                    "Continuous cardiac monitoring (!!mandatory!!)",
                    "Continuous pulse oximetry"
                ]
            },
            {
                "title": "Medications",
                "type": "drugTable",
                "drugs": [
                    {
                        "name": "Glucagon",
                        "dose": "5 mg IV bolus over 1 min → 2-5 mg/hr infusion; peds: 50 mcg/kg bolus → 70 mcg/kg/hr",
                        "route": "IV",
                        "contraindications": "Pheochromocytoma, insulinoma",
                        "notes": "!!First-line for beta-blocker OD!! — bypasses beta-receptor. Give antiemetic (ondansetron) w/ bolus. Tachyphylaxis occurs; less effective for CCBs"
                    },
                    {
                        "name": "High-dose insulin (regular)",
                        "dose": "1 unit/kg IV bolus + D50 (0.5 g/kg) → infusion 0.5-1 unit/kg/hr (titrate up to 10 units/kg/hr)",
                        "route": "IV",
                        "contraindications": "Monitor glucose q15 min; maintain K+ >3.0",
                        "notes": "!!Most effective tx for CCB OD!! — takes 30-60 min for full effect → start early. ↑ inotropy independent of beta-receptors. Maintain euglycemia w/ dextrose infusion"
                    },
                    {
                        "name": "Calcium chloride 10%",
                        "dose": "1-3 g IV (20-40 mg/kg) via central line; may repeat",
                        "route": "IV (central)",
                        "contraindications": "Digoxin toxicity (calcium worsens dig toxicity)",
                        "notes": "For CCB OD — ↑ extracellular calcium to overcome channel blockade. CaCl has 3x more elemental calcium than gluconate. Target Ca 15-18 mg/dL"
                    },
                    {
                        "name": "Atropine",
                        "dose": "0.5-1 mg IV q3-5 min, max 3 mg",
                        "route": "IV",
                        "contraindications": "Avoid in wide-complex bradycardia",
                        "notes": "For symptomatic bradycardia — often ineffective in severe BB/CCB OD"
                    },
                    {
                        "name": "Naloxone",
                        "dose": "0.4-2 mg IV; may repeat up to 10 mg; may need infusion",
                        "route": "IV",
                        "contraindications": "May precipitate withdrawal in opioid-dependent pts",
                        "notes": "For clonidine toxicity — high doses often required; partial response suggests clonidine vs opioid"
                    },
                    {
                        "name": "Lipid emulsion 20%",
                        "dose": "1.5 mL/kg IV bolus (repeat 1-2x if pulseless) → 0.25 mL/kg/min × 30-60 min; max 12.5 mL/kg",
                        "route": "IV",
                        "contraindications": "Pancreatitis, fat embolism risk",
                        "notes": "For lipophilic beta-blocker OD (propranolol) refractory to other tx; consider for severe CCB OD"
                    },
                    {
                        "name": "Sodium bicarbonate",
                        "dose": "1-2 mEq/kg IV bolus",
                        "route": "IV",
                        "contraindications": "Metabolic alkalosis",
                        "notes": "For QRS widening from propranolol (sodium channel blockade)"
                    }
                ]
            },
            {
                "title": "Ongoing Management & Pearls",
                "type": "bullets",
                "items": [
                    "!!Glucose is the key distinguishing clue!! — hypoglycemia = BB; hyperglycemia = CCB; hyperglycemia severity correlates w/ CCB severity",
                    "!!Clonidine mimics opioid OD!! — miosis + CNS depression + resp depression; consider clonidine in pts who don't fully respond to naloxone",
                    "!!Start HDI early for CCB OD!! — takes 30-60 min to full effect; don't wait for other therapies to fail",
                    "Sustained-release CCBs (amlodipine, ER verapamil/diltiazem): delayed & prolonged toxicity → admit ALL SR ingestions even if asymptomatic",
                    "Propranolol is most dangerous BB — lipophilic (crosses BBB → seizures) + Na channel blockade (→ QRS widening)",
                    "Sotalol is unique — K channel blockade → QT prolongation → TdP; give Mg 2 g IV; delayed toxicity",
                    "Consider whole-bowel irrigation for sustained-release preparations",
                    "VA-ECMO is the definitive rescue therapy for refractory cardiogenic shock — !!contact ECMO center early!!"
                ]
            },
            {
                "title": "RECAP Template",
                "type": "bullets",
                "items": [
                    "**R**ecognize — bradycardia + hypotension + ↓ LOC; check glucose (BB vs CCB); miosis (clonidine)",
                    "**E**valuate — ECG (blocks, QRS, QT), POC glucose, lactate, identify specific agent",
                    "**C**ritical actions — IV fluids, atropine, agent-specific antidote (glucagon for BB, HDI for CCB, naloxone for clonidine)",
                    "**A**ssess response — HR, BP, mental status, lactate clearance, perfusion status",
                    "**P**lan — ICU for all symptomatic pts; ECMO standby for massive ingestions; prolonged monitoring for SR formulations"
                ]
            },
            {
                "title": "Disposition",
                "type": "keyValue",
                "pairs": [
                    {"key": "Clonidine", "value": "Admit all symptomatic; peds ingestions observe 24 hrs (small doses = significant toxicity in children)"},
                    {"key": "Beta-blockers", "value": "Admit all symptomatic; ALL sotalol ingestions (delayed toxicity); observe asymptomatic 6+ hrs"},
                    {"key": "CCBs", "value": "Admit all symptomatic; !!ALL sustained-release ingestions!! (delayed, prolonged toxicity); observe IR asymptomatic 6-8 hrs"},
                    {"key": "ICU criteria", "value": "Vasopressors, HDI infusion, glucagon infusion, transcutaneous/transvenous pacing, ECMO"},
                    {"key": "!!ECMO alert!!", "value": "Contact ECMO center early for massive BB/CCB ingestions w/ refractory shock — do not delay transfer"}
                ]
            }
        ]
    },

    # ── 5. SEDATIVE-HYPNOTIC TOXIDROME ──
    {
        "title": "Sedative-Hypnotic Toxidrome",
        "subtitle": "Benzodiazepines, barbiturates, GHB, Z-drugs — CNS/respiratory depression, supportive care",
        "sections": [
            {
                "title": "Acute Management",
                "type": "steps",
                "items": [
                    "!!Airway is paramount!! — respiratory depression is the primary cause of death",
                    "Assess GCS, gag reflex, respiratory effort — intubate for GCS <8, absent gag, or resp failure",
                    "Supplemental O2, continuous pulse oximetry, capnography",
                    "IV access, POC glucose (hypoglycemia common w/ ethanol)",
                    "IV crystalloid for hypotension",
                    "Rewarming for hypothermia (passive + active)",
                    "!!Flumazenil is NOT routine!! — risk of withdrawal seizures in chronic benzo users; reserve for iatrogenic oversedation only",
                    "Activated charcoal 1 g/kg if w/in 1-2 hrs & airway protected",
                    "!!Always check co-ingestants!! — acetaminophen & salicylate levels mandatory in any OD"
                ]
            },
            {
                "title": "Chart Check / History",
                "type": "bullets",
                "items": [
                    "Specific agent — benzodiazepine, barbiturate, GHB, Z-drug, ethanol, baclofen",
                    "Chronic vs acute use — chronic benzo use = flumazenil contraindicated",
                    "Amount & time of ingestion",
                    "Co-ingestants — !!opioids + benzos = synergistic resp depression!!",
                    "Intentional vs recreational vs accidental",
                    "Psychiatric hx — suicidal ideation, prior attempts",
                    "Prescription history — which benzos, how long, what dose",
                    "Alcohol use hx — cross-tolerance w/ barbiturates/benzos"
                ]
            },
            {
                "title": "Exam",
                "type": "keyValue",
                "pairs": [
                    {"key": "Vitals pattern", "value": "HR normal or ↓; BP normal or ↓; !!RR ↓!! (resp depression — primary lethal mechanism); temp normal or ↓"},
                    {"key": "Pupils", "value": "Variable — usually midpoint, normal reactive (unlike opioids which are pinpoint)"},
                    {"key": "Neuro", "value": "Somnolence → stupor → coma; slurred speech, ataxia, hyporeflexia, nystagmus"},
                    {"key": "Skin", "value": "Variable; barbiturates may cause bullous skin lesions (\"barb blisters\")"},
                    {"key": "Respiratory", "value": "!!↓ RR, ↓ tidal volume, apnea!! — primary mechanism of death"},
                    {"key": "GHB-specific", "value": "!!Rapid cycling between coma & agitation!!; abrupt awakening; typically young adults at raves/parties"},
                    {"key": "Barbiturate-specific", "value": "!!May mimic brain death!! — loss of brainstem reflexes, fixed dilated pupils possible; do NOT withdraw care prematurely"}
                ]
            },
            {
                "title": "Etiology / DDx",
                "type": "keyValue",
                "pairs": [
                    {"key": "Benzodiazepines", "value": "Alprazolam, lorazepam, diazepam, clonazepam, midazolam — most common sedative-hypnotic OD"},
                    {"key": "Barbiturates", "value": "Phenobarbital, pentobarbital — more profound coma, longer duration, higher mortality"},
                    {"key": "Z-drugs", "value": "Zolpidem (Ambien), zaleplon, eszopiclone — generally less severe than benzos"},
                    {"key": "GHB / GBL", "value": "Rapid onset/offset; !!NOT detected on standard UDS!!; typically recover 2-6 hrs"},
                    {"key": "Others", "value": "Ethanol, chloral hydrate, meprobamate/carisoprodol (Soma), baclofen, propofol"},
                    {"key": "DDx", "value": "Opioid OD (miosis, responds to naloxone), sympatholytic (bradycardia + hypotension), hepatic encephalopathy, hypoglycemia, hypothyroidism, stroke, post-ictal state"}
                ]
            },
            {
                "title": "Labs & Orders",
                "type": "bullets",
                "items": [
                    "POC glucose (!!hypoglycemia common w/ ethanol!!)",
                    "!!Acetaminophen & salicylate levels!! — mandatory in any OD presentation",
                    "Serum ethanol level",
                    "BMP",
                    "CBC",
                    "ECG",
                    "VBG/ABG — ventilatory status assessment",
                    "UDS (!!limitations: may miss lorazepam, alprazolam, clonazepam, midazolam; GHB NOT detected!!)",
                    "Serum osmolality if toxic alcohol suspected",
                    "LFTs if chronic ethanol use"
                ]
            },
            {
                "title": "Medications",
                "type": "drugTable",
                "drugs": [
                    {
                        "name": "Flumazenil",
                        "dose": "0.2 mg IV; repeat q1 min up to max 3 mg total",
                        "route": "IV",
                        "contraindications": "!!Chronic benzo use/dependence, suspected TCA, seizure hx, unknown OD, co-ingestion of seizure-threshold-lowering agents!!",
                        "notes": "!!Very limited indications!! — primarily iatrogenic oversedation in benzo-naive pts. Duration 45-90 min (shorter than most benzos → rebound sedation). If causes seizures: benzos will be INEFFECTIVE → phenobarbital or propofol"
                    },
                    {
                        "name": "Activated charcoal",
                        "dose": "1 g/kg PO (max 50 g)",
                        "route": "PO",
                        "contraindications": "Unprotected airway, ↓ GCS w/o intubation",
                        "notes": "Most effective w/in 1-2 hrs of ingestion. Protect airway first. Consider multidose charcoal for phenobarbital"
                    },
                    {
                        "name": "Phenobarbital",
                        "dose": "15-20 mg/kg IV loading dose",
                        "route": "IV",
                        "contraindications": "Resp depression, hemodynamic instability",
                        "notes": "For flumazenil-induced seizures (benzos will be blocked by flumazenil). Also for severe barbiturate withdrawal"
                    },
                    {
                        "name": "Sodium bicarbonate (urinary alkalinization)",
                        "dose": "150 mEq in 1L D5W at 150-200 mL/hr; target urine pH 7.5-8.0",
                        "route": "IV",
                        "contraindications": "Metabolic alkalosis, pulmonary edema",
                        "notes": "For phenobarbital OD — ↑ renal clearance via ion trapping. Monitor urine pH, serum K+"
                    }
                ]
            },
            {
                "title": "Ongoing Management & Pearls",
                "type": "bullets",
                "items": [
                    "!!Airway management is the primary intervention!! — most sedative-hypnotic deaths are from respiratory failure",
                    "!!Flumazenil is almost never indicated!! — risk of precipitating withdrawal seizures far outweighs benefit in most scenarios",
                    "!!If flumazenil causes seizures, benzos will NOT work!! (blocked by flumazenil) → use phenobarbital or propofol",
                    "GHB: pts typically recover in 2-6 hrs; extended coma (>6 hrs) suggests alternative dx → expand workup",
                    "GHB: !!rapid cycling between coma & agitation!! — anticipate sudden awakening; restrain before intubation attempt",
                    "Barbiturate OD can !!mimic brain death!! — do NOT make withdrawal-of-care decisions acutely",
                    "Standard UDS misses many benzos (lorazepam, alprazolam, clonazepam, midazolam) & all GHB",
                    "Phenobarbital has very long half-life (80-120 hrs) — prolonged monitoring required",
                    "!!Opioid + benzo co-ingestion = synergistic resp depression!! — most common lethal combination"
                ]
            },
            {
                "title": "RECAP Template",
                "type": "bullets",
                "items": [
                    "**R**ecognize — CNS depression + resp depression + normal/↓ vitals; no SLUDGE (not cholinergic), no agitation (not sympathomimetic)",
                    "**E**valuate — GCS, resp rate/effort, gag reflex, co-ingestant screen (APAP, ASA, ethanol), ECG",
                    "**C**ritical actions — airway protection (intubate if GCS <8), avoid flumazenil unless iatrogenic/benzo-naive, check co-ingestants",
                    "**A**ssess response — mental status improving? Resp effort adequate? Hemodynamics stable?",
                    "**P**lan — ICU if intubated or hemodynamically unstable; observe mild cases 6+ hrs; psychiatry for intentional OD"
                ]
            },
            {
                "title": "Disposition",
                "type": "keyValue",
                "pairs": [
                    {"key": "Discharge", "value": "Uncomplicated benzo ingestion, clinically improved & ambulatory after 6-hr observation"},
                    {"key": "GHB", "value": "Most recover 2-6 hrs; extended coma >6 hrs → admit for expanded workup (alternative dx)"},
                    {"key": "Barbiturates", "value": "!!Admit all!! — ICU for severe cases, intubated pts, hemodynamic instability. Phenobarbital half-life 80-120 hrs"},
                    {"key": "Admit", "value": "Persistent AMS, resp depression requiring intervention, hemodynamic instability, co-ingestions, unknown agent"},
                    {"key": "Consults", "value": "Toxicology, Psychiatry for all intentional ingestions"}
                ]
            }
        ]
    }
]

# Find Toxicology system and append topics
tox_found = False
for system in data:
    if system["name"] == "Toxicology":
        system["topics"].extend(new_topics)
        tox_found = True
        print(f"✅ Added {len(new_topics)} toxidrome topics to Toxicology")
        print(f"   Toxicology now has {len(system['topics'])} topics")
        break

if not tox_found:
    print("❌ Toxicology system not found!")
    sys.exit(1)

# Count totals
total = sum(len(s["topics"]) for s in data)
print(f"   Total topics across all systems: {total}")

with open(PATH, "w") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ content.json written successfully")

# Validate by re-reading
with open(PATH, "r") as f:
    check = json.load(f)
tox_count = 0
for s in check:
    if s["name"] == "Toxicology":
        tox_count = len(s["topics"])
        for t in s["topics"]:
            print(f"   - {t['title']} ({len(t['sections'])} sections)")
print(f"✅ Validation passed — Toxicology has {tox_count} topics")
