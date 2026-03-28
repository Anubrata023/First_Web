import re

try:
    with open('studyverse (1).html', 'rb') as f:
        content = f.read()

    pattern = re.compile(br'(<button[^>]+onclick="window\.location\.href=\'/resources\'"[^>]*>Resources</button>)')
    match = pattern.search(content)
    
    if match:
        print("Match found!")
        new_str = match.group(1) + b'\n        <button class="btn btn-secondary" onclick="window.location.href=\'/physics\'" style="background:var(--accent);color:var(--bg);border:none;">\xe2\x9a\x9b\xef\xb8\x8f Physics Room</button>'
        content = content[:match.start()] + new_str + content[match.end():]
        with open('studyverse (1).html', 'wb') as f:
            f.write(content)
        print("Replaced!")
    else:
        print("No match found for regex either!")
except Exception as e:
    print(f"Error: {e}")
