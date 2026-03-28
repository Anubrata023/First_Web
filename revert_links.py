import glob
import re

files = glob.glob('*.html')

replacements = {
    "'/dashboard'": "'studyverse (1).html'",
    "'/resources'": "'studyverse-resources (3).html'",
    "'/doubts'": "'community-doubts (2).html'",
    "'/study-with-friends'": "'study-with-friends.html'",
    "'/physics'": "'subject-study-page (1).html'",
    "'/sakura'": "'sakura-studyverse (6).html'",
    '"/dashboard"': '"studyverse (1).html"',
    '"/resources"': '"studyverse-resources (3).html"',
    '"/doubts"': '"community-doubts (2).html"',
    '"/study-with-friends"': '"study-with-friends.html"',
    '"/physics"': '"subject-study-page (1).html"',
    '"/sakura"': '"sakura-studyverse (6).html"'
}

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    og = content
    for old, new in replacements.items():
        content = content.replace(f"href={old}", f"href={new}")
        content = content.replace(f"href={old}".replace("href=","href = "), f"href={new}")
        
    if content != og:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

print("Done reverting to .html files!")
