import os

ENTRY = "status: lid closed. cursor still blinking where you left it, mid-sentence, waiting for words that aren't coming."

OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUT_PATH = OUT_DIR + "/entry.txt"


def main():
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
