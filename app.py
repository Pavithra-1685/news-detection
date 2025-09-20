import streamlit as st
import pickle
import pandas as pd


@st.cache_resource
def load_model():
    with open("models/model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("models/vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model()

# ------------------------
# Streamlit UI
# ------------------------
st.title("📰 Fake News Detection App")
st.write("Check if a news article is **Fake** or **Real** using Logistic Regression.")

# User input
title = st.text_input("Enter the news title:")
text = st.text_area("Enter the news content:")

if st.button("Predict"):
    if text.strip() or title.strip():
        content = title + " " + text
        input_tfidf = vectorizer.transform([content])
        prediction = model.predict(input_tfidf)[0]

        if prediction.lower() == "fake":
            st.error("🚨 This news seems **FAKE**.")
        else:
            st.success("✅ This news seems **REAL**.")
    else:
        st.warning("Please enter either title or text of the news.")
