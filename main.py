import os

ENTRY = "I killed the Wi-Fi right at the climax because for once, I wanted to be the cliffhanger."

# The gate allows 1 to 200 characters, one line, not only whitespace.
assert 1 <= len(ENTRY) <= 200, len(ENTRY)
assert ENTRY.strip() and "\n" not in ENTRY

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY + "\n")
