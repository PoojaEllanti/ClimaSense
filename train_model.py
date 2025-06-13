import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import joblib

# Load data
df = pd.read_csv("data.csv")

# Encode labels
df["RainToday"] = LabelEncoder().fit_transform(df["RainToday"])
df["RainTomorrow"] = LabelEncoder().fit_transform(df["RainTomorrow"])

# Features and label
X = df[["MinTemp", "MaxTemp", "Rainfall", "WindSpeed", "Humidity", "Pressure", "RainToday"]]
y = df["RainTomorrow"]

# Train model
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save locally
joblib.dump(model, "weather_model.pkl")
print("✅ Model saved as weather_model.pkl")
