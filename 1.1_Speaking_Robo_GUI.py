import pyttsx3
import tkinter as tk
from tkinter import ttk

def speak_text():
    text = text_entry.get()
    if text.lower() == 'quit':
        root.destroy()
    else:
        selected_voice = voice_choice.get()
        if selected_voice == 'Male':
            engine.setProperty('voice', voices[0].id)  # Assuming the first voice is male.
        else:
            engine.setProperty('voice', voices[1].id)  # Assuming the second voice is female.
        engine.say(text)
        engine.runAndWait()

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Get a list of available voices
voices = engine.getProperty('voices')

root = tk.Tk()
root.title("RoboSpeaker 1.1")

main_frame = ttk.Frame(root, padding=10)
main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Text Entry
text_label = ttk.Label(main_frame, text="Enter what you want me to speak:")
text_label.grid(column=0, row=0, sticky=tk.W)

text_entry = ttk.Entry(main_frame, width=50)
text_entry.grid(column=1, row=0, columnspan=2, sticky=(tk.W, tk.E))

# Voice Selection
voice_label = ttk.Label(main_frame, text="Select a voice:")
voice_label.grid(column=0, row=1, sticky=tk.W)

voice_choice = tk.StringVar()
voice_choice.set("Male")

male_radio = ttk.Radiobutton(main_frame, text="Male", variable=voice_choice, value="Male")
female_radio = ttk.Radiobutton(main_frame, text="Female", variable=voice_choice, value="Female")

male_radio.grid(column=1, row=1, sticky=tk.W)
female_radio.grid(column=2, row=1, sticky=tk.W)

# Speak Button
speak_button = ttk.Button(main_frame, text="Speak", command=speak_text)
speak_button.grid(column=0, row=2, columnspan=3)

root.mainloop()