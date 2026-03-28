import sys

try:
    with open('c:/Users/anubr/Downloads/FastWeb/FastWeb/studyverse (1).html', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    print("Total lines:", len(lines))
    print("Lines 1329 to 1340:")
    for i, line in enumerate(lines[1329:1340]):
        print(f"Line {i+1330}:", repr(line))
except Exception as e:
    print(f"Error: {e}")
