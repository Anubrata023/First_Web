import sys

try:
    with open('studyverse (1).html', 'rb') as f:
        content = f.read()
    
    # Try to find 'quick-actions' to confirm presence
    if b'quick-actions' in content:
        print("Found quick-actions in binary!")
    else:
        print("quick-actions NOT found in binary!")

    old_str = b"Resources</button>"
    new_str = b"Resources</button>\n        <button class=\"btn btn-secondary\" onclick=\"window.location.href='/physics'\" style=\"background:var(--accent);color:var(--bg);border:none;\">\xe2\x9a\x9b\xef\xb8\x8f Physics Room</button>"
    
    if old_str in content:
        content = content.replace(old_str, new_str, 1)
        with open('studyverse (1).html', 'wb') as f:
            f.write(content)
        print('Replaced successfully')
    else:
        print('old_str not found!')
except Exception as e:
    print(f"Error: {e}")
