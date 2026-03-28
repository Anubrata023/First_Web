import sys

try:
    with open('studyverse (1).html', 'rb') as f:
        content = f.read()

    text = content.decode('utf-16')
    idx = text.find('quick-actions')
    if idx != -1:
        print("FOUND using UTF-16!")
        print(repr(text[idx:idx+200]))
        
        # Perform replacement
        target = '''<button class="btn btn-secondary" onclick="window.location.href='/resources'">Resources</button>'''
        if target in text:
            replacement = target + '''\n        <button class="btn btn-secondary" onclick="window.location.href='/physics'">Physics Room</button>'''
            text = text.replace(target, replacement)
            
            with open('studyverse (1).html', 'wb') as f:
                f.write(text.encode('utf-16'))
            print("Successfully replaced and saved!")
        else:
            print("Target string not found in UTF-16 text.")
    else:
        print("NOT FOUND using UTF-16 either.")
except Exception as e:
    print(f"Error: {e}")
