"""
Capture audio from the microphone and convert speech to text using Google's Speech Recognition API.

Requirements:
    - Python 3.x
    - SpeechRecognition library
    - PyAudio library (required for microphone input)

Install dependencies:
    pip install SpeechRecognition
    # For PyAudio, installation depends on OS:
    # Windows: pip install pipwin
    #          pipwin install pyaudio
    # macOS/Linux: install portaudio headers, then pip install pyaudio

Usage:
    1. Ensure your microphone is connected and working.
    2. Run the script:
        python speech_to_text.py
    3. Speak clearly when prompted.
    4. The recognized text will be printed to the console.

Author: Sachin Kumar
GitHub: https://github.com/sachin-py

"""

import speech_recognition as sr


def listen_and_recognize(timeout=10):
    """
    Listen to microphone input and recognize speech.

    Args:
        timeout (int): Maximum seconds to wait for phrase to start.

    Returns:
        str: Recognized speech as text.

    Raises:
        sr.UnknownValueError: Speech was unintelligible.
        sr.RequestError: Could not request results from Google API.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        audio = recognizer.listen(source, timeout=timeout)
    return recognizer.recognize_google(audio)


if __name__ == "__main__":
    try:
        result = listen_and_recognize()
        print(f"Recognized text: {result}")
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError as e:
        print(
            f"Could not request results from Google Speech Recognition service; {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
