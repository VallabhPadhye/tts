import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Text to Speech Converter",
                  page_icon=":microphone:",
                  layout="wide")

def tts(text, lang):
    tts = gTTS(text=text, lang=lang)
    tts.save("output.mp3")

text = st.text_area("Enter text here:")
lang = st.selectbox("Choose language:", ["English", "Hindi", "Spanish"])
if st.button("Convert to Speech"):
    tts(text, lang.lower())
    st.audio("output.mp3", format="audio/mp3")
