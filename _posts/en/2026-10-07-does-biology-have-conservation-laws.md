---
layout: post
title: "Does Biology Have Its Own Conservation Laws? A Test from the Central Dogma to Metabolic Scaling"
subtitle: "The central dogma fixes the steps and direction in which genetic information flows, but places almost no limit on where genomes and phenotypes can go. Biology lacks hard constraints like conservation laws that drastically cut down the space of possibilities, so data-driven accumulation is its normal state."
date: 2026-10-07 09:14:00 +0800
lang: en
ref: does-biology-have-conservation-laws
tags: [science]
wide: true
wechat_url: "https://mp.weixin.qq.com/s/kXmMStVwrP4z2Sfmo8A8cQ"
description: "The central dogma describes the mechanism of information flow; it doesn't draw the boundary of the states life can reach. Biology still lacks universal constraints of the conservation-law kind, metabolic scaling can hardly fill that role, and so its predictive power can only be built up layer by layer through data and models."
---

Biology often carries an unspoken optimism: molecular biology has already given us life's ground rules, and what remains is filling in the details. This piece puts that judgment to the test. The question is specific: **does biology have hard constraints that, like conservation laws, rule out large swathes of possibility before you look at any data?** It is worth asking now because the life sciences are betting heavily on data and foundation models. If hard constraints are scarce to begin with, that bet follows from the structure of the discipline, not just from a technological fashion.

## Mechanism, law and constraint: only constraints cut down possibilities before you see the data

Before talking about "first principles", we need to separate three kinds of statement that are often run together.

The first is mechanism. It says by what steps and in what direction a process happens — for example, transcription precedes translation, and the ribosome moves along mRNA from the 5′ end to the 3′ end.

The second is law. It gives a stable quantitative relation between variables — for example, the ideal gas equation, or Michaelis–Menten kinetics. A law can be very precise, but it often holds only under particular conditions, and its parameters have to be measured system by system.

The third is constraint. It doesn't describe how a process goes; it only marks which states are unreachable at all. Conservation of energy doesn't tell you how a marble rolls around a bowl, but it guarantees the marble will never roll by itself to a point higher than where it started.

- **Constraint**: an a priori limit on the states a system can reach — whatever the details of the process, states that violate it do not occur. The value of a constraint lies in what it excludes.

The difference among the three lies in what each contributes to prediction. Mechanism helps understanding; law helps calculation under known conditions; constraint cuts away a large part of the possibility space before you know the details. Conservation laws are said to be worth ten thousand sentences because they belong to the third kind.

To make the comparison workable, this piece uses a rough measure of a constraint's power.

- **Constraint strength**: how large a share of the possible state space a constraint can exclude, and how many degrees of freedom it can remove, without depending on data from the specific system. The stronger it is, the less is left to be pinned down by observation and fitting.

Three questions can gauge a regularity's constraint strength. First, can it be derived without fitting data from the system at hand? Second, does it hold across systems, so firmly that when an observation contradicts it, people suspect the observation before the regularity? Third, how many dimensions does it remove — or does it merely narrow the space a little?

The rest of this piece uses these three questions to test the candidates from physics and from biology.

## The central dogma says how information travels, not where life can go

