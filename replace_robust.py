import sys

try:
    with open('studyverse (1).html', 'r', encoding='utf-8', errors='ignore') as f:
        lines = f.readlines()

    replaced = False
    for i, line in enumerate(lines):
        if "window.location.href='/resources'" in line and "Resources</button>" in line:
            print("Found target line at", i)
            # Indentation
            indent = len(line) - len(line.lstrip())
            space = line[:indent]
            physics_button = space + '<button class="btn btn-secondary" onclick="window.location.href=\'/physics\'">Physics Room</button>\n'
            lines.insert(i + 1, physics_button)
            replaced = True
            break
            
    if replaced:
        with open('studyverse (1).html', 'w', encoding='utf-8') as f:
            f.writelines(lines)
        print("Successfully replaced and saved!")
    else:
        print("Target line not found.")
except Exception as e:
    print(f"Error: {e}")
