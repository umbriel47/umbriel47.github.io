---
layout: post
title: "Once Lab Automation Turns Craft into Data, Who Is Still Watching for Anomalies?"
subtitle: "This piece asks what lab automation filters out when it encodes tacit knowledge. It offers a framework for telling \"reproducible\" from \"discoverable\", and a few signs for judging whether an automated workflow can still correct its own errors."
date: 2026-10-02 08:00:00 +0800
lang: en
ref: who-is-watching-the-anomalies
tags: [science]
wide: true
wechat_url: "https://mp.weixin.qq.com/s/67nF7nJN3WSDrmZl1ih3wg"
description: "Automation encodes the operating knowledge that can be written into a protocol, but struggles to encode the judgment that \"this time is different\". As reproducibility improves, the chances to discover and to correct errors may be quietly shrinking."
---

Automated labs and AI agents are rapidly taking over the most repetitive part of experimental science. The usual ledger has only one column: higher throughput, smaller errors, better reproducibility. This piece tries to fill in the other column. The question is: **when tacit knowledge is encoded into protocols and data, what was the unencoded part doing?** My answer is that it carried the work of recognising anomalies and correcting errors — and that this function is being filtered out along with it. It is worth discussing now because AI has started to deliver results at the discovery end, while the scientific community has only just begun to discuss who decides whether those results are reliable.

## Encoding is not transfer but selective translation

"Tacit knowledge" is usually traced to Michael Polanyi's line: we know more than we can tell. In the 1970s, the sociologist Harry Collins followed attempts to replicate the TEA laser and found that almost no lab could build a working device from the published literature and drawings alone; the teams that succeeded had nearly all had personal contact with the original builders (Collins, The TEA Set[\[1\]](https://orca.cardiff.ac.uk/id/eprint/90648/)). Knowledge travelled with people, not with papers.

But "tacit knowledge" is too coarse a term — too coarse to say what exactly automation takes away. I suggest splitting it into two layers.

- **Operating knowledge**: tacit experience of *how to do it* — pipetting rhythm, incubation time, balancing before centrifugation. It is hard to put into words, but in principle it can be broken down into parameters, written into a protocol and handed to a machine.
- **Discriminating knowledge**: the ability to judge *whether this time is normal*. It depends on continuous sensory feedback, a tacit expectation of how "normal results" are distributed, and the ability to notice a deviation in context. It is hard to write down as rules in advance.

Automation is good at the first layer. Breaking a senior technician's technique down into steps, parameters and tolerances is exactly what lab-automation engineers do every day. The trouble is the second layer. In manual work, discriminating knowledge is not a separate step; it rides along with every operation: the cloudiness you see when you pick up a centrifuge tube, the sense while loading samples that "the liquid is a bit viscous today", the "something's not right" the moment a gel comes out.

So encoding does not move a manual workflow into a machine unchanged; it is a lossy translation. A protocol can record the variables that were judged relevant in advance — and what makes an anomaly an anomaly is precisely that it falls outside the variables judged relevant in advance.

<figure>
  {%- include charts/lab-anomalies/en/fig1.svg -%}
  <figcaption>Figure 1 | Encoding is a lossy translation: operating steps enter the standardised process, while sensing anomalies and judging context stay outside the funnel · Source: drawn by 一目半 (Yimuban)</figcaption>
</figure>

The question then is no longer "is automation good?" but "what does encoding filter out, and what was the filtered-out part doing?"

## Why anomalies are the hardest thing to write into a protocol

Discriminating knowledge is hard to encode for at least three reasons.

First, it depends on continuous feedback. A person doing the work by hand receives visual, tactile and timing signals throughout. Instruments have sensors too, of course, but a sensor records only what its designer decided in advance to record.

Second, it depends on a tacit distribution of "normal". A researcher who has run hundreds of similar experiments carries an experiential distribution of what results usually look like. A result that deviates from it raises an alarm. That distribution has never been written down; it was trained through repeated practice.

Third, it depends on the contextual judgment that "this time is different". Is a high reading a reagent-batch problem, an operator error or a real new phenomenon? Answering that draws on knowledge outside the experiment: where this batch of samples came from, what maintenance the equipment had yesterday, whether the literature reports anything similar.

