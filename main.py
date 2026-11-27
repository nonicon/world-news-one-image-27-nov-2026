#!/usr/bin/env python3
"""World News in One Image - 27 November 2026.

Entry program for the make.fun competition "Sum up 27 November's world
news in one image" (news-image-20261127).

The front page is painted at build time by render.py and shipped in this
repository as entry.png. This program only copies that file into the
output directory, so both grading runs produce identical bytes.

Standard library only, no network, deterministic.
"""

import os
import shutil
import sys


def run() -> int:
    """Copy the pre-rendered front page to the output directory."""
    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, "entry.png")
    if not os.path.isfile(source):
        print("entry.png is missing from the repository", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(source, os.path.join(out_dir, "entry.png"))
    return 0


if __name__ == "__main__":
    sys.exit(run())
