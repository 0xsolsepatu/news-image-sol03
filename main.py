#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.

Copies the pre-rendered entry.png (next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), byte for byte,
so two runs write identical bytes. Standard library only; no network.

The image is a 1024x1024 'THE WORLD IN ONE DAY' newspaper front page
summing up Tuesday 24 November 2026's world news: masthead + giant
date, a 6-number stat strip, 3 illustrated lead panels (KADIZ jets,
the Houthi drone strike on Riyadh's PIF tower, the Huawei verdict),
a 9-story grid, a 16-item tail list (28 stories in all, each verified
against a named source), a DATE CHECK box of stories rejected as not
24 November, a world map, and a footer. Rebuilt 25 November 2026 from
the 'Global Terminal' dashboard (round 3 rank 7,903/14,561): the old
entry had no pictures, only 10 stories, and 8 of its 10 stories were
dated 20-23 November, not 24 November.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _is_png(path):
    try:
        with open(path, "rb") as f:
            return f.read(len(PNG_MAGIC)) == PNG_MAGIC
    except OSError:
        return False


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    if not os.path.isfile(SRC):
        print(f"error: source image not found: {SRC}", file=sys.stderr)
        return 1
    if not _is_png(SRC):
        print(f"error: source is not a PNG file: {SRC}", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    if os.path.getsize(dst) != os.path.getsize(SRC):
        print(f"error: copy size mismatch: {dst}", file=sys.stderr)
        return 1
    if _sha256(dst) != _sha256(SRC):
        print(f"error: copy verification failed: {dst}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {_sha256(dst)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
