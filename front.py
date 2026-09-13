import streamlit as st
import pandas as pd
import pickle

# --------------------------------------------------
# Load trained model
# --------------------------------------------------

with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

# Get the exact columns used during training
feature_names = model.feature_names_in_

# --------------------------------------------------
# Page
# --------------------------------------------------

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️",
    layout="wide"
)

st.title("❤️ Heart Disease Prediction App")
st.write("Enter the patient's information below.")

st.divider()

# --------------------------------------------------
# Input fields
# --------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=40
    )

    sex = st.selectbox(
        "Sex (1 = Male, 0 = Female)",
        [1, 0]
    )

    cp = st.selectbox(
        "Chest Pain Type",
        [0, 1, 2, 3]
    )

    trestbps = st.number_input(
        "Resting Blood Pressure",
        min_value=50,
        max_value=250,
        value=120
    )

    chol = st.number_input(
        "Cholesterol",
        min_value=50,
        max_value=600,
        value=200
    )

    fbs = st.selectbox(
        "Fasting Blood Sugar",
        [0, 1]
    )

    restecg = st.selectbox(
        "Resting ECG",
        [0, 1, 2]
    )


with col2:

    thalach = st.number_input(
        "Maximum Heart Rate",
        min_value=50,
        max_value=250,
        value=150
    )

    exang = st.selectbox(
        "Exercise Induced Angina",
        [0, 1]
    )

    oldpeak = st.number_input(
        "ST Depression (Oldpeak)",
        min_value=0.0,
        max_value=10.0,
        value=1.0,
        step=0.1
    )

    slope = st.selectbox(
        "Slope",
        [0, 1, 2]
    )

    ca = st.selectbox(
        "Number of Major Vessels",
        [0, 1, 2, 3, 4]
    )

    thal = st.selectbox(
        "Thalassemia",
        [0, 1, 2, 3]
    )

# --------------------------------------------------
# Store all possible inputs
# --------------------------------------------------

all_inputs = {
    "age": age,
    "sex": sex,
    "cp": cp,
    "trestbps": trestbps,
    "chol": chol,
    "fbs": fbs,
    "restecg": restecg,
    "thalach": thalach,
    "exang": exang,
    "oldpeak": oldpeak,
    "slope": slope,
    "ca": ca,
    "thal": thal
}

# --------------------------------------------------
# Create dataframe using EXACT training columns
# --------------------------------------------------

user_data = pd.DataFrame(
    [[all_inputs[column] for column in feature_names]],
    columns=feature_names
)

# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.divider()

if st.button("🔍 Predict", use_container_width=True):

    prediction = model.predict(user_data)

    if prediction[0] == 1:

        st.error(
            "⚠️ The model predicts a higher likelihood of heart disease."
        )

    else:

        st.success(
            "✅ The model predicts a lower likelihood of heart disease."
        )

    # Show probability if available
    if hasattr(model, "predict_proba"):

        probability = model.predict_proba(user_data)[0][1]

        st.write(
            f"Estimated probability: **{probability * 100:.2f}%**"
        )