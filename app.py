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

# App title
st.title("SVM Prediction App 🤖")
st.markdown(
    """
    <style>
    .stApp {
        background-color: #f8f9fa;
    }
    .title {
        font-size: 36px;
        color: #333333;
        font-family: 'Arial', sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<div class='title'>Predict Purchase Likelihood</div>", unsafe_allow_html=True)

# Input form
with st.form("prediction_form"):
    st.subheader("Input User Data")
    gender = st.selectbox("Gender", ["Male", "Female"], index=0)
    age = st.number_input("Age", min_value=0, max_value=100, step=1, value=25)
    salary = st.number_input("Estimated Salary", min_value=0, step=1000, value=20000)

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
