import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Text to Speech Converter",
                  page_icon=":microphone:",
                  layout="wide")

def tts(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

text = st.text_area("Enter text here:")
if st.button("Convert to Speech"):
    tts(text)
    st.audio("output.mp3", format="audio/mp3")
