const fs = require('fs');

try {
    let content = fs.readFileSync('studyverse (1).html', 'utf8');
    const idx = content.indexOf('sidebar');
    if (idx !== -1) {
        fs.writeFileSync('sidebar_debug.txt', content.substring(Math.max(0, idx - 500), idx + 2000));
        console.log("Wrote sidebar to sidebar_debug.txt");
    } else {
        console.log("No sidebar found");
    }
} catch(e) {
    console.error(e);
}
