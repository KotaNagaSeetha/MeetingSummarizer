import React, { useState } from 'react';
import axios from 'axios';
import '../styles/AudioUpload.css';

export default function AudioUpload({ onResult }) {
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleFileChange = e => {
    setFile(e.target.files[0]);
    setError('');
  };

  const handleSubmit = async e => {
    e.preventDefault();
    if (!file) {
      setError('Please select an audio file.');
      return;
    }
    setLoading(true);
    const formData = new FormData();
    formData.append('file', file);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });
      onResult(response.data);
    } catch (err) {
      setError('Failed to upload and process audio.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="audio-upload-container" role="region" aria-label="Audio file upload">
      <form onSubmit={handleSubmit}>
        <input
          type="file"
          accept=".mp3,.wav"
          onChange={handleFileChange}
          className="audio-upload-input"
          aria-required="true"
        />
        {error && <p className="error-message" role="alert">{error}</p>}
        <button
          type="submit"
          disabled={loading}
          className="audio-upload-button"
          aria-busy={loading}
        >
          {loading ? 'Processing...' : 'Upload & Summarize'}
        </button>
      </form>
    </div>
  );
}
