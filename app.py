import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load the trained model
model = pickle.load(open('fitness_model.pkl', 'rb'))

# Streamlit app title
st.title("Personal Fitness Tracker")

# Sidebar for user inputs
st.sidebar.header("User Inputs")

# Age
age = st.sidebar.slider("Age", 10, 80, 25)

# Gender
gender = st.sidebar.selectbox("Gender", ("Male", "Female"))

# BMI
bmi = st.sidebar.slider("BMI", 10.0, 50.0, 22.0)

# Duration (in minutes)
duration = st.sidebar.slider("Duration of Exercise (minutes)", 0, 300, 30)

# Heart Rate
heart_rate = st.sidebar.slider("Heart Rate", 60, 200, 110)

# Body Temperature
body_temp = st.sidebar.slider("Body Temperature (°F)", 90.0, 110.0, 98.6)

# Prepare input data for prediction
input_data = pd.DataFrame({
    'Age': [age],
    'BMI': [bmi],
    'Duration': [duration],
    'Heart_Rate': [heart_rate],
    'Body_Temp': [body_temp],
    'Gender': [1 if gender == "Male" else 0]
})

# Display user input
st.subheader("User Input:")
st.write(input_data)

# Make prediction
prediction = model.predict(input_data)[0]

# Display the prediction
st.subheader("Predicted Calories Burned:")
st.write(f"{prediction:.2f} calories")
