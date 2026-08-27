# Decision report: local inference for small teams

**Scope:** Italy/EU · 3–6 users · coding assistants, internal RAG and light
automation  
**Snapshot date:** 2026-08-27  
**Status:** market assessment + procurement appendix

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
| Compact capacity | DGX Spark 128 GB or Mac Studio M5 Ultra | Larger quantized models, quiet low-power workstation | Capacity matters more than token speed |

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
| Recommended | €4,240–€5,230 | €2,000–€3,500 | **€6,200–€8,700** | Fast coding/RAG, 1–2 active users |
| Capacity | €14,890–€16,100 GPU; €4,000–€7,000 workstation | included | **€19,000–€23,000** | 70B, larger context, concurrency |
| Compact | €4,800–€5,700 DGX Spark; €6,699+ M5 Ultra | integrated | **€4,900–€7,000** | Quiet, memory-heavy local inference |

The entry GPU range uses current Italian 16 GB RTX 5060 Ti/5070 Ti observations.
The recommended and capacity ranges use current Italian/EU price-comparison
signals. Confirm seller, warranty, delivery and invoice treatment before ordering.

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
€6,200–€8,700 therefore needs sustained utilization and privacy value to beat
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

| Tool | Current public team price | Strength | Main caution |
| --- | ---: | --- | --- |
| GitHub Copilot Business | $19/user/month | Low-friction IDE/GitHub integration | Advanced usage consumes AI credits |
| GitHub Copilot Enterprise | $39/user/month | Enterprise controls and repository context | Requires the wider GitHub enterprise setup |
| Cursor Teams Standard | $40/user/month monthly, $32 annual | AI-first IDE, team administration and analytics | Usage beyond included allowance is metered |
| Cursor Teams Premium | $120/user/month monthly, $96 annual | Five times the Standard usage allowance | Expensive for every seat; reserve for power users |
| ChatGPT Business with Codex | Codex included; annual Business price announced at $20/user/month | Managed agentic coding and collaboration | Limits and additional-credit rules must be checked before rollout |

For a small team, start with one managed coding-tool standard and a local model
endpoint for sensitive code or documents. Avoid paying premium seats for every
developer; identify power users from usage data first.

## Pilot and acceptance criteria

Run a two-week pilot with representative repositories and documents. Record:

- first-token latency and tokens/second;
- peak VRAM/unified-memory use;
- prompt-processing time for long context;
- concurrent users before latency becomes unacceptable;
- retrieval hit rate and answer quality on a fixed evaluation set;
- daily requests and estimated monthly hardware/cloud cost;
- failure recovery after model reload, process restart and GPU exhaustion;
- data-retention, access-control and audit behaviour.

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
