from flask import Flask, render_template, Response, jsonify
from flask_cors import CORS
import cv2
import time
from deepface import DeepFace

app = Flask(__name__, template_folder='a_templates', static_folder='b_static')
CORS(app)

# Global state
current_emotion = "neutral"
last_detection_time = 0
camera = None

# Emotion → Music mapping
emotion_music = {
    'happy': [
        {'title': 'Happy - Pharrell Williams', 'id': 'ZbZSe6N_BXs', 'mood': 'Upbeat & Joyful'},
        {'title': 'Good Vibrations - The Beach Boys', 'id': 'Eab_beh07HU', 'mood': 'Feel Good'},
        {'title': 'Walking on Sunshine - Katrina', 'id': 'iPUmE-tne5U', 'mood': 'Energetic'}
    ],
    'sad': [
        {'title': 'Someone Like You - Adele', 'id': 'hLQl3WQQoQ0', 'mood': 'Melancholic'},
        {'title': 'Fix You - Coldplay', 'id': 'k4V3Mo61fJM', 'mood': 'Comforting'},
        {'title': 'The Scientist - Coldplay', 'id': 'RB-RcX5DS5A', 'mood': 'Reflective'}
    ],
    'angry': [
        {'title': 'In The End - Linkin Park', 'id': 'eVTXPUF4Oz4', 'mood': 'Release'},
        {'title': 'Lose Yourself - Eminem', 'id': '_Yhyp-_hX2s', 'mood': 'Intense'},
        {'title': 'Break Stuff - Limp Bizkit', 'id': 'ZpUYjpKg9KY', 'mood': 'Powerful'}
    ],
    'neutral': [
        {'title': 'Weightless - Marconi Union', 'id': 'UfcAVejslrU', 'mood': 'Calm'},
        {'title': 'Clair de Lune - Debussy', 'id': 'CvFH_6DNRCY', 'mood': 'Peaceful'},
        {'title': 'River Flows in You - Yiruma', 'id': '7maJOI3QMu0', 'mood': 'Serene'}
    ]
}

def generate_frames():
    global current_emotion, last_detection_time, camera
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        current_time = time.time()

        if current_time - last_detection_time > 2:
            try:
                result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                if isinstance(result, list):
                    result = result[0]
                current_emotion = result['dominant_emotion']
                last_detection_time = current_time
            except Exception as e:
                print("Detection error:", e)

        _, buffer = cv2.imencode('.jpg', frame)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + buffer.tobytes() + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/get_emotion')
def get_emotion():
    return jsonify({
        'emotion': current_emotion,
        'songs': emotion_music.get(current_emotion, emotion_music['neutral'])
    })

@app.route('/stop_camera')
def stop_camera():
    global camera
    if camera:
        camera.release()
    return jsonify({'status': 'stopped'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

