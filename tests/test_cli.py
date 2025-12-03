import ast
import subprocess
import sys
from pathlib import Path

root_path = Path(__file__).resolve().parent / "assets"


def test_running_as_module_outputs_redactions():
    pdf_path = root_path / "rectangles_yes.pdf"

    completed = subprocess.run(
        [sys.executable, "-m", "xray", str(pdf_path)],
        check=True,
        capture_output=True,
        text=True,
    )

    stdout = completed.stdout.strip()
    redactions = ast.literal_eval(stdout)

    assert 1 in redactions
    assert len(redactions[1]) == 3
    assert completed.stderr == ""
