import re
import glob

# Mapping of text/titles to their actual HTML filenames
link_mappings = {
    'Dashboard': 'studyverse (1).html',
    'Resources': 'studyverse-resources (3).html',
    'All Subjects': 'studyverse-resources (3).html',
    'Doubts & Q&A': 'community-doubts (2).html',
    'My Doubts': 'community-doubts (2).html',
    'Study with Friends': 'study-with-friends.html',
    'Physics': 'subject-study-page (1).html'
}

files = glob.glob('*.html')

for f in files:
    with open(f, 'r', encoding='utf-8', errors='ignore') as file:
        content = file.read()
    
    original_content = content
    
    # 1. Update popup items (e.g., <div class="sbp-item"...>Dashboard</div>)
    for title, html_file in link_mappings.items():
        # Match <div ... onclick="...nav(this)..."...>...title...</div>
        # Replace onclick with window.location.href
        pattern1 = r'(<div[^>]*class="sbp-item[^>]*onclick=")(?:closePopup\(\);)?(?:nav\(this\);?|toast\([^)]+\);?)*([^"]*)(".*?>)(?:<span[^>]*>.*?</span>)?\s*' + re.escape(title) + r'\s*(?:<span[^>]*>.*?</span>)?\s*(</div>)'
        
        def repl1(m):
            return f"{m.group(1)}window.location.href='{html_file}'{m.group(3)}<span class=\"sbp-item-icon\"></span>{title}{m.group(4)}"
            
        # We will use a simpler replace strategy:
        # Just find the lines containing the title and an onclick, then replace the onclick content.
        
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if 'class="sbp-item' in line or 'class="sb-item' in line or 'class="sb-sub-item' in line or 'class="sbp-sub-item' in line:
            for title, html_file in link_mappings.items():
                if f'>{title}<' in line or title in line:
                    # Replace onclick="..." with onclick="window.location.href='...'"
                    line = re.sub(r'onclick="[^"]*"', f'onclick="window.location.href=\'{html_file}\'"', line)
                    lines[i] = line
                    
    content = '\n'.join(lines)
    
    if content != original_content:
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"Updated links in {f}")

print("Done.")
