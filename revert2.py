import glob

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
        # Just blind replace these exact string literals inside the file
        content = content.replace(old, new)
        
    if content != og:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated {f}")

print("Done blind replace!")
