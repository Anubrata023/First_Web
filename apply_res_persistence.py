import glob
import re

print('Running script to add Title/Category and persistence to grid...')

try:
    with open('studyverse-resources (3).html', 'r', encoding='utf-8') as f:
        res_content = f.read()
    
    # Extract the modal block and script from resources
    modal_start = res_content.find('<!-- Upload Material Modal -->')
    notebook_end = res_content.find('</body>')
    notebook_code = res_content[modal_start:notebook_end]
    
    # We will inject title, category, and type before the dashed box
    inputs_html = """
    <input type="text" id="resTitle" placeholder="Resource Title (e.g. Optics Notes)" style="width:100%; background:rgba(48,71,94,0.2); border:1px solid rgba(48,71,94,0.4); border-radius:8px; padding:10px; color:#fff; font-family:'DM Sans', sans-serif; font-size:0.9rem; margin-bottom:15px; outline:none;">
    
    <div style="display:flex; gap:10px; margin-bottom:20px;">
      <select id="resCategory" style="flex:1; background:rgba(48,71,94,0.2); border:1px solid rgba(48,71,94,0.4); border-radius:8px; padding:10px; color:#fff; font-family:'DM Sans', sans-serif; font-size:0.9rem; outline:none;">
        <option value="Physics" style="color:#000">⚛️ Physics</option>
        <option value="Chemistry" style="color:#000">🧪 Chemistry</option>
        <option value="Mathematics" style="color:#000">📐 Mathematics</option>
        <option value="Biology" style="color:#000">🧬 Biology</option>
        <option value="CS" style="color:#000">💻 CS</option>
        <option value="English" style="color:#000">📖 English</option>
        <option value="SST" style="color:#000">🌍 SST</option>
      </select>
      <select id="resType" style="flex:1; background:rgba(48,71,94,0.2); border:1px solid rgba(48,71,94,0.4); border-radius:8px; padding:10px; color:#fff; font-family:'DM Sans', sans-serif; font-size:0.9rem; outline:none;">
        <option value="PDF" style="color:#000">📄 PDF</option>
        <option value="Video" style="color:#000">🎬 Video</option>
        <option value="Quiz" style="color:#000">✅ Quiz</option>
        <option value="Notes" style="color:#000">📝 Notes</option>
      </select>
    </div>
    """
    
    # Inject inputs before the dashed box
    notebook_code = notebook_code.replace('<div style="border: 2px dashed', inputs_html + '<div style="border: 2px dashed')
    
    # We need to inject JS to handle loading and saving resources
    js_inject = """
function renderNewResource(res) {
  const grid = document.getElementById('resGrid');
  if(!grid) return;
  
  const div = document.createElement('div');
  div.className = `res-card`;
  div.dataset.subject = res.category;
  div.dataset.type = res.type;
  
  let icn = '📄';
  if(res.type==='Video') icn='🎬';
  if(res.type==='Quiz') icn='✅';
  if(res.type==='Notes') icn='📝';
  
  let subjIcn = '📘';
  if(res.category==='Physics') subjIcn='⚛️';
  if(res.category==='Chemistry') subjIcn='🧪';
  if(res.category==='Mathematics') subjIcn='📐';
  if(res.category==='Biology') subjIcn='🧬';
  if(res.category==='CS') subjIcn='💻';
  
  div.innerHTML = `
    <div class="rc-header"><span class="rc-em">${subjIcn}</span><span class="rc-type tp">${res.type}</span></div>
    <div class="rc-t">${res.title}</div>
    <div class="rc-d">Uploaded recently by you.</div>
    <div class="rc-meta"><span class="rc-stat">⬇ 0</span><span class="rc-stat">⭐ New</span></div>
    <div class="rc-foot"><div class="rc-action" onclick="toast('📥','Opening NotebookLM...')">Open NotebookLM ›</div><div class="rc-bm" onclick="bm(this)">🔖</div></div>
  `;
  grid.insertBefore(div, grid.firstChild);
  if(typeof applyFilters === 'function') applyFilters();
}

window.addEventListener('DOMContentLoaded', () => {
   const saved = JSON.parse(localStorage.getItem('savedResources') || '[]');
   // render in reverse order to keep newest at top
   saved.reverse().forEach(r => renderNewResource(r));
});
"""

    # We update `submitUpload` to save the resource
    # find where toast('✅', 'Resource successfully processed! Opening NotebookLM...'); is
    save_logic = """
      const t = document.getElementById('resTitle').value || (selectedUploadFile ? selectedUploadFile.name : 'Untitled');
      const c = document.getElementById('resCategory').value;
      const type = document.getElementById('resType').value;
      const newRes = {title: t, category: c, type: type};
      let saved = JSON.parse(localStorage.getItem('savedResources') || '[]');
      saved.unshift(newRes);
      localStorage.setItem('savedResources', JSON.stringify(saved));
      if(typeof renderNewResource === 'function') renderNewResource(newRes);
      
      toast('✅', 'Resource saved successfully! Opening NotebookLM...');
"""
    notebook_code = notebook_code.replace("toast('✅', 'Resource successfully processed! Opening NotebookLM...');", save_logic)
    notebook_code = notebook_code.replace("toast('✅', 'File uploaded successfully! Generation started.');", save_logic)
    
    # inject the new functions into the script tag
    notebook_code = notebook_code.replace("function openNotebookLm", js_inject + "\nfunction openNotebookLm")
    
    files = glob.glob('*.html')
    for f in files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read()
            
        og = content
        if '<!-- Upload Material Modal -->' in content:
            old_start = content.find('<!-- Upload Material Modal -->')
            old_end = content.find('</body>')
            if old_start != -1 and old_end != -1:
                content = content[:old_start] + notebook_code + '\n' + content[old_end:]
        
        if content != og:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print('Updated', f)

    print('Done applying changes.')

except Exception as e:
    print('Error:', e)
