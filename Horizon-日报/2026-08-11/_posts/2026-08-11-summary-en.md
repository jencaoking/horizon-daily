---
layout: default
title: "Horizon Summary: 2026-08-11 (EN)"
date: 2026-08-11
lang: en
---

> From 45 items, 12 important content pieces were selected

---

**Technology News**
1. [Hidden Reasoning Traces Extracted from Proprietary LLM APIs](#item-tech-news-1) ⭐️ 8.0/10
2. [Meta Releases Muse Glimmer, a 30B Apache-2.0 Agentic Model](#item-tech-news-2) ⭐️ 8.0/10
3. [NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Routing](#item-tech-news-3) ⭐️ 7.0/10
4. [Modular Ships Mojo 1.0 for AI Workloads](#item-tech-news-4) ⭐️ 7.0/10
5. [Nvidia&\#x27;s Strategic Risks: CUDA Moat and AI Demand](#item-tech-news-5) ⭐️ 7.0/10
6. [BTP expands live facial recognition trials to London Underground](#item-tech-news-6) ⭐️ 7.0/10
7. [HyperSAE: Decoupled Poincaré Geometry for Sparse Autoencoders Cuts MSE and Dead Latents](#item-tech-news-7) ⭐️ 7.0/10
8. [Anthropic to Add AI Watermarks and C2PA Metadata to Claude Outputs](#item-tech-news-8) ⭐️ 7.0/10
9. [SK Hynix Restarts Dalian NAND Fab, Boosting Capacity 50%](#item-tech-news-9) ⭐️ 7.0/10

**Financial News**
1. [Nvidia&\#x27;s $500 billion AI financing plan faces GPU depreciation and China price-war risk](#item-finance-news-1) ⭐️ 8.0/10
2. [After-hours movers: Super Micro, CoreWeave, H&amp;R Block jump on earnings and guidance](#item-finance-news-2) ⭐️ 7.0/10
3. [CME plans first futures contracts for AI computing power](#item-finance-news-3) ⭐️ 7.0/10

---

## Technology News

<a id="item-tech-news-1"></a>
### [Hidden Reasoning Traces Extracted from Proprietary LLM APIs](https://stolen-thoughts.com/) ⭐️ 8.0/10

A technical write-up posted at stolen-thoughts.com demonstrates that hidden reasoning traces can be extracted from proprietary LLM APIs, despite providers&\#x27; efforts to keep chain-of-thought private. The reported methods include replaying a trace produced by a frontier model into a weaker sibling model and jailbreaking it, as well as disabling thinking and supplying a &\#x27;deep\_think&\#x27; tool that causes the model to emit internal CoT formatting. Community reports add variations: one user bypassed Codex&\#x27;s encryption of compaction with a two-sentence developer prompt, and another notes Opus 4.8 sometimes states AIME answers before deriving them while API summaries hide that distinction. The findings matter because they show current protections for hidden reasoning are fragile and raise legal and ethical questions about who controls model outputs.

hackernews · quantumgarbage · Aug 11, 13:22 · [Discussion](https://news.ycombinator.com/item?id=49257876)

**「Background」** Leading proprietary LLM providers now conceal models&\#x27; step-by-step reasoning, or chain-of-thought, to protect intellectual property and limit information leakage, sometimes encrypting reasoning traces shared across sessions and models. The reported technique takes a trace produced by a frontier model, replays it into a weaker sibling model, and jailbreaks the weaker model to extract the reasoning in plaintext, without directly jailbreaking the more capable model. This builds on earlier observations that replaying traces across models might expose hidden reasoning, and it demonstrates multiple attack vectors such as circumventing anti-distillation mechanisms and exposing private data or hidden prompts.

**「Impact」** API providers that hide reasoning traces face a concrete bypass risk: users can recover internal chain-of-thought through prompt or model-replay tricks, undermining current confidentiality measures and complicating terms-of-service enforcement. For developers and researchers using proprietary APIs, the demonstrated techniques provide a practical way to access hidden reasoning, while providers must treat trace confidentiality as an active security problem rather than a fixed guarantee.

**「Community discussion」** Commenters disagree on framing: one argues that extracting paid-for tokens is not &\#x27;stealing&\#x27; and that training on model outputs should be normal, while others report successful variations and question whether the behavior was intentionally allowed. A separate report confirms that API summaries can make Opus 4.8&\#x27;s reasoning look cleaner than it actually is.

<details><summary>References</summary>
<ul>
<li><a href="https://news.ycombinator.com/item?id=49257876">Stealing Reasoning Traces from Proprietary LLM APIs | Hacker News</a></li>
<li><a href="https://stolen-thoughts.com/paper.pdf">Stealing Reasoning Traces from Proprietary LLM APIs</a></li>
<li><a href="https://huggingface.co/papers/2608.09867">Paper page - Stealing Reasoning Traces from Proprietary LLM APIs</a></li>

</ul>
</details>

**Tags**: `#llm-security`, `#reasoning-traces`, `#ai-research`, `#proprietary-models`, `#model-extraction`

---

<a id="item-tech-news-2"></a>
### [Meta Releases Muse Glimmer, a 30B Apache-2.0 Agentic Model](https://simonwillison.net/2026/Aug/10/introducing-muse-glimmer/#atom-everything) ⭐️ 8.0/10

Meta released Muse Glimmer, a 30B open-weights vision-language model under the Apache 2.0 license, positioned for end-to-end agentic task completion, reliable tool use, and multi-step reasoning. Meta claims strong results on benchmarks including DeepSearch QA, MCP-Atlas, τ-Bench, and SWE-Bench. Simon Willison tested an 18.16 GB LM Studio quantized version, used it with his llm-coding-agent plugin against a fresh Datasette checkout, and confirmed it can describe images. He notes the 30B size suits machines with 32GB or more RAM, leaving room for other applications. The license is a step up from Meta&\#x27;s earlier Llama licenses.

rss · Simon Willison · Aug 10, 23:56

**「Background」** Muse Glimmer is Meta&\#x27;s new open-weights 30B model, released under Apache 2.0, a permissive license unlike the more restrictive Llama licenses. It is a vision-language model optimized for agentic workflows, tool use, and multi-step reasoning, making it relevant for local-model developers and AI practitioners.

**「Impact」** The Apache 2.0 license and 18.16 GB quantized size make Muse Glimmer immediately usable by local-model developers on 32GB+ RAM machines for agentic coding and vision tasks, though the benchmark claims are vendor-supplied and not independently validated.

**Tags**: `#AI`, `#open source`, `#Meta`, `#language models`, `#agentic AI`

---

<a id="item-tech-news-3"></a>
### [NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Routing](https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/) ⭐️ 7.0/10

NVIDIA announced Nemotron 3.5 Lightning, a family of small efficient models, alongside NeMo Switchyard, an open-source library that intelligently routes each request to the most capable and suitable model for the job. The release matters because it combines new small-model options with practical model-routing infrastructure, giving AI engineers a way to reduce reliance on very large models while maintaining quality. The announcement positions these tools for deployment with NVIDIA RTX and DGX systems, and community testing already shows Nemotron 3.5 Lightning running on Apple Silicon through MLX. The move reflects a broader industry push toward smaller, more efficient models rather than ever-larger parameter counts.

hackernews · droidjj · Aug 11, 19:35 · [Discussion](https://news.ycombinator.com/item?id=49263340)

**「Background」** NVIDIA&\#x27;s Nemotron 3.5 Lightning is a lightweight open model built on a 30B-parameter mixture-of-experts \(MoE\) architecture with only 3B active parameters, designed for fast, high-volume execution in long-running AI agents. NeMo Switchyard is an accompanying open-source library that routes each request to the most suitable model for the task, aiming to balance capability, cost, and efficiency across edge devices, PCs, workstations, data centers, and the cloud. The release reflects a broader industry push toward smaller, more efficient models and practical infrastructure for managing multiple models in production.

**「Impact」** Developers can now use NeMo Switchyard to route requests across models and run Nemotron 3.5 Lightning on Apple Silicon via MLX, though one user reported the 30B variant runs slowly on an older Mac.

**「Community Discussion」** Commenters welcomed the wave of small efficient models and one reported positive results running Nemotron 3.5 Lightning 30B on Apple Silicon with OpenCode, but others raised concerns about how routing affects prompt caching and criticized the benchmark graphs for omitting most Qwen models.

<details><summary>References</summary>
<ul>
<li><a href="https://blogs.nvidia.com/blog/nemotron-lightning-switchyard-rtx-dgx/">NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver ...</a></li>
<li><a href="https://x.com/nvidia/article/2087172614896988545">NVIDIA Nemotron 3.5 Lightning and NeMo Switchyard Deliver ...</a></li>
<li><a href="https://developer.nvidia.com/blog/nvidia-nemotron-3-5-lightning-delivers-fast-accurate-specialized-task-execution-for-long-running-agents/">NVIDIA Nemotron 3.5 Lightning Delivers Fast, Accurate ...</a></li>

</ul>
</details>

**Tags**: `#NVIDIA`, `#Nemotron`, `#LLM routing`, `#open source`, `#efficient models`

---

<a id="item-tech-news-4"></a>
### [Modular Ships Mojo 1.0 for AI Workloads](https://www.modular.com/blog/modular-26-5-mojo-1-0-is-here) ⭐️ 7.0/10

Modular has announced Mojo 1.0, a major milestone for its Python-compatible systems language aimed at high-performance AI and machine learning development. The release is significant for AI workloads, but it is tempered by ongoing concerns about the closed-source compiler and the project&\#x27;s revised stance on Python compatibility. Modular says it will progressively open-source more of Mojo and related MAX components, with a commitment to open-source the Mojo compiler and toolchain in 2026. The roadmap now states that Mojo may or may not evolve into a full superset of Python, and that it is acceptable if it does not.

hackernews · dayanruben · Aug 11, 16:56 · [Discussion](https://news.ycombinator.com/item?id=49261128)

**「Background」** Mojo is a systems programming language designed by Modular for high-performance AI and ML workloads, with syntax intended to be approachable for Python developers. It was originally positioned as a superset of Python, but Modular has since walked that goal back, stating that Mojo may or may not become a full Python superset. The project reached its 1.0 milestone after completing Phase 1 of its roadmap, which focused on stability for CPU and GPU programming; the standard library was open-sourced in 2024, and Modular has committed to open-sourcing the Mojo compiler and toolchain in 2026.

**「Impact」** Mojo 1.0 gives AI and ML developers a production-oriented, high-performance systems language with Python-like syntax, though adoption may be limited until the compiler is open-sourced in 2026 and the Python-superset question is resolved.

**「Community Discussion」** Commenters expressed confusion about Mojo&\#x27;s purpose and differentiation, skepticism about using a language with a closed-source compiler when Rust-backed Python libraries already provide performance, and concern about the walked-back Python-superset promise. Some remain hopeful, but many question why the compiler cannot be made source-available now rather than waiting until 2026.

<details><summary>References</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Mojo_%28programming_language%29">Mojo (programming language) - Wikipedia</a></li>
<li><a href="https://www.modular.com/blog/the-path-to-mojo-1-0">Modular: The path to Mojo 1.0</a></li>
<li><a href="https://forum.modular.com/t/mojo-1-0-is-here/3391">Mojo 🔥 1.0 is here! - Official Announcements - Modular</a></li>

</ul>
</details>

**Tags**: `#mojo`, `#programming-languages`, `#ai`, `#machine-learning`, `#open-source`

---

<a id="item-tech-news-5"></a>
### [Nvidia&\#x27;s Strategic Risks: CUDA Moat and AI Demand](https://stratechery.com/2026/nvidias-risky-business/) ⭐️ 7.0/10

Stratechery published an analysis of Nvidia&\#x27;s strategic position, arguing that its main risks are concentrated in AI compute demand and its entrenched CUDA software ecosystem. The piece examines whether Nvidia&\#x27;s hardware performance and software lock-in can sustain its market position as scrutiny grows over AI infrastructure spending. Community discussion on Hacker News highlights that CUDA is deeply embedded in ML research despite being widely criticized as a poor development environment, and that while demand for compute is real, expectations for its growth may be exaggerated. The analysis underscores that Nvidia&\#x27;s future depends on both continued demand growth and the durability of its software moat.

hackernews · jonbaer · Aug 11, 10:02 · [Discussion](https://news.ycombinator.com/item?id=49255710)

**「Background」** Nvidia&\#x27;s competitive position in AI infrastructure rests on more than its GPUs: the company combines hardware, networking, and a deep software stack, with CUDA developer lock-in widely considered a key moat that makes its AI chips harder to displace than raw specifications suggest. In its FY2026 annual report, Nvidia itself frames differentiation around this integrated combination of hardware, software ecosystem, networking, and developer tooling. The strategic debate centers on whether that moat will hold if AI compute demand growth slows or if competing software and hardware ecosystems gain traction.

**「Impact」** For AI infrastructure developers and investors, the analysis and debate point to a concrete risk: Nvidia&\#x27;s CUDA software moat is strong but technically unpopular, and the market&\#x27;s growth expectations for AI compute may be overstated.

**「Community Discussion」** Commenters broadly agree that CUDA&\#x27;s entrenchment in ML research is Nvidia&\#x27;s real advantage even though the CUDA C/C++ ecosystem is painful to use, but they split on whether AI compute demand growth justifies current investment theses. Some also note Nvidia&\#x27;s robotics efforts and its dominant position in the West as potential offsets to the risks.

<details><summary>References</summary>
<ul>
<li><a href="https://news.alphastreet.com/nvidias-cuda-lock-in-and-supply-scarcity-make-its-ai-chip-moat-harder-to-break-than-it-looks/">Nvidia’s CUDA Lock-In and Supply Scarcity Make Its AI Chip ...</a></li>
<li><a href="https://pitchgrade.com/research/ai-infrastructure-moat">NVIDIA&#x27;s AI Infrastructure Moat: Why CUDA, Supply Chain, and ...</a></li>

</ul>
</details>

**Tags**: `#Nvidia`, `#AI infrastructure`, `#CUDA`, `#semiconductors`, `#tech industry analysis`

---

<a id="item-tech-news-6"></a>
### [BTP expands live facial recognition trials to London Underground](https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/) ⭐️ 7.0/10

British Transport Police \(BTP\) is expanding its live facial recognition \(LFR\) trial into London Underground stations, according to an official police announcement. The deployment uses real-time face scanning of passengers as they move through the transit system, making it a notable real-world application of surveillance biometrics. The expansion matters because it intensifies ongoing debates about privacy, civil liberties, and the acceptability of mass biometric monitoring in public spaces. The announcement itself provides no technical performance data or evaluation criteria, and the trial&\#x27;s scope and duration are not specified in the available material.

hackernews · BlueBerry2001 · Aug 11, 09:40 · [Discussion](https://news.ycombinator.com/item?id=49255496)

**「Background」** Live Facial Recognition \(LFR\) technology uses cameras to scan faces in real time and compare them against a watchlist of individuals of interest, unlike retrospective facial recognition that searches recorded footage. British Transport Police began a pilot of LFR on 11 February 2026 at selected key transport hubs in London and is now expanding the trial into Transport for London \(TfL\) Underground stations. The expansion follows earlier deployments of the technology at railway stations and represents a broader move toward real-time biometric surveillance in the UK transport network.

**「Impact」** London Underground passengers will now be subject to live facial recognition scanning during the trial, meaning their biometric data may be captured and processed as they travel.

**「Community discussion」** Commenters are broadly skeptical: some argue that privacy loss is already baked into the system because contactless bank-card payments track travel, while others question what a successful trial would even look like and compare the surveillance to China. A few also dismiss the effort as ineffective given broader crime and sentencing concerns.

<details><summary>References</summary>
<ul>
<li><a href="https://www.btp.police.uk/news/btp/news/england/btp-expands-live-facial-recognition-lfr-trial-into-london-underground-stations/">BTP expands Live Facial Recognition (LFR) trial into London Underground stations | British Transport Police</a></li>
<li><a href="https://www.btp.police.uk/police-forces/british-transport-police/areas/about-us/about-us/facial-recognition-technology/">British Transport Police use of Live Facial Recognition Technology | British Transport Police</a></li>
<li><a href="https://www.mylondon.news/news/british-transport-police-trial-live-34435589">British Transport Police to trial live facial recognition cameras at London Tube stations - My London</a></li>

</ul>
</details>

**Tags**: `#facial recognition`, `#surveillance`, `#AI ethics`, `#privacy`, `#biometrics`

---

<a id="item-tech-news-7"></a>
### [HyperSAE: Decoupled Poincaré Geometry for Sparse Autoencoders Cuts MSE and Dead Latents](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/) ⭐️ 7.0/10

HyperSAE is a new open-source PyTorch library that applies decoupled Poincaré hyperbolic geometry to sparse autoencoders \(SAEs\) for mechanistic interpretability, available via pip install hypersae with code on GitHub and an accompanying paper. The forward pass remains entirely Euclidean, so causal steering stays a single vector addition and inference overhead is zero, while training projects dictionary weights into the Poincaré ball and uses an entailment cone loss to organize parent concepts near the origin and child concepts near the boundary. On Gemma-2-2B Layer 13 trained on 20M tokens of FineWeb-Edu with an NVIDIA L4, the reported gains over a flat SAE are reconstruction MSE 4.5724 to 4.1232 \(-9.8%\), CE loss recovery 75.5% to 78.9% \(+3.4 percentage points\), dead latents 3.8% to 0.2% \(-3.6 percentage points\), MMLU-Pro accuracy 16.11% to 16.26% \(+0.15 percentage points\), and GPQA Diamond unchanged at 100%. The library includes co-activation queue tracking, a TriPartite loss combining reconstruction, L1 sparsity, and entailment, and a single-class trainer interface. These results are self-reported in a Reddit announcement and have not yet received independent validation.

reddit · r/MachineLearning · /u/visha1v · Aug 11, 18:37 · [Discussion](https://www.reddit.com/r/MachineLearning/comments/1vlpyh2/hypersae_decoupled_poincar%C3%A9_geometry_for_sparse/)

**「Background」** Sparse autoencoders are used in mechanistic interpretability to decompose large language model activations into sparse, interpretable dictionary features. Standard SAEs embed dictionary atoms in Euclidean space, where volume grows polynomially, while the concepts LLMs learn often form branching hierarchies that expand exponentially, causing feature collisions, dead latents, and reconstruction degradation at large dictionary sizes. HyperSAE addresses this mismatch by decoupling training geometry from inference geometry: dictionary weights are projected into the Poincaré ball during training, where hyperbolic volume expands exponentially, while the forward pass remains Euclidean.

**「Impact」** For researchers and practitioners training SAEs for interpretability, HyperSAE offers a potentially low-cost training change that can reduce reconstruction error and dead latents with zero inference overhead, but the reported gains are self-reported and should be treated as preliminary until independently replicated.

**Tags**: `#sparse autoencoders`, `#mechanistic interpretability`, `#hyperbolic geometry`, `#PyTorch`, `#LLM interpretability`

---

<a id="item-tech-news-8"></a>
### [Anthropic to Add AI Watermarks and C2PA Metadata to Claude Outputs](https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content) ⭐️ 7.0/10

Anthropic has signed the EU AI Act Article 50\(2\) code of conduct on AI-generated content transparency. New Claude models released in the EU on or after August 2, 2026 will embed invisible machine-readable watermarks in generated text and add digitally signed provenance metadata using the C2PA standard in supported files, starting at release. The marking will apply globally across Claude&\#x27;s API, Claude, Claude Code, Claude Cowork, and Claude Tag products. Anthropic is also retrofitting older models released before that date and plans to publish technical details for detecting the markers. Detection of a marker only indicates content may have been processed by Claude, while the absence of a marker does not prove content was not AI-generated or processed.

telegram · zaihuapd · Aug 11, 03:06

**「Background」** The EU AI Act&\#x27;s Article 50\(2\) introduces transparency obligations for providers of AI systems that generate synthetic content, requiring machine-readable marking of outputs. C2PA is an open technical standard for embedding cryptographically verifiable provenance metadata in digital content. Anthropic&\#x27;s announcement is a compliance commitment ahead of the August 2026 applicability date.

**「Impact」** Developers and enterprises using Claude APIs and products will need to account for machine-readable watermarks and C2PA metadata in their output pipelines, especially for EU-facing releases from August 2026, and should not treat a missing marker as proof of human authorship.

**Tags**: `#Anthropic`, `#AI watermarking`, `#EU AI Act`, `#content provenance`, `#Claude API`

---

<a id="item-tech-news-9"></a>
### [SK Hynix Restarts Dalian NAND Fab, Boosting Capacity 50%](https://en.sedaily.com/finance/2026/08/11/sk-hynix-to-boost-china-nand-output-50-percent-with-dalian) ⭐️ 7.0/10

SK Hynix will restart construction of its second NAND flash fab in Dalian, China, increasing local capacity by about 50%, according to Seoul Economic Daily. The fab, which began construction four years ago and was halted during a memory downcycle, is now scheduled to start moving in equipment by the end of this year and reach mass production in the first half of next year. The new production line will add roughly 50,000 wafers per month of capacity. The move responds to surging enterprise SSD demand from AI data centers, with NAND prices up nearly tenfold over the past year. SK Hynix plans a dual-track strategy: Dalian will use mature technology for 100-layer NAND, while Cheongju focuses on 300-layer-plus high-stack products.

telegram · zaihuapd · Aug 11, 16:21

**「Background」** NAND flash is a non-volatile memory used in solid-state drives, and enterprise SSDs are a key storage component for AI data centers. SK Hynix had paused the Dalian expansion during a prolonged memory market downturn, but the recent AI-driven demand surge and sharp NAND price recovery have made restarting the project viable.

**「Impact」** For SK Hynix, the restart adds roughly 50,000 wafers per month of mature 100-layer NAND capacity for enterprise SSDs while the company keeps advanced 300-layer production in Cheongju, potentially helping ease AI-driven NAND supply pressure.

**Tags**: `#NAND`, `#SK Hynix`, `#semiconductor manufacturing`, `#AI infrastructure`, `#memory market`

---

## Financial News

<a id="item-finance-news-1"></a>
### [Nvidia&\#x27;s $500 billion AI financing plan faces GPU depreciation and China price-war risk](https://www.cnbc.com/2026/08/11/nvidia-ai-funding-jensen-huang-china-risk.html) ⭐️ 8.0/10

Nvidia announced agreements with BlackRock, Blackstone, Apollo, KKR, Brookfield and Goldman Sachs to build a $500 billion financing pipeline for AI data centers and GPU clusters. Analysts cited by CNBC say the plan&\#x27;s biggest risk is that Nvidia chips depreciate faster than expected, especially if Chinese chipmakers start a price war.

rss · CNBC Finance · Aug 11, 21:01

**「Background」** In asset-backed finance, lenders can repossess and sell the asset if a borrower defaults, so GPU resale value is central. Nvidia argues its chips are long-lived, revenue-generating infrastructure, but cutting-edge GPUs typically move to lower-margin work after a few years.

**「Impact」** According to analysts cited by CNBC, a Chinese price war could erode GPU collateral faster than debt terms, exposing investors to losses; borrowers are likely to be non-investment-grade AI startups and neoclouds.

**Tags**: `#Nvidia`, `#AI infrastructure`, `#asset-backed finance`, `#China chip competition`, `#GPU depreciation`

---

<a id="item-finance-news-2"></a>
### [After-hours movers: Super Micro, CoreWeave, H&amp;R Block jump on earnings and guidance](https://www.cnbc.com/2026/08/11/stocks-making-the-biggest-moves-after-hours-smci-crwv-hrb.html) ⭐️ 7.0/10

After hours, Super Micro Computer, CoreWeave, and H&amp;R Block rose after issuing stronger-than-expected results or guidance. Super Micro guided first-quarter adjusted EPS of $1.01-$1.10 versus the $0.76 consensus and revenue of $14.5-$15.5 billion versus $11.68 billion; CoreWeave reported second-quarter revenue of $2.58 billion, up 112% year over year, with adjusted operating income margin of 5% versus 2.7% expected; H&amp;R Block forecast fiscal 2027 adjusted EPS of $6.04-$6.24 and revenue of $4.11-$4.16 billion, above consensus.

rss · CNBC Finance · Aug 11, 21:18

**「Background」** The after-hours moves followed quarterly earnings reports and forward guidance released after the market close.

**Tags**: `#earnings`, `#guidance`, `#Super Micro Computer`, `#CoreWeave`, `#H&amp;R Block`

---

<a id="item-finance-news-3"></a>
### [CME plans first futures contracts for AI computing power](https://www.cnbc.com/2026/08/11/ai-computing-power-becomes-a-tradable-asset-class-as-cme-starts-futures.html) ⭐️ 7.0/10

CME Group plans to launch the first futures contracts tied to AI computing power on Oct. 5, pending regulatory approval, based on Silicon Data indexes that track hourly rental prices for Nvidia H100 and Blackwell B200 GPUs. Each contract would represent a month&\#x27;s rent for an H100, giving companies and investors a way to trade or hedge AI computing capacity.

rss · CNBC Finance · Aug 11, 18:09

**「Background」** CME Group and Silicon Data have announced plans to launch two compute futures contracts on October 5, 2026, pending regulatory approval. Futures are financial contracts that let buyers and sellers bet on or hedge against a future price; these would be tied to Silicon Data indexes tracking hourly rental prices for Nvidia&\#x27;s H100 and Blackwell B200 graphics processing units \(GPUs\), with each contract representing one month&\#x27;s rent for an H100.

<details><summary>References</summary>
<ul>
<li><a href="https://www.cnbc.com/2026/08/11/ai-computing-power-becomes-a-tradable-asset-class-as-cme-starts-futures.html">AI computing power is becoming a tradable asset class as CME launches futures contracts</a></li>
<li><a href="https://www.tradingview.com/news/prnewswire:7611ae98bb536:0-cme-group-and-silicon-data-to-launch-compute-futures-on-october-5-to-unlock-new-way-to-hedge-ai-risks/">CME Group and Silicon Data to Launch Compute Futures on October 5 to Unlock New Way to Hedge AI Risks — TradingView News</a></li>
<li><a href="https://ca.investing.com/news/stock-market-news/cme-group-to-launch-gpu-compute-futures-contracts-in-october-93CH-4792580">CME Group to launch GPU compute futures contracts in October By Investing.com</a></li>

</ul>
</details>

**Tags**: `#AI compute`, `#CME Group`, `#futures contracts`, `#GPU pricing`, `#AI infrastructure`

---