import pyttsx3

print("Welcome to RoboSpeaker 1.0")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

while True:
    x = input("Enter what you want me to speak (or type 'quit' to exit): ")

    if x.lower() == 'quit':
        break  # Exit the loop if the user inputs 'quit'

    # Say the input text
    engine.say(x)

    # Wait for the speech to finish
    engine.runAndWait()

print("Goodbye! RoboSpeaker is now exiting.")
engine.say("Goodbye! RoboSpeaker is now exiting.")
engine.runAndWait()
