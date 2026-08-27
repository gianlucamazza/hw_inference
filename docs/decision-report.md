# Decision report: local inference for small teams

**Scope:** Italy/EU · 3–6 users · coding assistants, internal RAG and light
automation  
**Snapshot date:** 2026-08-27  
**Status:** quote-ready shortlist + procurement appendix
**Initial capex ceiling:** €9,000 IVA inclusa, excluding subscriptions and
financing

## Executive summary

For a small team, memory capacity is the first purchase constraint:

- 16 GB VRAM is a practical entry point for 7B–14B quantized models.
- 24–32 GB VRAM is the best general-purpose class for fast coding and RAG.
- 96–128 GB of GPU or unified memory is the practical threshold for 70B-class
  quantized models and larger contexts.

The recommended first step is one 32 GB NVIDIA workstation plus a cloud fallback.
It gives the team fast CUDA-compatible inference without committing to an
enterprise server. A 96 GB professional GPU or 128 GB unified-memory system is
justified when the pilot demonstrates a sustained need for larger models,
multiple concurrent users or a strict data-residency requirement.

## Workload assumptions

The report assumes:

- 3–6 people, with normally one or two active inference sessions at once;
- code completion, codebase questions, pull-request assistance and document RAG;
- open-weight models served through an internal HTTP API;
- no model training in the initial phase;
- sensitive source code and internal documents should remain local by default.

The pilot must replace these assumptions with measured concurrency, context
length, requests/day and acceptable latency before a large hardware purchase.

## Hardware options

| Tier | Reference configuration | Suitable workload | Decision signal |
| --- | --- | --- | --- |
| Entry | RTX 5060 Ti 16 GB, 64 GB RAM, 1–2 TB NVMe | 7B–14B quantized models, embeddings, light RAG | Cheapest useful local pilot |
| Recommended | RTX 5090 32 GB, 128 GB RAM, 2–4 TB NVMe | Fast coding assistant, 7B–30B models, image workloads | Best speed/flexibility balance |
| Capacity | RTX PRO 6000 Blackwell 96 GB, 128–256 GB RAM | 70B quantized models, larger context, more concurrency | Memory is the proven bottleneck |
| Compact capacity | DGX Spark 128 GB or Mac Studio M5 Ultra | Larger quantized models, quiet low-power workstation | Compare availability and software ecosystem separately |

### Hardware evidence and pricing

- NVIDIA lists 96 GB GDDR7 and approximately 1.8 TB/s bandwidth for the RTX PRO
  6000 Blackwell Workstation Edition. NVIDIA does not expose a simple consumer
  checkout price; obtain an EU OEM quote.
- NVIDIA’s Italian marketplace lists DGX Spark at €4,800, with 128 GB unified
  memory and 4 TB NVMe, but marked it out of stock at the snapshot date. An EU
  price comparison showed €5,699 excluding delivery; treat €4,800–€5,700 as a
  volatile consumer reference range.
- Apple launched Mac Studio M5 Max from €3,049 and M5 Ultra from €6,699 in
  Italy. The M5 Ultra line supports up to 512 GB unified memory; delivery was
  announced from 22 September 2026, so availability is a procurement risk.
- Italian price comparison showed RTX 5090 32 GB offers roughly from €4,240 to
  €5,230 including VAT, depending on model and seller. Do not approve a purchase
  using the $1,999 launch MSRP alone.
- European price comparison showed RTX PRO 6000 Blackwell 96 GB offers from
  approximately €14,890 including shipping, with other offers above €16,000.
  This is a retail signal, not an OEM workstation quote.

## Procurement BOMs

The following ranges are planning estimates in EUR, generally VAT-inclusive,
based on the linked component observations and a quality workstation build. They
exclude monitor, software subscriptions, labor, VAT recovery and financing.

| BOM | GPU / accelerator | Supporting hardware | Estimated capex | Best use |
| --- | ---: | ---: | ---: | --- |
| Entry pilot | €680–€1,055 | €900–€1,500 | **€1,600–€2,600** | 7B–14B, one active user |
| Recommended | €4,240–€5,230 | €2,000–€3,500 | **€6,300–€8,800** | Fast coding/RAG, 1–2 active users |
| Capacity | €14,890–€16,100 GPU; €4,000–€7,000 workstation | included | **€19,000–€23,000** | 70B, larger context, concurrency |
| Compact | €4,800–€5,700 DGX Spark; €6,699+ M5 Ultra | integrated | **€4,900–€7,000** | Quiet, memory-heavy local inference |

