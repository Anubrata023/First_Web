import glob
import re

print('Starting script...')

# Read the modern NotebookLM & Modal code from studyverse-resources (3).html
try:
    with open('studyverse-resources (3).html', 'r', encoding='utf-8') as f:
        res_content = f.read()
    
    # Extract the modal block and script from resources
    modal_start = res_content.find('<!-- Upload Material Modal -->')
    notebook_end = res_content.find('</body>')
    notebook_code = res_content[modal_start:notebook_end]
    
    # Also we want to ensure there is a clear "Upload from Laptop" button inside the new modal box (in notebook_code)
    # We will replace the dashed box to say "Upload from Laptop" more clearly
    # But wait, it already says "Click to browse or drag file here"
    # Let's add an explicit button to it
    new_dashed = """<div style="border: 2px dashed rgba(240,84,84,0.4); background:rgba(240,84,84,0.05); padding: 40px 20px; text-align: center; border-radius: 10px; margin-bottom: 20px; cursor:pointer; transition:all 0.2s;" onclick="document.getElementById('fileUploadInput').click()" onmouseover="this.style.background='rgba(240,84,84,0.1)'" onmouseout="this.style.background='rgba(240,84,84,0.05)'">
      <div style="font-size: 40px; color: var(--red); margin-bottom: 15px;">☁️</div>
      <p style="margin:0; font-weight:500;">Click to browse or drag file here</p>
      <button style="margin-top:15px; padding:8px 16px; background:rgba(48,71,94,0.8); border:1px solid rgba(245,245,245,0.2); border-radius:6px; color:#fff; cursor:pointer;" onclick="event.stopPropagation(); document.getElementById('fileUploadInput').click()">Upload from Laptop</button>
      <input type="file" id="fileUploadInput" style="display:none;" onchange="handleFileSelect(event)">
    </div>"""
    
    # Instead of full regex, let's just find the dashed box and replace
    p2 = r'<div style="border: 2px dashed[^>]*>.*?<input type="file".*?>\s*</div>'
    notebook_code = re.sub(p2, new_dashed, notebook_code, flags=re.DOTALL)
    
    files = glob.glob('*.html')
    for f in files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
        og = content
        
        # 1. Update the 'sb-resources' sidebar item to link directly
        content = re.sub(r'id=\"sb-resources\"[^>]*onclick=\"openPopup\(\'study\'\,this\)\"', 'id=\"sb-resources\" onclick=\"window.location.href=\'studyverse-resources (3).html\'\"', content)
        # Also handle any variants
        content = re.sub(r'id=\"sb-resources\"\s*onclick=\"[^\"]*\"(.*?)', r'id="sb-resources" onclick="window.location.href=\'studyverse-resources (3).html\'"\1', content)
        
        # 2. Add the modal & NotebookLM overlay by replacing the old one
        if '<!-- Upload Material Modal -->' in content:
            old_start = content.find('<!-- Upload Material Modal -->')
            old_end = content.find('</body>')
            if old_start != -1 and old_end != -1:
                content = content[:old_start] + notebook_code + '\n' + content[old_end:]
        
        # Write back changes
        if content != og:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print('Updated', f)

    print('Done applying changes.')

except Exception as e:
    print('Error:', e)