Francis Crick proposed the central dogma in 1958. In 1970 he restated it in *Nature*, with one sentence at its core: once sequence information has passed into protein, it cannot get out again (Crick 1970, *Nature*[\[1\]](https://www.nature.com/articles/227561a0)).

In the same paper, Crick sorted the nine possible information transfers into three classes. General transfers occur in all cells: DNA→DNA, DNA→RNA, RNA→protein. Special transfers occur only in particular circumstances: RNA→RNA, RNA→DNA, and DNA→protein in cell-free systems. The remaining three — from protein to any nucleic acid or protein — were postulated never to occur.

That same year, Temin and Mizutani, and Baltimore, independently reported reverse transcriptase (Temin & Mizutani 1970[\[2\]](https://www.nature.com/articles/2261211a0); Baltimore 1970[\[3\]](https://www.nature.com/articles/2261209a0)). In Crick's classification, RNA→DNA is a special transfer and does not violate the central dogma. Today's textbooks usually teach the central dogma as the three-step DNA→RNA→protein flow, listing reverse transcription and RNA replication separately as special cases; prions transmit conformation, not sequence information, and are generally not regarded as counterexamples either.

There is a detail here that has to be faced: Crick's original formulation is itself a prohibition, formally like a constraint. But what it prohibits is a few edges on the graph of information transfers. It doesn't tell you what a species' genome can become, which regulatory networks can exist, or whether a given phenotype can appear.

By the three questions of the previous section, this prohibition holds across taxa and has no reliable counterexample to date, so it passes the first two. But it removes very few dimensions: in the space of possible genotypes and phenotypes, it rules out almost no specific state.

<figure>
  {%- include charts/biology-constraints/en/fig1.svg -%}
  <figcaption>Figure 1 | Mechanism versus constraint: on the left, a directed flow that fixes the steps and the direction; on the right, a boundary that cuts most of the possible solutions away, leaving only a small reachable region · Source: drawn by 一目半 (Yimuban)</figcaption>
</figure>

The impression that "the first principles are already in place" comes largely from reading this flow as a boundary. Knowing how information flows from DNA to protein and knowing which proteins, which cell states, cannot occur are two different kinds of knowledge. Molecular biology has the first fairly completely; the second can still only be measured case by case.

## Physics' predictive power comes from a few conservation relations carving up the state space

Physics' strong predictive power is often credited to the precision of its equations. The deeper reason lies in the structure of its constraints.

In 1918 Emmy Noether proved that if a system's dynamics can be derived from a variational principle on an action, then every continuous symmetry of the action corresponds to a conserved quantity (Noether 1918, English translation[\[4\]](https://arxiv.org/abs/physics/0503066)). Time-translation symmetry gives conservation of energy, spatial-translation symmetry gives conservation of momentum, rotational symmetry gives conservation of angular momentum.

The theorem has two preconditions. The system must have an action formulation, and the symmetry must be continuous. For dissipative, open systems there is no ready-made action, the theorem does not apply directly, and existing generalisations all require extra construction.

When the preconditions hold, the compression is considerable. Take the relative motion of two bodies under gravity: the phase space is six-dimensional. Energy, the three components of angular momentum, and the Laplace–Runge–Lenz vector together provide five independent conserved quantities. The orbit is thereby squeezed onto a one-dimensional closed curve, and its type of shape can be determined with almost no observational data.

The hardness of a constraint also shows in how people treat contradictions. Around 1930, the energy of electrons in beta decay had a continuous spectrum, apparently violating conservation of energy. Pauli chose to keep the conservation law and postulated an unobserved neutral particle that carried off the energy. The particle was detected in 1956 in Cowan and Reines's reactor experiment (Cowan et al. 1956, *Science*[\[5\]](https://doi.org/10.1126/science.124.3212.103)).

This is exactly the situation the second question describes: when observation conflicts with a constraint, people revise their description of the world first and keep the constraint.

<figure>
  {%- include charts/biology-constraints/en/fig2.svg -%}
  <figcaption>Figure 2 | How conservation constraints compress the prediction space: a few conservation relations cut a large space of unconstrained possible states down to a narrow band, and experimental observations fall inside it · Source: drawn by 一目半 (Yimuban)</figcaption>
</figure>

A general relation follows: the more constraints there are, and the harder they are, the less data it takes to pin a system down; the fewer the constraints, the more of the space has to be filled by fitting. Physics doesn't always escape fitting, but it fits within a space that has already been drastically reduced.

The difficulty of carrying Noether's theorem straight over to biological objects is that neither precondition holds. Cells and populations are open systems far from equilibrium; nobody knows what their action would be, or which continuous symmetries are worth considering. Longo, Montévil and Kauffman even argue that what characterises biological evolution is precisely that symmetries keep changing, so the phase space itself cannot be given in advance (Longo et al. 2012, arXiv[\[6\]](https://arxiv.org/abs/1201.2069)). This is a theoretical position without consensus, but it does at least show that transplanting physics' constraint machinery into biology is not straightforward.

## Biology's existing invariants: mostly borrowed from physics, or carrying exceptions

To say that biology lacks hard constraints is not to say that life is unconstrained. Taking stock item by item, the candidates fall into three groups.

The first is physical constraints. Conservation of energy limits an organism's energy budget; diffusion rates limit how large a cell can grow without active transport; temperature affects almost every physiological process through reaction rates. These constraints are real and hard, but they belong to physics and chemistry; biology didn't discover them itself.

Constraint-based metabolic modelling is a representative example. Flux balance analysis uses the stoichiometric matrix and a steady-state assumption to confine reaction fluxes to a polytope (Orth et al. 2010, *Nat Biotechnol*[\[7\]](https://doi.org/10.1038/nbt.1614)). Mass conservation genuinely removes many dimensions here, but the feasible region left over is usually still large. Picking a specific flux distribution from it requires assuming an objective function — maximising biomass, say — and whether that assumption holds has to be tested experimentally, condition by condition.

The second group is quantitative invariants. These are biology's own discoveries, but each comes with exceptions or a limited range of application.

The genetic code was long called "universal". In 1979 it was found that in human mitochondria UGA codes for tryptophan rather than stop (Barrell et al. 1979, *Nature*[\[8\]](https://doi.org/10.1038/282189a0)). More and more variants have been found since; besides the standard code, NCBI now maintains more than twenty translation tables — *Candida albicans*, for example, reads CUG as serine (NCBI Genetic Codes[\[9\]](https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi)). These findings were catalogued as exceptions; no one doubted the sequencing results because of them. That is exactly the opposite of how beta decay was handled.

Sequence conservation is the same. In 2004 Bejerano and colleagues found 481 ultraconserved elements of at least 200 bp that were identical across the human, rat and mouse genomes (Bejerano et al. 2004, *Science*[\[10\]](https://doi.org/10.1126/science.1098119)). Conservation that extreme is naturally read as "cannot be changed".

Yet in 2007 Ahituv and colleagues knocked out four of these elements in mice, one at a time. All four strains were viable and fertile, and tests of growth, longevity, pathology and metabolism found no critical abnormalities (Ahituv et al. 2007, *PLoS Biol*[\[11\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC1964772/)). Conservation is a statistical residue of evolutionary history; it is not a limit on reachable states.

Elemental stoichiometry is similar. The carbon, nitrogen and phosphorus ratios of marine plankton are often referenced to the Redfield ratio, but measured ratios vary systematically with latitude and environment (Martiny et al. 2013, *Nat Geosci*[\[12\]](https://doi.org/10.1038/ngeo1757)). It is more of a useful average.

The third group is scaling relations. They are the only candidate that seems both to belong to biology and to be possibly universal across taxa, and the next section treats them on their own.

<figure>
  {%- include charts/biology-constraints/en/fig3.svg -%}
  <figcaption>Figure 3 | Three sources of candidate constraints in biology: physical constraints, quantitative invariants and scaling relations; together they raise the question of which are real constraints and which are only fits · Source: drawn by 一目半 (Yimuban)</figcaption>
</figure>

## Metabolic scaling: why the strongest counterexample still falls short

If some scaling relation could be derived from mechanism and gave the same exponent across all taxa, biology would have a hard constraint of its own, and this piece's argument would have to give way. The relation between metabolic rate and body mass is the strongest candidate for that position.

The relation is usually written as metabolic rate proportional to some power of body mass. Simple reasoning from the ratio of surface area to volume gives an exponent of 2/3, an idea that goes back to Rubner's work in the nineteenth century. In 1932 Kleiber compiled data on mammals and found an exponent close to 3/4 (Kleiber 1932, *Hilgardia*[\[13\]](https://doi.org/10.3733/hilg.v06n11p315)), and the "3/4 law" spread widely from there.

In 1997 West, Brown and Enquist proposed a fractal transport-network model that derived 3/4 from assumptions of space filling, invariant terminal units and minimal energy dissipation (West et al. 1997, *Science*[\[14\]](https://doi.org/10.1126/science.276.5309.122)). This was the moment scaling came closest to being a constraint derived from mechanism.

The trouble is that later measurements disagree.

In 2001 Dodds, Rothman and Weitz reanalysed the classic datasets for mammals and birds and found almost no evidence for rejecting 2/3 in favour of 3/4; they also argued that the existing theories deriving 3/4 all rest on unconvincing assumptions (Dodds et al. 2001, arXiv[\[15\]](https://arxiv.org/abs/physics/0007096)).

In 2003 White and Seymour analysed the basal metabolic rates of **619 species** of mammals across 19 orders. After controlling for body temperature, digestive state and phylogeny, the relation they found was consistent with 2/3 (White & Seymour 2003, *PNAS*[\[16\]](https://pmc.ncbi.nlm.nih.gov/articles/PMC153045/)).

In 2010 Kolokotrones and colleagues showed that, even accounting for temperature, mammalian metabolic rate against body mass is a convex curve on log axes, not a pure power law (Kolokotrones et al. 2010, *Nature*[\[17\]](https://www.nature.com/articles/nature08920)). If the curve itself bends, different studies fitting different exponents is partly just a matter of sampling different ranges of body mass.

The same year, Capellini and colleagues found within a phylogenetic framework that the exponent differs significantly between lineages: some close to 3/4, some close to 2/3, some consistent with neither (Capellini et al. 2010, *Ecology*[\[18\]](https://hull-repository.worktribe.com/output/371734)).

Widen the scale to the whole tree of life and the differences grow. DeLong and colleagues report that the exponent for prokaryotes is clearly greater than 1, for protists close to 1, and for metazoans close to 3/4 (DeLong et al. 2010, *PNAS*[\[19\]](https://doi.org/10.1073/pnas.1007783107)).

There is also a layer of confounding that is hard to get around. Body size, body temperature and phylogeny covary: large and small mammals tend to belong to different orders, with different ways of life and different body temperatures. Gillooly and colleagues brought temperature into the model as a Boltzmann factor (Gillooly et al. 2001, *Science*[\[20\]](https://doi.org/10.1126/science.1061967)), which improved the fit but also showed that body mass alone is not self-sufficient. In observational data these factors are hard to separate completely.

Put through the three questions, metabolic scaling's position becomes clear. Can it be derived a priori? Some models claim so, but their assumptions are themselves contested. Does it hold across systems? Different taxa and different scales give different exponents. Faced with inconsistent data, the field's response has been to add temperature terms, curvature terms and lineage differences, not to doubt the data. That is how one treats an empirical regularity.

> Whether a regularity is a hard constraint depends on who gives way when it conflicts with observation: physics revises its description of the world to save the conservation law; biology adds exceptions and correction terms to the regularity.

This doesn't deny the value of scaling relations. They are extremely useful empirical generalisations that give order-of-magnitude estimates when details are missing. But their constraint strength is far below that of conservation laws: they narrow the space without removing dimensions.

## Conclusion, and questions still open

Back to the opening question. The central dogma is one of molecular biology's most important theoretical achievements, but what it describes is the mechanism of information flow; its prohibition holds across taxa, yet barely reduces the space of possible genotypes and phenotypes. The quantities in biology called "invariant" are either borrowed from physics and chemistry or come with exceptions. Metabolic scaling is the strongest candidate, but its exponent varies with taxon and scale, its confounders are hard to control, and for now it looks more like a useful empirical regularity.

The judgment that follows: biology's predictive power can only be built up layer by layer through data and models, and this is a consequence of the discipline's structure. Few constraints mean a large possibility space, and filling it takes a great many observations. That data-driven methods sit at the centre of biology does not show the discipline is immature; it is dictated by its subject matter.

This judgment has some limitations that should be stated.

First, this piece's definition of "constraint strength" is qualitative. Turning it into a computable quantity would require first defining a state space and a prior distribution — and a state space is exactly what biology finds hard to specify in advance.

Second, evolution itself may supply another kind of constraint. Natural selection, historical contingency and developmental pathways can make some regions practically unreachable, but such constraints depend on history and lack the cross-system universality of conservation laws.

Third, this piece has not discussed extensions of the second law of thermodynamics to living systems — for example, limits that non-equilibrium thermodynamics places on replication and adaptation. Such work may give biology constraints closer to the physical sense, but it is still some way from directly predicting biological states.

## Key points

1. Mechanism fixes steps and direction; constraint cuts down reachable states. Only the latter can compress the prediction space before you look at data.
2. The central dogma holds across taxa but places almost no limit on where genomes and phenotypes can go; biology's invariants are mostly borrowed from physics, or come with exceptions.
3. The exponent of metabolic scaling varies with taxon and scale and covaries with body temperature and lineage; for now it is not enough to serve as biology's own hard constraint.

At least two questions remain open. First, are there biological invariants not yet identified, perhaps hidden in the structure of high-dimensional data, that will only show up once there are enough perturbation experiments? Second, if a constraint can only be read out of data after the fact, what separates it from a successful fit? One possible criterion: when a new observation contradicts it, which one are we willing to doubt first?

## References

1. <https://www.nature.com/articles/227561a0>
2. <https://www.nature.com/articles/2261211a0>
3. <https://www.nature.com/articles/2261209a0>
4. <https://arxiv.org/abs/physics/0503066>
5. <https://doi.org/10.1126/science.124.3212.103>
6. <https://arxiv.org/abs/1201.2069>
7. <https://doi.org/10.1038/nbt.1614>
8. <https://doi.org/10.1038/282189a0>
9. <https://www.ncbi.nlm.nih.gov/Taxonomy/Utils/wprintgc.cgi>
10. <https://doi.org/10.1126/science.1098119>
11. <https://pmc.ncbi.nlm.nih.gov/articles/PMC1964772/>
12. <https://doi.org/10.1038/ngeo1757>
13. <https://doi.org/10.3733/hilg.v06n11p315>
14. <https://doi.org/10.1126/science.276.5309.122>
15. <https://arxiv.org/abs/physics/0007096>
16. <https://pmc.ncbi.nlm.nih.gov/articles/PMC153045/>
17. <https://www.nature.com/articles/nature08920>
18. <https://hull-repository.worktribe.com/output/371734>
19. <https://doi.org/10.1073/pnas.1007783107>
20. <https://doi.org/10.1126/science.1061967>
