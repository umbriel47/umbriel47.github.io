---
layout: post
title: "From Calling Tools to Operating Instruments: A Review of Anthropic's Model Hardware Standard (MHS)"
date: 2026-09-29 08:55:00 +0800
lang: en
ref: model-hardware-standard
tags: [science]
wide: true
wechat_url: "https://mp.weixin.qq.com/s/N3kSguRUtGkuKZQjSImaBQ"
description: "The Model Hardware Standard (MHS), released by Anthropic as a research preview on 27 August 2026, is a shared specification that lets AI agents discover, understand and safely operate laboratory and manufacturing equipment — often called \"MCP for hardware\"."
---

<figure class="lead">
  <img src="/assets/img/posts/model-hardware-standard/hero.png" alt="A beam of optical fibre splits into strands running to a liquid-handling workstation, a robot arm and a microscope on a lab bench">
</figure>

## Summary

MHS (Model Hardware Standard) is a shared specification released by Anthropic as a research preview on 27 August 2026, intended to let AI agents discover, understand and safely operate laboratory and manufacturing equipment. Fortune called it Anthropic's first move into physical AI; because MCP is its main access protocol, it is widely described as "MCP for hardware".

This review makes three main judgments:

- **Positioning**: MHS addresses *integration fragmentation*, not autonomy as such — cutting device integration from weeks to hours and enforcing safety limits at the device layer.
- **Evidence**: six public case studies provide solid proof-of-concept data (for example, QuEra's laser relock success rate rose from 58% to 99.3%; CMU went from devices ready to a finished dose–response curve in about 8 hours, where vendor-delivered solutions usually take weeks). But every case uses Claude, and cross-model interoperability remains a design promise.
- **Maturity**: the specification itself has not been published. Outside analysts note that it lacks a versioned spec, conformance tests, a security threat model and governance rules. For now it is a well-evidenced research preview, not yet a de facto standard.

## What MHS is: an "agent manual" for a device

The official definition of MHS is "a shared specification for AI agents to safely operate physical equipment", aimed first at research labs and advanced manufacturers. The public cases involve microscopes, liquid-handling workstations, robot arms, plate readers, qPCR machines, centrifuges, cameras and lasers.

**The problem it addresses:** integrating a set of hardware in a lab or factory usually takes weeks to months. Device interfaces are mutually incompatible, so integration depends on experts writing custom code. Much of the operating knowledge — safe ranges, physical characteristics — lives only in manuals and engineers' experience. Alek Kemeny of Anthropic's technical staff put it this way: "There's currently no universal way to connect a model to physical equipment." (via R&D World)

**Relationship to MCP:** MCP (Model Context Protocol) carries the tool calls; MHS describes the device behind the tool — what it can measure, what it can adjust, what its safety limits are. By design MHS is model-agnostic: any agent framework can reach it through MCP, a command line (CLI) or a code API. Kemeny has compared MCP to "a USB for AI connecting to software" (via Fortune); MHS can be seen as extending that port to hardware.

| Dimension | MCP | MHS |
|---|---|---|
| Released | November 2024 | August 2026 (research preview) |
| Connects to | Software tools, data sources | Physical devices |
| Core abstraction | tools / resources / prompts | Standard driver + a small set of primitives (e.g. read/write) + device reference file |
| Safety boundary | Mainly client-side authorisation | Safety limits enforced at the device layer |
| Openness | Open source; donated in December 2025 to the Linux Foundation's AAIF (Agentic AI Foundation) | Spec unpublished; individual device drivers will be published |

## Technical approach: five key design choices

In short: a minimal standard driver layer hides device heterogeneity, operating knowledge and safety limits are compiled into the driver, and agents call it through existing protocols.

<figure>
  {%- include charts/mhs/en/architecture.svg -%}
</figure>

From the top down, the agent only ever sees a uniform driver interface. Device heterogeneity is encapsulated below the driver layer, and the safety boundary is enforced there too.

### 1. A small set of primitives + standardised discovery

A driver exposes a small set of primitives, typified by read (read state, e.g. "read temperature") and write (write a setting, e.g. "set temperature"). Devices are discoverable in a standard format, so agents no longer need point-to-point "translation programs" for each device. Data from multiple instruments flows into the MHS state dictionary — a shared memory area that many programs can read and write at once.

### 2. Compiling tacit knowledge into a reference file

Users write driver tags in natural language (or have an agent "interview" the device operator), and the driver generates a reference file from them, stating what the device can measure, what it can adjust and which safety limits it enforces. Anthropic says this lets an agent pick up "equipment it has never seen before".

### 3. Separating exploration from consolidation

During development, the agent reasons online and iterates by trial and error. Once a procedure matures, it is consolidated into deterministic, reviewable code, which chains driver commands across one or more devices and runs long jobs faster than the model could reason online. QuEra is the canonical case: Claude rewrote a linear laser-relock procedure into a decision-tree script driven by instrument readings, and the final script runs with no AI involved. Kingy AI summed up the pattern as "an automation engineer that can debug, test, monitor and leave behind a reviewable program", not "a chatbot taking over the factory".

### 4. Safety limits enforced at the device layer

MHS enforces safety limits (a laser power ceiling, say) at the device layer, so the agent cannot go beyond the vendor's specification; MarkTechPost put it as "the limits live in the driver, not in the prompt". In CMU's tests, all six deliberately induced faults (a missing plate, a rotated plate and so on) were caught before the device moved. Third-party implementations are reinforcing this layer too: Fastly's edge research prototype validates limits before forwarding a call, and adds per-device call quotas (to prevent hardware wear) and audit logs with hashed identities.

### 5. Decoupling protocols from hardware

Tetsuwan replaced its existing scheduler with MHS. The experimental protocol states the centrifugal force required; the system queries the available centrifuge drivers, and Claude converts the force into a rotor speed from the rotor radius. This means a protocol can move between instruments from different vendors.

## History: from MCP to MHS

On the timeline, MHS is not an isolated product but the third step on a path Anthropic has followed for two years: connect to software → enter research workflows → run physical experiments. MCP provided the protocol foundation; Claude for Life Sciences and Claude Science built up research use cases and customers; the acquisition of Coefficient Bio brought in a drug-discovery team. The first two research products stayed at the level of literature, analysis and code; MHS adds the missing hands-on step of doing the experiment.

| Date | Event | Significance |
|---|---|---|
| 2024-11 | MCP released | Open protocol for connecting agents to external tools; later MHS's main access protocol |
| 2025-10-20 | Claude for Life Sciences launched | Connectors for Benchling, PubMed, 10x Genomics and others; focused on computation and literature |
| 2025-12-09 | MCP donated to the Agentic AI Foundation | Protocol moves to neutral governance, underpinning MHS's "model-agnostic" story |
| 2026-04-03 | Coefficient Bio acquired (reportedly about $400M in stock; a team of about 10) | Founders from Genentech's Prescient Design; fills in drug-discovery capability |
| 2026-06-30 | Claude Science public beta | Research workbench: multi-agent + 60+ skills + compute scheduling, but no hardware control |
| 2026-08-27 | MHS research preview; scientist support programme announced the same day | First formal entry into physical AI; co-developed with HHMI Janelia |

**Origins:** MHS grew out of a collaboration between Alek Kemeny of Anthropic's Beneficial Deployments team and Arco Bast, a postdoc in the Spruston lab at HHMI Janelia. The shared-memory dictionary Bast wrote to get several instruments talking to each other evolved into today's MHS state dictionary. When the project started and how large the team is have not been disclosed.

## Current status: research preview and first proofs of concept

As of 28 September 2026, MHS remains a research preview: invited partners only, a waitlist open (modelhardwarestandard.com), specification unpublished. The public evidence comes from six partner case studies — well quantified, but still proofs of concept.

### Results from the first partners

All figures below come from Anthropic's announcement and partners' blog posts; none has been independently reproduced.

| Partner | Task | Key results | Integration or completion time |
|---|---|---|---|
| QuEra | Laser relocking and PID tuning on a quantum computer | Relock success 58% → 99.3% (the baseline script took a team of four months to write by hand; the final script succeeded 695/700 times in randomised-perturbation tests with no AI involved); recovery time cut from about 150 s to a few seconds for most faults, about 10–14 s for the hardest; 363 tuning experiments run unattended over 16 hours, servo-loop RMS error 15.7 → 1.55 mV | — |
| Carnegie Mellon | Serial-dilution dose–response curves | About 3× faster overall; saturated batches with R² < 0.9 automatically discarded and rerun to R² > 0.98; all 6 induced faults caught; a plate reader with no API connected by driving its GUI as a human would | About 8 hours from devices ready to finished dose–response curve (including one autonomous rerun); vendor solutions usually take weeks |
| Tetsuwan Scientific | Closed-loop optimisation of a qPCR pipetting compiler | 9,143 dispenses, 300 transfer types; multi-dispense accuracy predicted about 12% better than the vendor spec (Tetsuwan's blog: wins in 33 of 45 held-out batches, p ≈ 0.003; Anthropic's announcement gives 31/45, p ≈ 0.001 — the two disagree); bubbles detected visually and recovered by automatic centrifugation | — |
| Genentech | Pipetting-parameter optimisation for BCA protein assays | Optimal flow about 140 µL/s for water (RMSE 0.016), about 10 µL/s for viscous BSA (RMSE 0.181); bubble problems needed human guidance | — |
| University of Washington (Baker/Pinglay labs) | Real-time qPCR monitoring; hand-offs between robot arm and pipettor | Recognised amplification curves in real time, asked researchers at key points whether to stop, and on instruction halted the reaction and moved it to 4 °C storage; zero collisions over multiple test rounds | 6 instruments in under a week (including writing drivers) |
| HHMI Janelia | Microscope light-path alignment and online analysis | Manual alignment and tuning that took half a day reduced to one step | Adding a new camera cut from days to minutes |

### Developments since the preview

- **2026-09-02**: Fastly released the edge-mhs research prototype, adding limit validation, per-device call quotas and audit logs to its edge MCP implementation.
- **2026-09-18**: according to Startup Fortune (citing Reuters), Anthropic has built a robotic wet lab in the Bay Area where Claude directs real biological experiments and drug discovery for neglected diseases; staff still supervise for safety.

### Ecosystem and related initiatives

- **Vendors** (with varying degrees of commitment): Tecan (Fluent), Automata (LINQ) and MBF Bioscience (ScanImage) are adding support; Universal Robots plans to; QIAGEN (QIAsymphony Connect) has completed a proof of concept; Doosan Robotics is testing; Danaher is still exploring.
- **Developer ecosystem**: Hugging Face is adding support in LeRobot; AWS is giving preview participants a private pre-release of Strands Robots; Raspberry Pi is moving to integrate several products after successful camera-driver tests.
- **Openness**: during the preview Anthropic leads the specification, and plans to open-source it with safe-deployment guidance after completing safety evaluations with partners; individual instrument drivers will be published for reuse.
- **Related programmes**: the scientist support programme announced the same day offers 10,000 Team seats to PIs at academic and non-profit institutions — standard seats free for a year, premium seats at $15 a month; the AI for Science programme provides up to $50,000 in credits per project.

### Relationship to existing lab standards (author's analysis)

The fundamental difference between MHS and traditional lab standards is who the *reader* is. Traditional standards assume the caller is a program written by an engineer; MHS assumes the caller is a model that has to "understand" the device. Anthropic's public materials do not compare MHS with these standards; the positioning below is my own judgment from public information.

| Standard | Designed by | Aimed at | Relationship to MHS |
|---|---|---|---|
| SiLA 2 | Non-profit industry consortium (1.0 released 2019) | Scheduling software and engineers | Already has self-description (FDL includes text descriptions and parameter constraints) and service discovery; MHS differs in taking the agent as reader, enforcing limits at the device layer and generating reference files from natural language — the two may be complementary |
| OPC UA LADS | SPECTARIS working group + OPC Foundation (1.0 released 2023) | Lab and analytical instruments | Builds on the mature OPC UA information model, though LADS itself is new; MHS is lighter, centred on primitives plus natural-language description |
| ROS 2 | Open-source robotics community | Robot motion and perception | Motion and perception stay with ROS 2 / ros2_control and controller firmware; MHS sits higher up, handling task orchestration |

## Challenges and outlook: the bottleneck is physical intuition, the wild card is governance

The biggest bottleneck for MHS is not the protocol but the model's physical intuition; the biggest uncertainty is governance and the pace of opening up.

### Technical limitations (as Anthropic states them)

- **Weak physical reasoning**: Claude's knowledge of the physical world comes from text and images. When a bubble error came up in Genentech's experiments, Claude's default was to retry in the same well with different parameters, which produced more bubbles. When QuEra's hardware failed, Claude's "understanding of the apparatus was procedural rather than physical", and it could not troubleshoot.
- **Over-caution**: at the slightest risk it pauses and waits for human confirmation, sometimes stalling an experiment overnight. Anthropic's position is that "an overly cautious agent is better than an insufficiently cautious one".
- **Limited coverage**: Anthropic says MHS does not yet support devices without a programmatic interface and is working with vendors on built-in drivers. The CMU case connected a plate reader with no API by simulating a human operating its GUI, but with no means of validation.

### Outside criticism

- **Not yet a "standard"**: Kingy AI points out that there is no versioned spec, conformance test suite, security threat model, certification or release timeline. The bioinformatics blogger Keith Robison (Omics! Omics!), in a post titled "Model Hardware Standard: What Is It? Seriously, That's What I'm Asking", notes that the specification has not been publicly disclosed.
- **Model-agnosticism unproven**: every detailed case uses Claude. Fortune reports that MHS can also be used with OpenAI and open-source models, but there is no public cross-model comparison.
- **Governance gap**: licensing, ownership and contribution rules are all undecided.
- **Biosafety and misuse risk**: agents operating wet-lab equipment introduce biosafety risks. Anthropic says it is drawing up a "physical safety roadmap" to strengthen anti-misuse policy and enforcement, and will build more safety evaluations with partners during the preview.

### Outlook

1. **Short term (6–12 months)**: more vendors ship built-in drivers and driver libraries are published; partners move from single-point optimisation to end-to-end workflows. Genentech has explicitly said it plans to build an autonomous discovery engine where "scientists set high-level biological intent and AI agents coordinate the physical workflow".
2. **Medium term (1–2 years)**: the specification may be open-sourced with safe-deployment guidance. Governance may follow MCP's "open-source first, donate later" route to a neutral foundation, though physical safety will probably slow the pace; bridges to SiLA 2 and OPC UA will be key to adoption.
3. **Long term**: the bottleneck shifts to the model's physical and chemical intuition. Anthropic's public rationale for building its own wet lab is that "the final test of biology is still the real experiment". Whether such closed-loop experimental data will be used for training has not been disclosed, but it may well be key to improving models' physical intuition.

## Closing: what this means for AI-driven biological R&D

MHS answers the question "how does an agent operate an instrument?". AI-driven scientific discovery has a bigger question to answer: starting from a hypothesis, how do you automatically decide which experiment to run, how to run it, how to revise the hypothesis afterwards — and keep that loop recursing?

A system like The Popper Project (TPP), which INFevo is building, is positioned as a Recursive Scientific Discovery system. It covers the whole of that loop, not only hypothesis generation upstream. MHS and TPP are complementary, at different levels. MHS standardises the agent ↔ instrument interface; TPP's protocol layer handles the level above — how a hypothesis is compiled into composable, portable experimental protocols, and how results flow back to revise the hypothesis. The former makes instruments *readable*; the latter makes scientific questions *executable*.

Two implications follow. First, the protocol layer will be the next focus of standardisation: as device interfaces converge, the bottleneck moves up to how experimental protocols are expressed, composed and reused by machines, and an open language at that layer will decide how automated science interoperates. Second, the gap the MHS cases keep exposing — models lacking physical and biological intuition — is exactly where virtual cell models can help: validating virtually before running the wet experiment both screens out experiments not worth doing and gives general-purpose agents biological priors.

TPP has completed hypothesis generation and computational sandbox orchestration, and the physical execution layer is being filled in — which is why a device standard like MHS matters directly to us.

## References

**Primary sources**

1. Previewing the Model Hardware Standard — Anthropic, 2026-08-27
2. Expanding support for scientists — Anthropic, 2026-08-27
3. Model Hardware Standard website
4. Claude Science, an AI workbench for scientists — Anthropic, 2026-06-30
5. MCP joins the Agentic AI Foundation — MCP Blog, 2025-12-09
6. Holding the light: teaching an AI to lock and tune our quantum computer's lasers — QuEra
7. Tetsuwan × MHS — Tetsuwan Scientific, 2026-08-27
8. Building for the Model Hardware Standard — Fastly, 2026-09-02

**Media and analysis**

9. Anthropic makes first move into physical AI with universal standard — Fortune, 2026-08-27
10. Anthropic wants Claude to run life sciences R&D. Now it is wiring AI agents into the lab. — R&D World, 2026-08-28
11. Anthropic Opens a Research Preview of the Model Hardware Standard — MarkTechPost, 2026-08-29
12. Anthropic's Model Hardware Standard: What MHS Actually Changes — Kingy AI
13. Model Hardware Standard: What Is It? Seriously, That's What I'm Asking. — Keith Robison, Omics! Omics!
14. Anthropic buys biotech startup Coefficient Bio in $400M deal — TechCrunch, 2026-04-03
15. Anthropic launches Claude for Life Sciences — Maginative, 2025-10-20
16. Anthropic quietly built a biology lab so Claude can run real experiments — Startup Fortune, 2026-09-18
{: start="9"}
