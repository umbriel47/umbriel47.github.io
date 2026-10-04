---
layout: post
title: "Of Every $100 of AI Capex, Whose Profit Does It Become?"
date: 2026-10-04 08:37:00 +0800
lang: en
ref: who-profits-from-ai-capex
tags: [science]
wide: true
wechat_url: "https://mp.weixin.qq.com/s/6Ph3sB2uH7urAQxdrXVw4A"
description: "An estimate chart cited by a16z Growth splits $100 of AI capex across the layers of the supply chain. Checked against public filings, the spending shares are broadly credible, but profit is highly concentrated: chips take about half the spending yet may account for 60–70% of the chain's gross profit, and memory is pushing its way to the top of that layer."
---

In 2026 the four largest US cloud providers plan to spend a combined ~$725 billion on capex, up more than 70% from ~$410 billion in 2025 (Tom's Hardware, 2026-04-30[\[1\]](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)). Nvidia's figure on its August earnings call was bigger still: capex by the top five cloud providers close to $800 billion in 2026 and about $1.3 trillion in 2027 (Nvidia FY2027 Q2 earnings call transcript[\[2\]](https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf)). With that much money flowing into the supply chain, the usual discussion stops at "who got the orders". This piece asks the next question: **once orders become revenue, which layer does the profit stay in?** My view is that there is a clear mismatch between share of spending and share of profit, and that in 2026 the mismatch is shifting towards memory.

## One estimate chart, and what it can answer

The starting point is a Sankey diagram recently circulated by a16z Growth, titled "Following The AI Capex Money". It splits a hypothetical $100 of AI capex across the layers of the supply chain, credits BNP Paribas Equity Research as the source, is dated August 2026, and notes that it is a "high-level estimate, subject to rapid change with costs and supply and demand".

<figure>
  {%- include charts/ai-capex/en/fig1.svg -%}
  <figcaption>Figure 1 | An illustrative split of $100 of AI capex across the supply chain (estimate, not measured) · Source: data from BNP Paribas Equity Research (August 2026), via a chart by a16z Growth; redrawn by 一目半 (Yimuban)</figcaption>
</figure>

By the chart's numbers, of the $100: semiconductors $50 (accelerators 25, memory 15, CPUs, other chips and server manufacturing 10), networking equipment $15 (optical modules 5.5, switches 4.5, network processors 3, cables 2), power $20 (grid connection and on-site generation 10, power distribution 6.5, on-site electrical wiring 3.5), cooling $7.5, and buildings and construction $7.5. A further branch, wafer fab equipment (WFE) at $8, comes off the chip layer. Below I check the chart as a broker's estimate, not as data.

The chart answers "who gets paid first". It doesn't answer another question.

Share of spending vs value capture: share of spending is the proportion of a capex dollar that flows to a given link in the chain — that link's revenue. Value capture is how much of that revenue is left as profit after costs. Two links can win the same amount of orders and keep very different profits.

## Layer by layer: the chip half

**Accelerators and system vendors.** For the quarter ended 26 July 2026, Nvidia's revenue was $96.2 billion, of which data centre $89.0 billion; gross margin was 75.0%, GAAP operating income $63.7 billion, an operating margin of about 66% (Nvidia press release[\[3\]](https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm)). Broadcom's AI semiconductor revenue in the same period was $16.7 billion, with a non-GAAP gross margin of about 75% as derived from the financial tables in its press release (Broadcom press release[\[4\]](https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm)). The accelerator layer sits at the top of the whole chain in both revenue scale and gross margin.

There is one notable discrepancy with the chart here. In August 2025 Jensen Huang said on the earnings call that a 1-gigawatt AI factory costs about $50–60 billion to build, of which Nvidia's share is about $35 billion (Nvidia FY2026 Q2 earnings call transcript[\[5\]](https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/NVDA-Q2-2026-Earnings-Call-27-August-2025-5_00-PM-ET.pdf)); the August 2026 call went further, saying Nvidia content per gigawatt rises from about $18 billion for Hopper and about $25 billion for Blackwell to about $40 billion for Vera Rubin. On that basis Nvidia alone accounts for 60–70% of an AI factory — more than the chart's "accelerators $25". Most of the difference comes from definitions: Nvidia's revenue includes the HBM it buys and packages into GPUs, Grace/Vera CPUs, NVLink switch chips and network cards, which the chart counts separately under memory, CPUs and networking. Even so, seen side by side, the two bases suggest that by selling bundles, system vendors may actually capture a larger share than a chart split by chip category implies. Note too that this figure comes from the seller itself.

**Memory.** This is the layer that has changed most in 2026. SK hynix's second-quarter revenue was 79.3 trillion won, with operating profit of 60.5 trillion won — an operating margin of 76% (SK hynix 2Q26 results[\[6\]](https://www.storagenewsletter.com/2026/07/30/sk-hynix-fiscal-2q26-financial-results/)). Micron's revenue for the quarter ended 3 September 2026 was $54.2 billion, with a GAAP gross margin of 86.8%, and it guided next-quarter revenue to about $61.5 billion at a gross margin of about 86% (Micron press release[\[7\]](https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm)). In other words, in the most recent quarter both memory makers' margins were higher than Nvidia's.

Evidence from the cost side points the same way. Nvidia said on its call that memory price increases were "more than previously expected, and will be higher next year", and cut its next-quarter gross-margin guidance to 74%. Microsoft's CFO attributed about $25 billion of 2026 capex to higher memory and component prices, and Meta gave a similar explanation (Tom's Hardware[\[1\]](https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion)). If those statements hold, the chart's "memory $15" may be low for the second half of 2026; at the very least, memory is taking part of the profit away from accelerators.