The entry GPU range uses current Italian 16 GB RTX 5060 Ti/5070 Ti observations.
The recommended and capacity ranges use current Italian/EU price-comparison
signals. Confirm seller, warranty, delivery and invoice treatment before ordering.

### Component-level BOM

Prices below are planning ranges. GPU and complete-system prices are observed
market signals; supporting components are explicitly marked as estimates until a
seller quote is obtained.

| BOM | GPU / accelerator | CPU + motherboard | RAM | NVMe | PSU + case + cooling | UPS/network | Total |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Entry pilot | €680–€1,055 observed | €350–€550 stima | €120–€220 stima | €80–€150 stima | €250–€380 stima | €120–€250 stima | **€1,600–€2,600** |
| Recommended | €4,240–€5,230 observed | €700–€1,100 stima | €350–€650 stima | €180–€350 stima | €700–€1,200 stima | €150–€300 stima | **€6,300–€8,800** |
| Capacity | €14,890–€16,100 observed | €4,000–€7,000 stima workstation | included | included | included | included | **€19,000–€23,000** |
| DGX Spark | €4,800–€5,700 observed | integrated | integrated | integrated | integrated | €100–€250 stima | **€4,900–€6,000** |
| M5 Ultra | €6,699+ official starting price | integrated | integrated | integrated | integrated | €100–€250 stima | **€6,800+** |

All observed retail prices are treated as VAT-inclusive unless the source says
otherwise. Supporting-component estimates are not purchase quotes. The final
order must record seller, SKU, delivery date, warranty, VAT treatment and total
landed cost.

### Price and evidence status

| Option | Price basis | IVA/shipping | Availability at snapshot | Evidence confidence | Procurement action |
| --- | --- | --- | --- | --- | --- |
| RTX 5060 Ti 16 GB | Italian comparison from ~€680 | VAT included in displayed offer | Offer-dependent | Medium | Request one complete-system quote |
| RTX 5090 32 GB | Italian comparison ~€4,240–€5,230 | VAT included; shipping varies | Offer-dependent | Medium | Do not buy without warranty and power check |
| RTX PRO 6000 96 GB | EU comparison from ~€14,890 | Shipping included in lowest displayed offer | Offers listed | Medium | Obtain OEM workstation quote |
| DGX Spark | NVIDIA Italy €4,800 | Official listing | Out of stock at check | High for spec, medium for price | Confirm authorized-channel delivery |
| Mac Studio M5 Ultra | Apple Italy from €6,699 | Official Italian price | Delivery announced from 22 Sep 2026 | High for starting price | Price the required memory/storage tier |

The evidence confidence describes the purchase signal, not the technical
capability: an official specification can be high-confidence while a live
retailer price remains volatile.

### Quote-ready shortlist under €9,000

These are procurement targets, not purchase quotes. A configuration is eligible
only when one EU seller confirms the complete landed price, warranty, delivery
date and power requirements in writing.

| Candidate | Target configuration | Planning ceiling | Role in decision | Hard gate |
| --- | --- | ---: | --- | --- |
| **A — CUDA performance** | RTX 5090 32 GB, 128 GB RAM, 2–4 TB NVMe, sustained-load case/cooling, 1,200–1,600 W PSU | **€9,000** | Default choice for fast 7B–32B coding/RAG | Quote must include validated PSU/connectors, thermals and 2-year warranty |
| **B — lower-cost pilot** | RTX 5060 Ti 16 GB, 64 GB RAM, 1–2 TB NVMe, quality PSU/cooling | **€2,600** | Time-boxed validation for 7B–14B models | Do not approve if long context or two active users is required |
| **C — compact alternative** | DGX Spark 128 GB, 4 TB NVMe, UPS/network allowance | **€6,000** | Quiet, memory-heavy alternative when CUDA throughput is secondary | Confirm stock, delivery and supported runtime before approval |

Candidate A is the recommended quote request. Candidate B is the fallback when
the team is validating demand rather than buying for daily performance. Candidate
C is not a drop-in CUDA workstation equivalent and must pass a software-stack
compatibility check.

#### Purchase gate

Approve a quote only if all of the following are true:

