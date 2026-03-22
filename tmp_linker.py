import re, glob

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    if re.search(r'class="[^"]*sidebar', content):
        print(f, 'has sidebar')
