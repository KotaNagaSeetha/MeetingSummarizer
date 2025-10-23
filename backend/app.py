import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, Meeting
from asr_client import transcribe_audio
from llm_client import summarize_text

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_audio():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(filepath)
    transcript = transcribe_audio(filepath)
    summary, actions = summarize_text(transcript)
    meeting = Meeting(filename=file.filename, transcript=transcript, summary=summary, action_items=actions)
    db.session.add(meeting)
    db.session.commit()
    return jsonify({
        'transcript': transcript,
        'summary': summary,
        'action_items': actions
    }), 200

if __name__ == '__main__':
    app.run(debug=True)
