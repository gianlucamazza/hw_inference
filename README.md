# Local inference for small teams

Decision and procurement documentation for a 3–6 person team in Italy/EU
evaluating local AI inference for coding assistants, internal RAG and lightweight
automation.

## Recommendation in one paragraph

Start with one NVIDIA workstation in the 32 GB VRAM class for fast daily
development, currently budgeting roughly €6,300–€8,800 for a complete EU build.
Keep a cloud GPU available for burst workloads, and buy into the 96–128 GB
memory class only after a pilot proves that model size or concurrency is the
bottleneck. Use Ollama/Open WebUI for simple internal experimentation and vLLM
behind an authenticated gateway when the service becomes shared.

## Documents

- [Decision report](docs/decision-report.md) — hardware, software, pricing and
  purchase criteria.
- [Sources and verification log](docs/sources.md) — URLs, dates and evidence
  classification.

Prices and availability are volatile. This snapshot was checked on 2026-08-27;
all purchase decisions should re-check the linked source pages and obtain a
seller quote.
