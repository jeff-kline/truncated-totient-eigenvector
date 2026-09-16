#!/usr/bin/env python3
"""Check frozen bytes and reproduce the integer certificate without overwriting it.

This verifies reproducibility and integrity, not correctness of the mathematics.
Run from the repository root with any Python 3 interpreter:
    python3 code/verify_reproduction.py
"""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import tempfile


def require(condition, message):
    # Deliberately not an assert: this wrapper also rejects errors under -O.
    if not condition:
        raise RuntimeError(message)


def main():
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root/'audit/frozen-artifacts.json').read_text())
    for name, expected in manifest['sha256'].items():
        actual = hashlib.sha256((root/name).read_bytes()).hexdigest()
        require(actual == expected, 'Changed frozen artifact: '+name)
    expected = json.loads((root/'results/scalar-certificate.json').read_text())
    with tempfile.TemporaryDirectory(prefix='truncated-totient-reproduction-') as folder:
        work = Path(folder)
        (work/'code').mkdir()
        (work/'results').mkdir()
        script = work/'code/certify_scalar.py'
        script.write_bytes((root/'code/certify_scalar.py').read_bytes())
        # -E ignores PYTHONOPTIMIZE, and no -O is passed. The proof assertions run.
        run = subprocess.run([sys.executable, '-E', str(script)], cwd=work,
                             capture_output=True, text=True, timeout=120)
        require(run.returncode == 0, 'Certificate execution failed: '+run.stderr)
        actual = json.loads((work/'results/scalar-certificate.json').read_text())
        observed_cpu = actual.pop('process_cpu_seconds')
        expected.pop('process_cpu_seconds')
        require(actual == expected, 'Reproduced certificate differs from frozen result')
    print(json.dumps({'status': 'FROZEN_CERTIFICATE_REPRODUCED',
                      'hashed_artifacts': len(manifest['sha256']),
                      'endpoint_checks': actual['endpoint_checks'],
                      'half_interval_checks': actual['half_interval_checks'],
                      'process_cpu_seconds': observed_cpu,
                      'scope': 'integrity and reproducibility of the frozen certificate; not a proof of correctness'},
                     indent=2))


if __name__ == '__main__':
    main()
