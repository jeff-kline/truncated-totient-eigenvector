#!/usr/bin/env python3
"""Build paper/main.pdf twice from the authoritative paper/main.tex source."""

from __future__ import annotations

import hashlib
import os
from pathlib import Path
import shutil
import subprocess


ROOT = Path(__file__).resolve().parents[1]
TEX = ROOT / "paper" / "main.tex"
PDF = ROOT / "paper" / "main.pdf"
BUILD_ROOT = ROOT / "tmp" / "pdfs"
PDFLATEX = Path("/opt/local/bin/pdflatex")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def run_build(build_dir: Path) -> Path:
    if build_dir.exists():
        shutil.rmtree(build_dir)
    build_dir.mkdir(parents=True)
    env = os.environ.copy()
    env.update(
        {
            "SOURCE_DATE_EPOCH": "1789430400",
            "FORCE_SOURCE_DATE": "1",
            "TZ": "UTC",
        }
    )
    command = [
        str(PDFLATEX),
        "-interaction=nonstopmode",
        "-halt-on-error",
        f"-output-directory={build_dir}",
        str(TEX),
    ]
    for _ in range(2):
        subprocess.run(command, cwd=ROOT, env=env, check=True)
    return build_dir / "main.pdf"


def main() -> None:
    if not PDFLATEX.exists():
        raise SystemExit(f"missing required executable: {PDFLATEX}")
    first = run_build(BUILD_ROOT / "build-a")
    second = run_build(BUILD_ROOT / "build-b")
    first_hash = sha256(first)
    second_hash = sha256(second)
    if first_hash != second_hash or first.read_bytes() != second.read_bytes():
        raise SystemExit(
            "nondeterministic PDF build: " f"{first_hash} != {second_hash}"
        )
    shutil.copyfile(first, PDF)
    print(f"deterministic PDF: {PDF.relative_to(ROOT)}")
    print(f"sha256: {first_hash}")
    print(f"bytes: {PDF.stat().st_size}")


if __name__ == "__main__":
    main()
