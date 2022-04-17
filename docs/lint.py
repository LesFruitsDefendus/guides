#!/usr/bin/env python3
# Useful to cleanup text copy/pasted from PDFs,
# Custom linter to remove annoying charaters.

import argparse
import pathlib
import itertools

quotes_to_clean = (
    ("’", "'"),
    ("“", '"'),
    ("”", '"'),
    ("•", "-"),
    ("➔", "-"),
)

def get_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument('--path')
    parser.add_argument('--exit-code', action='store_true',
            help='Do not write the files and exit with non-zero status if lint fails.')
    return parser

if __name__ == "__main__":
    parser = get_parser()
    args = parser.parse_args()

    source_path = args.path or pathlib.Path(__file__).parent.joinpath('source')
    assert isinstance(source_path, pathlib.Path)
    assert source_path.exists()

    exit_code = 0

    for entry in itertools.chain(source_path.glob('**/*.md'), 
                                 source_path.glob('**/*.po')):
        content = ''
        with entry.open('r') as f:
            content = f.read()
        
        cleaned_content = content
        for v,r in quotes_to_clean:
            cleaned_content = cleaned_content.replace(v, r)
        
        if cleaned_content != content:
            print(f"{entry} contains unallowed characters.")
            if args.exit_code:
                exit_code = 5
            else:
                print("fixing it...")
                with entry.open('w') as f:
                    f.write(cleaned_content)
    exit(exit_code)
