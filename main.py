import os
from pathlib import Path


LINE = "My smart fridge photographs my cheese like it died suspiciously."


def main():
    if not 1 <= len(LINE) <= 160 or not LINE.strip():
        raise ValueError("Entry must contain 1–160 characters of nonblank text")
    if LINE.splitlines() != [LINE]:
        raise ValueError("Entry must be exactly one line")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
