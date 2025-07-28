#!/usr/bin/env python3
from pathlib import Path
import subprocess
import os

ROOT = Path(__file__).resolve().parents[3]
COVERAGE_DIR = ROOT / "coverage"
COVERAGE_DIR.mkdir(exist_ok=True)
ENV = os.environ.copy()
ENV["PYTHONPATH"] = str(ROOT / "backend")

cmd = [
    "pytest",
    "backend/app/tests",
    "--import-mode=importlib",
    "--cov=backend",
    "--cov-report=term-missing",
    f"--cov-report=xml:{COVERAGE_DIR / 'coverage.xml'}",
    f"--cov-report=html:{COVERAGE_DIR / 'html'}",
    "--cov-fail-under=60",
]
raise SystemExit(subprocess.call(cmd, cwd=ROOT, env=ENV))
