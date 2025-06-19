# 🚲 Bike Sharing Demand Prediction

This project predicts the number of rented bikes based on environmental and seasonal features in Seoul, South Korea, using a regression-based Machine Learning model. It includes full model development, evaluation, and a user-friendly Streamlit frontend.

---

## 📁 Dataset

- **Source**: [Seoul Bike Sharing Demand Dataset](https://www.kaggle.com/datasets)
- **Attributes**:
  - Temperature (°C)
  - Humidity (%)
  - Wind speed (m/s)
  - Visibility (10m)
  - Dew point temperature (°C)
  - Solar Radiation (MJ/m²)
  - Rainfall (mm)
  - Snowfall (cm)
  - Hour of the day
  - Season, Holiday, Functioning Day

---

## 📊 Project Workflow

### 1. 🧹 Data Preprocessing

- Converted date column to datetime format
- Extracted hour and day-related features
- One-hot encoded categorical variables
- Removed outliers and null values

### 2. 📈 Exploratory Data Analysis (EDA)

Visualizations used:

- 📉 Demand vs Hour  
- 📊 Demand vs Temperature  
- 🌧️ Demand vs Rainfall  
- ❄️ Demand vs Snowfall  
- 📆 Demand by Season/Holiday

![image](https://github.com/user-attachments/assets/490ec2fd-2a2c-4072-851f-3554cf2417d5)

![image](https://github.com/user-attachments/assets/bb916218-0c39-4f06-a0d2-6489dcfee02b)

![image](https://github.com/user-attachments/assets/6eca020b-6a57-4304-864f-25d87f5b40c9)

![image](https://github.com/user-attachments/assets/0017846b-7a57-4577-8563-a5bd7ba748ed)

![image](https://github.com/user-attachments/assets/ea2745b6-0c4d-4f0e-87b0-ea0b85d05231)

![image](https://github.com/user-attachments/assets/e301242e-c994-4737-8639-b2bde1a44a08)



---

### 3. 🤖 Model Training

- Model Used: `RandomForestRegressor`
- Features: 18 total (including one-hot encoded Season, Holiday, etc.)
- Target: `Rented Bike Count`

✅ Saved model as `.joblib` for faster loading  
✅ Saved `feature_columns.pkl` for prediction input structure  

---

### 4. 📊 Model Evaluation

| Metric              | Score      |
|---------------------|------------|
| **MAE** (Mean Absolute Error)   | ~330 |
| **MSE** (Mean Squared Error)    | ~226,000 |
| **R² Score**        | ~0.82      |


---

## 🌐 Streamlit Frontend

Built a dynamic frontend to allow:

- 📥 Manual input of weather/time parameters
- 🧪 Benchmark scenarios (Sunny Morning, Rainy Evening, Cold Night)
- 📊 Real-time prediction of bike demand
- 📸 Enhanced UI with emojis and streamlined layout

![image](https://github.com/user-attachments/assets/38b63aed-ff6b-4247-a181-f8753c887742)

---

### ▶️ Demo Video

📽️ A **demo video** showing the working of the app is available in this repository.

---

## 🧠 How to Run

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run Streamlit App
streamlit run bike_demand_app.py
Ensure the following files exist:

bike_demand_model.joblib

feature_columns.pkl

📂 Folder Structure
Copy
Edit
├── bike_demand_app.py
├── bike_demand_model.joblib
├── feature_columns.pkl
├── demo.mp4
├── assets/
│   ├── eda_temp_vs_demand.png
│   ├── eda_hour_vs_demand.png
│   └── ...
└── README.md
📬 Author
Developed by V. Yuvan Krishnan
Machine Learning Intern, 2025
✉️ Feel free to connect on GitHub or LinkedIn
