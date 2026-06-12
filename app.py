import streamlit as st
import joblib
import re
import string

model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")


def clean_text(text):

    text = text.lower()

    text = re.sub(r'\[.*?\]', '', text)

    text = re.sub(r'https?://\S+|www\.\S+', '', text)

    text = re.sub(r'<.*?>+', '', text)

    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)

    return text


st.title("📰 Fake News Detection")

news = st.text_area("Enter News Article")


if st.button("Predict"):

    news = clean_text(news)

    news = vectorizer.transform([news])

    prediction = model.predict(news)

    if prediction[0] == 1:
        st.success("✅ Real News")
    else:
        st.error("❌ Fake News")