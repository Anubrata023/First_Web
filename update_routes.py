import glob, re

replacements = {
    r'studyverse \(1\)\.html': '/dashboard',
    r'studyverse-resources \(3\)\.html': '/resources',
    r'community-doubts \(2\)\.html': '/doubts',
    r'study-with-friends\.html': '/study-with-friends',
    r'subject-study-page \(1\)\.html': '/physics',
    r'sakura-studyverse \(6\)\.html': '/sakura'
}

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
        
    og = content
    
    # We replace inside window.location.href='...'
    # Example: window.location.href='studyverse-resources (3).html' -> window.location.href='/resources'
    for old, new in replacements.items():
        # Using regex to target exact strings inside quotes
        # E.g. href="studyverse (1).html" or href='studyverse (1).html'
        pattern1 = r'(href|window\.location\.href)\s*=\s*(["\'])' + old + r'\2'
        content = re.sub(pattern1, r'\1=\2' + new + r'\2', content)

    if content != og:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated links in', f)
print('Done frontend route updates.')
