# ❤️ Heart Disease Prediction

A machine learning web application that predicts the likelihood of heart disease based on patient health information. The project uses a trained machine learning model and an interactive Streamlit interface.

## Live Demo

🔗 [Open the deployed application](https://heart-disease-prediction-roshni.streamlit.app/)

## Features

- Simple and interactive Streamlit user interface
- Accepts important patient health inputs
- Predicts the likelihood of heart disease
- Uses a trained machine learning model
- Deployed online using Streamlit Community Cloud

## Input Features

The application collects the following information:

- Age
- Sex
- Chest pain type
- Resting blood pressure
- Cholesterol level
- Fasting blood sugar
- Resting ECG result
- Maximum heart rate
- Exercise-induced angina
- ST depression (Oldpeak)
- Slope
- Number of major vessels
- Thalassemia

## Tech Stack

- Python
- Streamlit
- Pandas
- Scikit-learn
- Machine Learning

## Project Structure

```text
heart-disease-prediction/
│
├── front.py              # Streamlit web application
├── herat.py              # Model training script
├── heart_model.pkl       # Trained machine learning model
├── heart.csv             # Dataset
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
```

## Run Locally

1. Clone the repository:

```bash
git clone [https://github.com/roshnirawat909/heart-disease-prediction.git](https://github.com/roshnirawat909/heart-disease-prediction.git)
```

2. Move into the project folder:

```bash
cd heart-disease-prediction
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit application:

```bash
streamlit run front.py
```

5. Open the local URL shown in your terminal, usually:

```text
http://localhost:8501
```

## Disclaimer

This application is created for educational and demonstration purposes only. It does not provide medical advice, diagnosis, or treatment. Always consult a qualified healthcare professional for medical guidance.

## Author

**Roshni Rawat**

- GitHub: [@roshnirawat909](https://github.com/roshnirawat909)
- Live App: [Heart Disease Prediction](https://heart-disease-prediction-roshni.streamlit.app/)
