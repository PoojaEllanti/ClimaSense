# 🌦️ ClimaSense

ClimaSense is a modern weather application that provides real-time weather updates using **LangChain** and **Ollama (LLaMA3)** for natural language processing. It fetches current weather data (like temperature, condition, and wind speed) using the free **Open-Meteo API**, and displays it on a beautiful animated frontend.

![screenshot](./assets/screenshot.png) <!-- optional: replace with your image path -->

---

## 🚀 Features

- 🌍 Get weather by city name (e.g., "Chennai")
- 📡 Fetches real-time weather data using [Open-Meteo](https://open-meteo.com/)
- 🧠 Natural Language Processing via [LangChain](https://www.langchain.com/) + [Ollama](https://ollama.com/)
- 🎨 Sleek and animated frontend
- ⚡ FastAPI backend with CORS enabled

---

## 🛠️ Tech Stack

| Frontend      | Backend     | AI / LLM     | Weather API   |
|---------------|-------------|--------------|----------------|
| HTML, CSS, JS | FastAPI     | LangChain + Ollama (LLaMA3) | Open-Meteo API |

---

## 📦 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/climasense.git
cd climasense

Set up Python environment (backend)
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt

Install & Run Ollama
Make sure Ollama is installed:
ollama run llama3
You should see Ollama running a model locally.

Start the FastAPI server
uvicorn main:app --reload
Your backend will be live at http://127.0.0.1:8000.

Open the Frontend
In another terminal:
cd frontend
# Simply open index.html in your browser
Or use VS Code Live Server for easier development.

📂 Project Structure
climasense/
├── backend/
│   ├── main.py
│   ├── requirements.txt
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
└── README.md
