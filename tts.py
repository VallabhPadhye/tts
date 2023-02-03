import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Text to Speech Converter",
                  page_icon=":microphone:",
                  layout="wide")

def tts(text, voice):
    tts = gTTS(text=text, lang='en', gender=voice)
    tts.save("output.mp3")

text = st.text_area("Enter text here:")
voice = st.selectbox("Choose voice:", ["Male", "Female"])
if st.button("Convert to Speech"):
    tts(text, voice.lower()[0])
    st.audio("output.mp3", format="audio/mp3")
