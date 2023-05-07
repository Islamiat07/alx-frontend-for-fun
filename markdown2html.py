#!/usr/bin/python3
"""
A script that converts Markdown to HTML.
"""

import sys
import markdown

if len(sys.argv) < 3:
    print("Usage: ./markdown2html.py <inputfile> <outputfile>", file=sys.stderr)
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

try:
    with open(input_file, 'r') as f:
        text = f.read()
except FileNotFoundError:
    print(f"Missing {input_file}", file=sys.stderr)
    sys.exit(1)

html = markdown.markdown(text)

with open(output_file, 'w') as f:
    f.write(html)

sys.exit(0)
