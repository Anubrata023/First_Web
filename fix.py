import glob

save_logic = '''    if (response.ok) {
      const t = document.getElementById('resTitle').value || (selectedUploadFile ? selectedUploadFile.name : 'Untitled');
      const c = document.getElementById('resCategory').value;
      const type = document.getElementById('resType').value;
      const newRes = {title: t, category: c, type: type};
      let saved = JSON.parse(localStorage.getItem('savedResources') || '[]');
      saved.unshift(newRes);
      localStorage.setItem('savedResources', JSON.stringify(saved));
      if(typeof renderNewResource === 'function') renderNewResource(newRes);
      
      toast('✅', 'Resource saved successfully! Opening NotebookLM...');
      closeUploadModal();
      
      const title = selectedUploadFile ? selectedUploadFile.name : 'Pasted Text/Link';
      setTimeout(() => openNotebookLm(title), 800);
    } else {'''

files = glob.glob('*.html')
for f in files:
    if f == 'studyverse-resources (3).html': continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    old_logic1 = '''    if (response.ok) {
      toast('✅', 'Resource successfully processed! Opening NotebookLM...');
      closeUploadModal();
      
      const title = selectedUploadFile ? selectedUploadFile.name : 'Pasted Text/Link';
      setTimeout(() => openNotebookLm(title), 800);
    } else {'''
    
    if old_logic1 in content:
        content = content.replace(old_logic1, save_logic)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated submitUpload in', f)
print('Done frontend updates.')
