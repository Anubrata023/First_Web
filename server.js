const express = require('express');
const path = require('path');
const fs = require('fs');
const multer = require('multer');

const app = express();
const port = 3000;

app.use(express.json());

// Set up multer for file uploads
const uploadDir = path.join(__dirname, 'uploads');
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

const storage = multer.diskStorage({
    destination: function (req, file, cb) {
        cb(null, uploadDir);
    },
    filename: function (req, file, cb) {
        cb(null, Date.now() + '-' + file.originalname);
    }
});

const upload = multer({ storage: storage });

// Enable CORS
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*');
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

// Serve static files from the current directory
app.use(express.static(path.join(__dirname, '')));

const otpStore = new Map();

app.post('/api/auth/send-otp', (req, res) => {
    const { identifier } = req.body;
    if (!identifier) {
        return res.status(400).json({ success: false, message: 'Identifier is required' });
    }

    const otp = Math.floor(100000 + Math.random() * 900000).toString();
    otpStore.set(identifier, otp);

    console.log(`\n=========================================`);
    console.log(`[🔐 OTP GENERATED] For ${identifier}: \x1b[32m${otp}\x1b[0m`);
    console.log(`=========================================\n`);

    res.json({ success: true, message: 'OTP sent to terminal', otp: otp });
});

app.post('/api/auth/verify-otp', (req, res) => {
    const { identifier, otp } = req.body;
    if (!identifier || !otp) {
        return res.status(400).json({ success: false, message: 'Identifier and OTP are required' });
    }

    const storedOtp = otpStore.get(identifier);
    if (storedOtp && storedOtp === otp) {
        otpStore.delete(identifier);
        res.json({ success: true, redirectUrl: '/dashboard' });
    } else {
        res.status(401).json({ success: false, message: 'Invalid OTP' });
    }
});

app.get('/dashboard', (req, res) => {
    res.sendFile(path.join(__dirname, 'studyverse (1).html'));
});

app.get('/resources', (req, res) => {
    res.sendFile(path.join(__dirname, 'studyverse-resources (3).html'));
});

app.get('/doubts', (req, res) => {
    res.sendFile(path.join(__dirname, 'community-doubts (2).html'));
});

app.get('/study-with-friends', (req, res) => {
    res.sendFile(path.join(__dirname, 'study-with-friends.html'));
});

app.get('/physics', (req, res) => {
    res.sendFile(path.join(__dirname, 'subject-study-page (1).html'));
});

app.get('/sakura', (req, res) => {
    res.sendFile(path.join(__dirname, 'sakura-studyverse (6).html'));
});
// Material Upload API Endpoint
app.post('/api/material/upload', upload.single('material'), (req, res) => {
    try {
        const { generatePodcast, generateQuiz, generateFlashcards, manualText } = req.body;

        if (!req.file && (!manualText || manualText.trim() === '')) {
            return res.status(400).json({ success: false, message: 'No file or manual text uploaded' });
        }
        
        console.log(`\n=========================================`);
        if (req.file) {
            console.log(`[📤 MATERIAL UPLOADED] File: \x1b[36m${req.file.filename}\x1b[0m`);
        } else {
            console.log(`[📤 MATERIAL ADDED] Manual Text/Link received: \x1b[36m${manualText.substring(0, 30)}...\x1b[0m`);
        }
        console.log(`- Podcast Requested: ${generatePodcast}`);
        console.log(`- Quiz Requested:    ${generateQuiz}`);
        console.log(`- Flashcards Req:    ${generateFlashcards}`);
        console.log(`=========================================\n`);

        res.json({
            success: true, 
            message: 'Material uploaded successfully.',
            file: req.file ? req.file.filename : null,
            textReceived: !!manualText,
            generations: {
                podcast: generatePodcast === 'true' || generatePodcast === true,
                quiz: generateQuiz === 'true' || generateQuiz === true,
                flashcards: generateFlashcards === 'true' || generateFlashcards === true
            }
        });
    } catch (err) {
        console.error(err);
        res.status(500).json({ success: false, message: 'Server error during upload' });
    }
});

// Fallback to studyverse-login.html or a specific default if no path is provided
app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, 'studyverse-login.html'));
});

app.listen(port, () => {
    console.log(`StudyVerse server running at http://localhost:${port}`);
});