- total landed cost is at or below €9,000 IVA inclusa;
- the exact GPU SKU and memory capacity are stated;
- the seller states warranty, return terms and delivery date;
- PSU, power connector, chassis clearance and sustained cooling are documented;
- the quote includes 128 GB system RAM and 2–4 TB NVMe for Candidate A;
- no claim relies on launch MSRP or an unavailable listing;
- the supplier accepts an invoice suitable for the team’s VAT treatment.

Reject or defer the purchase if the quote is incomplete, the GPU is unavailable,
the total exceeds the ceiling, or the team cannot operate the system safely at
sustained load.

#### Quote request template

Request the following fields for each candidate: seller and legal entity, SKU
and manufacturer part number, GPU VRAM, CPU and motherboard, RAM capacity and
ECC status, NVMe model/capacity, PSU model and connector, case dimensions and
cooling, operating system, warranty and RMA location, delivery date, shipping,
VAT treatment, total landed price, and confirmation of Ubuntu/CUDA support.

### Weighted decision matrix

The default weighting reflects coding + RAG for a small team: performance 25%,
memory 20%, price 20%, software ecosystem 15%, power 10%, reliability 5% and
expandability 5%. Scores are 1–5 and are directional, not benchmark results.

| Option | Performance | Memory | Price | Software | Power | Reliability | Expandability | Weighted score / 100 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| RTX 5060 Ti | 2 | 2 | 5 | 5 | 4 | 3 | 4 | 68 |
| RTX 5090 | 5 | 3 | 2 | 5 | 2 | 3 | 4 | **71** |
| RTX PRO 6000 | 4 | 5 | 1 | 5 | 2 | 5 | 3 | **71** |
| DGX Spark | 2 | 5 | 3 | 4 | 5 | 4 | 1 | 69 |
| Mac Studio M5 Ultra | 3 | 5 | 2 | 3 | 5 | 4 | 1 | 67 |

The score does not override hard gates. RTX 5090 wins the speed-oriented pilot;
RTX PRO 6000 wins when 70B capacity or sustained multi-user service is a hard
requirement. DGX Spark and Mac Studio are alternatives when unified memory,
noise and power matter more than CUDA throughput.

### Final selection guide

| Choose | If | Do not choose if | Next action |
| --- | --- | --- | --- |
| RTX 5060 Ti | Budget pilot and models stay below 14B | Long context or more than one active user is required | Buy only as a time-boxed pilot |
| RTX 5090 workstation | Fast coding/RAG and CUDA are priorities | 70B must run in one GPU or 24/7 thermals cannot be managed | Request a complete EU build quote |
| RTX PRO 6000 | 70B, context headroom or concurrency is proven | Workload is occasional or budget is below ~€19k | Request OEM quote and support terms |
| DGX Spark | Compact, quiet 128 GB system is preferred | Stock is unavailable or high decode speed is required | Confirm authorized-channel delivery |
| Mac Studio M5 Ultra | Unified memory, quiet operation and Apple ecosystem matter | CUDA-only tooling or modular GPU upgrades are required | Price exact memory/storage configuration |

### Recommended workstation bill of materials

For the first pilot, target the **Recommended** BOM:

- one RTX 5090-class 32 GB NVIDIA GPU;
- 128 GB system RAM;
- 2–4 TB NVMe, with a separate backup target;
- 1,200–1,600 W quality PSU where required by the selected GPU;
- a case and cooling solution designed for sustained load;
- wired Ethernet and a UPS if the service is shared internally.

Choose the **Entry** BOM when the pilot is exploratory and models remain below
14B. Choose **Capacity** only when 70B or concurrency is a measured requirement.
Choose **Compact** when low noise, unified memory and low idle power outweigh
CUDA throughput.

## Model-fit and memory planning

| Model class | Practical memory target | Expected fit |
| --- | ---: | --- |
| 7B–14B quantized | 8–16 GB plus runtime/context headroom | Entry and all larger tiers |
| 20B–32B quantized | 20–32 GB plus context headroom | Recommended and larger tiers |
| 70B Q4-class | 45–60 GB plus context/KV cache | Capacity and Compact |
| 70B with long context or concurrency | 80–128 GB | Capacity preferred |

These are sizing bands, not performance guarantees. Quantization format,
context length, multimodal components, KV-cache settings and batching can move
the requirement substantially. Keep at least 15–25% memory headroom; do not size
to the model file alone.

## Three-year energy TCO

