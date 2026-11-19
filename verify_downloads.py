"""
Checks the downloaded model files against Varun's copies.

    python verify_downloads.py --models C:\\models

BGE: every file must match the SHA-256 in PIN.json (BAAI/bge-small-en-v1.5 at revision 5c38ec7c).
Qwen GGUF: must be exactly 2,104,932,768 bytes and have the same SHA-256 as Varun's copy.
"""
import argparse
import hashlib
import json
import os
import shutil
import sys

GGUF_NAME = "qwen2.5-3b-instruct-q4_k_m.gguf"
GGUF_BYTES = 2104932768
GGUF_SHA256 = "626b4a6678b86442240e33df819e00132d3ba7dddfe1cdc4fbb18e0a9615c62d"  # Varun's copy


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", default=r"C:\models")
    args = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    ok = True

    bge = os.path.join(args.models, "bge-small-en-v1.5")
    pin_src = os.path.join(here, "bge-small-en-v1.5", "PIN.json")
    pin_dst = os.path.join(bge, "PIN.json")
    if os.path.isdir(bge) and not os.path.exists(pin_dst):
        shutil.copy(pin_src, pin_dst)
        print(f"[bge] copied PIN.json into {bge}")
    pin = json.load(open(pin_src, encoding="utf-8"))
    for rel, want in pin["files"].items():
        p = os.path.join(bge, rel)
        if not os.path.exists(p):
            print(f"[bge] MISSING {rel}"); ok = False; continue
        got = sha256(p)
        print(f"[bge] {'ok  ' if got == want else 'BAD '} {rel}")
        ok &= got == want

    g = os.path.join(args.models, GGUF_NAME)
    if not os.path.exists(g):
        print(f"[qwen] MISSING {g}"); ok = False
    else:
        size = os.path.getsize(g)
        print(f"[qwen] size {size} ({'ok' if size == GGUF_BYTES else 'DIFFERENT from Varun: ' + str(GGUF_BYTES)})")
        ok &= size == GGUF_BYTES
        digest = sha256(g)
        same = digest == GGUF_SHA256
        print(f"[qwen] sha256 {digest} ({'matches Varun' if same else 'DIFFERENT from Varun'})")
        ok &= same
    print("ALL OK" if ok else "SOMETHING DIFFERS, do not start the runs")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
