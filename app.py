import streamlit as st
import joblib
import numpy as np
import os

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(page_title="Iris Classifier Demo 🌸", page_icon="🌿", layout="centered")

# ---------------------------
# Load Model
# ---------------------------
MODEL_PATH = os.environ.get("MODEL_PATH", "artifacts/model.pkl")
model = joblib.load(MODEL_PATH)

# Iris classes
CLASSES = ["Setosa", "Versicolor", "Virginica"]

# ---------------------------
# UI Layout
# ---------------------------
st.title("🌸 Iris Flower Classifier")
st.markdown(
    """
    This demo predicts the **species of Iris flower** based on four features:
    - Sepal Lengt
    - Sepal Width  
    - Petal Length  
    - Petal Width  

    The model was trained on the famous [Iris dataset](https://archive.ics.uci.edu/ml/datasets/iris).
    """
)

# Sidebar for user inputs
st.sidebar.header("🔧 Input Features")
sepal_len = st.sidebar.slider("Sepal Length (cm)", 4.0, 8.0, 5.1)
sepal_wid = st.sidebar.slider("Sepal Width (cm)", 2.0, 4.5, 3.5)
petal_len = st.sidebar.slider("Petal Length (cm)", 1.0, 7.0, 1.4)
petal_wid = st.sidebar.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Button to predict
if st.sidebar.button("🚀 Predict"):
    x = np.array([[sepal_len, sepal_wid, petal_len, petal_wid]])
    pred = model.predict(x)[0]
    probs = model.predict_proba(x)[0]

    st.subheader("🔮 Prediction Result")
    st.success(f"Predicted class: **{CLASSES[pred]}**")

    st.markdown("### 📊 Prediction Confidence")
    st.progress(int(probs[pred] * 100))
    st.write(
        {CLASSES[i]: f"{probs[i]*100:.2f}%" for i in range(len(CLASSES))}
    )

# ---------------------------
# Add Sample Test Cases
# ---------------------------
st.sidebar.markdown("---")
st.sidebar.subheader("📌 Try Sample Cases")
if st.sidebar.button("Setosa Example"):
    st.sidebar.write("Setosa values loaded.")
    st.experimental_set_query_params(example="setosa")
    st.sidebar.text("Sepal: 5.1 x 3.5\nPetal: 1.4 x 0.2")

if st.sidebar.button("Versicolor Example"):
    st.sidebar.write("Versicolor values loaded.")
    st.sidebar.text("Sepal: 6.0 x 2.9\nPetal: 4.5 x 1.5")

if st.sidebar.button("Virginica Example"):
    st.sidebar.write("Virginica values loaded.")
    st.sidebar.text("Sepal: 6.7 x 3.0\nPetal: 5.2 x 2.3")

# Footer
st.markdown("---")
