import sys

try:
    with open('studyverse (1).html', 'rb') as f:
        text = f.read().decode('utf-8', errors='ignore')
    
    idx = text.find('quick-actions')
    if idx != -1:
        print("FOUND:")
        print(repr(text[idx:idx+300]))
    else:
        print("NOT FOUND")
except Exception as e:
    print(f"Error: {e}")
