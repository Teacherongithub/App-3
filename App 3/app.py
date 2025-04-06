import streamlit as st
import speech_recognition as sr
from gtts import gTTS
import os
import time
from googletrans import Translator
import cv2
from PIL import Image
import numpy as np
import tempfile
from playsound import playsound

# Initialize the speech recognizer and translator
recognizer = sr.Recognizer()
translator = Translator()

def text_to_speech_urdu(text):
    """Convert text to Urdu speech"""
    tts = gTTS(text=text, lang='ur')
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
    tts.save(temp_file.name)
    playsound(temp_file.name)
    os.unlink(temp_file.name)

def speech_to_text():
    """Convert speech to text"""
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio, language='ur-PK')
            return text
        except sr.UnknownValueError:
            st.error("Could not understand the audio")
            return None
        except sr.RequestError:
            st.error("Could not request results")
            return None

def capture_photo():
    """Capture photo using webcam"""
    cap = cv2.VideoCapture(0)
    if cap.isOpened():
        ret, frame = cap.read()
        if ret:
            # Convert BGR to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cap.release()
            return rgb_frame
    cap.release()
    return None

def main():
    st.title("اردو رجسٹریشن فارم")
    st.write("Welcome to Urdu Registration Form")

    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.responses = {}

    if st.session_state.step == 0:
        if st.button("شروع کریں (Start)"):
            text_to_speech_urdu("آپ کا نام کیا ہے؟")
            st.session_state.step = 1

    elif st.session_state.step == 1:
        st.write("آپ کا نام کیا ہے؟")
        if st.button("بولیں (Speak)"):
            name = speech_to_text()
            if name:
                st.session_state.responses['name'] = name
                st.write(f"آپ کا نام: {name}")
                st.session_state.step = 2
                text_to_speech_urdu("آپ کی عمر کیا ہے؟")

    elif st.session_state.step == 2:
        st.write("آپ کی عمر کیا ہے؟")
        age = st.number_input("Age", min_value=0, max_value=150)
        if st.button("Next"):
            if age > 60:
                st.error("معذرت، آپ کی عمر زیادہ ہے")
                text_to_speech_urdu("معذرت، آپ کی عمر زیادہ ہے")
                st.session_state.step = 0
            else:
                st.session_state.responses['age'] = age
                st.session_state.step = 3
                text_to_speech_urdu("آپ کی جنس کیا ہے؟")

    elif st.session_state.step == 3:
        st.write("آپ کی جنس کیا ہے؟")
        if st.button("بولیں (Speak)"):
            gender = speech_to_text()
            if gender:
                st.session_state.responses['gender'] = gender
                st.write(f"آپ کی جنس: {gender}")
                st.session_state.step = 4
                text_to_speech_urdu("آپ کے سربراہ کا شناختی کارڈ نمبر کیا ہے؟")

    elif st.session_state.step == 4:
        st.write("آپ کے سربراہ کا شناختی کارڈ نمبر کیا ہے؟")
        nic = st.text_input("NIC Number", key="nic")
        if st.button("Next"):
            if len(nic) == 13 and nic.isdigit():
                st.session_state.responses['nic'] = nic
                st.session_state.step = 5
                text_to_speech_urdu("براہ کرم اپنی تصویر کھینچنے کے لیے تیار ہو جائیں")
            else:
                st.error("براہ کرم درست شناختی کارڈ نمبر درج کریں")

    elif st.session_state.step == 5:
        st.write("اپنی تصویر کھینچیں")
        if st.button("تصویر کھینچیں (Capture Photo)"):
            photo = capture_photo()
            if photo is not None:
                st.image(photo, caption="آپ کی تصویر")
                st.session_state.responses['photo'] = photo
                st.session_state.step = 6
            else:
                st.error("تصویر کھینچنے میں مسئلہ")

    elif st.session_state.step == 6:
        st.success("رجسٹریشن مکمل ہو گئی!")
        text_to_speech_urdu("آپ کی رجسٹریشن مکمل ہو گئی ہے۔ شکریہ")
        st.write("### Submitted Information:")
        for key, value in st.session_state.responses.items():
            if key != 'photo':
                st.write(f"{key}: {value}")
        if 'photo' in st.session_state.responses:
            st.image(st.session_state.responses['photo'], caption="Captured Photo")
        
        if st.button("نئی رجسٹریشن (New Registration)"):
            st.session_state.step = 0
            st.session_state.responses = {}
            st.experimental_rerun()

if __name__ == "__main__":
    main() 