For a comparable planning basis, use €0.30/kWh and 8 hours/day, 30 days/month.
The table uses estimated whole-system load, not GPU TDP. It excludes labor,
maintenance, cooling overhead, financing and resale value.

| BOM | Planning load | Energy / month | Energy / 36 months | Capex + energy |
| --- | ---: | ---: | ---: | ---: |
| Entry | 400 W | ~€29 | ~€350 | **€1,950–€2,950** |
| Recommended | 850 W | ~€61 | ~€735 | **€6,935–€9,435** |
| Capacity | 1,100 W | ~€79 | ~€950 | **€19,950–€23,950** |
| DGX Spark | 100 W | ~€7 | ~€87 | **€4,887–€5,787** |
| M5 Ultra | 150 W | ~€11 | ~€130 | **€6,829+** |

Formula: `watts × hours/month ÷ 1,000 × electricity price`. Replace the tariff
with the team’s actual business rate before using this table for approval.

The exact GPU model should be selected from an EU quote after checking physical
dimensions, power connectors, noise and warranty. Do not buy a second GPU before
measuring whether the workload is memory-bound, throughput-bound or
concurrency-bound.

## Buy versus rent

Runpod currently lists an RTX 5090 reference rate around $0.99/hour in its
server-cost guide. That is approximately $238/month at 8 hours/day or
$713/month continuously, before storage, egress and tax. Actual availability,
region and spot/reserved terms can change the result. A local 5090 BOM at
€6,300–€8,800 therefore needs sustained utilization and privacy value to beat
cloud on total cost; the break-even point cannot be declared without a real
usage profile and exchange/tax treatment.

Use cloud GPU for:

- short benchmark campaigns;
- occasional 70B or multimodal workloads;
- temporary capacity while hardware is unavailable;
- burst traffic that does not justify a permanent GPU.

Use local hardware when:

- code or documents must not leave the organization;
- usage is sustained and predictable;
- low network latency matters;
- the team needs a stable internal endpoint;
- the operational burden of GPU hosting is acceptable.

Do not claim local cost superiority without including depreciation, support,
electricity, cooling, downtime and engineering time. Cloud remains attractive
for low or irregular utilization.

## Software architecture

### Pilot stack

1. **Ollama** for quick model installation and a local REST API.
2. **Open WebUI** for a shared browser interface, document interaction and
   connections to local OpenAI-compatible endpoints.
3. **vLLM** when two or more users need a production-like shared endpoint,
   batching or higher throughput.
4. A small gateway in front of the model server for authentication, rate
   limits, request logging, model allowlists and spend/usage controls.

The gateway should expose only the models approved for internal use. Keep the
runtime API OpenAI-compatible so coding tools can switch between local and cloud
providers without giving users a second workflow or a second manual action.
Cloud should be an escalation path selected by policy, not an extra button in
the user interface.

### Coding tools

The relevant distinction is not only model quality but also where the agent runs
and what it may do. Inline completion, interactive agent mode, terminal agents
and asynchronous cloud agents have different privacy, approval and cost
profiles.

| Tool | Current public team price | Execution surface | Strength | Main caution |
| --- | ---: | --- | --- | --- |
| GitHub Copilot Business | $19/user/month | IDE, CLI, GitHub and cloud agent | Low-friction GitHub workflow with organization controls | AI credits and agent usage must be budgeted; verify current self-serve availability |
| GitHub Copilot Enterprise | $39/user/month or contract terms | Enterprise GitHub and agent surfaces | Repository context, policy and enterprise integration | Requires the wider GitHub Enterprise setup |
| Cursor Teams Standard | $40/user/month | AI-first IDE, cloud agents and Bugbot | Strong interactive agent workflow and team analytics | Included usage is per seat; on-demand usage is extra |
| Cursor Teams Premium | $120/user/month | Same surfaces with 5x Standard usage | Suitable for identified agent power users | Do not assign to every developer by default |
| Claude Team | $20/user/month annual, $25 monthly | Claude Code terminal/IDE plus Claude apps | Strong terminal-oriented agent workflow and SSO | Usage limits apply; API/programmatic usage has separate cost rules |
| Codex / GPT-5.3-Codex API | Token-priced; GPT-5.3-Codex $1.75/$14 per 1M input/output tokens | Codex and Responses API | Coding-optimized agent model with function calling | API cost is usage-based and not equivalent to a seat subscription |
| Local OpenAI-compatible stack | Hardware + operations | Ollama/vLLM behind gateway and local IDE client | Data stays inside the declared boundary and provider can be changed | Team must operate updates, auth, model policy, logs and recovery |

