import React, { useState } from 'react';
import AudioUpload from './components/AudioUpload';
import TranscriptDisplay from './components/TranscriptDisplay';
import SummaryDisplay from './components/SummaryDisplay';
import './styles/App.css';

function App() {
  const [result, setResult] = useState({ transcript: '', summary: '', action_items: '' });

  return (
    <main className="app-container">
      <h1 className="app-title">Meeting Summarizer</h1>

      <AudioUpload onResult={setResult} />
      <TranscriptDisplay transcript={result.transcript} />
      <SummaryDisplay summary={result.summary} actionItems={result.action_items} />
    </main>
  );
}

export default App;
