
# 🧠 Meeting Summarizer

## 📖 Introduction
Meeting Summarizer is a full-stack web application that automatically transcribes and summarizes meeting audio using AI and NLP models. It streamlines the process of capturing, transcribing, and summarizing meetings, making it easy to extract key insights and share them with your team.

---

## ✨ Features
- 🎤 Audio Upload & Real-time Transcription (Whisper ASR)
- 📝 Automatic Summarization (LLM)
- 📄 Downloadable transcripts and summaries
- ⚡ Simple, responsive UI (React)
- 🔗 RESTful API integration (Flask)
- 🛡️ Secure storage of meeting data

---

## 🏗️ Architecture

```
User ──▶ Frontend (React) ──▶ Backend (Flask) ──▶ ASR & LLM Models
  ▲             │                │
  └─────────────┴────────────────┘
      SQLite DB & File Storage
```

- **Frontend:** Handles file upload, displays transcript and summary, interacts with backend APIs.
- **Backend:** Receives audio, runs ASR (speech-to-text), sends transcript to LLM for summarization, stores results.
- **Database:** SQLite for storing transcripts and summaries.

---

## 📂 Project Structure
```
Meeting-Summarizer-Project/
│
├── backend/                  # 🐍 Flask backend
│   ├── app.py                # Main Flask application
│   ├── asr_client.py         # Handles ASR (speech-to-text)
│   ├── llm_client.py         # Handles LLM summarization
│   ├── models.py             # Database models
│   ├── requirements.txt      # Python dependencies
│   ├── db.sqlite3            # SQLite database (default)
│   ├── .env                  # Environment variables
│   ├── instance/
│   │   └── db.sqlite3        # SQLite database (alternate location)
│   ├── static/
│   │   └── uploads/          # Uploaded audio files
│   └── __pycache__/          # Python cache files
│
├── frontend/                 # ⚛️ React frontend
│   ├── package.json          # NPM dependencies and scripts
│   ├── public/
│   │   ├── index.html        # Main HTML file
│   │   └── robots.txt        # Robots exclusion file
│   ├── src/
│   │   ├── App.js            # Main React app
│   │   ├── App.test.js       # App tests
│   │   ├── index.js          # Entry point
│   │   ├── index.css         # Global styles
│   │   ├── reportWebVitals.js# Web vitals reporting
│   │   ├── setupTests.js     # Test setup
│   │   ├── components/
│   │   │   ├── AudioUpload.js        # Audio upload component
│   │   │   ├── SummaryDisplay.js     # Summary display component
│   │   │   └── TranscriptDisplay.js  # Transcript display component
│   │   └── styles/
│   │       ├── App.css               # App styles
│   │       ├── AudioUpload.css       # Audio upload styles
│   │       ├── SummaryDisplay.css    # Summary display styles
│   │       └── TranscriptDisplay.css # Transcript display styles
│
└── README.md                # Project documentation
```

---

## ⚡ Quick Start & Installation

### 1️⃣ Clone the repository
```powershell
git clone https://github.com/KotaNagaSeetha/MeetingSummarizer.git
cd MeetingSummarizer
```

### 2️⃣ Backend Setup
```powershell
cd backend
python -m venv venv
venv\Scripts\activate  # (Windows)
pip install -r requirements.txt
```

### 3️⃣ Frontend Setup
Open a new terminal:
```powershell
cd frontend
npm install
npm start
```

---

## 🚀 Usage
1. Start the backend server:
   ```powershell
   python app.py
   ```
2. Start the frontend development server:
   ```powershell
   npm start
   ```
3. Open your browser at [http://localhost:3000](http://localhost:3000)
4. Upload an audio file, view the transcript, and get the summary.

---

## 🛠️ Development

### Manual Setup
- Ensure Python 3.8+ and Node.js 16+ are installed.
- Backend dependencies: see `backend/requirements.txt`
- Frontend dependencies: see `frontend/package.json`

### Environment Variables
- Create a `.env` file in `backend/` for API keys and secrets:
  ```env
  GOOGLE_AI_STUDIO_API_KEY=your_google_ai_studio_key
  FLASK_SECRET_KEY=your_secret
  ...
  ```
- To get your Google AI Studio API key, sign up at [Google AI Studio](https://aistudio.google.com/) and generate your API key from your account dashboard.

### API Endpoints (Backend)
- `POST /upload` — Upload audio file
- `GET /transcript/<id>` — Get transcript
- `GET /summary/<id>` — Get summary

## Backend
- **Tech Stack:** Python, Flask
- **Key Files:**
  - `app.py`: Main Flask application
  - `asr_client.py`: Handles ASR (speech-to-text)
  - `llm_client.py`: Handles communication with LLM (summarization)
  - `models.py`: Database models
  - `requirements.txt`: Python dependencies
- **Setup:**
  1. Navigate to `backend/`
  2. Install dependencies:
     ```powershell
     pip install -r requirements.txt
     ```
  3. Set up environment variables in `.env` as needed
  4. Run the server:
     ```powershell
     python app.py
     ```

## Frontend
- **Tech Stack:** React
- **Key Files:**
  - `src/App.js`: Main React app
  - `src/components/AudioUpload.js`: Audio upload component
  - `src/components/TranscriptDisplay.js`: Transcript display
  - `src/components/SummaryDisplay.js`: Summary display
- **Setup:**
  1. Navigate to `frontend/`
  2. Install dependencies:
     ```powershell
     npm install
     ```
  3. Start the development server:
     ```powershell
     npm start
     ```


---

## ⚠️ Safety & Notes
- Do not share your API keys publicly.
- Uploaded files are stored locally; ensure disk space and privacy.
- For production, use HTTPS and secure your Flask secret key.

---

## 📜 License
This project is licensed under the MIT License.

---

## 🧠 Troubleshooting

If you encounter any issues while running the project, consider the following:

- Ensure both the **frontend** and **backend** servers are running correctly.  
- Verify that your **Gemini API key** is properly set in the `.env` file.  
- Confirm that your **audio file** is valid and within size limits (preferably under 10MB).  
- Check the **browser console** or **backend logs** for any specific error messages.  
- Restart both servers after making configuration changes.

---

## 🌟 Future Enhancements
- 🔊 Real-time streaming transcription
- 🌐 Multi-language support
- 🧾 Speaker diarization
- ☁️ Cloud integration for storage & retrieval

---

## 🎥 Demo Video

Watch the demo of **MeetingSummarizer** here:  
https://drive.google.com/file/d/12JE8qlKb6d_O2aj-szR964BVZSgMnUFg/view?usp=drive_link

---

## 🙌 Acknowledgments

Special thanks to **OpenAI Whisper** and **Gemini API** for providing the core AI components that power this project.  
Designed and developed by [KOTA NAGA SEETHA](https://github.com/KotaNagaSeetha).
