import React, { useState } from "react";
import { queryAnswer } from "../api";

export default function ChatBox() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = async () => {
    if (!question.trim()) return;
    setLoading(true);
    setAnswer("");
    setError(null);

    try {
      const res = await queryAnswer(question);
      setAnswer(res.data.answer);
    } catch (err) {
      setError("Failed to get answer. Try again.");
      console.error(err);
    }
    setLoading(false);
  };

  return (
    <div>
      <textarea
        rows={3}
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        placeholder="Ask a question about your documents..."
        style={{ width: "100%", resize: "vertical" }}
      />
      <button onClick={handleSubmit} disabled={loading} style={{ marginTop: 10 }}>
        {loading ? "Wait..." : "Ask"}
      </button>
      {error && <div style={{ color: "red", marginTop: 10 }}>{error}</div>}
      {answer && (
        <div
          style={{
            marginTop: 20,
            whiteSpace: "pre-wrap",
            background: "#f4f4f4",
            padding: 15,
            borderRadius: 5,
          }}
        >
          <strong>Answer:</strong> <br />
          {answer}
        </div>
      )}
    </div>
  );
}
