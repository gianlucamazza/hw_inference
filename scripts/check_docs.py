#!/usr/bin/env python3
"""Check documentation links and required release metadata."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = (ROOT / "README.md", ROOT / "docs" / "decision-report.md", ROOT / "docs" / "sources.md")
URL_RE = re.compile(r"https?://[^)\s>]+")
LOCAL_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
REPORT_REQUIRED = ("# Decision report", "Snapshot date:", "## Procurement BOMs")


def check_local_links(errors: list[str]) -> None:
    for path in DOCS:
        text = path.read_text(encoding="utf-8")
        for target in LOCAL_RE.findall(text):
            if target.startswith(("http://", "https://", "#")):
                continue
            target_path = (path.parent / target.split("#", 1)[0]).resolve()
            if not target_path.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing local link target {target}")


def check_required_content(errors: list[str]) -> None:
    report = (ROOT / "docs" / "decision-report.md").read_text(encoding="utf-8")
    for marker in REPORT_REQUIRED:
        if marker not in report:
            errors.append(f"decision-report.md: missing required marker {marker!r}")
    sources = (ROOT / "docs" / "sources.md").read_text(encoding="utf-8")
    if "# Sources and verification log" not in sources:
        errors.append("sources.md: missing sources heading")


def check_external_links(warnings: list[str], errors: list[str]) -> None:
    urls = sorted({url.rstrip(".,") for path in DOCS for url in URL_RE.findall(path.read_text(encoding="utf-8"))})
    for url in urls:
        request = urllib.request.Request(url, headers={"User-Agent": "hw_inference-docs-check/1.0"})
        try:
            with urllib.request.urlopen(request, timeout=15) as response:
                status = response.status
        except urllib.error.HTTPError as exc:
            status = exc.code
        except (urllib.error.URLError, TimeoutError) as exc:
            warnings.append(f"external link not checked ({url}): {exc}")
            continue

        # Commercial sites and security gateways commonly reject CI user agents.
        if status in (403, 429) or status >= 500:
            warnings.append(f"external link returned {status} ({url})")
        elif status >= 400:
            errors.append(f"external link returned {status} ({url})")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--online", action="store_true", help="check external HTTP links")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    missing = [path for path in DOCS if not path.exists()]
    errors.extend(f"missing documentation file {path.relative_to(ROOT)}" for path in missing)
    if not missing:
        check_local_links(errors)
        check_required_content(errors)
        if args.online:
            check_external_links(warnings, errors)

    for warning in warnings:
        print(f"warning: {warning}", file=sys.stderr)
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if errors:
        return 1
    print(f"documentation checks passed ({len(DOCS)} files, {len(warnings)} warnings)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
