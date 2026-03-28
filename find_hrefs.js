const fs = require('fs');

try {
    let content = fs.readFileSync('studyverse (1).html', 'utf8');
    const lines = content.split('\n');
    lines.forEach((line, i) => {
        if (line.includes('window.location.href')) {
            console.log(`Line ${i}: ${line.trim()}`);
        }
    });
} catch (e) {
    console.error("Error:", e);
}
