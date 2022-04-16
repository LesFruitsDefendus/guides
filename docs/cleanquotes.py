#!/usr/bin/env python3
# Useful to cleanup text copy/pasted from PDFs

quotes_to_clean = (
    ("”", '"'),
    ("’", "'"),
    ("“", '"'),
    ("”", '"'),
    ("“", '"'),
    ("”", '"'),
    ("•", "-"),
)

if __name__ == "__main__":
    import sys
    result = sys.stdin.read()
    for v,r in quotes_to_clean:
        result = result.replace(v, r)
    print(result)
