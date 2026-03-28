import sys

try:
    with open('studyverse (1).html', 'r', encoding='latin-1') as f:
        content = f.read()

    target = "Resources</button>"
    if target in content:
        print("Found target using latin-1!")
        
        replacement = "Resources</button>\n        <button class=\"btn btn-secondary\" onclick=\"window.location.href='/physics'\">Physics Room</button>"
        new_content = content.replace(target, replacement)
        
        with open('studyverse (1).html', 'w', encoding='latin-1') as f:
            f.write(new_content)
        print("Successfully replaced and saved!")
    else:
        print("NOT FOUND using latin-1")
except Exception as e:
    print(f"Error: {e}")
