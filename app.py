import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("multi_target_model.pkl")

st.title("AI-Driven Manufacturing Intelligence")

st.header("Enter Batch Parameters")

temp = st.number_input("Temperature", value=180.0)
pressure = st.number_input("Pressure", value=5.0)
hold = st.number_input("Hold Time", value=60.0)
rpm = st.number_input("Machine RPM", value=1500.0)
load = st.number_input("Machine Load (%)", value=75.0)
batch_size = st.number_input("Batch Size", value=1000)

if st.button("Predict Batch Performance"):
    
    input_data = pd.DataFrame([[temp, pressure, hold, rpm, load, batch_size]],
                              columns=["Temperature", "Pressure", "Hold_Time",
                                       "Machine_RPM", "Machine_Load", "Batch_Size"])
    
    prediction = model.predict(input_data)
    
    energy = prediction[0][0]
    quality = prediction[0][1]
    yield_val = prediction[0][2]
    performance = prediction[0][3]
    
    carbon_factor = 0.82
    carbon_emission = energy * carbon_factor
    
    st.subheader("Prediction Results")
    st.write("Energy Consumption:", round(energy,2))
    st.write("Quality Score:", round(quality,2))
    st.write("Yield Percentage:", round(yield_val,2))
    st.write("Performance Index:", round(performance,2))
    st.write("Estimated Carbon Emission:", round(carbon_emission,2))
    
    if carbon_emission > 120:
        st.warning("Recommendation: Reduce Machine Load or RPM to meet carbon targets.")
    else:
        st.success("Batch within carbon limits.")