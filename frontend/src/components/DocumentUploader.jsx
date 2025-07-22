import React, { useState } from "react";
import { uploadDocument } from "../api";

export default function DocumentUploader() {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
    setMessage("");
  };

  const handleUpload = async () => {
    if (!file) {
      setMessage("Please select a file to upload.");
      return;
    }
    try {
      await uploadDocument(file);
      setMessage("Document uploaded successfully!");
      setFile(null);
    } catch (error) {
      setMessage("Upload failed. Please try again.");
      console.error(error);
    }
  };

  return (
    <div style={{ marginBottom: "20px" }}>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} style={{ marginLeft: "10px" }}>
        Upload
      </button>
      <div style={{ marginTop: 10, color: "green" }}>{message}</div>
    </div>
  );
}
