lines = open('studyverse (1).html', 'r', encoding='utf-8').readlines()
for i, line in enumerate(lines):
    if "Resources</button>" in line:
        print(f"Line {i}: {repr(line)}")
