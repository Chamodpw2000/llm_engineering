import React, { useState } from 'react';
import './App.css';
import ReactMarkdown from 'react-markdown';

function App() {
  const [url, setUrl] = useState('');
  const [summary, setSummary] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();
    
    // Reset states
    setError('');
    setSummary('');
    setLoading(true);

    try {
      const response = await fetch('http://localhost:5000/api/summarize', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ url }),
      });

      const data = await response.json();

      if (data.success) {
        setSummary(data.summary);
      } else {
        setError(data.error || 'Failed to summarize website');
      }
    } catch (err) {
      setError('Failed to connect to the API. Make sure the Flask server is running on port 5000.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <div className="container">
        <h1>🌐 Website Summarizer</h1>
        <p className="subtitle">Get snarky AI-powered summaries of any website</p>

        <form onSubmit={handleSubmit} className="url-form">
          <input
            type="text"
            value={url}
            onChange={(e) => setUrl(e.target.value)}
            placeholder="Enter website URL (e.g., https://example.com)"
            className="url-input"
            required
          />
          <button type="submit" disabled={loading} className="submit-btn">
            {loading ? 'Summarizing...' : 'Summarize'}
          </button>
        </form>

        {error && (
          <div className="error-box">
            <strong>Error:</strong> {error}
          </div>
        )}

        {summary && (
          <div className="summary-box">
            <h2>Summary</h2>
            <div className="summary-content">
              <ReactMarkdown>{summary}</ReactMarkdown>
            </div>
          </div>
        )}

        {loading && (
          <div className="loading">
            <div className="spinner"></div>
            <p>Analyzing website content...</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
