"""Five Seconds to Explain the Glass — make.fun entry.

Writes the house cat's one-sentence excuse to /output/entry.txt.
Deterministic: the same sentence, byte-identical, on every run.
"""

import os

SENTENCE = (
    "That glass was squatting dead center in my sunbeam, "
    "so really I just evicted a trespasser with excellent paw technique."
)


def main() -> None:
    # Gate check, mirroring the competition gate: 1-200 chars, one sentence.
    assert 1 <= len(SENTENCE) <= 200, "sentence must be 1-200 chars"
    assert SENTENCE.count(".") == 1 and SENTENCE.endswith("."), (
        "sentence must be exactly one sentence"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)
    print(SENTENCE)


if __name__ == "__main__":
    main()