One often-cited example shows how much discriminating knowledge weighs. In 2014 the labs of Mina Bissell and Kornelia Polyak wrote in *Cell Reports* that they had sorted human breast cells using seemingly identical protocols and got inconsistent results; after repeated troubleshooting, the difference was traced to how the tissue was physically handled during digestion — vigorous stirring on one side, long gentle rocking on the other (Hines et al., 2014[\[2\]](https://www.cell.com/cell-reports/fulltext/S2211-1247(14)00121-1); cited in a review in *The EMBO Journal*[\[3\]](https://link.springer.com/article/10.15252/embj.2018101011)). The story is usually told as a lesson that the protocol wasn't detailed enough. But it equally shows that the difference was found only because two groups stayed uneasy about "inconsistent results" for long enough.

That brings us to the heart of the mechanism. In an automated workflow, an anomaly usually goes one of two ways: the statistics pipeline discards it as an outlier, or it triggers a rerun until the result falls back into the expected range. Both are reasonable and both are efficient. But their shared consequence is that the anomaly never reaches anyone's attention and leaves no traceable record.

<figure>
  {%- include charts/lab-anomalies/en/fig2.svg -%}
  <figcaption>Figure 2 | Two feedback loops: in the manual process an anomaly reaches human judgment and corrects the method; in the automated process it is logged as noise or rerun, and the loop never passes through judgment · Source: drawn by 一目半 (Yimuban)</figcaption>
</figure>

The difference here is not efficiency but whether the anomaly enters the feedback loop. In the manual loop, every anomaly is a round of training in discrimination: notice it, judge whether it is real, correct the method — so the ability to discriminate is used and strengthened again and again. In the automated loop, that training opportunity no longer arises. Over time, what degrades is not just the recognition of one particular anomaly but the team's very ability to sense that something is off.

I sum up the chain as *encoding → filtering → degraded error correction*: encoding decides what is recorded, unrecorded signals are filtered out, filtered-out signals no longer train people's discrimination, and the ability to discriminate gradually weakens. To be clear, this is an inferred mechanism, not a measured finding. I have found no empirical study that directly measures the relationship between the degree of lab automation and the rate at which anomalies are discovered, or the capacity for error correction. Existing work mostly runs in the opposite direction — how to get automated systems to recognise execution anomalies themselves. One example is a 2025 visual-anomaly dataset for self-driving labs from teams including Tsinghua University, which focuses on operational anomalies such as failed robot-arm grasps and missing items (*Scientific Data*, 2025[\[4\]](https://www.nature.com/articles/s41597-025-06060-y)). Such work is valuable, but what it detects is whether the workflow was executed according to protocol, not whether a result suggests the protocol itself is wrong.

## A precedent from agriculture: as efficiency rises, local knowledge can drain away with it

History offers a process with a similar structure. In the mid-to-late twentieth century, agricultural mechanisation and the spread of high-yield varieties happened together in many regions. There was long-standing concern that this would bring the replacement of local varieties — and with them the loss of the local knowledge built around them: seed selection, crop rotation, ways of dealing with local pests and diseases.

The concern is not baseless, but the evidence is more complicated than usually told. A 2022 review in *New Phytologist* surveyed the evidence on crop genetic erosion and concluded that in farmers' fields, modern cultivars, crop wild relatives and gene banks alike, both clear losses and maintained or even increased diversity have been observed, the degree depending on species, scale, region and method of analysis (Khoury et al., 2022[\[5\]](https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.17733)). A 2010 meta-analysis of 44 studies covering eight field crops found that the genetic diversity of varieties released by breeders fell about 6% in the 1960s compared with the 1950s, but recovered somewhat afterwards, with no large long-term reduction (van de Wouw et al., 2010[\[6\]](https://research.wur.nl/en/publications/genetic-diversity-trends-in-twentieth-century-crop-cultivars-a-me/)).

So what can safely be borrowed from agricultural history is not the causal claim that mechanisation inevitably causes loss, but a weaker and more useful proposition: gains in efficiency and losses of local knowledge can happen side by side, and the losses often don't show up in efficiency metrics. Yield statistics won't tell you how many people in a village can still recognise the disease-resistance traits of a particular local variety.

The analogy has its limits. The similarities: both replace experience dispersed among individuals and places with standardised inputs and processes; the knowledge being replaced depends on context and is hard to put into writing; and the loss happens outside the main metrics. The differences matter just as much: germplasm can be stored in a seed bank, but anomalies are hard to record after the fact; agriculture's goal is relatively single-minded, while experimental science pursues two goals at once, reproducibility and discovery; the loss of agricultural knowledge spans generations, while a lab's ability to discriminate may degrade in one or two PhD cycles. Finally, an analogy can only suggest that a mechanism might exist; it cannot replace measurement in labs themselves.

## AI enters mathematics and experimental science: is the debate about verification or discovery?

Several recent events around AI doing science have made this question concrete.

**11 September 2026**: a joint statement on mathematics and AI was published at mathandai.org[\[7\]](https://mathandai.org/). Terence Tao explained on social media that it was initially signed by 25 Fields Medallists and that more were welcome to join (Tao's post[\[8\]](https://mathstodon.xyz/@tao/117253629967855195)); the statement page now lists more medallist signatures than that and remains open. The statement does not call for bans or regulation. Its central claim is that solving problems is only a tool and a proxy; the primary goal of mathematics is conceptual understanding and insight. One line goes straight to this piece's question: years of training produce not only final answers but also understanding and the ability to pose new questions. The statement also worries that mass-producing true/false statements at ever greater speed may destroy, rather than nourish, the soil in which new ideas grow.

**1 September 2026**: Anthropic disclosed that its model had completed a nine-loop calculation of the six-particle scattering amplitude in planar N=4 supersymmetric Yang–Mills theory; the previous record was eight loops, by Lance Dixon and colleagues in 2023 (Anthropic research blog[\[9\]](https://www.anthropic.com/research/yes-claude-can-do-nine-loops)). To be clear, this is a theoretical-physics calculation, not a graph-theory problem. According to the post, the result was checked by Dixon at SLAC; participants also stressed that the model used the known "bootstrap" method, not new physical principles. The formal paper will be published by the human collaborators; at the time of writing no peer-reviewed version had appeared.

**23 September 2026**: Anthropic disclosed that its model agent had screened more than 200,000 reverse transcriptases in large sequence databases and proposed a previously uncharacterised class of systems structurally similar to CRISPR; human scientists then expressed the proteins in the lab and carried out biochemical and structural characterisation (Anthropic announcement[\[10\]](https://www.anthropic.com/news/claude-discovers-novel-enzyme-system)). This is a company disclosure with an accompanying preprint, not yet peer-reviewed; the authors themselves state that the system's function is still unclear.

Taken together, the three events make the centre of the debate clear. The nine-loop calculation's value lies almost entirely at the verification end: the problem is well defined, the method is known, and the answer can be checked independently. The enzyme discovery spans both ends: the computation screens candidates in a vast space, while "is this a real, meaningful new thing?" still comes back to wet-lab experiments and human judgment. The Fields Medallists' statement aims at something else: when answers are produced far faster than they can be understood, the very process that trains discernment may be skipped.

This is isomorphic to the lab-automation problem. AI and automation both greatly accelerate the end that produces checkable results against established standards; the ability to sense that the standards themselves might be wrong is not among their optimisation targets — and it is precisely what people were passively trained in through repetitive work.

## The strongest objection: what gets filtered out is mostly noise

This argument has an objection that must be met head-on, and it is a strong one.

The "feel" of the manual era was also the main source of irreproducible error. A 2016 *Nature* online survey of 1,576 researchers found that more than 70% of respondents had tried and failed to reproduce another scientist's experiment, and more than half had failed to reproduce their own (Baker, *Nature*, 2016[\[11\]](https://www.nature.com/articles/533452a)). The sample was self-selected *Nature* readers, so the proportions cannot be extrapolated to "70% of research is irreproducible", but it does show that experimental systems relying on individual handling are full of hard-to-trace variation. Seen from another angle, the breast-cell example above is a textbook case of manual differences producing irreproducibility.

Automation does two genuinely important things here. First, it removes a great deal of noise, so that real signals emerge more easily. Second, knowledge that used to live only in individuals starts to become cumulative, teachable and auditable: when a technician leaves, the technique doesn't leave with them; when a protocol goes wrong, it can be traced back step by step.

The objection can go one step further: the vast majority of the "anomalies" filtered out may have been nothing but noise. Truly meaningful anomalies are very rare, and tolerating all manual variation to preserve them may not be worth the cost. The so-called loss of discriminating ability may simply be a transfer of judgment from operators to workflow designers and instruments; when designers set tolerances and choose QC checkpoints, they are exercising discriminating knowledge.

I accept most of this objection and use it to set the boundaries of my argument. The argument fails under these conditions: the automated workflow itself keeps a low-cost channel for recording and tracing anomalies, and final judgment still rests with scientists who have the ability to discriminate. When both hold, encoding need not degrade error correction; more complete records may even make anomalies easier to see.

> Automation itself does not weaken science's ability to correct its errors. What weakens it is a workflow that leaves anomalies no record and no longer needs anyone to judge them.

So this piece is less an argument against automation than against a default design: treating the rerun as the only exit for an anomaly, and treating outlier removal as the end point of quality control.

## Reproducible and discoverable: questions still open

To draw the discussion together: "reproducible" and "discoverable" are different goals. The first requires pushing variance down; the second sometimes requires paying attention to variance. For the first, automation is almost pure gain; for the second, its effect depends on how the workflow is designed.

A few signs show whether a workflow still has the capacity for discovery. Are key steps still done by hand — or does someone at least regularly look at the raw samples and raw data with their own eyes? Are anomalous results recorded, flagged and reviewed periodically, or silently rerun? Is there still someone on the team who can say what a normal result usually looks like, and explain why? If the answer to all three is no, the workflow may already be trading discovery for reproducibility — a trade that shows up in no metric.

The limits of this piece bear repeating. *Encoding → filtering → degraded error correction* is an inferred mechanism; agricultural history is only an analogy; and most of the AI-related events come from company disclosures or work not yet peer-reviewed. What would really test this judgment is a kind of study that is still rare: comparing, across labs with different degrees of automation, the share of anomalies that are recorded, investigated and finally confirmed as new phenomena.

Several questions remain open.

First, will the boundary of what can be encoded move with technology? Multimodal sensing and vision models may turn today's "feel" into tomorrow's data. If so, the line between discriminating and operating knowledge is not fixed, and the split proposed here holds only under particular technical conditions.

Second, how can a workflow keep an anomaly channel open at low enough cost? For instance, requiring every rerun to leave the raw record and one human-written note costs little, yet may preserve some of the chances to correct errors.

Third, who trains the ability to discriminate, and who inherits it? If a new generation of researchers works with automated workflows from day one, where do they build their tacit expectation of "normal"? This is the same question the Fields Medallists worry about: the value of training lies not only in the answers it produces.

## Key points

1. Tacit knowledge has two layers: operating knowledge that can be written into a protocol, and discriminating knowledge that depends on context; automation mainly encodes the first.
2. The risk is not about efficiency but about whether anomalies enter the feedback loop: anomalies logged as noise or silently rerun no longer train human discrimination.
3. To judge whether a workflow can still discover new things, look at whether people remain at key steps, and whether anomalies are recorded and reviewed by a person.

Automation is not a neutral swap of tools. In deciding what is worth recording, it also decides which anomalies science can still see.

## References

1. <https://orca.cardiff.ac.uk/id/eprint/90648/>
2. <https://www.cell.com/cell-reports/fulltext/S2211-1247(14)00121-1>
3. <https://link.springer.com/article/10.15252/embj.2018101011>
4. <https://www.nature.com/articles/s41597-025-06060-y>
5. <https://nph.onlinelibrary.wiley.com/doi/10.1111/nph.17733>
6. <https://research.wur.nl/en/publications/genetic-diversity-trends-in-twentieth-century-crop-cultivars-a-me/>
7. <https://mathandai.org/>
8. <https://mathstodon.xyz/@tao/117253629967855195>
9. <https://www.anthropic.com/research/yes-claude-can-do-nine-loops>
10. <https://www.anthropic.com/news/claude-discovers-novel-enzyme-system>
11. <https://www.nature.com/articles/533452a>
