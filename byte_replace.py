import sys

try:
    with open('studyverse (1).html', 'rb') as f:
        content = f.read()
    
    target = b"Resources</button>"
    if target in content:
        print("Found target!")
        replacement = b"Resources</button>\n        <button class=\"btn btn-secondary\" onclick=\"window.location.href='/physics'\">Physics Room</button>"
        new_content = content.replace(target, replacement)
        with open('studyverse (1).html', 'wb') as f:
            f.write(new_content)
        print("Successfully replaced.")
    else:
        print("Target NOT FOUND in bytes")
        # Try to find part of it
        if b"Resources" in content:
            print("Found 'Resources' somewhere else:")
            idx = content.find(b"Resources")
            print(content[max(0, idx-50):idx+50])
        else:
            print("Could not find 'Resources' at all.")
except Exception as e:
    print(f"Error: {e}")