**CPUs, other chips and server manufacturing.** These $10 vary enormously inside. CPUs and custom chips carry high gross margins, while system assembly is thin: Foxconn's 2026 second-quarter revenue grew 41% year on year, but its gross margin was only 6.12% and its operating margin 3.75% (Foxconn 2Q26 results[\[8\]](https://iconnect007.com/article/151169/foxconn-announces-q2-2026-financial-results/151166/ein)). The link that ships the most servers is one of the least profitable.

**Foundries and equipment: the second-tier money.** TSMC is not on the chart, but it sits upstream of the accelerators. In the second quarter TSMC's gross margin was 67.7% and operating margin 60.3%; high-performance computing made up 66% of revenue, and full-year capex was raised to $60–64 billion (TSMC 2Q26 results[\[9\]](https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm); earnings call transcript[\[10\]](https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf)). TSMC's capex in turn becomes the equipment makers' revenue: ASML's second-quarter gross margin was 54.0%, with full-year revenue guidance of €43–45 billion (ASML press release[\[11\]](https://investor.asml.com/news-releases/news-release-details/q2-2026-financial-results)); SEMI expects global WFE sales of $143.9 billion in 2026, up 23% year on year (SEMI, 2026-07-14[\[12\]](https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports)).

This determines how to read the chart's WFE $8: it is not spending on top of the $100 but reinvestment that chipmakers pay for out of their revenue — a second-tier flow that cannot be added to the first tier.

## Layer by layer: networking, power, cooling and buildings

**Networking.** Networking takes $15 in the chart, with sharply divergent gross margins inside. Arista's second-quarter revenue was $3.04 billion, with a non-GAAP gross margin of 63.4% and an operating margin of 49.9% (Arista press release[\[13\]](https://finviz.com/news/377054/arista-networks-inc-reports-second-quarter-2026-financial-results)); the optical-module maker Coherent reported revenue of $2.05 billion for the quarter to June, with a non-GAAP gross margin of 40.2% (Coherent press release[\[14\]](https://www.sec.gov/Archives/edgar/data/0000820318/000119312526346860/d128030dex991.htm)). Within networking, switches and network chips have margins close to semiconductors, optical modules are clearly lower, and cables are closer to manufacturing.

**Power, cooling and buildings.** Together these take $35 in the chart, more than a third. Outside data broadly supports that order of magnitude: Cushman & Wakefield's 2026 cost guide puts the average cost of a new data centre in the US and Canada at $17.6 million per megawatt, excluding chips and GPUs, up 21% from the fourth quarter of 2024, with electrical infrastructure the largest single item at about 21% (Cushman & Wakefield, 2026-09-03[\[15\]](https://finviz.com/news/388803/cushman-wakefield-releases-2026-data-center-development-cost-guide-citing-21-rise-in-per-mw-construction-costs)). If a gigawatt costs $50–60 billion in total, the non-chip part, about $17.6 billion, is roughly 30%, close to the chart's 35%. Note that the chart's "grid connection and on-site generation $10" may partly fall outside Cushman's scope, so the two cannot be matched item by item.

Margins are another matter. Vertiv, the leader in cooling and power distribution, reported second-quarter revenue of $3.27 billion and an adjusted operating margin of 22.6%, with full-year guidance of 23.3% to 24.3% (Vertiv press release[\[16\]](https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm)). That is already high for an industrial company, and GE Vernova's second-quarter orders grew 88% organically year on year (Quartz[\[17\]](https://qz.com/ge-vernova-2026-revenue-guidance-second-quarter-earnings-072226)) — but it is still an order of magnitude below semiconductors. Construction margins are thinner still; I found no reliable public data on data-centre general contracting, and below I assume a gross margin in the low double digits.

## From spending to earning: recalculating by gross profit

Putting the data above together allows a rough conversion: multiply each layer's spending in the chart by the latest-quarter gross margin of that layer's representative companies, to get the gross profit each $100 leaves in each layer. The assumptions: accelerators 75% (Nvidia, Broadcom), memory 80% (a conservative value between Micron and SK hynix), CPUs and server manufacturing 25% (a mix of high-margin chips and roughly 6% assembly), networking 50%, power 25%, cooling 35%, buildings 12%. The last three lack directly comparable gross-margin disclosures and are my estimates.

On this calculation, $100 of spending leaves about $49 of gross profit: about $19 in accelerators, $12 in memory, $2.5 in CPUs and servers, $7.5 in networking, $5 in power, $2.6 in cooling and $0.9 in buildings.

<figure>
  {%- include charts/ai-capex/en/fig2.svg -%}
  <figcaption>Figure 2 | Share of spending vs estimated share of gross profit: chips take half the spending but about two-thirds of the gross profit; power, cooling and buildings take over 30% of the spending but under 20% of the gross profit · Source: estimated by 一目半 (Yimuban) from figure 1 and company filings</figcaption>
</figure>

As shares, the mismatch is plain. Accelerators, memory and CPUs together take 50% of spending but about 67% of gross profit; power, cooling and buildings together take 35% of spending but only about 17% of gross profit. Accelerators and memory alone turn 40% of the spending into about 60% of the gross profit.

<figure>
  {%- include charts/ai-capex/en/fig3.svg -%}
  <figcaption>Figure 3 | Latest-quarter gross margins of representative supply-chain companies (fiscal quarters end on different dates; see text) · Source: company press releases, compiled by 一目半 (Yimuban)</figcaption>
</figure>

The result is not especially sensitive to the assumptions. Raise the gross margins for power and cooling by 10 percentage points each and chips' share of gross profit is still above 60%. What it is really sensitive to is memory: memory margins have always swung widely with the cycle, and if they fell back to around 40%, the chain's gross profit would drop by about $6 and chips' share to around 60%. In other words, this piece's surest conclusion is that profit is concentrated in chips; its least certain is how long memory can stay in that layer.

> The spending map of AI capex is a wide chart; the profit map is a narrow one. The money flows to dozens of links, but the profit stays mainly in a few kinds of chips.

## Where the chart and public data disagree

In checking the chart, three things are worth the reader's attention.

First, the chart has an internal arithmetic inconsistency. The WFE node is labelled $8, but its five branches sum to $18 (deposition 2, lithography 12, etch 1, inspection 1, packaging and other 2). If lithography were actually 2, the five items would sum to exactly 8, so a labelling error is likely, but I cannot confirm it. Also, by Yole's statistics for 2023, patterning equipment was about 30% of WFE, deposition about 26–27%, and etch and clean about 19% (Yole Group[\[18\]](https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/)); in the chart etch is only an eighth, which looks low. The chart's source line also misspells "BNP Paribas" as "BNP Panbas".

Second, the system vendor's share. As noted above, Nvidia's own basis implies that it alone takes 60–70% of an AI factory, more than the chart's split by chip category suggests. Different definitions explain most of the gap, but not all of it.

Third, memory's share and profit. The chart is dated August 2026 and may already partly reflect higher memory prices; but statements by Nvidia and Microsoft in July and August both indicate that memory costs are still rising. The chart's $15 looks more like a point-in-time estimate than a steady state.

## The strongest objection: gross margin isn't the whole account

This conversion has several limitations that must be acknowledged head-on.

Gross margin is not economic profit. Chip designers spend heavily on R&D, and foundries and memory makers must reinvest much of their revenue in capacity every year: TSMC's 2026 capex is over $60 billion, and memory makers are expanding too. Measured by return on capital rather than gross margin, the gaps between layers would narrow — memory most of all, since its high margins tend to appear in windows when supply is tight and large-scale expansion has not yet arrived.

The ultimate capturer of value may also not be in the supply chain at all but among the buyers. AWS's second-quarter operating margin was 39.4%, but according to one analysis based on its filings, Amazon's trailing-twelve-month free cash flow has turned to about negative $7.6 billion (beancount.io analysis[\[19\]](https://beancount.io/blog/2026/07/31/amazon-fy2026-q2-earnings-analysis)). Today's spending by cloud providers buys years of future compute revenue. The depreciation lives, utilisation and pricing of these assets will decide whether the $700-plus billion ends up as the supply chain's profit or the buyers' return. Nvidia says a gigawatt AI factory rents for about as much a year as it costs to build (as reported by 24/7 Wall St.[\[20\]](https://247wallst.com/investing/2026/09/24/nvidias-ceo-says-a-1-gigawatt-ai-factory-rents-for-50-billion-a-year-as-much-as-it-costs-to-build/)); that claim also comes from the seller and has not been independently verified.

Finally, this piece mixes fiscal quarters with different end dates: Nvidia's ends in late July, Micron's in early September, Coherent's at the end of June. In a year of fast-moving prices, that introduces error.

## Questions still open

First, how long can memory's excess profits last? That depends on the pace of HBM expansion, and on whether accelerator makers can pass the cost on to the cloud providers.

Second, will system vendors' bundling power keep growing? If the claim that Nvidia content per gigawatt rises from $18 billion to $40 billion comes true, the value of networking, CPUs and even part of cooling and power supply may be drawn further into a single supplier's quote.

Third, will power go from being a big spender to a big earner? When grid-connection queues and generating-equipment deliveries become the constraint, scarcity may shift some bargaining power to power-equipment makers and to developers that hold grid connections. Current margin data does not yet show such a shift.

## Key points

1. Figure 1 answers who gets paid, not where the profit stays; WFE is a second-tier flow and cannot be added to the first tier.
2. Converted at representative gross margins, chips take about half the spending and two-thirds of the gross profit; power, cooling and buildings take over 30% of the spending and under 20% of the gross profit.
3. The biggest variable in 2026 is memory: in the latest quarter, memory makers' margins were already above Nvidia's, and the chart's memory share may be too low.

Follow the capex and you can see where the orders go; follow the gross margins to see whose hands the profits of this build-out actually land in.

## References

1. <https://www.tomshardware.com/tech-industry/big-tech/big-techs-ai-spending-plans-reach-725-billion>
2. <https://investor.nvidia.com/files/content_files/TRANSCRIPT_-NVIDIA-Corp-NVDA-US-Q2-2027-Earnings-Call-26-August-2026-5_00-PM-ET.pdf>
3. <https://www.sec.gov/Archives/edgar/data/0001045810/000104581026000073/q2fy27pr.htm>
4. <https://www.sec.gov/Archives/edgar/data/0001730168/000173016826000076/avgo-08022026x8kxex99.htm>
5. <https://s201.q4cdn.com/141608511/files/doc_financials/2026/q2/NVDA-Q2-2026-Earnings-Call-27-August-2025-5_00-PM-ET.pdf>
6. <https://www.storagenewsletter.com/2026/07/30/sk-hynix-fiscal-2q26-financial-results/>
7. <https://www.sec.gov/Archives/edgar/data/0000723125/000072312526000018/a2026q4ex991-pressrelease.htm>
8. <https://iconnect007.com/article/151169/foxconn-announces-q2-2026-financial-results/151166/ein>
9. <https://www.sec.gov/Archives/edgar/data/0001046179/000104617926000451/a2q26e_withguidancexfinal.htm>
10. <https://investor.tsmc.com/english/encrypt/files/encrypt_file/reports/2026-07/547d1696765e05ce3adb81c108ce1c8c1682b80c/TSMC%202Q26%20Transcript.pdf>
11. <https://investor.asml.com/news-releases/news-release-details/q2-2026-financial-results>
12. <https://www.semi.org/en/semi-press-release/global-semiconductor-equipment-sales-forecast-to-reach-a-record-229-billion-dollars-in-2028-semi-reports>
13. <https://finviz.com/news/377054/arista-networks-inc-reports-second-quarter-2026-financial-results>
14. <https://www.sec.gov/Archives/edgar/data/0000820318/000119312526346860/d128030dex991.htm>
15. <https://finviz.com/news/388803/cushman-wakefield-releases-2026-data-center-development-cost-guide-citing-21-rise-in-per-mw-construction-costs>
16. <https://www.sec.gov/Archives/edgar/data/0001674101/000162828026050323/q22026exhibit991vrt07292026.htm>
17. <https://qz.com/ge-vernova-2026-revenue-guidance-second-quarter-earnings-072226>
18. <https://www.yolegroup.com/strategy-insights/semiconductor-equipment-market-share-reshuffles-amid-memory-demand-decline/>
19. <https://beancount.io/blog/2026/07/31/amazon-fy2026-q2-earnings-analysis>
20. <https://247wallst.com/investing/2026/09/24/nvidias-ceo-says-a-1-gigawatt-ai-factory-rents-for-50-billion-a-year-as-much-as-it-costs-to-build/>
