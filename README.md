# ANCHOR - Cognitive Prosthetic Intelligence

ANCHOR is a sophisticated Cognitive Prosthetic designed to assist individuals with Alzheimer’s or dementia. It serves as an external "Working Memory," providing proactive orientation, safety alerts, and daily reflections.

## 🌟 Features
- **Proactive Orientation**: Identifies people and surroundings to help users stay oriented.
- **Anomaly Detection**: Monitors for signs of distress, sundowning, or wandering.
- **Object Localization**: Helps users find lost items like keys or glasses.
- **Cognitive Threading**: Maintains a persistent narrative of the day using a long-context window.
- **Modern Web Interface**: A premium, high-contrast, "Glassmorphism" UI designed for ease of use.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- A Google Gemini API Key

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/LiwaaCoder/ANCHOR-Agent.git
   cd ANCHOR-Agent
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Configure Environment Variables:
   Create a `.env` file in the root directory:
   ```text
   GOOGLE_API_KEY=your_gemini_api_key_here
   ```

### Running the Application
Start the FastAPI server:
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000
```
Then visit [http://localhost:8000](http://localhost:8000).

## 🛡️ Safety & Privacy
- **PII Redaction**: Automatically masks sensitive numerical data like credit card numbers.
- **Emergency Alerts**: Built-in `emergency_alert` tool for critical safety scenarios.

## 🛠️ Built With
- **Gemini 1.5/2.5 Pro**: Core LLM for cognitive reasoning.
- **FastAPI**: Modern, high-performance web backend.
- **Vanilla JS/CSS**: Lightweight, responsive frontend with premium aesthetics.

---
*Dedicated to providing dignity and clarity to those navigating memory challenges.*
