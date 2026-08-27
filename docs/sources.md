# Sources and verification log

**Checked:** 2026-08-27  
**Currency:** prices are source-currency references; EU VAT, delivery, exchange
rates and regional stock are not included unless stated.

## Hardware

| Source | Claim used | Classification |
| --- | --- | --- |
| [NVIDIA RTX PRO 6000 datasheet](https://www.nvidia.com/content/dam/en-zz/Solutions/design-visualization/quadro-product-literature/workstation-datasheet-blackwell-rtx-pro6000-x-nvidia-us-3519208-web.pdf) | 96 GB memory and 1.8 TB/s bandwidth | Official specification |
| [NVIDIA DGX Spark announcement](https://nvidianews.nvidia.com/_gallery/download_pdf/68ed8e343d633239c8c8a051/) | 128 GB unified memory and compact local inference platform | Official announcement |
| [Apple Mac Studio announcement](https://www.apple.com/newsroom/2025/03/apple-unveils-new-mac-studio-the-most-powerful-mac-ever/) | M4 Max up to 128 GB unified memory | Official announcement |
| [Apple Mac Studio specifications](https://www.apple.com/mac-studio/specs/) | Memory and bandwidth configuration details | Official specification |
| [Apple US Mac Studio store](https://www.apple.com/us/shop/buy-mac/mac-studio/12-core-cpu-30-core-gpu-16-core-neural-engine-32gb-memory-512gb) | $1,999 base reference configuration | Official store price; US only |
| [Tom’s Hardware: DGX Spark price increase](https://www.tomshardware.com/desktops/mini-pcs/nvidia-dgx-spark-gets-18-percent-price-increase-as-memory-shortages-bite-founders-edition-now-usd4-699-up-from-usd3-999) | Reported increase from $3,999 to $4,699 | Secondary market report |
| [TechRadar: RTX 5090 street pricing](https://www.techradar.com/pro/nvidia-rtx-5090-gpus-are-so-expensive-that-intels-arc-pro-b70-is-now-a-genuine-bargain-for-ai) | Street price materially above $1,999 launch MSRP | Secondary market report |

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
