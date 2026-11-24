#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261124.

Copies the pre-rendered entry.png (next to this file) to
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png), byte for byte,
so two runs write identical bytes. Standard library only; no network.

The image is a 1024x1024 'Global Terminal' dashboard summing up Tuesday
24 November 2026's world news: Nvidia reinstating Jensen Huang with
shares up 31%; US sanctions on Iran-linked exchanges and Tehran's $290B
demand; Russian jets entering South Korea's air defence zone with a
3-minute island alert; Ukraine's claim it sank the Russian corvette
Merkury off Libya; NATO sending AWACS to Poland after Russian missiles
landed there; the Cikande candy factory fire (24 dead, ~30 missing);
the Russian drone strike on Dymer (11 killed); the Israeli strike in
Gaza that killed 3 including UNRWA staff; Mexico capturing 'El Chapo
Isidro'; and Virginia and Oregon suing SpaceX over Grok sexual
deepfakes.
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
    if _sha256(dst) != _sha256(SRC):
        print(f"error: copy verification failed: {dst}", file=sys.stderr)
        return 1
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes, sha256 {_sha256(dst)})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
