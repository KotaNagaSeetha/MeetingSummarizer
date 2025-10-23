import React from 'react';
import '../styles/SummaryDisplay.css';

export default function SummaryDisplay({ summary, actionItems }) {
  if (!summary && !actionItems) return null;
  return (
    <section className="summary-section" aria-label="Summary and action items">
      <h2 className="summary-title">Summary</h2>
      <p className="summary-text">{summary}</p>
      <h3 className="action-items-title">Action Items</h3>
      <p className="action-items-text">{actionItems}</p>
    </section>
  );
}
