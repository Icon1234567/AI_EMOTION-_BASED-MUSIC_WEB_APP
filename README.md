🎧 Emotion-Based AI Music Web App
Where Technology Feels You — An intelligent web application that detects your real-time emotion and plays music that matches your mood. Built with DeepFace, Flask, and Spotify API, this project bridges the gap between human emotion and AI-driven music curation.

🌟 Features
🎭 Real-Time Emotion Detection using DeepFace and OpenCV

🎵 Mood-Based Music Playback via Spotify API

💻 Flask Backend for emotion processing and API routing

🌐 Responsive Frontend UI with HTML, CSS, JavaScript, and Bootstrap

🔄 Live Webcam Integration for seamless user interaction

📊 Emotion-to-Music Mapping for personalized experiences

🧠 Tech Stack
Layer	Tools & Libraries
Frontend	HTML, CSS, JavaScript, Bootstrap
Backend	Python, Flask, DeepFace, OpenCV
Music API	Spotify Web API
Emotion AI	DeepFace (Facial Expression Recognition)
Deployment	Flask server (local or cloud-hosted)
🚀 How It Works
Capture Emotion: The app accesses your webcam and captures facial expressions in real time.

Analyze Emotion: DeepFace analyzes the frame and classifies your emotion (e.g., happy, sad, angry).

Map to Music: The backend maps the detected emotion to a curated music genre or mood.

Play Music: The frontend fetches and plays a matching track using the Spotify API.

🛠️ Installation & Setup
Prerequisites
Python 3.7+

Node.js (optional, for frontend enhancements)

A Spotify Developer Account (for API credentials)

Clone the Repository
bash
git clone https://github.com/yourusername/emotion-music-ai.git
cd emotion-music-ai
Backend Setup
bash
pip install -r requirements.txt
python app.py
Frontend Setup
Open index.html in your browser or serve it using a local server (e.g., Live Server in VS Code).

🔐 Environment Variables
Create a .env file in the root directory and add your Spotify credentials:

Code
SPOTIFY_CLIENT_ID=your_client_id
SPOTIFY_CLIENT_SECRET=your_client_secret
📸 Emotion Labels Supported
Happy

Sad

Angry

Neutral

Surprise

Fear

Disgust

Each emotion is mapped to a specific music genre or playlist to enhance your mood or match your vibe.

📦 Folder Structure
Code
emotion-music-ai/
│
├── static/              # CSS, JS, and assets
├── templates/           # HTML templates
├── app.py               # Flask backend
├── emotion_utils.py     # Emotion detection logic
├── spotify_utils.py     # Spotify API integration
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
💡 Future Improvements
Add voice emotion detection

Integrate user preferences and mood history

Deploy on cloud (Heroku, Render, etc.)

Add dark mode and UI themes

