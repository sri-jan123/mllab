import streamlit as st
import pickle
import numpy as np

with open("logistic_regression_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Diabetes Prediction App")

st.header("Enter the following details:")

gender = st.selectbox("Gender", ("Male", "Female"))
age = st.slider("Age", 1, 100, 25)
hypertension = st.selectbox("Hypertension", ("No", "Yes"))
heart_disease = st.selectbox("Heart Disease", ("No", "Yes"))
smoking_history = st.selectbox(
    "Smoking History",
    ("never", "former", "current", "ever", "not current", "No Info")
)
bmi = st.slider("BMI", 10.0, 50.0, 25.0)
hba1c_level = st.slider("HbA1c Level", 3.0, 15.0, 5.5)
blood_glucose_level = st.slider("Blood Glucose Level", 50, 300, 120)

gender = 1 if gender == "Male" else 0
hypertension = 1 if hypertension == "Yes" else 0
heart_disease = 1 if heart_disease == "Yes" else 0

smoking_history_dict = {
    "never": 4,
    "former": 2,
    "current": 1,
    "ever": 0,
    "not current": 3,
    "No Info": 5
}
smoking_history = smoking_history_dict[smoking_history]

input_data = np.array([[gender, age, hypertension, heart_disease, smoking_history, bmi, hba1c_level, blood_glucose_level]])
prediction = model.predict(input_data)[0]

if st.button("Predict"):
    if prediction == 1:
        st.write("The model predicts that this person **has diabetes**.")
    else:
        st.write("The model predicts that this person **does not have diabetes**.")
