const fs = require('fs');

try {
    let content = fs.readFileSync('studyverse (1).html', 'utf8');
    const target = `<button class="btn btn-secondary" onclick="window.location.href='/resources'">Resources</button>`;
    
    const idx = content.indexOf(target);
    if (idx !== -1) {
        console.log("FOUND exact target in node utf8!");
        const replacement = target + `\n        <button class="btn btn-secondary" onclick="window.location.href='/physics'">Physics Room</button>`;
        content = content.replace(target, replacement);
        fs.writeFileSync('studyverse (1).html', content, 'utf8');
        console.log("Replaced successfully!");
    } else {
        console.log("NOT FOUND exact target. Let's look for 'Resources'");
        const idx2 = content.indexOf('Resources');
        if (idx2 !== -1) {
            console.log("Found 'Resources' at", idx2);
            console.log("Context around it:");
            console.log(content.substring(Math.max(0, idx2 - 50), idx2 + 100));
        } else {
            console.log("Could not find 'Resources' at all.");
        }
    }
} catch (e) {
    console.error("Error:", e);
}
