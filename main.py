"""One-line office joke entry for make.fun.

Writes a single fresh office joke to /output/entry.txt.
Python 3.13, no network, deterministic output.
"""

import os

ENTRY = (
    "We had a meeting to decide if the last meeting could have "
    "been an email, and the answer was a follow-up meeting."
)

OUTPUT_DIR = "/output"


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clear only the contents of /output, never the directory itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isdir(path):
            import shutil

            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
