import sys

try:
    with open('c:/Users/anubr/Downloads/FastWeb/FastWeb/studyverse (1).html', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    with open('c:/Users/anubr/Downloads/FastWeb/FastWeb/debug_output.txt', 'w', encoding='utf-8') as out:
        for i, line in enumerate(lines[1325:1345]):
            out.write(f"Line {i+1326}: {repr(line)}\n")
    print("Successfully wrote to debug_output.txt")
except Exception as e:
    print(f"Error: {e}")
