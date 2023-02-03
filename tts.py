import streamlit as st
import pyttsx3

st.set_page_config(page_title="Text to Speech Converter",
                  page_icon=":microphone:",
                  layout="wide")

engine = pyttsx3.init()

def tts(text, voice):
    if voice == 'Male':
        engine.setProperty('voice', 'male')
    else:
        engine.setProperty('voice', 'female')
    engine.say(text)
    engine.runAndWait()

text = st.text_area("Enter text here:")
voice = st.selectbox("Select Voice:", ["Male", "Female"])
if st.button("Convert to Speech"):
    tts(text, voice)
