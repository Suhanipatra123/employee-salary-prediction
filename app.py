import streamlit as st
import pickle
import numpy as np

# Load Model
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# Page Settings
st.set_page_config(
    page_title="Employee Salary Prediction",
    page_icon="💰"
)

# Title
st.title("💰 Employee Salary Prediction")
st.write("Enter employee details below")

st.divider()

# Inputs
age = st.number_input(
    "Age",
    min_value=18,
    max_value=65,
    value=25
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education Level",
    ["Bachelor's", "Master's", "PhD"]
)

job_title = st.number_input(
    "Job Title Code",
    min_value=0,
    max_value=200,
    value=0
)

experience = st.number_input(
    "Years of Experience",
    min_value=0,
    max_value=40,
    value=1
)

# Encoding
gender_encoded = 1 if gender == "Male" else 0

education_dict = {
    "Bachelor's": 0,
    "Master's": 2,
    "PhD": 3
}

education_encoded = education_dict[education]

# Prediction
if st.button("Predict Salary"):

    input_data = np.array([
        [
            age,
            gender_encoded,
            education_encoded,
            job_title,
            experience
        ]
    ])

    prediction = model.predict(input_data)

    st.success(
        f"Predicted Salary: ₹ {prediction[0]:,.2f}"
    )

st.divider()

st.caption("Built with Streamlit & Machine Learning")