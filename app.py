import streamlit as st
import joblib

#load the spam-ham file

model_nb = joblib.load('Spam-Ham')
st.title("Spam-Ham Classifier")
ip = st.text_input("Enter your text message")
op = model_nb.predict([ip])
if st.button("Predict"):
  st.title("Entered message is a")
  st.title(op[0].upper())