For a small team, start with one managed coding-tool standard and a local model
endpoint for sensitive code or documents. Avoid paying premium seats for every
developer; identify power users from usage data first. Treat cloud agents as a
separate data-flow and cost decision, even when bundled into the same product.

### Model catalog for the pilot

The following catalog separates vendor declarations from measurements. Context
length and parameter count do not predict coding quality or usable throughput by
themselves; every candidate must be tested with the selected runtime,
quantization, repository and concurrency.

| Model | Deployment | Declared profile | Practical pilot role | Gate before adoption |
| --- | --- | --- | --- | --- |
| Qwen3-Coder-30B-A3B-Instruct | Local, open weights | 30.5B total / 3.3B active; 256K native context; Apache-2.0 | First local agent candidate for a 32 GB GPU | Validate tool calling, quantized memory use and repo-level fixes |
| Qwen3-Coder-Next | Local, open weights | 80B total / 3B active; 256K context; Apache-2.0 | Capacity-oriented agent candidate for larger-memory systems | Validate actual quantization, runtime support and long-context latency |
| GPT-5.3-Codex | Cloud/API | Coding-optimized; 400K context; function calling; $1.75/$14 per 1M input/output tokens | Managed quality reference for agentic coding | Track tokens, tool calls, data policy and monthly spend |
| Claude models through Claude Code | Cloud/API | Model and limits depend on plan or API route | Managed terminal-agent comparison | Record selected model, plan, usage limit and API/subscription path |

The local baseline should begin with Qwen3-Coder-30B-A3B-Instruct on the
recommended GPU. Qwen3-Coder-Next belongs in the larger-memory or cloud phase;
its low active-parameter count does not remove the memory cost of its total
weights and KV cache.

### Governance and tool permissions

Every managed or local agent must have a declared policy for:

- file read/write scope and excluded paths such as secrets, credentials and production data;
- terminal commands requiring approval versus commands allowed automatically;
- network access, domains, package installation and external tool calls;
- Git operations, branch protection and whether an agent may create or merge a PR;
- model/provider routing, fallback behavior and whether prompts may leave the local boundary;
- token, seat, cloud-GPU and on-demand usage budgets;
- audit logs, retention, deletion and incident response.

The default policy is read-only inspection first, explicit approval for writes,
network and destructive commands, no production credentials, and mandatory human
review before merge or deployment. A tool being available through an IDE or MCP
does not make it approved for unrestricted use.

## Pilot and acceptance criteria

Run a two-week pilot with representative repositories and documents before
committing to a capacity-tier purchase. Record:

- first-token latency and tokens/second;
- peak VRAM/unified-memory use;
- prompt-processing time for long context;
- concurrent users before latency becomes unacceptable;
- retrieval hit rate and answer quality on a fixed evaluation set;
- daily requests and estimated monthly hardware/cloud cost;
- failure recovery after model reload, process restart and GPU exhaustion;
- data-retention, access-control and audit behaviour.

Store one dated result sheet per candidate with model name, quantization,
context length, concurrency, prompt size, first-token latency, decode rate,
peak memory and pass/fail against the agreed threshold. Until that sheet exists,
the matrix scores remain directional and cannot justify the Capacity tier.

The pilot is successful when:

- the selected local model meets the agreed quality threshold;
- two concurrent users remain within the agreed latency target;
- no sensitive prompt or retrieved document leaves the local boundary unless
  explicitly allowed by policy;
- the measured utilization supports the buy/rent decision;
- the team can reproduce setup and rollback from documented instructions.

## Risks and review triggers

- **Memory shortage or price inflation:** recheck EU stock and quotations before
  purchase; do not rely on launch MSRP.
- **Model/runtime incompatibility:** pin tested model and runtime versions and
  keep an OpenAI-compatible API contract.
- **One-user monopolization:** enforce per-user limits and queueing at the
  gateway.
- **False privacy assurance:** verify logs, telemetry, backups and cloud
  escalation behavior, not just where the GPU is located.
- **Underused hardware:** review utilization after 30 days; move bursty loads
  to cloud if the local machine is mostly idle.

Reassess after the pilot, after 30 days of operation, and whenever model size,
user count or concurrency doubles.
