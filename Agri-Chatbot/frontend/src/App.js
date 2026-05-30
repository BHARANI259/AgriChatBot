import React from "react";
import Chatbot from "./Chatbot";
import "./styles.css";

function App() {
  return (
    <div className="app-container">
      <h1 className="title">Agricultural Advisory Chatbot</h1>
      <p className="subtitle">
        Ask questions about crops, fertilizers, irrigation, pest control, and farming tips.
      </p>
      <Chatbot />
    </div>
  );
}

export default App;