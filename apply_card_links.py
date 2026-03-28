import sys
import re

file_path = r'c:\Users\anubr\Downloads\FastWeb\FastWeb\studyverse (1).html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = {
    "onclick=\"toast('👥','Opening Community...')\"": "onclick=\"window.location.href='community-doubts.html'\"",
    "onclick=\"toast('🤝','Opening Study With Friends...')\"": "onclick=\"window.location.href='study-with-friends.html'\"",
    "onclick=\"toast('⚛️','Opening Physics...')\"": "onclick=\"window.location.href='subject-study-page (1).html'\"",
    "onclick=\"toast('🔍','Browser resources...')\"": "onclick=\"window.location.href='studyverse-resources (3).html'\""
}

for old, new_str in replacements.items():
    content = content.replace(old, new_str)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print('Replacements done.')
