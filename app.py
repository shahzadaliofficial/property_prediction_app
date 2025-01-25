import streamlit as st
import joblib

# Load the pre-trained SVM model
model = joblib.load("svm_model.pkl")

def predict(input_data):
    """Function to predict using the SVM model."""
    prediction = model.predict([input_data])
    return prediction

# Streamlit app configuration
st.set_page_config(page_title="SVM Prediction App", layout="centered", page_icon="🤖")

# Common CSS styles with a constant color scheme
CONSTANT_STYLE = """
      <style>
    :root {
        --primary-bg: #ffffff; /* Light background */
        --secondary-bg: #0d1117; /* Dark background */
        --primary-text: #24292e; /* Light text */
        --secondary-text: #c9d1d9; /* Dark text */
        --accent-color: #4CAF50; /* Green accent */
        --button-hover: #45a049; /* Darker green for hover */
    }

    .stApp {
        background-color: var(--primary-bg);
        color: var(--primary-text);
        font-family: 'Arial', sans-serif;
    }
    body[data-color-mode="dark"] .stApp {
        background-color: var(--secondary-bg);
        color: var(--secondary-text);
    }
    .title {
        font-size: 36px;
        color: var(--accent-color);
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        background-color: var(--accent-color);
        color: white;
        font-size: 16px;
        border-radius: 5px;
        padding: 10px 20px;
    }
    .stButton>button:hover {
        background-color: var(--button-hover);
    }
    .stNumberInput input, .stSelectbox select {
        border-radius: 5px;
        border: 1px solid #cccccc;
        padding: 5px;
        font-size: 14px;
    }
    </style>
"""

# Apply the constant style
st.markdown(CONSTANT_STYLE, unsafe_allow_html=True)

# App title
st.markdown("<div class='title'>SVM Prediction App 🤖</div>", unsafe_allow_html=True)

# Input form
with st.form("prediction_form"):
    st.subheader("Input User Data")
    gender = st.selectbox("Gender", ["Male", "Female"], index=0, help="Select the gender.")
    age = st.number_input("Age", min_value=0, max_value=100, step=1, placeholder="Enter age")
    salary = st.number_input("Estimated Salary", min_value=0, step=1000, placeholder="Enter estimated salary")

    # Submit button
    submitted = st.form_submit_button("Predict")

    if submitted:
        # Preprocess input
        gender_numeric = 1 if gender == "Male" else 0
        user_input = [gender_numeric, age, salary]

        # Predict
        result = predict(user_input)

        # Display result
        st.markdown("### Prediction Result:")
        st.success(f"The user is predicted to {'Purchase' if result[0] == 1 else 'Not Purchase'} the product.")
