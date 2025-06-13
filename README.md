# 🌦️ ClimaSense - ML Powered Weather Monitoring System

ClimaSense is a modern and interactive weather monitoring system that not only fetches **real-time weather data** using the **OpenWeatherMap API**, but also predicts the **possibility of rain** for the next day using a **machine learning model** trained on historical weather patterns.

---

## 🚀 Features

- 🔍 Search weather by **city name**
- 🌡️ View:
  - Minimum & Maximum Temperature (°C)
  - Humidity (%)
  - Wind Speed (km/h)
  - Rainfall (last 1 hour)
  - Pressure (hPa)
- 🤖 **AI Prediction**: Will it rain tomorrow? YES/NO
- 🖌️ Stylish and animated **radiating gradient UI**
- 📊 Expandable section to preview sample weather dataset

---

## 📁 Project Structure

ClimaSense/
├── app.py # Main Streamlit app
├── data.csv # Historical weather dataset (used for model training)
├── weather_model.pkl # Pre-trained machine learning model
├── requirements.txt # Python dependencies
└── README.md # This file

yaml
Copy
Edit

---

## 🧠 Machine Learning Model

- Model: Decision Tree Classifier (or similar)
- Input Features:
  - Min Temp, Max Temp, Rainfall, Wind Speed, Humidity, Pressure, Rain Today
- Output: `0` = No Rain, `1` = Rain

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/ClimaSense.git
cd ClimaSense

2. Install Dependencies
pip install -r requirements.txt
If joblib or scikit-learn are missing, install manually:
pip install joblib scikit-learn

3. Add Your API Key
Replace "YOUR_API_KEY_HERE" in app.py with your OpenWeatherMap API key

You can get a free API key from: https://openweathermap.org/api

4. Run the App
streamlit run app.py
