# speech_to_text.py

import speech_recognition as sr

# Initialize recognizer
recognizer = sr.Recognizer()

# Load the audio file
audio_file = "sample.wav"  # Replace with your .wav file

# Use audio file as source
with sr.AudioFile(audio_file) as source:
    print("🎧 Listening to audio...")
    audio_data = recognizer.record(source)  # read entire audio file

# Try converting speech to text
try:
    print("\n📝 Transcribing...")
    text = recognizer.recognize_google(audio_data)
    print("\n--- Transcription ---")
    print(text)

except sr.UnknownValueError:
    print("😕 Could not understand audio")
except sr.RequestError:
    print("❌ Could not request results (check internet connection)")
