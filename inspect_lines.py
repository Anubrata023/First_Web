with open('studyverse (1).html', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines):
    if "Let's Study" in line:
        print(f"Line {i}:", repr(line))
        if i + 1 < len(lines):
            print(f"Line {i+1}:", repr(lines[i+1]))
