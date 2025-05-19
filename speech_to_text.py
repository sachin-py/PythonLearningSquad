"""
speech_to_text.py

A simple script to capture audio from the microphone and convert speech
to text using Google's Speech Recognition API via the SpeechRecognition library.

Requirements:
    - Python 3.x
    - SpeechRecognition library
    - PyAudio library (required for microphone input)

Install dependencies using:
    pip install SpeechRecognition
    # For PyAudio, installation varies by OS.

Usage:
    1. Connect and configure your microphone.
    2. Run this script:
        python speech_to_text.py
    3. Speak clearly when prompted.
    4. The recognized text will be printed on the console.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print('Listening ....Please Speak')
    audio = recognizer.listen(source, timeout=10)

text = recognizer.recognize_google(audio)

print(f'text is : {text}')
