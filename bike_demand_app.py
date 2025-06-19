import streamlit as st

# Must be first Streamlit command
st.set_page_config(page_title="🚲 Bike Sharing Demand Predictor", layout="centered")

import pandas as pd
import numpy as np
import joblib
import pickle

# --- Load model and features ---
@st.cache_resource
def load_model_and_features():
    model = joblib.load("D:/ML PROJECTS/Bike Sharing Demand Prediction/bike_demand_model.joblib")
    with open("D:/ML PROJECTS/Bike Sharing Demand Prediction/feature_columns.pkl", "rb") as f:
        feature_columns = pickle.load(f)
    return model, feature_columns

model, feature_columns = load_model_and_features()

st.title("🚲 Bike Sharing Demand Predictor")
st.markdown("Predict the number of rented bikes based on weather and time conditions in Seoul 🌦️")

# --- Benchmark Scenarios ---
scenarios = {
    "🌤️ Sunny Morning (Spring Workday)": {
        "Hour": 9, "Temperature(°C)": 18.0, "Humidity(%)": 55, "Wind speed (m/s)": 2.5,
        "Visibility (10m)": 2000, "Dew point temperature(°C)": 8.0, "Solar Radiation (MJ/m2)": 0.6,
        "Rainfall(mm)": 0.0, "Snowfall (cm)": 0.0, "Functioning Day_Yes": 1,
        "Holiday_No Holiday": 1, "Season_Spring": 1
    },
    "🌧️ Rainy Evening (Autumn Holiday)": {
        "Hour": 18, "Temperature(°C)": 14.0, "Humidity(%)": 90, "Wind speed (m/s)": 3.0,
        "Visibility (10m)": 700, "Dew point temperature(°C)": 12.0, "Solar Radiation (MJ/m2)": 0.1,
        "Rainfall(mm)": 2.5, "Snowfall (cm)": 0.0, "Functioning Day_No": 1,
        "Holiday_Public Holiday": 1, "Season_Autumn": 1
    },
    "❄️ Cold Night (Winter No Holiday)": {
        "Hour": 22, "Temperature(°C)": -2.0, "Humidity(%)": 40, "Wind speed (m/s)": 1.0,
        "Visibility (10m)": 500, "Dew point temperature(°C)": -5.0, "Solar Radiation (MJ/m2)": 0.0,
        "Rainfall(mm)": 0.0, "Snowfall (cm)": 3.0, "Functioning Day_Yes": 1,
        "Holiday_No Holiday": 1, "Season_Winter": 1
    }
}

st.markdown("### 🧪 Select a Benchmark Scenario (Optional)")
scenario_name = st.selectbox("Choose a Scenario", ["Manual Input"] + list(scenarios.keys()))
scenario_values = scenarios.get(scenario_name, {})

# --- Input fields ---
st.markdown("### 📥 Input Features")
col1, col2 = st.columns(2)

with col1:
    hour = st.slider("Hour", 0, 23, value=scenario_values.get("Hour", 12))
    temperature = st.number_input("Temperature(°C)", value=scenario_values.get("Temperature(°C)", 20.0))
    humidity = st.slider("Humidity(%)", 0, 100, value=scenario_values.get("Humidity(%)", 50))
    wind_speed = st.number_input("Wind speed (m/s)", value=scenario_values.get("Wind speed (m/s)", 2.0))
    visibility = st.number_input("Visibility (10m)", value=scenario_values.get("Visibility (10m)", 1500))
    dew_point = st.number_input("Dew point temperature(°C)", value=scenario_values.get("Dew point temperature(°C)", 10.0))

with col2:
    solar = st.number_input("Solar Radiation (MJ/m2)", value=scenario_values.get("Solar Radiation (MJ/m2)", 0.5))
    rainfall = st.number_input("Rainfall(mm)", value=scenario_values.get("Rainfall(mm)", 0.0))
    snowfall = st.number_input("Snowfall (cm)", value=scenario_values.get("Snowfall (cm)", 0.0))
    func_day = st.selectbox("Functioning Day", ["Yes", "No"], index=0 if scenario_values.get("Functioning Day_Yes", 1) else 1)
    holiday = st.selectbox("Holiday", ["No Holiday", "Public Holiday", "Working Day"],
                           index=["No Holiday", "Public Holiday", "Working Day"].index(
                               next((k.split("_")[1] for k in scenario_values if k.startswith("Holiday_") and scenario_values[k] == 1), "No Holiday")
                           ))
    season = st.selectbox("Season", ["Autumn", "Spring", "Summer", "Winter"],
                          index=["Autumn", "Spring", "Summer", "Winter"].index(
                              next((k.split("_")[1] for k in scenario_values if k.startswith("Season_") and scenario_values[k] == 1), "Spring")
                          ))

# --- Construct Input DataFrame with One-Hot Encoding ---
input_dict = {
    "Hour": hour,
    "Temperature(°C)": temperature,
    "Humidity(%)": humidity,
    "Wind speed (m/s)": wind_speed,
    "Visibility (10m)": visibility,
    "Dew point temperature(°C)": dew_point,
    "Solar Radiation (MJ/m2)": solar,
    "Rainfall(mm)": rainfall,
    "Snowfall (cm)": snowfall,
    f"Functioning Day_{func_day}": 1,
    f"Holiday_{holiday}": 1,
    f"Season_{season}": 1
}

# Fill missing feature columns with 0
for col in feature_columns:
    if col not in input_dict:
        input_dict[col] = 0

# Order columns correctly
input_df = pd.DataFrame([[input_dict[col] for col in feature_columns]], columns=feature_columns)

# --- Predict Button ---
if st.button("📊 Predict Bike Demand"):
    try:
        prediction = model.predict(input_df)[0]
        st.success(f"🔮 Estimated Rented Bikes: `{int(prediction):,}`")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {e}")
