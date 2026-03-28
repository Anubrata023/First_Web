import glob, re

print('Applying custom user mappings...')

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    og = content
    
    # 1. 'Book tab' (sb-resources) -> Physics
    content = re.sub(r'id="sb-resources"\s*onclick="[^"]*"(.*?)', r'id="sb-resources" onclick="window.location.href=\'/physics\'"\1', content)
    
    # 2. 'Community' (sb-doubts) -> Doubts directly (already applied but let's ensure)
    # Wait, the regex in previous attempt was:
    # re.sub(r'id=\"sb-doubts\"\s*onclick=\"[^\"]*\"(.*?)', r'id=\"sb-doubts\" onclick=\"window.location.href=\'/doubts\'\"\1', content)
    # The (.*?) matches non-greedy until the end of string... which is the whole file if re.DOTALL is not used, but without DOTALL it stops at newline!
    # Let's just use string replace for safety.
    # What does sb-resources look like now?
    # <div class="sb-icon-btn" id="sb-resources" onclick="window.location.href='/resources'" title="Study">📚</div>
    content = re.sub(r'(id="sb-resources"\s*onclick=")window\.location\.href=\'/resources\'(")', r'\1window.location.href=\'/physics\'\2', content)
    
    # 3. What does sb-doubts look like now?
    # <div class="sb-icon-btn" id="sb-doubts" onclick="openPopup('doubts',this)" title="Doubts & Q&A">❓<span class="sb-count">3</span></div>
    content = re.sub(r'(id="sb-doubts"\s*onclick=")openPopup\(\'doubts\',this\)(")', r'\1window.location.href=\'/doubts\'\2', content)
    
    # 4. Add Study With Friends!
    # If sb-friends doesn't exist, add it
    if 'id="sb-friends"' not in content and 'id="sb-doubts"' in content:
        # Find the line with sb-doubts and append sb-friends
        content = re.sub(r'(<div[^>]*id="sb-doubts"[^>]*>.*?</div>)', r'\1\n  <div class="sb-icon-btn" id="sb-friends" onclick="window.location.href=\'/study-with-friends\'" title="Study with Friends">👥</div>', content)

    # 5. In physics page, link Study Resources 'View all ->' to /resources
    if f == 'subject-study-page (1).html':
        content = content.replace("onclick=\"toast('📚','Viewing all resources...')\"", "onclick=\"window.location.href='/resources'\"")

    # 6. In dashboard, link 'Physics' card to /physics explicitly if needed (it already says 'Opening Physics...')
    if f == 'studyverse (1).html':
        content = content.replace("toast('⚛️','Opening Physics...')", "window.location.href='/physics'")
    
    if content != og:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated links in', f)

print('Done.')
