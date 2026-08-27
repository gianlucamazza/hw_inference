# Sources and verification log

**Checked:** 2026-08-27  
**Currency:** prices are source-currency references; VAT and delivery are stated
where the source exposes them. Retail prices and availability are volatile.

## Hardware

| Source | Claim used | Classification |
| --- | --- | --- |
| [NVIDIA RTX PRO 6000 datasheet](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/workstation-datasheet-blackwell-rtx-pro6000-x-nvidia-us-3519208-web.pdf) | 96 GB memory and 1.8 TB/s bandwidth | Official specification |
| [NVIDIA DGX Spark announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/68ed8e343d633239c8c8a051/) | 128 GB unified memory and compact local inference platform | Official announcement |
| [NVIDIA DGX Spark Italy marketplace](https://marketplace.nvidia.com/it-it/enterprise/personal-ai-supercomputers/dgx-spark/) | €4,800, 128 GB unified memory, 4 TB NVMe; out of stock at check | Official Italian marketplace; volatile |
| [Idealo Italy DGX Spark](https://www.idealo.it/confronta-prezzi/208146353/nvidia-dgx-spark-founders-edition-940-54242-0005-000.html) | €5,699 reference offer, delivery excluded | EU price comparison; volatile |
| [Apple Mac Studio M5 announcement Italy](https://images.apple.com/it/newsroom/2026/08/apple-introduces-new-mac-studio-with-m5-max-and-m5-ultra/) | M5 Max from €3,049; M5 Ultra from €6,699; delivery from 22 September | Official announcement |
| [Trovaprezzi RTX 5060 Ti 16 GB](https://www.trovaprezzi.it/prezzo_schede-grafiche_nvidia_geforce_rtx_5060_ti_16gb.aspx) | Italian 16 GB offers from approximately €680 | Italian price comparison; volatile |
| [Trovaprezzi RTX 5070 Ti 16 GB](https://www.trovaprezzi.it/prezzo_schede-grafiche_rtx_5070_ti_16.aspx) | Italian 16 GB offers from approximately €1,017 | Italian price comparison; volatile |
| [Trovaprezzi RTX 5090 32 GB](https://www.trovaprezzi.it/prezzo_schede-grafiche_rtx_5090_32.aspx) | Italian offers observed roughly €4,240–€5,230 including VAT | Italian price comparison; volatile |
| [Idealo Italy RTX 5090](https://www.idealo.it/cat/16073F106540549/schede-video.html) | Current comparison confirms 32 GB class and seller-dependent offers | EU price comparison; volatile |
| [GEB Informatica RTX 5090 Gaming OC](https://www.gebinformatica.it/prodotto/gigabyte-rtx-5090-gaming-oc-32gb?action=genpdf&id=578575) | Example single-seller listing observed at €3,798.99 IVA inclusa | Seller listing; availability and price volatile |
| [Idealo Germany RTX PRO 6000 Blackwell](https://www.idealo.de/preisvergleich/OffersOfProduct/206328547_-rtx-pro-6000-blackwell-nvidia.html) | EU offers from approximately €14,890 including shipping | EU price comparison; volatile |

## Cloud

| Source | Claim used | Classification |
| --- | --- | --- |
| [Runpod GPU pricing](https://www.runpod.io/pricing) | GPU Pods, Serverless and Clusters are separate products | Official pricing page |
| [Runpod server-cost guide](https://www.runpod.io/articles/guides/ai-server-cost) | RTX 5090 reference rate around $0.99/hour | Provider guide; volatile |

## Runtime and interfaces

| Source | Claim used | Classification |
| --- | --- | --- |
| [vLLM OpenAI-compatible server](https://docs.vllm.ai/en/latest/serving/online_serving/openai_compatible_server/) | OpenAI-compatible completions/chat HTTP server | Official documentation |
| [Ollama documentation](https://docs.ollama.com/) | Local model management and integration surface | Official documentation |
| [Open WebUI provider connection](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible/) | Connections to OpenAI-compatible local providers | Official documentation |
| [OpenAI open-weight models](https://help.openai.com/en/articles/11870455-openai-open-weight-models) | gpt-oss weights are not served through OpenAI API or ChatGPT | Official help documentation |

## Coding tools

| Source | Claim used | Classification |
| --- | --- | --- |
| [GitHub Copilot plans](https://docs.github.com/en/copilot/get-started/plans) | Business $19/user/month; Enterprise $39/user/month; included credits | Official documentation |
| [GitHub Copilot billing](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-billing) | AI credits are usage-based; 1 credit equals $0.01 | Official documentation |
| [Cursor team pricing](https://prod.cursor.com/docs/account/teams/pricing) | Standard $40/user/month; Premium $120/user/month | Official documentation |
| [Cursor pricing update](https://cursor.com/blog/teams-pricing-june-2026) | Annual prices $32/$96 and Premium 5× allowance | Official product announcement |
| [OpenAI Codex pricing](https://chatgpt.com/codex/pricing/) | Codex is included in ChatGPT plan families, with plan-specific limits | Official pricing page |
| [OpenAI flexible pricing for teams](https://openai.com/index/codex-flexible-pricing-for-teams/) | Business annual price announced at $20/user/month and usage-based options | Official product announcement; policy may change |

## Evidence policy

- Official specifications establish capabilities, not street price or real-world
  throughput.
- Provider pricing is a point-in-time observation and must be rechecked before
  procurement.
- Secondary reports are used only to flag market movement, not to certify a
  purchase price.
- No throughput number is treated as an acceptance result until measured on the
  target models, context lengths and concurrency.
- BOM totals are planning ranges, not purchase orders. A quote is required for
  the final seller, warranty, delivery date and VAT treatment.
- Energy TCO uses an explicit €0.30/kWh assumption and must be recalculated with
  the team’s actual business tariff.
