---
layout: post
title: "Age at Onset and Time to Progression in the Leading Causes of Death: A Region-Stratified Synthesis"
date: 2026-09-03 12:00:00 +0800
lang: en
ref: global-causes-of-death-timelines
tags: [science]
wide: true
description: "Age at onset and disease-progression timelines for the leading causes of death, stratified by WHO region and income group — and how much of the regional difference is real biology versus a difference in measurement."
---

<div class="standfirst" markdown="1">
**Final version, cross-checked against two independent deep-research reports (Claude Advanced Research and Gemini Deep Research)**

Data baseline: WHO Global Health Estimates 2021 (released August 2024) · GBD 2021 · cohort studies including INTERHEART, China Kadoorie Biobank, Framingham and DIAN
</div>

## Abstract

This article surveys the leading causes of death identified by the World Health Organization (WHO), setting out for each the **statistical time of onset** (mean or median age at onset or diagnosis) and the **time to progression** (latency, dwell time within a stage, survival after an event or after diagnosis), stratified along two orthogonal dimensions: the six WHO geographical regions and income group. Three central conclusions:

1. **The list of causes is itself different by region.** The global top-ten list cannot be applied directly to individual regions. Eight of Africa's top ten are infectious or perinatal conditions (malaria, HIV, diarrhoeal disease, prematurity and so on); in the Western Pacific, stroke displaces ischaemic heart disease at the top; in the Americas, interpersonal violence enters the top ten. Any cross-regional analysis must start from each region's own list.
2. **Age at onset shifts along two axes at once — region and sex.** Vascular and metabolic disease presents roughly 5–10 years earlier in South Asian and African populations (mean age at first myocardial infarction 53.0 in South Asia versus 58.8 elsewhere), while high-income countries, by controlling cardiovascular risk factors in midlife, have pushed the age at dementia diagnosis back by about five years (80 → 85). Women develop cardiovascular and cerebrovascular disease 6–10 years later than men, but do worse after the event.
3. **Disease timelines come in two topologies.** *Event-type* diseases run long latency → acute event → post-event survival (ischaemic heart disease, stroke, lung cancer); *trajectory-type* diseases decline continuously and monotonically (Alzheimer's disease, COPD, chronic kidney disease, untreated HIV). The first suits competing-risk and multi-state survival models, the second trajectory or state-space models. And the timeline is not a natural constant: new therapies such as SGLT2 inhibitors and GLP-1 receptor agonists can now "buy" an individual patient 3–5.5 years of healthy time.

---

## 1. The evidence base, and cross-checking the two reports

This article merges two independently produced deep-research reports: Report A (Claude Advanced Research), stratified by the six WHO geographical regions, covering the natural history of infectious disease and the regional top-ten lists; and Report B (Gemini Deep Research), stratified by income group, covering sex differences, stage-level survival parameters, therapeutic intervention and the methodology of statistical bias. The two agree closely on the backbone figures, and their stratifying dimensions are orthogonal and complementary.

### 1.1 Parameters confirmed by both reports (highest confidence)

- Ischaemic heart disease is the leading cause of death worldwide: roughly 9.1 million deaths in 2021, 13% of the global total, an absolute increase of about 2.7 million since 2000.
- From the INTERHEART programme: mean age at first acute myocardial infarction is 53.0 years (SD 11.4) in South Asian countries versus 58.8 (SD 12.2) elsewhere.
- Deaths from diabetes have risen by about 95% since 2000; HIV-related deaths have fallen by about 60%.
- Age at onset of chronic disease is systematically earlier in low- and middle-income populations; high-income countries show an apparent "earlier diagnosis" driven by screening.
- The burden of dementia deaths is concentrated among women (about 68% of dementia deaths globally).

### 1.2 Points of conflict, and how they were resolved

| Point of conflict | Report B | Report A | Resolution and basis |
|---|---|---|---|
| Rank of stroke vs COPD | Calls both stroke and COPD "third globally" (internally inconsistent) | Stroke 3rd (~7.3 million), COPD 4th | **Stroke 3rd, COPD 4th.** "COPD third" reflects the older GHE 2019 basis; WHO GHE 2021 (updated August 2024) governs |
| Share attributable to NCDs | "NCDs in the top ten account for over 70% of all deaths" | WHO's own wording: 7 of the top ten are NCDs, accounting for **38% of all deaths** and **68% of the top-ten deaths** | Report B conflated two different denominators — "all NCDs ≈ 74% of total deaths" and "NCDs' share within the top ten". WHO's wording is used |
| Size of the South Asian MI advance | About 6 years earlier | About 10 years earlier | **Not a conflict — different denominators.** 5.8 years is the difference in country-level means (53.0 vs 58.8); ~10 years is the difference in median age at first presentation by ethnicity (South Asian 52 vs European 62). Both come from the INTERHEART programme |
| Age at stroke onset in LMICs | LMIC mean about 57 | About 63–66 in China, about 70 globally | "LMIC" is too coarse a bucket: the ~57 figure comes mainly from sub-Saharan African hospital cohorts, while China Kadoorie Biobank gives 63–66. This article splits by region and does not use a single LMIC mean |
| Fall in HIV deaths | 63% | 61% | Different reference years, same order of magnitude; "about 60%" is used |

### 1.3 What each report contributed

Unique to Report A: the top-ten lists for the six regions and their union; the natural history of infectious disease (malaria, tuberculosis, HIV, diarrhoeal disease); 28-day case fatality by stroke subtype from CKB; the preclinical time course of Alzheimer's disease from DIAN; EGFR-mutant lung cancer in never-smoking East Asian women; CKDu and biomass-related COPD; the event-type/trajectory-type modelling dichotomy.

Unique to Report B: sex differences in onset and prognosis; years of life lost by COPD GOLD stage and survival after an acute exacerbation; delay in dementia diagnosis and the falling incidence seen in Framingham; the CKM syndrome framework and the time gained from new drugs; the methodology of lead-time bias, length-time bias and overdiagnosis.

---

## 2. The global and regional top-ten lists

### 2.1 Global top ten (WHO GHE 2021, verified)

1 Ischaemic heart disease (9.1 million, 13%) · 2 COVID-19 (8.8 million) · 3 Stroke (~10%) · 4 COPD (~5%) · 5 Lower respiratory infections (2.5 million) · 6 Cancer of the trachea, bronchus and lung (1.9 million) · 7 Alzheimer's disease and other dementias (1.8 million) · 8 Diabetes · 9 Kidney disease · 10 Tuberculosis. Together the top ten account for about 39 million of the 68 million deaths worldwide, or 57%; ischaemic heart disease and stroke alone account for about 23% of all deaths.

### 2.2 The six regional lists (ranks 1–4 are high confidence; ranks 5–10 are reconstructed estimates — see §8)

| Region | Main entries (by number of deaths) | How it differs from the global list |
|---|---|---|
| Africa (AFRO) | Lower respiratory infections (8.6%), malaria (6.5%), stroke, ischaemic heart disease, neonatal/preterm conditions, diarrhoeal disease, HIV/AIDS (8th, ~406,000), tuberculosis | Eight entries are infectious or perinatal; malaria, diarrhoeal disease, prematurity and HIV enter the top ten but are absent from the global list |
| South-East Asia (SEARO, incl. India) | Ischaemic heart disease, stroke, COVID-19, COPD, lower respiratory infections, tuberculosis, diabetes, neonatal/preterm conditions, diarrhoeal disease, road injury | The classic "double burden": chronic and infectious disease on the same list |
| Eastern Mediterranean (EMRO) | Ischaemic heart disease, COVID-19, stroke, neonatal/preterm conditions, COPD / lower respiratory infections, diabetes, road injury (~127,000 in 2021), chronic kidney disease, cirrhosis | Road injury is prominent; the largest regional increase in diabetes deaths; very large uncertainty in conflict-affected areas |
| Europe (EURO) | Ischaemic heart disease, stroke, COVID-19, lung cancer, Alzheimer's disease, COPD, colorectal cancer, lower respiratory infections, diabetes and kidney disease, hypertensive heart disease | Colorectal cancer and hypertensive heart disease stand out; tuberculosis is not in the top ten |
| Americas (AMRO/PAHO) | Ischaemic heart disease, COVID-19, stroke, diabetes, Alzheimer's disease, COPD / lower respiratory infections, chronic kidney disease, lung cancer, interpersonal violence, colorectal cancer / road injury | Interpersonal violence uniquely appears; Latin America and the Caribbean had the world's highest age-standardised COVID-19 mortality (~195 per 100,000) |
| Western Pacific (WPRO, dominated by China) | **Stroke first**, ischaemic heart disease, lung cancer, COPD, COVID-19 (ranked very low), lower respiratory infections, Alzheimer's disease, liver and stomach cancer, diabetes, chronic kidney disease | The only region where stroke leads; liver and stomach cancer are prominent given the East Asian cancer profile; the world's lowest age-standardised COVID-19 mortality (~23 per 100,000) |

**The union set (roughly 16–18 conditions):** ischaemic heart disease, stroke, COVID-19, COPD, lower respiratory infections, lung cancer, Alzheimer's disease and other dementias, diabetes, kidney disease, tuberculosis, malaria, HIV/AIDS, diarrhoeal disease, neonatal and preterm complications, road injury, cirrhosis, liver and stomach cancer, interpersonal violence, colorectal cancer.

### 2.3 The income-group view (orthogonal to geography)

High-income countries: chronic disease dominates, survival with disease after diagnosis is long, and screening plus chronic-disease management markedly slow progression. Low- and middle-income countries: a double burden, younger onset, and delayed presentation meaning most diagnoses are made at an advanced stage, so the interval from diagnosis to death is compressed. Low-income countries: infectious disease remains the principal threat, lower life expectancy limits the scale at which degenerative conditions such as dementia become visible, and there are structural gaps in the statistics for complex chronic disease.

---

## 3. Finding one: age at onset shifts by region and by sex

<figure>
  <img src="/assets/img/posts/global-causes-of-death-timelines/fig1_onset_age.png" alt="Mean age at onset or diagnosis for the major chronic diseases, compared across regions and between sexes">
  <figcaption>Figure 1. Mean age at onset or diagnosis for the major chronic diseases, by region and by sex.</figcaption>
</figure>

**Shifted earlier by region (vascular and metabolic disease).** Mean age at first acute myocardial infarction is 53.0 in South Asian populations, 5.8 years earlier than elsewhere on the country-mean basis. On the ethnicity-based median-at-first-presentation basis, South Asians present at 52 (IQR 45–60), about ten years before Europeans (62) and Chinese (63), and 10.6% present before the age of 40 (against 6% overall). The drivers are not simply genetic: premature exposure to smoking in early life, psychosocial stress, diabetes and an abnormal ApoB/ApoA-1 ratio are the main causes. Type 2 diabetes shifts the same way — South Asians are diagnosed 5–10 years earlier than white Europeans, and UK Biobank data show that the BMI at which South Asians reach the diabetes risk of a white person with BMI > 30 is only 22 (the "thin-fat" phenotype, with lower beta-cell function). In Germany, the mean age at new diagnosis of type 2 diabetes fell from 63.1 in 2014 to 61.7 in 2020, with a rising share of early-onset cases diagnosed before 40. The extreme case is CKDu (chronic kidney disease of unknown origin), which strikes agricultural workers aged 30–50 in Central America and Sri Lanka: among Guatemalan sugarcane cutters in their first harvest season, 22% showed unstable kidney function at a median age of just 19.

**Shifted later by region (neurodegenerative disease, high-income countries).** Forty years of follow-up in the Framingham study show age-specific dementia incidence falling by about 20% per decade — 44% cumulatively — with mean age at diagnosis pushed back from 80 to 85; the Rotterdam study shows the same trend. The mechanism is chiefly that control of blood pressure and lipids in midlife slows cerebral microvascular damage — the mirror image of the earlier dementia onset seen in patients with heart failure, coronary disease or atrial fibrillation.

**The sex shift.** Women develop ischaemic heart disease about ten years later than men. Between 30 and 64, male IHD mortality is 4–5 times the female rate; after 65, as the protection of the premenopausal state is lost, the ratio narrows to about 2. Median age at stroke is 79 in women against 73 in men — but later onset does not mean a better outcome. Women more often have atrial fibrillation (33.3% vs 25.6%), and atypical symptoms delay diagnosis and cost them the window for thrombolysis or thrombectomy; after adjustment for confounding, in-hospital mortality risk remains 12% higher (OR 1.12), and post-stroke depression and vascular dementia are also more frequent. In COPD, women lose more years of life than men at the same GOLD stage.

---

## 4. Finding two: regional differences in post-event survival are mostly differences in subtype mix

<figure>
  <img src="/assets/img/posts/global-causes-of-death-timelines/fig2_stroke.png" alt="The main explanation for poorer stroke outcomes in China: a higher share of haemorrhagic stroke">
  <figcaption>Figure 2. Why stroke outcomes are worse in China: the subtype mix, not the care of any one subtype.</figcaption>
</figure>

The gap between Chinese and Western stroke outcomes is not chiefly a matter of the same disease faring differently — it is a **different mix of subtypes**. Haemorrhagic stroke accounts for about 25–27% of strokes in China against about 12% in the West, and intracerebral haemorrhage itself carries very high case fatality. In the China Kadoorie Biobank (about 500,000 adults, 45,732 first strokes), 28-day case fatality was about 3% for ischaemic stroke, about 19% for subarachnoid haemorrhage, about 24% for unclassified stroke, and **about 47% for intracerebral haemorrhage**. Risk of myocardial infarction or vascular death within five years of a first ischaemic stroke is about 17.4% (Northern Manhattan Study).

On the myocardial-infarction side, cumulative case fatality after the event in a US Medicare cohort was 18% at 28 days, 32% at one year and 56% at five years. In cross-country comparison, 30-day case fatality is 1–3 percentage points lower in high-income populations, and the gap widens further by one year, driven largely by access to acute reperfusion therapy. Age-standardised IHD mortality in Germany fell by 3.2–3.9% a year between 1998 and 2023, but the decline has slowed since the 2010s: the dividend from acute care has peaked, and large numbers of survivors are entering the long chronic phase of ischaemic heart failure.

**Implication for modelling:** post-event survival parameters must be parameterised in three dimensions — subtype × region × treatment era. A global mean will simultaneously understate the lethality of intracerebral haemorrhage in China and overstate how treatable ischaemic stroke is in low-income regions.

---

## 5. Finding three: a unified timeline for event-type and trajectory-type disease

<figure>
  <img src="/assets/img/posts/global-causes-of-death-timelines/fig5_timeline.png" alt="A unified timeline comparing event-type and trajectory-type diseases">
  <figcaption>Figure 3. A unified timeline: event-type disease against trajectory-type disease.</figcaption>
</figure>

This is the central analytical framework of the merged report. **Event-type disease** is structured as long latency → acute event → post-event survival: atherosclerosis progresses silently for 20–40 years before a first myocardial infarction (in the Copenhagen General Population Study, asymptomatic obstructive subclinical coronary disease raised MI risk more than eightfold); lung cancer is estimated to take 10–20 years from the initiating mutation to clinical detectability. **Trajectory-type disease** is a continuous monotonic decline: amyloid-beta deposition in Alzheimer's disease begins roughly 15–20 years before expected symptom onset, and the fall in CSF Aβ42 is detectable about 25 years before onset (the DIAN cohort, *NEJM*); accelerated decline in FEV1 in COPD precedes diagnosis by more than 20 years; eGFR in CKD falls by 1–4 mL/min/1.73 m² a year with 2–5 years spent in each stage (median dwell time in stage 3b can reach 7.9 years — the critical line for intensive intervention); untreated HIV takes a median of 8–10 years from seroconversion to AIDS (12.5 years for those infected at 15–24, 7.2 years at 45–54: the older the faster), and only about nine months from AIDS to death.

The **behaviour of the diagnostic timestamp differs completely** between the two. For event-type disease the "event" is a biologically defined hard timestamp and compares well across regions. For trajectory-type disease, "diagnosis" is a soft timestamp defined by the health system — dementia is diagnosed on average about 3.6 years late (in a UAE cohort, mean 34.7 months from symptom to diagnosis, longest where forgetfulness was the presenting feature and shortest where it was behavioural or psychiatric change). That delay directly determines whether a patient is still inside the time-sensitive window for early intervention with lecanemab or donanemab.

**Progression parameters at stage granularity, using COPD as the example:**

<figure>
  <img src="/assets/img/posts/global-causes-of-death-timelines/fig3_copd_gold.png" alt="Years of life lost in COPD by GOLD stage">
  <figcaption>Figure 4. Years of life lost in COPD by GOLD stage.</figcaption>
</figure>

The loss of survival scales non-linearly with GOLD stage: in a Western cohort of male smokers, GOLD stage 1 costs only 0.3 additional years, stage 2 costs 2.2 and stage 3 costs 5.8; Asian hospital cohorts are higher still (6.2 years at stage 2, 9.3 at stage 3); for women stage 3 can reach 5 years and stage 4 nine. The real cliff edge is hospitalisation for an acute exacerbation: a GOLD stage 1 patient has about 9.7 years of survival remaining after admission, a GOLD stage 4 patient only 3.4. Among those with severe CO2 retention (PaCO2 > 50 mmHg), about 10% die during that admission and 33% within six months.

**Survival after diagnosis by dementia subtype:** late-onset Alzheimer's disease (onset after 65) has a median survival of 5–8 years (8.3 years if diagnosed at 65, 3.4 years if at 90); early-onset disease (before 65) 12–13 years; frontotemporal dementia 8–12 years; FTD with ALS only about 2.4 years.

**Timing parameters on the infectious-disease side** (mostly relevant to the African and South Asian lists): latent tuberculosis infection carries a roughly 5–10% lifetime risk of progressing to active disease, about half of it in the first two years after infection, with HIV co-infection raising the annual risk of progression to 5–15%; malaria takes 10–15 days from the infective bite to illness, with deaths heavily concentrated in children under five (Africa bears about 95% of malaria deaths worldwide); diarrhoeal disease and lower respiratory infections both show a bimodal distribution, under 5 and over 70.

---

## 6. Finding four: the timeline is an intervenable variable

<figure>
  <img src="/assets/img/posts/global-causes-of-death-timelines/fig4_ckm_gain.png" alt="Time gained from triple therapy under the CKM framework">
  <figcaption>Figure 5. Time gained from triple therapy in cardiovascular-kidney-metabolic syndrome.</figcaption>
</figure>

Under the cardiovascular-kidney-metabolic (CKM) syndrome framework proposed by the AHA in 2023, multiple comorbidity compresses survival multiplicatively: patients with four or more comorbidities have an adjusted all-cause mortality HR of 2.53, and patients under 60 with early advanced-stage CKM have 8.07 times the mortality risk of healthy peers. But pharmaceutical innovation is rewriting the timeline as never before. Actuarial models built on the CREDENCE, DAPA-CKD and LEADER trials show that for a 50-year-old with type 2 diabetes and moderate-to-severe albuminuria, triple therapy with an SGLT2 inhibitor, a GLP-1 receptor agonist and a non-steroidal MRA reduces relative MACE risk by 35% against standard care (HR 0.65) — which, converted into absolute time, is the +3.2 years of MACE-free survival, +3.2 years free of heart-failure hospitalisation and **+5.5 years before kidney disease progresses to dialysis** shown in Figure 5. Systematic disease management works too: ten-year follow-up of the German DMP programme reduced absolute risk of amputation by 20.3%, of myocardial infarction by 14.9% and of dialysis by 10.1% in patients with type 2 diabetes and coronary disease.

**Implication for modelling:** progression parameters must carry a treatment-era label (pre/post-SGLT2i, pre/post-ART, pre/post-immunotherapy, pre/post-anti-amyloid antibody). Extrapolating a natural history fitted on historical cohorts to a contemporary population will systematically overestimate the rate of progression; conversely, extrapolating contemporary high-income data to regions with poor access to these drugs will systematically underestimate it.

---

## 7. Finding five: three filters of statistical bias

Any claimed "regional difference" must pass through these in turn.

**Lead-time bias.** Screening moves the diagnostic clock forward. If a lung cancer patient dies in year 9 regardless, then diagnosis on symptoms in year 6 yields an apparent survival of 3 years while detection by LDCT screening in year 3 yields an apparent 6 — with not one day of life added. The survival advantage of high-income countries, where screening is widespread, can only be attributed to treatment after this has been corrected for.

**Length-time bias and overdiagnosis.** Cross-sectional screening naturally enriches for slow-growing indolent tumours, while aggressive cases arise and kill within the screening interval and are missed. In prostate and thyroid cancer screening, large numbers of patients carrying cancer cells that would never have caused disease in their lifetime enter the denominator, artificially inflating the apparent cure rate.

**The illusion of compressed survival created by systemic delay.** In low- and middle-income countries, 75% of breast and colorectal cancer patients are diagnosed at stage III or IV (the reverse of high-income countries, where 75% are diagnosed at stage I or II). An apparent interval of only months from diagnosis to death does not mean the disease is more aggressive; it means a large part of the occult progressive phase is walled off outside the medical statistics. Add to that the heavy reliance on verbal autopsy for cause-of-death estimates in sub-Saharan Africa, and the overall judgement follows: **roughly half the regional difference in age at onset in Figure 1 is a genuine difference in biology and exposure profile, and the other half is a difference in measurement systems.** Distinguishing the two rigorously requires cross-national cohorts with unified diagnostic criteria — INTERHEART and PURE are designed for exactly this.

---

## 8. Recommendations for modelling and application

1. **Choose the model from the topology.** Use competing-risk or multi-state survival models for event-type disease (with latency as a hidden state), and mixed-effects trajectory or state-space models for trajectory-type disease (joint latent-class mixed models for eGFR in CKD, biomarker change-point models for AD). This event-type/trajectory-type split is more useful for modelling than classification by organ system.
2. **Regionalise the parameters; refuse the global mean.** Use region-specific values for age at onset (MI at 53 in South Asia versus 59 in the West; type 2 diabetes 5–10 years earlier in Asia; CKDu at 30–50), and parameterise post-event survival by subtype × region (China's high share of intracerebral haemorrhage, with ~47% 28-day case fatality).
3. **Label parameters with a treatment era.** Natural-history parameters (untreated HIV 8–10 years, TB 5–10% lifetime and so on) come from the pre-treatment era and differ enormously from the contemporary course of disease.
4. **Thresholds that trigger re-estimation.** Re-extract the regional lists and parameters whenever a region's age-standardised mortality for any disease changes by more than 20%, or when a new GHE or GBD release appears.

## 9. Outstanding checks and a statement on data quality

- **Risk of extrapolating single-country data.** Data from one country — Germany (age at IHD diagnosis, type 2 diabetes trend, DMP outcomes), the UAE (delay in dementia diagnosis) — has limited representativeness when extrapolated to an entire income group.
- **Bases that are not directly comparable.** WHO states explicitly that GHE 2021 cannot be compared directly with earlier WHO estimates because of methodological change; GBD's 21 regions do not match WHO's six.
- **The scope of the DIAN data.** The 15–25-year preclinical time course comes from autosomal dominant Alzheimer's disease; the course of sporadic AD may differ.

## 10. Principal sources

WHO, *The top 10 causes of death* (fact sheet, Aug 2024) · WHO Global Health Estimates 2021 · GBD 2021 (*Lancet*, 2024) · Joshi et al., Risk factors for early myocardial infarction in South Asians (INTERHEART, *JAMA* 2007) · Lacey/Chen et al., China Kadoorie Biobank stroke outcomes (*Lancet Global Health* 2020) · Bateman et al., Clinical and biomarker changes in dominantly inherited Alzheimer's disease (*NEJM* 2012, DIAN) · Satizabal et al., Incidence of dementia over three decades in the Framingham Heart Study (*NEJM* 2016) · Shavelle et al., Life expectancy and years of life lost in COPD · AHA Presidential Advisory on CKM syndrome (*Circulation* 2023) · CREDENCE / DAPA-CKD / LEADER meta-analyses and lifetime-benefit actuarial models (AHA Journals) · Copenhagen General Population Study, subclinical coronary atherosclerosis (*Ann Intern Med* 2023) · CASCADE collaboration, untreated HIV natural history · WHO World Malaria Report 2024.

---

*This article was assembled by cross-checking two AI deep-research reports against each other; every quantitative figure carries its source attribution.*
