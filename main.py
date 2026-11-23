# THE MONDAY LEDGER — Monday 23 November 2026 (news-image-20261123)
# Entry program: copy the bundled front-page image verbatim to /output/entry.png.
# Python 3.13, standard library only. No network, no timestamps, no rendering
# at run time, so run 1 and run 2 write byte-identical files.
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("OUTPUT_DIR", "/output")
DST = os.path.join(OUT_DIR, "entry.png")


def main() -> None:
    if not os.path.isfile(SRC):
        print("missing entry.png next to main.py", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, DST)
    print(f"wrote {DST} ({os.path.getsize(DST)} bytes)")


if __name__ == "__main__":
    main()
