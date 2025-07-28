import subprocess
from pathlib import Path

# Bagimliliklarin guvenlik taramasini yapar
ROOT = Path(__file__).resolve().parents[3]
REQUIREMENTS = ROOT / "backend" / "requirements.txt"


def test_pip_audit_clean():
    """pip-audit ile acik taramasi"""
    result = subprocess.run([
        "pip-audit",
        "-r",
        str(REQUIREMENTS),
        "--no-deps",
    ], capture_output=True, text=True)
    assert result.returncode == 0, f"Guvenlik acigi bulundu:\n{result.stdout}{result.stderr}"

