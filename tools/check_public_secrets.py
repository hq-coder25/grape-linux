#!/usr/bin/env python3
"""Conservative public-repository credential check. Never prints matched secrets."""
from pathlib import Path
import re
import subprocess
import sys

PATTERNS = {
    "GitHub token": re.compile(rb"gh[pousr]_[A-Za-z0-9_]{30,}"),
    "GitHub fine-grained token": re.compile(rb"github_pat_[A-Za-z0-9_]{40,}"),
    "AWS access key": re.compile(rb"AKIA[0-9A-Z]{16}"),
    "Private key header": re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "Slack token": re.compile(rb"xox[baprs]-[A-Za-z0-9-]{20,}"),
}
MAX_BYTES = 2_000_000
EXCLUDE = (".git/",)
def main():
    raw = subprocess.check_output(["git", "ls-files", "-z"])
    files = [Path(x.decode("utf-8", "surrogateescape")) for x in raw.split(b"\0") if x]
    found = 0
    scanned = 0
    for path in files:
        if any(str(path).startswith(p) for p in EXCLUDE) or not path.is_file():
            continue
        if path.stat().st_size > MAX_BYTES:
            continue
        data = path.read_bytes()
        if b"\0" in data[:4096]:
            continue
        scanned += 1
        for name, regex in PATTERNS.items():
            for match in regex.finditer(data):
                line = data.count(b"\n", 0, match.start()) + 1
                print(f"Potential {name} at {path}:{line} (value redacted)")
                found += 1
    print(f"Checked {scanned} tracked text files; potential secret matches: {found}")
    return 1 if found else 0
if __name__ == "__main__":
    sys.exit(main())
