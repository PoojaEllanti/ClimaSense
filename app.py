import streamlit as st
import requests
import numpy as np
import pandas as pd
import joblib

# === CONFIGURATION ===
API_KEY = "2937c0846861593154c4de9c7ae67546"  # Replace with your OpenWeatherMap API key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
model = joblib.load("weather_model.pkl")

# === Streamlit Page Settings ===
st.set_page_config(page_title="ClimaSense", page_icon="🌦️", layout="centered")

# === Radiating Gradient Background ===
st.markdown("""
    <style>
        html, body, [class*="st-"] {
            background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            color: white !important;
        }

        @keyframes gradientBG {
            0% {background-position: 0% 50%;}
            50% {background-position: 100% 50%;}
            100% {background-position: 0% 50%;}
        }

        .stButton > button {
            background-color: #ff7e5f;
            color: white;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            padding: 0.75em 1em;
            cursor: pointer;
        }

        .stTextInput > div > div > input {
            background-color: #ffffff10;
            color: white;
        }

        .stDataFrame {
            background-color: #00000020;
        }

        .stAlert, .stInfo, .stSuccess {
            background-color: #00000050 !important;
        }
    </style>
""", unsafe_allow_html=True)

# === App Title ===
st.title("🌈 ClimaSense - ML Powered Weather Monitoring")

# === City Input ===
city = st.text_input("🏙️ Enter City Name")

# === Apply Button ===
if st.button("Apply"):
    if city:
        params = {
            "q": city,
            "appid": API_KEY
        }

        try:
            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if data.get("cod") != 200:
                st.error(f"City not found: {city}")
            else:
                weather = data["main"]
                wind = data["wind"]

                # Extract weather details
                def k_to_c(k): return round(k - 273.15, 2)
                min_temp = k_to_c(weather["temp_min"])
                max_temp = k_to_c(weather["temp_max"])
                humidity = weather["humidity"]
                pressure = weather["pressure"]
                wind_speed = wind["speed"]
                rainfall = data.get("rain", {}).get("1h", 0.0)
                rain_today = 1 if rainfall > 0 else 0

                st.success(f"✅ Live Weather for {city.title()}")
                st.write(f"🌡️ Min Temp: {min_temp} °C")
                st.write(f"🌡️ Max Temp: {max_temp} °C")
                st.write(f"💧 Humidity: {humidity}%")
                st.write(f"🌬️ Wind Speed: {wind_speed} km/h")
                st.write(f"🌧️ Rainfall (last 1h): {rainfall} mm")
                st.write(f"📈 Pressure: {pressure} hPa")

                # === ML Prediction ===
                input_data = np.array([[min_temp, max_temp, rainfall, wind_speed, humidity, pressure, rain_today]])
                prediction = model.predict(input_data)[0]
                result = "🌧️ Rain Expected Tomorrow!" if prediction == 1 else "☀️ No Rain Expected Tomorrow!"
                st.subheader("🤖 AI Prediction")
                st.info(result)

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a city name.")

# === Show Sample Data (Optional) ===
with st.expander("📊 View Sample Weather Data"):
    try:
        df = pd.read_csv("data.csv")
        st.dataframe(df.head())
    except:
        st.warning("data.csv not found.")
