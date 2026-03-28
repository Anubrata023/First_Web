import sys

try:
    content = open('studyverse (1).html', 'r', encoding='utf-8').read()
    old_str = "<button class=\"btn btn-secondary\" onclick=\"window.location.href='/resources'\">Resources</button>"
    new_str = "<button class=\"btn btn-secondary\" onclick=\"window.location.href='/resources'\">Resources</button>\n        <button class=\"btn btn-secondary\" onclick=\"window.location.href='/physics'\" style=\"background:var(--accent);color:var(--bg);border:none;\">⚛️ Physics Room</button>"
    
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open('studyverse (1).html', 'w', encoding='utf-8') as f:
            f.write(content)
        print('Replaced successfully')
    else:
        print('String not found!')
except Exception as e:
    print(f"Error: {e}")
