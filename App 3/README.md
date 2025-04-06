# Urdu Voice Registration Chatbot

This is a Streamlit-based application that implements an Urdu voice chatbot for registration purposes. The chatbot interacts with users in Urdu, collecting information through voice input and form fields.

## Features

- Voice interaction in Urdu
- Name collection through voice input
- Age verification
- Gender collection through voice input
- NIC number validation
- Photo capture using webcam
- Complete registration summary

## Requirements

- Python 3.7+
- Webcam
- Microphone
- Internet connection (for speech recognition)

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```

## Running the Application

To run the application, execute:
```bash
streamlit run app.py
```

## Usage

1. Click "Start" to begin the registration process
2. Follow the voice prompts in Urdu
3. Speak clearly when providing voice input
4. Enter the NIC number manually
5. Allow camera access when prompted for photo
6. Review your submission at the end

## Note

- Make sure your microphone is properly configured
- Ensure you have a working webcam for photo capture
- The application requires an internet connection for speech recognition
- The age limit is set to 60 years 