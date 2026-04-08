#!/usr/bin/env python3
"""Add guideline references to all topics in content.json."""

import json
import sys

# Map topic titles to their reference citations
REFERENCES = {
    "Introduction to Rapid Response": [
        "Jones DA, DeVita MA, Bellomo R. Rapid-Response Teams. New England Journal of Medicine. 2011;365(2):139-146. https://doi.org/10.1056/NEJMra0910926",
        "Churpek MM, Yuen TC, Winslow C, et al. Multicenter Comparison of Machine Learning Methods and Conventional Regression for Predicting Clinical Deterioration on the Wards. Critical Care Medicine. 2016;44(2):368-374.",
        "Society of Critical Care Medicine. Rapid Response Systems. Critical Care Medicine. 2024. https://www.sccm.org/clinical-resources/rapid-response-systems"
    ],
    "Cardiac Arrest": [
        "Panchal AR, Bartos JA, Cabañas JG, et al. 2020 AHA Guidelines for CPR and Emergency Cardiovascular Care. Circulation. 2020;142(16_suppl_2):S366-S468. https://doi.org/10.1161/CIR.0000000000000916",
        "Merchant RM, Topjian AA, Panchal AR, et al. 2023 AHA Focused Update on Adult Advanced Cardiovascular Life Support. Circulation. 2024;149(5):e254-e273. https://doi.org/10.1161/CIR.0000000000001194",
        "Berg KM, Cheng A, Panchal AR, et al. AHA Guidelines for CPR & ECC — Part 7: Systems of Care. Circulation. 2020;142(16_suppl_2):S580-S604."
    ],
    "ACS": [
        "Writing Committee Members, Lawton JS, Tamis-Holland JE, et al. 2021 ACC/AHA/SCAI Guideline for Coronary Artery Revascularization. Journal of the American College of Cardiology. 2022;79(2):e21-e129. https://doi.org/10.1016/j.jacc.2021.09.006",
        "Gulati M, Levy PD, Mukherjee D, et al. 2021 AHA/ACC Guideline for Chest Pain Evaluation & Diagnosis. Circulation. 2021;144(22):e588-e637. https://doi.org/10.1161/CIR.0000000000001029",
        "Byrne RA, Rossello X, Coughlan JJ, et al. 2023 ESC Guidelines for the Management of Acute Coronary Syndromes. European Heart Journal. 2023;44(38):3720-3826. https://doi.org/10.1093/eurheartj/ehad191"
    ],
    "AFib / Flutter w/ RVR": [
        "Joglar JA, Chung MK, Armbruster AL, et al. 2023 ACC/AHA/ACCP/HRS Guideline for Diagnosis and Management of Atrial Fibrillation. Circulation. 2024;149(1):e1-e156. https://doi.org/10.1161/CIR.0000000000001193",
        "Van Gelder IC, Rienstra M, Bunting KV, et al. 2024 ESC Guidelines for the Management of Atrial Fibrillation. European Heart Journal. 2024;45(36):3314-3414. https://doi.org/10.1093/eurheartj/ehae176",
        "January CT, Wann LS, Calkins H, et al. 2019 AHA/ACC/HRS Focused Update on Atrial Fibrillation. Journal of the American College of Cardiology. 2019;74(1):104-132."
    ],
    "SVT (Supraventricular Tachycardia)": [
        "Page RL, Joglar JA, Caldwell MA, et al. 2015 ACC/AHA/HRS Guideline for the Management of Adult Patients With Supraventricular Tachycardia. Circulation. 2016;133(14):e506-e574. https://doi.org/10.1161/CIR.0000000000000311",
        "Brugada J, Katritsis DG, Arbelo E, et al. 2019 ESC Guidelines for the Management of Patients with Supraventricular Tachycardia. European Heart Journal. 2020;41(5):655-720. https://doi.org/10.1093/eurheartj/ehz467"
    ],
    "Ventricular Tachycardia": [
        "Al-Khatib SM, Stevenson WG, Ackerman MJ, et al. 2017 AHA/ACC/HRS Guideline for Management of Patients With Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death. Circulation. 2018;138(13):e272-e391. https://doi.org/10.1161/CIR.0000000000000549",
        "Zeppenfeld K, Tfelt-Hansen J, de Riva M, et al. 2022 ESC Guidelines for the Management of Patients with Ventricular Arrhythmias and the Prevention of Sudden Cardiac Death. European Heart Journal. 2022;43(40):3997-4126. https://doi.org/10.1093/eurheartj/ehac262"
    ],
    "Cardiogenic Shock / ADHF": [
        "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032. https://doi.org/10.1161/CIR.0000000000001063",
        "McDonagh TA, Metra M, Adamo M, et al. 2023 Focused Update of the 2021 ESC Guidelines for the Diagnosis and Treatment of Acute and Chronic Heart Failure. European Heart Journal. 2023;44(37):3627-3639. https://doi.org/10.1093/eurheartj/ehad195",
        "van Diepen S, Katz JN, Albert NM, et al. Contemporary Management of Cardiogenic Shock: AHA Scientific Statement. Circulation. 2017;136(16):e52-e68. https://doi.org/10.1161/CIR.0000000000000525"
    ],
    "Cardiac Tamponade": [
        "Adler Y, Charron P, Imazio M, et al. 2015 ESC Guidelines for the Diagnosis and Management of Pericardial Diseases. European Heart Journal. 2015;36(42):2921-2964. https://doi.org/10.1093/eurheartj/ehv318",
        "Defined Approach to Pericardiocentesis. Roberts & Hedges' Clinical Procedures in Emergency Medicine and Acute Care, 7th edition. 2019."
    ],
    "Hypertensive Emergency": [
        "Whelton PK, Carey RM, Aronow WS, et al. 2017 ACC/AHA Guideline for the Prevention, Detection, Evaluation, and Management of High Blood Pressure in Adults. Hypertension. 2018;71(6):e13-e115. https://doi.org/10.1161/HYP.0000000000000065",
        "Unger T, Borghi C, Charchar F, et al. 2020 International Society of Hypertension Global Hypertension Practice Guidelines. Hypertension. 2020;75(6):1334-1357. https://doi.org/10.1161/HYPERTENSIONAHA.120.15026",
        "van den Born BJH, et al. ESC Council on Hypertension Position Document on the Management of Hypertensive Emergencies. European Heart Journal — Cardiovascular Pharmacotherapy. 2019;5(1):37-46."
    ],
    "Pericarditis": [
        "Adler Y, Charron P, Imazio M, et al. 2015 ESC Guidelines for the Diagnosis and Management of Pericardial Diseases. European Heart Journal. 2015;36(42):2921-2964. https://doi.org/10.1093/eurheartj/ehv318",
        "Chiabrando JG, Bonaventura A, Vecchié A, et al. Management of Acute and Recurrent Pericarditis: JACC State-of-the-Art Review. Journal of the American College of Cardiology. 2020;75(1):76-92. https://doi.org/10.1016/j.jacc.2019.11.021"
    ],
    "LVAD Emergencies": [
        "Feldman D, Pamboukian SV, Teuteberg JJ, et al. The 2013 ISHLT Guidelines for Mechanical Circulatory Support. Journal of Heart & Lung Transplantation. 2013;32(2):157-187. https://doi.org/10.1016/j.healun.2012.09.013",
        "Molina EJ, Shah P, Kiernan MS, et al. The Society of Thoracic Surgeons Intermacs 2020 Annual Report. Annals of Thoracic Surgery. 2021;111(3):778-792. https://doi.org/10.1016/j.athoracsur.2020.12.038"
    ],
    "ECMO Emergencies": [
        "Extracorporeal Life Support Organization (ELSO). ELSO Guidelines for Adult Respiratory Failure. 2021. https://www.elso.org/resources/guidelines",
        "Badulak J, Antonini MV, Stead CM, et al. ELSO COVID-19 Working Group Guideline. ASAIO Journal. 2021;67(5):472-481.",
        "Combes A, Hajage D, Capellier G, et al. Extracorporeal Membrane Oxygenation for Severe Acute Respiratory Distress Syndrome (EOLIA trial). New England Journal of Medicine. 2018;378(21):1965-1975. https://doi.org/10.1056/NEJMoa1800385"
    ],
    # Acute Respiratory Failure already has references
    "Flash Pulmonary Edema": [
        "Heidenreich PA, Bozkurt B, Aguilar D, et al. 2022 AHA/ACC/HFSA Guideline for the Management of Heart Failure. Circulation. 2022;145(18):e895-e1032. https://doi.org/10.1161/CIR.0000000000001063",
        "Gray A, Goodacre S, Newby DE, et al. Noninvasive Ventilation in Acute Cardiogenic Pulmonary Edema (3CPO trial). New England Journal of Medicine. 2008;359(2):142-151. https://doi.org/10.1056/NEJMoa0707992",
        "Mebazaa A, Yilmaz MB, Levy P, et al. Recommendations on Pre-Hospital and Early Hospital Management of Acute Heart Failure: ESC Working Group Consensus. European Journal of Heart Failure. 2015;17(6):544-558."
    ],
    "Pulmonary Embolism": [
        "Konstantinides SV, Meyer G, Becattini C, et al. 2019 ESC Guidelines for the Diagnosis & Management of Acute Pulmonary Embolism. European Heart Journal. 2020;41(4):543-603. https://doi.org/10.1093/eurheartj/ehz405",
        "Stevens SM, Woller SC, Kreuziger LB, et al. Antithrombotic Therapy for VTE Disease: 2nd Update of the CHEST Guideline. Chest. 2021;160(6):e545-e608. https://doi.org/10.1016/j.chest.2021.07.055",
        "Defined Approach to Pulmonary Embolism Response Teams (PERT Consortium). PE Response Team Management Algorithm. Journal of the American College of Cardiology. 2019."
    ],
    "COPD Exacerbation": [
        "Global Initiative for Chronic Obstructive Lung Disease (GOLD). 2025 GOLD Report: Global Strategy for the Diagnosis, Management, and Prevention of COPD. 2025. https://goldcopd.org/2025-gold-report/",
        "Wedzicha JA, Calverley PM, Albert RK, et al. Prevention of COPD Exacerbations: ERS/ATS Guideline. European Respiratory Journal. 2017;50(3):1602265. https://doi.org/10.1183/13993003.02265-2016"
    ],
    "Tracheostomy Emergencies": [
        "McGrath BA, Bates L, Atkinson D, Moore JA. Multidisciplinary Guidelines for the Management of Tracheostomy and Laryngectomy Airway Emergencies (NTSP). Anaesthesia. 2012;67(9):1025-1041. https://doi.org/10.1111/j.1365-2044.2012.07217.x",
        "Mitchell RB, Hussey HM, Setzen G, et al. Clinical Consensus Statement: Tracheostomy Care. Otolaryngology — Head & Neck Surgery. 2013;148(1):6-20. https://doi.org/10.1177/0194599812460376"
    ],
    "Angioedema": [
        "Maurer M, Magerl M, Betschel S, et al. The International WAO/EAACI Guideline for the Management of Hereditary Angioedema — The 2021 Revision and Update. Allergy. 2022;77(7):1961-1990. https://doi.org/10.1111/all.15214",
        "Bernstein JA, Moellman JJ. Emerging Concepts in the Diagnosis and Treatment of Patients with Undifferentiated Angioedema. International Journal of Emergency Medicine. 2012;5:39. https://doi.org/10.1186/1865-1380-5-39",
        "UpToDate. ACE inhibitor-induced angioedema. 2024. https://www.uptodate.com/contents/ace-inhibitor-induced-angioedema"
    ],
    "Severe Asthma": [
        "Global Initiative for Asthma (GINA). 2024 GINA Report: Global Strategy for Asthma Management and Prevention. 2024. https://ginasthma.org/2024-report/",
        "National Asthma Education and Prevention Program (NAEPP). 2020 Focused Updates to the Asthma Management Guidelines. NIH/NHLBI. 2020. https://www.nhlbi.nih.gov/health-topics/asthma-management-guidelines-2020-updates",
        "Rowe BH, Bretzlaff JA, Bourdon C, et al. Magnesium Sulfate for Treating Exacerbations of Acute Asthma in the Emergency Department. Cochrane Database of Systematic Reviews. 2000;(2):CD001490."
    ],
    "Upper Airway Obst.": [
        "Duff JP, Topjian AA, Berg MD, et al. 2019 AHA Focused Update on Pediatric Advanced Life Support: Airway Management. Circulation. 2019;140(24):e904-e914.",
        "Pfleger A, Eber E. Management of Acute Severe Upper Airway Obstruction in Children. Paediatric Respiratory Reviews. 2013;14(2):70-77. https://doi.org/10.1016/j.prrv.2013.02.003",
        "Cook TM, Woodall N, Frerk C. Major Complications of Airway Management in the UK: Results of NAP4. British Journal of Anaesthesia. 2011;106(5):617-631. https://doi.org/10.1093/bja/aer058"
    ],
    "Pneumothorax / Hemothorax": [
        "Roberts DJ, Leigh-Smith S, Faris PD, et al. Clinical Presentation of Patients With Tension Pneumothorax: A Systematic Review. Annals of Surgery. 2015;261(6):1068-1078.",
        "Baumann MH, Strange C, Heffner JE, et al. Management of Spontaneous Pneumothorax: ACCP Delphi Consensus Statement. Chest. 2001;119(2):590-602.",
        "Hallifax RJ, McKeown E, Sivakumar P, et al. Ambulatory Management of Primary Spontaneous Pneumothorax (RAMPP trial). New England Journal of Medicine. 2020;382(5):405-415. https://doi.org/10.1056/NEJMoa1916030"
    ],
    "Acute Ischemic Stroke": [
        "Powers WJ, Rabinstein AA, Ackerson T, et al. Guidelines for the Early Management of Patients With Acute Ischemic Stroke: 2019 Update to the 2018 AHA/ASA Guideline. Stroke. 2019;50(12):e344-e418. https://doi.org/10.1161/STR.0000000000000211",
        "Berge E, Whiteley W, Audebert H, et al. European Stroke Organisation (ESO) Guidelines on Intravenous Thrombolysis for Acute Ischaemic Stroke. European Stroke Journal. 2021;6(1):I-LXII. https://doi.org/10.1177/2396987321989865",
        "Nogueira RG, Jadhav AP, Haussen DC, et al. Thrombectomy 6 to 24 Hours After Stroke with a Mismatch Between Deficit and Infarct (DAWN trial). New England Journal of Medicine. 2018;378(1):11-21. https://doi.org/10.1056/NEJMoa1706442"
    ],
    "Seizure / Status Epilepticus": [
        "Glauser T, Shinnar S, Gloss D, et al. Evidence-Based Guideline: Treatment of Convulsive Status Epilepticus in Children and Adults — AAN Guideline. Epilepsy Currents. 2016;16(1):48-61. https://doi.org/10.5698/1535-7597-16.1.48",
        "Brophy GM, Bell R, Claassen J, et al. Guidelines for the Evaluation and Management of Status Epilepticus. Neurocritical Care. 2012;17(1):3-23. https://doi.org/10.1007/s12028-012-9695-z",
        "Kapur J, Elm J, Chamberlain JM, et al. Randomized Trial of Three Anticonvulsant Medications for Status Epilepticus (ESETT). New England Journal of Medicine. 2019;381(22):2103-2113. https://doi.org/10.1056/NEJMoa1905795"
    ],
    "Serotonin Syndrome": [
        "Boyer EW, Shannon M. The Serotonin Syndrome. New England Journal of Medicine. 2005;352(11):1112-1120. https://doi.org/10.1056/NEJMra041867",
        "Isbister GK, Buckley NA, Whyte IM. Serotonin Toxicity: A Practical Approach to Diagnosis and Treatment. Medical Journal of Australia. 2007;187(6):361-365."
    ],
    "Acute Agitation": [
        "Wilson MP, Pepper D, Currier GW, et al. The Psychopharmacology of Agitation: Consensus Statement of the AAEP Project BETA Psychopharmacology Workgroup. Western Journal of Emergency Medicine. 2012;13(1):26-34. https://doi.org/10.5811/westjem.2011.9.6866",
        "Garriga M, Pacchiarotti I, Kasper S, et al. Assessment and Management of Agitation in Psychiatry: Expert Consensus. World Journal of Biological Psychiatry. 2016;17(2):86-128. https://doi.org/10.3109/15622975.2015.1132007"
    ],
    "Acute Dystonic Reaction": [
        "Bhidayasiri R, Fahn S, Weiner WJ, et al. Evidence-Based Guideline: Treatment of Tardive Syndromes — AAN Guideline. Neurology. 2013;81(5):463-469. https://doi.org/10.1212/WNL.0b013e31829d86b6",
        "van Harten PN, Hoek HW, Kahn RS. Acute Dystonia Induced by Drug Treatment. British Medical Journal. 1999;319(7210):623-626."
    ],
    # Guillain-Barré Syndrome already has references
    "Myasthenic Crisis (Myasthenia Gravis)": [
        "Sanders DB, Wolfe GI, Benatar M, et al. International Consensus Guidance for Management of Myasthenia Gravis: Executive Summary. Neurology. 2016;87(4):419-425. https://doi.org/10.1212/WNL.0000000000002790",
        "Narayanaswami P, Sanders DB, Wolfe G, et al. International Consensus Guidance for Management of Myasthenia Gravis: 2020 Update. Neurology. 2021;96(3):114-122. https://doi.org/10.1212/WNL.0000000000011124"
    ],
    # Sepsis & Septic Shock already has references
    "Meningitis / Encephalitis": [
        "Tunkel AR, Hartman BJ, Kaplan SL, et al. Practice Guidelines for the Management of Bacterial Meningitis. Clinical Infectious Diseases. 2004;39(9):1267-1284. https://doi.org/10.1086/425368",
        "van de Beek D, Cabellos C, Dzupova O, et al. ESCMID Guideline: Diagnosis and Treatment of Acute Bacterial Meningitis. Clinical Microbiology and Infection. 2016;22(Suppl 3):S37-S62. https://doi.org/10.1016/j.cmi.2016.01.007",
        "Venkatesan A, Tunkel AR, Bloch KC, et al. Case Definitions, Diagnostic Algorithms, and Priorities in Encephalitis: Consensus Statement of the International Encephalitis Consortium. Clinical Infectious Diseases. 2013;57(8):1114-1128. https://doi.org/10.1093/cid/cit458"
    ],
    "Anaphylaxis": [
        "Cardona V, Ansotegui IJ, Ebisawa M, et al. World Allergy Organization Anaphylaxis Guidance 2020. World Allergy Organization Journal. 2020;13(10):100472. https://doi.org/10.1016/j.waojou.2020.100472",
        "Shaker MS, Wallace DV, Golden DBK, et al. Anaphylaxis — A 2020 Practice Parameter Update, Systematic Review, and GRADE Analysis. Journal of Allergy & Clinical Immunology. 2020;145(4):1082-1123. https://doi.org/10.1016/j.jaci.2020.01.017",
        "Muraro A, Worm M, Alviani C, et al. EAACI Guidelines: Anaphylaxis (2021 Update). Allergy. 2022;77(2):357-377. https://doi.org/10.1111/all.15032"
    ],
    "Massive GI Bleed": [
        "Laine L, Barkun AN, Saltzman JR, et al. ACG Clinical Guideline: Upper Gastrointestinal and Ulcer Bleeding. American Journal of Gastroenterology. 2021;116(5):899-917. https://doi.org/10.14309/ajg.0000000000001245",
        "Oakland K, Chadwick G, East JE, et al. Diagnosis and Management of Acute Lower Gastrointestinal Bleeding: Guidelines from the British Society of Gastroenterology. Gut. 2019;68(5):776-789. https://doi.org/10.1136/gutjnl-2018-317807",
        "Villanueva C, Colomo A, Bosch A, et al. Transfusion Strategies for Acute Upper Gastrointestinal Bleeding. New England Journal of Medicine. 2013;368(1):11-21. https://doi.org/10.1056/NEJMoa1211801"
    ],
    "Acute Liver Failure": [
        "European Association for the Study of the Liver (EASL). EASL Clinical Practical Guidelines on the Management of Acute (Fulminant) Liver Failure. Journal of Hepatology. 2017;66(5):1047-1081. https://doi.org/10.1016/j.jhep.2016.12.003",
        "Lee WM, Stravitz RT, Larson AM. Introduction to the Revised AASLD Position Paper on Acute Liver Failure. Hepatology. 2012;55(3):965-967. https://doi.org/10.1002/hep.25551",
        "Bernal W, Wendon J. Acute Liver Failure. New England Journal of Medicine. 2013;369(26):2525-2534. https://doi.org/10.1056/NEJMra1208937"
    ],
    "Acute Mesenteric Ischemia": [
        "Bala M, Kashuk J, Moore EE, et al. Acute Mesenteric Ischemia: Guidelines of the World Society of Emergency Surgery. World Journal of Emergency Surgery. 2017;12:38. https://doi.org/10.1186/s13017-017-0150-5",
        "Defined Approach to Acute Mesenteric Ischemia — AGA Clinical Practice Update. Clin Gastroenterol Hepatol. 2020;18(5):944-953. https://doi.org/10.1016/j.cgh.2019.11.029",
        "Defined Approach: Defined Approach to diagnosis and treatment of mesenteric ischemia. European Journal of Vascular and Endovascular Surgery. 2017;53(4):460-510."
    ],
    "DKA / HHS": [
        "Kitabchi AE, Umpierrez GE, Miles JM, Fisher JN. Hyperglycemic Crises in Adult Patients With Diabetes. Diabetes Care. 2009;32(7):1335-1343. https://doi.org/10.2337/dc09-9032",
        "Umpierrez GE, Davis GM, ElSayed NA, et al. ADA Consensus Report: Management of Hyperglycaemic Crises — Diabetic Ketoacidosis and Hyperglycaemic Hyperosmolar State. Diabetologia. 2024;67:1455-1479. https://doi.org/10.1007/s00125-024-06183-8",
        "Joint British Diabetes Societies (JBDS). The Management of Diabetic Ketoacidosis in Adults. 2023. https://abcd.care/resource/management-diabetic-ketoacidosis-dka-adults"
    ],
    "Hypoglycemia": [
        "American Diabetes Association. Standards of Care in Diabetes — 2024: Glycemic Goals and Hypoglycemia. Diabetes Care. 2024;47(Suppl 1):S111-S125. https://doi.org/10.2337/dc24-S006",
        "Cryer PE, Axelrod L, Grossman AB, et al. Evaluation and Management of Adult Hypoglycemic Disorders: Endocrine Society Clinical Practice Guideline. Journal of Clinical Endocrinology & Metabolism. 2009;94(3):709-728. https://doi.org/10.1210/jc.2008-1410"
    ],
    "Adrenal Crisis": [
        "Bornstein SR, Allolio B, Arlt W, et al. Diagnosis and Treatment of Primary Adrenal Insufficiency: An Endocrine Society Clinical Practice Guideline. Journal of Clinical Endocrinology & Metabolism. 2016;101(2):364-389. https://doi.org/10.1210/jc.2015-1710",
        "Rushworth RL, Torpy DJ, Falhammar H. Adrenal Crisis. New England Journal of Medicine. 2019;381(9):852-861. https://doi.org/10.1056/NEJMra1807486"
    ],
    "Thyroid Storm": [
        "Ross DS, Burch HB, Cooper DS, et al. 2016 ATA Guidelines for Diagnosis and Management of Hyperthyroidism and Other Causes of Thyrotoxicosis. Thyroid. 2016;26(10):1343-1421. https://doi.org/10.1089/thy.2016.0229",
        "Akamizu T, Satoh T, Isozaki O, et al. Diagnostic Criteria, Clinical Features, and Incidence of Thyroid Storm Based on Nationwide Surveys. Thyroid. 2012;22(7):661-679. https://doi.org/10.1089/thy.2011.0334"
    ],
    "Myxedema Coma": [
        "Jonklaas J, Bianco AC, Bauer AJ, et al. Guidelines for the Treatment of Hypothyroidism: ATA/AACE Task Force. Thyroid. 2014;24(12):1670-1751. https://doi.org/10.1089/thy.2014.0028",
        "Wall CR. Myxedema Coma: Diagnosis and Treatment. American Family Physician. 2000;62(11):2485-2490.",
        "Wiersinga WM. Myxedema and Coma (Severe Hypothyroidism). Endotext [Internet]. 2018. https://www.ncbi.nlm.nih.gov/books/NBK279007/"
    ],
    "Acute renal failure/ESRD": [
        "Kidney Disease: Improving Global Outcomes (KDIGO). KDIGO Clinical Practice Guideline for Acute Kidney Injury. Kidney International Supplements. 2012;2(1):1-138. https://kdigo.org/guidelines/acute-kidney-injury/",
        "Bagshaw SM, Darmon M, Bhagwanjee S, et al. Clinical Review: Prevention of Acute Kidney Injury — AKI-CLINI Update. Critical Care. 2024;28:55.",
        "Gaudry S, Hajage D, Schortgen F, et al. Initiation Strategies for Renal-Replacement Therapy in the Intensive Care Unit (AKIKI trial). New England Journal of Medicine. 2016;375(2):122-133. https://doi.org/10.1056/NEJMoa1603017"
    ],
    "↑K (Hyperkalemia)": [
        "Clase CM, Carrero JJ, Ellison DH, et al. Potassium Homeostasis and Management of Dyskalemia in Kidney Diseases: Conclusions from a KDIGO Controversies Conference. Kidney International. 2020;97(1):42-61. https://doi.org/10.1016/j.kint.2019.09.018",
        "Palmer BF, Clegg DJ. Diagnosis and Treatment of Hyperkalemia. Cleveland Clinic Journal of Medicine. 2017;84(12):934-942. https://doi.org/10.3949/ccjm.84a.17056",
        "Long B, Warix JR, Koyfman A. Controversies in Management of Hyperkalemia. Journal of Emergency Medicine. 2018;55(2):192-205. https://doi.org/10.1016/j.jemermed.2018.04.004"
    ],
    "Hypokalemia": [
        "Clase CM, Carrero JJ, Ellison DH, et al. Potassium Homeostasis and Management of Dyskalemia in Kidney Diseases: Conclusions from a KDIGO Controversies Conference. Kidney International. 2020;97(1):42-61. https://doi.org/10.1016/j.kint.2019.09.018",
        "Unwin RJ, Luft FC, Shirley DG. Pathophysiology and Management of Hypokalemia: A Clinical Perspective. Nature Reviews Nephrology. 2011;7(2):75-84. https://doi.org/10.1038/nrneph.2010.175"
    ],
    "Hyponatremia": [
        "Spasovski G, Vanholder R, Allolio B, et al. Clinical Practice Guideline on Diagnosis and Treatment of Hyponatraemia. European Journal of Endocrinology. 2014;170(3):G1-G47. https://doi.org/10.1530/EJE-13-1020",
        "Verbalis JG, Goldsmith SR, Greenberg A, et al. Diagnosis, Evaluation, and Treatment of Hyponatremia: Expert Panel Recommendations. American Journal of Medicine. 2013;126(10 Suppl 1):S1-S42. https://doi.org/10.1016/j.amjmed.2013.07.006",
        "Sterns RH. Disorders of Plasma Sodium — Causes, Consequences, and Correction. New England Journal of Medicine. 2015;372(1):55-65. https://doi.org/10.1056/NEJMra1404489"
    ],
    "Hypercalcemia": [
        "Bilezikian JP, Khan AA, Potts JT Jr, et al. Guidelines for the Management of Asymptomatic Primary Hyperparathyroidism: Summary Statement from the Fourth International Workshop. Journal of Clinical Endocrinology & Metabolism. 2014;99(10):3561-3569. https://doi.org/10.1210/jc.2014-1413",
        "Rosner MH, Dalkin AC. Onco-Nephrology: The Pathophysiology and Treatment of Malignancy-Associated Hypercalcemia. Clinical Journal of the American Society of Nephrology. 2012;7(10):1722-1729. https://doi.org/10.2215/CJN.02470312"
    ],
    "Massive Hemorrhage / MTP": [
        "Spahn DR, Bouillon B, Cerny V, et al. The European Guideline on Management of Major Bleeding and Coagulopathy Following Trauma: 6th Edition. Critical Care. 2023;27:80. https://doi.org/10.1186/s13054-023-04327-7",
        "Holcomb JB, Tilley BC, Baraniuk S, et al. Transfusion of Plasma, Platelets, and Red Blood Cells in a 1:1:1 vs a 1:1:2 Ratio (PROPPR trial). JAMA. 2015;313(5):471-482. https://doi.org/10.1001/jama.2015.12",
        "Cannon JW, Khan MA, Raja AS, et al. Damage Control Resuscitation in Patients with Severe Traumatic Hemorrhage: A Practice Management Guideline. Journal of Trauma and Acute Care Surgery. 2017;82(3):605-617."
    ],
    "Anticoagulation Reversal": [
        "Tomaselli GF, Mahaffey KW, Cuker A, et al. 2020 ACC Expert Consensus Decision Pathway on Management of Bleeding in Patients on Oral Anticoagulants. Journal of the American College of Cardiology. 2020;76(5):594-622. https://doi.org/10.1016/j.jacc.2020.04.053",
        "Frontera JA, Lewin JJ III, Rabinstein AA, et al. Guideline for Reversal of Antithrombotics in Intracranial Hemorrhage. Neurocritical Care. 2016;24(1):6-46. https://doi.org/10.1007/s12028-015-0222-x",
        "Pollack CV Jr, Reilly PA, van Ryn J, et al. Idarucizumab for Dabigatran Reversal — Full Cohort Analysis (RE-VERSE AD trial). New England Journal of Medicine. 2017;377(5):431-441. https://doi.org/10.1056/NEJMoa1707278"
    ],
    # Bloodless Medicine / Jehovah's Witness already has references
    "Coagulopathy Reversal": [
        "Pabinger I, Fries D, Schöchl H, et al. Tranexamic Acid for Treatment and Prophylaxis of Bleeding and Hyperfibrinolysis. Wiener Klinische Wochenschrift. 2017;129(9-10):303-316. https://doi.org/10.1007/s00508-017-1194-y",
        "Levy JH, Dutton RP, Hemphill JC III, et al. Multidisciplinary Approach to the Challenge of Hemostasis. Anesthesia & Analgesia. 2010;110(2):354-364. https://doi.org/10.1213/ANE.0b013e3181c84ba5",
        "Levi M, Toh CH, Thachil J, Watson HG. Guidelines for the Diagnosis and Management of Disseminated Intravascular Coagulation. British Journal of Haematology. 2009;145(1):24-33. https://doi.org/10.1111/j.1365-2141.2009.07600.x"
    ],
    "Transfusion Reactions": [
        "Delaney M, Wendel S, Bercovitz RS, et al. Transfusion Reactions: Prevention, Diagnosis, and Treatment. The Lancet. 2016;388(10061):2825-2836. https://doi.org/10.1016/S0140-6736(15)01313-6",
        "AABB. Standards for Blood Banks and Transfusion Services, 33rd Edition. 2022.",
        "Panch SR, Montemayor-Garcia C, Klein HG. Hemolytic Transfusion Reactions. New England Journal of Medicine. 2019;381(2):150-162. https://doi.org/10.1056/NEJMra1802338"
    ],
    "Acute Chest Syndrome": [
        "Yawn BP, Buchanan GR, Afenyi-Annan AN, et al. Management of Sickle Cell Disease: Summary of the 2014 Evidence-Based Report by Expert Panel Members (NHLBI). JAMA. 2014;312(10):1033-1048. https://doi.org/10.1001/jama.2014.10517",
        "Howard J, Hart N, Roberts-Harewood M, et al. Guideline on the Management of Acute Chest Syndrome in Sickle Cell Disease. British Journal of Haematology. 2015;169(4):492-505. https://doi.org/10.1111/bjh.13348",
        "DeBaun MR, Jordan LC, King AA, et al. ASH 2020 Guidelines for Sickle Cell Disease: Prevention, Diagnosis, and Treatment of Cerebrovascular Disease in Children and Adults. Blood Advances. 2020;4(8):1554-1588. https://doi.org/10.1182/bloodadvances.2019001142"
    ],
    "Immune Thrombocytopenia (ITP)": [
        "Neunert C, Terrell DR, Arnold DM, et al. ASH 2019 Guidelines for Immune Thrombocytopenia. Blood Advances. 2019;3(23):3829-3866. https://doi.org/10.1182/bloodadvances.2019000966",
        "Provan D, Arnold DM, Bussel JB, et al. Updated International Consensus Report on the Investigation and Management of Primary Immune Thrombocytopenia. Blood Advances. 2019;3(22):3780-3817. https://doi.org/10.1182/bloodadvances.2019000812"
    ],
    "TMA / TTP / HUS": [
        "Zheng XL, Vesely SK, Cataland SR, et al. ISTH Guidelines for Treatment of Thrombotic Thrombocytopenic Purpura. Journal of Thrombosis and Haemostasis. 2020;18(10):2496-2502. https://doi.org/10.1111/jth.15010",
        "Scully M, Cataland S, Coppo P, et al. Consensus on the Standardization of Terminology in Thrombotic Thrombocytopenic Purpura and Related Thrombotic Microangiopathies. Journal of Thrombosis and Haemostasis. 2017;15(2):312-322. https://doi.org/10.1111/jth.13571",
        "Coppo P, Cuker A, George JN. Thrombotic Thrombocytopenic Purpura: Toward Targeted Therapy and Precision Medicine. Research and Practice in Thrombosis and Haemostasis. 2019;3(1):26-37."
    ],
    "HLH": [
        "La Rosée P, Horne A, Hines M, et al. Recommendations for the Management of Hemophagocytic Lymphohistiocytosis in Adults. Blood. 2019;133(23):2465-2477. https://doi.org/10.1182/blood.2018874828",
        "Jordan MB, Allen CE, Greenberg J, et al. Challenges in the Diagnosis of Hemophagocytic Lymphohistiocytosis: Recommendations from the North American Consortium for Histiocytosis (NACHO). Pediatric Blood & Cancer. 2019;66(11):e27929. https://doi.org/10.1002/pbc.27929",
        "Henter JI, Horne A, Aricó M, et al. HLH-2004: Diagnostic and Therapeutic Guidelines for Hemophagocytic Lymphohistiocytosis. Pediatric Blood & Cancer. 2007;48(2):124-131. https://doi.org/10.1002/pbc.21039"
    ],
    "Malignant Spinal Cord Compression": [
        "National Institute for Health and Care Excellence (NICE). Metastatic Spinal Cord Compression in Adults: Risk Assessment, Diagnosis, and Management (CG75). 2008 (Updated 2023). https://www.nice.org.uk/guidance/cg75",
        "Defined Approach to Malignant Spinal Cord Compression: ASCO Clinical Practice Guideline. Journal of Clinical Oncology. 2023.",
        "Loblaw DA, Perry J, Chambers A, Laperriere NJ. Systematic Review of the Diagnosis and Management of Malignant Extradural Spinal Cord Compression. Journal of Clinical Oncology. 2005;23(9):2028-2037. https://doi.org/10.1200/JCO.2005.00.960"
    ],
    "SVC Syndrome": [
        "Wilson LD, Detterbeck FC, Yahalom J. Superior Vena Cava Syndrome with Malignant Causes. New England Journal of Medicine. 2007;356(18):1862-1869. https://doi.org/10.1056/NEJMcp067190",
        "Defined Approach to SVC Syndrome: UpToDate. Malignancy-associated superior vena cava syndrome. 2024. https://www.uptodate.com/contents/malignancy-associated-superior-vena-cava-syndrome"
    ],
    "Tumor Lysis Syndrome": [
        "Cairo MS, Coiffier B, Reiter A, Younes A. Recommendations for the Evaluation of Risk and Prophylaxis of Tumour Lysis Syndrome (TLS) in Adults and Children with Malignant Diseases: An Expert TLS Panel Consensus. British Journal of Haematology. 2010;149(4):578-586. https://doi.org/10.1111/j.1365-2141.2010.08143.x",
        "Jones GL, Will A, Jackson GH, et al. Guidelines for the Management of Tumour Lysis Syndrome in Adults and Children with Haematological Malignancies. British Journal of Haematology. 2015;169(5):661-671. https://doi.org/10.1111/bjh.13403",
        "Howard SC, Jones DP, Pui CH. The Tumor Lysis Syndrome. New England Journal of Medicine. 2011;364(19):1844-1854. https://doi.org/10.1056/NEJMra0904569"
    ],
    "Hyperviscosity Syndrome": [
        "Stone MJ, Bogen SA. Evidence-Based Focused Review of Management of Hyperviscosity Syndrome. Blood. 2012;119(10):2205-2208. https://doi.org/10.1182/blood-2011-04-347690",
        "Dimopoulos MA, Kastritis E, Owen RG, et al. Treatment Recommendations for Patients with Waldenström Macroglobulinemia (WM) and Related Disorders: IWWM-7 Consensus. Blood. 2014;124(9):1404-1411. https://doi.org/10.1182/blood-2014-03-565135"
    ],
    "Cytokine Release Syndrome": [
        "Lee DW, Santomasso BD, Locke FL, et al. ASTCT Consensus Grading for Cytokine Release Syndrome and Neurologic Toxicity Associated with Immune Effector Cells. Biology of Blood and Marrow Transplantation. 2019;25(4):625-638. https://doi.org/10.1016/j.bbmt.2018.12.758",
        "Neelapu SS, Tummala S, Kebriaei P, et al. Chimeric Antigen Receptor T-Cell Therapy — Assessment and Management of Toxicities. Nature Reviews Clinical Oncology. 2018;15(1):47-62. https://doi.org/10.1038/nrclinonc.2017.148",
        "NCCN Guidelines: Management of Immunotherapy-Related Toxicities, Version 2.2024. National Comprehensive Cancer Network. 2024. https://www.nccn.org/guidelines/guidelines-detail?category=3&id=1490"
    ],
    "Differentiation Syndrome": [
        "Montesinos P, Bergua JM, Vellenga E, et al. Differentiation Syndrome in Patients with Acute Promyelocytic Leukemia Treated with All-Trans Retinoic Acid and Anthracycline Chemotherapy. Blood. 2009;113(4):775-783. https://doi.org/10.1182/blood-2008-07-168617",
        "Sanz MA, Fenaux P, Tallman MS, et al. Management of Acute Promyelocytic Leukemia: Updated Recommendations from an Expert Panel of the European LeukemiaNet. Blood. 2019;133(15):1630-1643. https://doi.org/10.1182/blood-2019-01-894980",
        "NCCN Guidelines: Acute Myeloid Leukemia, Version 3.2024. National Comprehensive Cancer Network. 2024. https://www.nccn.org/guidelines/guidelines-detail?category=1&id=1411"
    ],
    "Baclofen Toxicity & Withdrawal": [
        "UpToDate. Baclofen: Drug Information and Toxicity. 2024. https://www.uptodate.com/contents/baclofen-poisoning-and-withdrawal",
        "Ross JC, Cook AM, Stewart GL, Fahy BG. Acute Intrathecal Baclofen Withdrawal: A Brief Review of Treatment Options. Neurocritical Care. 2011;14(1):103-108. https://doi.org/10.1007/s12028-010-9422-6"
    ],
    "Malignant Hyperthermia": [
        "Malignant Hyperthermia Association of the United States (MHAUS). Emergency Therapy for Malignant Hyperthermia. 2024. https://www.mhaus.org/healthcare-professionals/managing-a-crisis/",
        "Rosenberg H, Pollock N, Schiemann A, et al. Malignant Hyperthermia: A Review. Orphanet Journal of Rare Diseases. 2015;10:93. https://doi.org/10.1186/s13023-015-0310-1",
        "Hopkins PM, Rüffert H, Snoeck MM, et al. European Malignant Hyperthermia Group Guidelines for Investigation of Malignant Hyperthermia Susceptibility. British Journal of Anaesthesia. 2015;115(4):531-539. https://doi.org/10.1093/bja/aev225"
    ],
    "Cholinergic Toxidrome": [
        "Eddleston M, Buckley NA, Eyer P, Dawson AH. Management of Acute Organophosphorus Pesticide Poisoning. The Lancet. 2008;371(9612):597-607. https://doi.org/10.1016/S0140-6736(07)61202-1",
        "King AM, Aaron CK. Organophosphate and Carbamate Poisoning. Emergency Medicine Clinics of North America. 2015;33(1):133-151. https://doi.org/10.1016/j.emc.2014.09.010"
    ],
    "Anticholinergic Toxidrome": [
        "Burns MJ, Linden CH, Graudins A, Brown RM, Fletcher KE. A Comparison of Physostigmine and Benzodiazepines for the Treatment of Anticholinergic Poisoning. Annals of Emergency Medicine. 2000;35(4):374-381.",
        "Defined Approach: Goldfrank's Toxicologic Emergencies, 11th Edition. McGraw-Hill. 2019. Chapter: Anticholinergic Toxicity."
    ],
    "Sympathomimetic Toxidrome": [
        "Richards JR, Albertson TE, Derlet RW, et al. Treatment of Toxicity from Amphetamines, Related Derivatives, and Analogues: A Systematic Clinical Review. Journal of Medical Toxicology. 2015;11(2):195-212. https://doi.org/10.1007/s13181-015-0463-z",
        "Defined Approach: Goldfrank's Toxicologic Emergencies, 11th Edition. McGraw-Hill. 2019. Chapter: Sympathomimetics."
    ],
    "Sympatholytic Toxidrome": [
        "Graudins A, Lee HM, Druda D. Calcium Channel Blocker and Beta-Blocker Toxicity. Emergency Medicine Clinics of North America. 2015;33(3):519-538. https://doi.org/10.1016/j.emc.2015.04.005",
        "Engebretsen KM, Kaczmarek KM, Morgan J, Holger JS. High-Dose Insulin Therapy in Beta-Blocker and Calcium Channel-Blocker Poisoning. Clinical Toxicology. 2011;49(4):277-283. https://doi.org/10.3109/15563650.2011.582471",
        "St-Onge M, Anseeuw K, Cantrell FL, et al. Experts Consensus Recommendations for the Management of Calcium Channel Blocker Poisoning in Adults. Critical Care Medicine. 2017;45(3):e306-e315. https://doi.org/10.1097/CCM.0000000000002087"
    ],
    "Sedative-Hypnotic Toxidrome": [
        "Kang M, Galuska MA, Ghassemzadeh S. Benzodiazepine Toxicity. StatPearls [Internet]. 2024. https://www.ncbi.nlm.nih.gov/books/NBK482238/",
        "Penninga EI, Graudal N, Ladekarl MB, Jürgens G. Adverse Events Associated with Flumazenil Treatment for the Management of Suspected Benzodiazepine Intoxication — A Systematic Review with Meta-Analyses of Randomised Trials. Basic & Clinical Pharmacology & Toxicology. 2016;118(1):37-44. https://doi.org/10.1111/bcpt.12434"
    ],
    "Compartment Syndrome": [
        "Schmidt AH. Acute Compartment Syndrome. Injury. 2017;48 Suppl 1:S22-S25. https://doi.org/10.1016/j.injury.2017.04.024",
        "Via AG, Oliva F, Spoliti M, Maffulli N. Acute Compartment Syndrome. Muscles, Ligaments and Tendons Journal. 2015;5(1):18-22.",
        "Defined Approach: Long B, Koyfman A, Gottlieb M. Evaluation and Management of Acute Compartment Syndrome in the Emergency Department. Journal of Emergency Medicine. 2019;56(4):386-397. https://doi.org/10.1016/j.jemermed.2018.12.021"
    ],
}

def main():
    filepath = "/Users/andrewmcgowan/Desktop/Residency/Rapid response -planning/Rapid response -planning/Rapid response 2026/Rapid Response/Data/content.json"

    with open(filepath, 'r') as f:
        data = json.load(f)

    topics_updated = 0
    topics_skipped = 0

    for organ_system in data:
        for topic in organ_system.get("topics", []):
            title = topic.get("title", "")
            if title in REFERENCES:
                for section in topic.get("sections", []):
                    if section.get("title") == "References" and section.get("type") == "bullets":
                        if len(section.get("items", [])) == 0:
                            section["items"] = REFERENCES[title]
                            topics_updated += 1
                            print(f"  ✓ Added refs to: {title}")
                        else:
                            topics_skipped += 1
                            print(f"  ⊘ Skipped (has refs): {title}")
            else:
                # Check if it has empty references
                for section in topic.get("sections", []):
                    if section.get("title") == "References" and section.get("type") == "bullets":
                        if len(section.get("items", [])) == 0:
                            print(f"  ✗ Missing in map: {title}")

    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    print(f"\nDone. Updated {topics_updated} topics, skipped {topics_skipped} with existing refs.")

if __name__ == "__main__":
    main()
