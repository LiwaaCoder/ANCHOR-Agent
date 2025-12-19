# ANCHOR: The Cognitive Prosthetic Intelligence

<p align="center">
  <img src="images/hero.png" alt="ANCHOR Hero" width="600px">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Model-Gemini--2.5--Flash-blueviolet?style=for-the-badge&logo=google-gemini" alt="Gemini">
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi" alt="FastAPI">
  <img src="https://img.shields.io/badge/Safety-PII--Redaction-E91E63?style=for-the-badge&logo=shield" alt="Safety">
  <img src="https://img.shields.io/badge/Architecture-Cognitive--Threading-4CAF50?style=for-the-badge" alt="Architecture">
</p>

---

## 🧠 Overview
**ANCHOR** is an advanced, AI-driven Cognitive Prosthetic designed to restore dignity and functional independence to individuals with Alzheimer’s, dementia, or severe memory impairment. By serving as an external **"Working Memory,"** ANCHOR bridges the gap between disorientation and clarity.

## 📱 Interface Snapshot
<p align="center">
  <img src="images/dashboard.png" alt="Dashboard Screenshot" width="300px">
</p>

## 🛠️ Technical Architecture

### The "Cognitive Threading" Pipeline
ANCHOR utilizes a **2-million token context window** to maintain a persistent state of the user's day, ensuring that every interaction is contextually aware and empathetic.

```mermaid
graph TD
    Input[Multimodal Input: Audio/Image/Context] --> Redactor[PII Redaction Engine]
    Redactor --> Gemini[Gemini 2.5 Flash / Long-Context Window]
    Gemini --> Orientation[Proactive Orientation]
    Gemini --> Safety[Safety & Anomaly Detection]
    Gemini --> Reflection[Daily Cognitive Threading]
    Orientation --> Output[Natural Language Output]
    Safety --> Alert[Emergency Alert Trigger]
    Reflection --> Summary[8 PM Daily Reflection]
```

## 🚀 Key Features

### 1. **Proactive Orientation**
Automatically identifies individuals, objects, and locations. 
- *Input*: Image of a neighbor.
- *Response*: "That is Sarah, your neighbor. She is wearing a green coat today."

### 2. **Anomaly Detection & Redirection**
Monitors for 'Sundowning' patterns or GPS wandering.
- *Logic*: If time is evening and GPS indicates an unfamiliar route, ANCHOR initiates calming redirection.

### 3. **PII Safety Layer**
Robust regex-based redaction ensures that sensitive numerical data (bank PINs, credit cards) never leave the local environment or enter the model's history without masking.

## 💻 Tech Spec
- **Core Engine**: Google Gemini Pro 1.5/2.5
- **Web Backend**: FastAPI (Python)
- **Frontend**: ES6+ JavaScript, CSS3 (Glassmorphism), Semantic HTML5
- **Security**: Local `.env` management and pattern-matching redaction.

## ⚙️ Setup & Deployment

```bash
# Clone the repository
git clone https://github.com/LiwaaCoder/ANCHOR-Agent.git

# Install expert-tier dependencies
pip install -r requirements.txt

# Configure your secure credentials
cp .env.example .env

# Launch the platform
uvicorn server:app --reload
```

---
<p align="center">
  <i>"Empowering memory through intelligent companionship."</i>
</p>
