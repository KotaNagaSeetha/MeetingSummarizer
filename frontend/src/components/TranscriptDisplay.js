import React from 'react';
import '../styles/TranscriptDisplay.css';

export default function TranscriptDisplay({ transcript }) {
  if (!transcript) return null;
  return (
    <section className="transcript-section" aria-label="Transcript section">
      <h2 className="transcript-title">Transcript</h2>
      <p className="transcript-text">{transcript}</p>
    </section>
  );
}
