import glob, re

new_submit = '''async function submitUpload() {
  const manualText = document.getElementById('manualResourceText').value.trim();
  
  if (!selectedUploadFile && !manualText) {
    toast('❌', 'Please select a file or paste a link/text to upload.');
    return;
  }
  const generatePodcast = document.getElementById('genPodcast').checked;
  const generateQuiz = document.getElementById('genQuiz').checked;
  const generateFlashcards = document.getElementById('genFlashcards').checked;

  const formData = new FormData();
  if (selectedUploadFile) formData.append('material', selectedUploadFile);
  formData.append('manualText', manualText);
  formData.append('generatePodcast', generatePodcast);
  formData.append('generateQuiz', generateQuiz);
  formData.append('generateFlashcards', generateFlashcards);

  try {
    toast('☁️', 'Uploading file...');
    const response = await fetch('http://localhost:3000/api/material/upload', {
      method: 'POST',
      body: formData
    });
    const data = await response.json();
    if (response.ok) {
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
    } else {
      toast('❌', data.message || 'Upload failed.');
    }
  } catch (error) {
    console.error('Upload Error:', error);
    toast('❌', 'Network error during upload.');
  }
}'''

files = glob.glob('*.html')
for f in files:
    if f == 'studyverse-resources (3).html': continue
    
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # regex to replace async function submitUpload() { ... }
    match = re.search(r'(async function submitUpload\(\) \{.*?^\})', content, re.DOTALL | re.MULTILINE)
    if match:
        content = content.replace(match.group(1), new_submit)
        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        print('Updated submitUpload in', f)
print('Done frontend updates.')
