import glob, re

files = glob.glob('*.html')
for f in files:
    if f == 'studyverse (1).html': continue
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    og = content
    if 'id="sb-friends"' not in content and 'id="sb-doubts"' in content:
        # Use regex substitution with re.DOTALL to match the multi-line doubt span
        content = re.sub(
            r'(<div[^>]*id="sb-doubts"[^>]*>.*?</div>)', 
            r'\1\n  <div class="sb-icon-btn" id="sb-friends" onclick="window.location.href=\'/study-with-friends\'" title="Study with Friends">👥</div>', 
            content, 
            flags=re.DOTALL
        )
    
    if content != og:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Added sb-friends to', f)

print('Done frontend updates.')
