import React from "react";
import DocumentUploader from "./components/DocumentUploader";
import ChatBox from "./components/ChatBox";

export default function App() {
  return (
    <div style={{ maxWidth: 720, margin: "40px auto", padding: "0 20px" }}>
      <h1>AI-Powered Document QA Bot</h1>
      <DocumentUploader />
      <ChatBox />
    </div>
  );
}
