const fs = require('fs');
const path = require('path');

const config = JSON.parse(fs.readFileSync(path.join(__dirname, 'links.json'), 'utf-8'));
const files = fs.readdirSync(__dirname).filter(f => f.endsWith('.html'));

files.forEach(f => {
    let content = fs.readFileSync(path.join(__dirname, f), 'utf-8');
    const og = content;

    const escapeRegExp = (string) => string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');

    // 1. Replace mapped file names to clean routes in window.location.href or href
    for (const [oldName, cleanRoute] of Object.entries(config.file_to_route)) {
        const escapedOldName = escapeRegExp(oldName);
        const hrefRegex = new RegExp(`(href|window\\.location\\.href)\\s*=\\s*(["'])${escapedOldName}\\2`, 'g');
        content = content.replace(hrefRegex, `$1=$2${cleanRoute}$2`);
    }

    // 2. Ensure sb-resources points to /resources and sb-doubts points to /doubts
    content = content.replace(/(id="sb-resources"\s*onclick=")window\.location\.href=[^"]+(")/g, `$1window.location.href='/resources'$2`);
    content = content.replace(/(id="sb-doubts"\s*onclick=")window\.location\.href=[^"]+(")/g, `$1window.location.href='/doubts'$2`);

    // 3. Add Study With Friends!
    if (!content.includes('id="sb-friends"') && content.includes('id="sb-doubts"')) {
        content = content.replace(/(<div[^>]*id="sb-doubts"[^>]*>.*?<\/div>)/g, `$1\n  <div class="sb-icon-btn" id="sb-friends" onclick="window.location.href='/study-with-friends'" title="Study with Friends">👥</div>`);
    }

    // 4. Update the popup titles based on config.routes by replacing onclick directly in titles 
    // This part is a bit tricky, but since we've already done most via file mapping, 
    // we just ensure window.location goes to the right places.

    if (f === 'subject-study-page (1).html') {
        content = content.replace(/onclick="toast\('📚','Viewing all resources\.\.\.'\)"/g, `onclick="window.location.href='/resources'"`);
    }

    if (f === 'studyverse (1).html') {
        content = content.replace(/toast\('⚛️','Opening Physics\.\.\.'\)/g, `window.location.href='/physics'`);
    }

    if (content !== og) {
        fs.writeFileSync(path.join(__dirname, f), content, 'utf-8');
        console.log('Updated links in ' + f);
    }
});

console.log('Done mapping links from links.json.');
