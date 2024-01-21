import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

print("Welcome to RoboSpeaker 1.1")
engine.say("Welcome to RoboSpeaker 1.1")
engine.runAndWait()

# Get a list of available voices
voices = engine.getProperty('voices')

# Print the available voices
print("Available voices:")
for i, voice in enumerate(voices):
    print(f"{i + 1}. {voice.name}")

while True:
    x = input("Enter what you want me to speak (or type 'quit' to exit): ")

    if x.lower() == 'quit':
        break  # Exit the loop if the user inputs 'quit'

    # Ask the user to select a voice
    voice_choice = input("Choose a voice (Enter the number): ")
    try:
        voice_index = int(voice_choice) - 1
        if 0 <= voice_index < len(voices):
            engine.setProperty('voice', voices[voice_index].id)
        else:
            print("Invalid voice choice. Using the default voice.")
    except ValueError:
        print("Invalid input. Using the default voice.")

    # Say the input text
    engine.say(x)

    # Wait for the speech to finish
    engine.runAndWait()

print("Goodbye! RoboSpeaker is now exiting.")
engine.say("Goodbye! RoboSpeaker is now exiting.")
engine.runAndWait()