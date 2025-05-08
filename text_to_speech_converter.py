import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Define the message
message = (
    "Hello! You are listening to Python Learning Squad, "
    "a dedicated channel for learning Python programming. "
    "We appreciate your support—please help us grow by subscribing. "
    "Thank you for being part of our learning community."
)

# Speak the message
engine.say(message)
engine.runAndWait()

# Stop the engine
engine.stop()
