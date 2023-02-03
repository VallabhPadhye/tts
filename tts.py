import streamlit as st
from gtts import gTTS

st.set_page_config(page_title="Text to Speech Converter",
                  page_icon=":microphone:",
                  layout="wide")

def tts(text, voice):
    tts = gTTS(text=text, lang='hi', slow=False)
    if voice == 'Male':
        tts.voice = gTTS.VOICE_MALE_HI
    else:
        tts.voice = gTTS.VOICE_FEMALE_HI
    tts.save("output.mp3")

text = st.text_area("Enter text here:")
voice = st.selectbox("Select Voice:", ["Male", "Female"])
if st.button("Convert to Speech"):
    tts(text, voice)
    st.audio("output.mp3", format="audio/mp3")
