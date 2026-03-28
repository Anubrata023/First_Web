const fs = require('fs');

try {
    let content = fs.readFileSync('studyverse (1).html', 'utf8');
    const idx = content.indexOf('Study with Friends');
    if (idx !== -1) {
        console.log("Context around 'Study with Friends':");
        console.log(content.substring(Math.max(0, idx - 800), idx + 1000));
    } else {
        console.log("Could not find 'Study with Friends'.");
    }
} catch (e) {
    console.error("Error:", e);
}
