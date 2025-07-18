# 🗣️ Speech Recognition System

This is a Python-based speech-to-text tool that converts spoken audio (from `.wav` files) into written text using the `SpeechRecognition` library and Google Web Speech API.

## ✅ Task Description

**Task 2 – Speech Recognition System**  
- **Instruction**: Build a basic speech-to-text system using pre-trained models and libraries like `SpeechRecognition` or `Wav2Vec`.  
- **Deliverable**: A functional system capable of transcribing short audio clips.

---

## 🚀 Features

- Converts speech in `.wav` files to readable text
- Uses the Google Web Speech API via the `SpeechRecognition` library
- Supports short, clear voice recordings
- Easy to run and customize

---

## 📂 Project Structure
```
speech-recognition-system/
│
├── speech_to_text.py # Main Python script
├── sample.wav # Sample audio file (user recorded)
├── requirements.txt # Required Python packages
└── README.md # Project documentation
```
🛠️ Requirements

- Python 3.8 or later
- Internet connection (for Google API)
- Required libraries:
  - `SpeechRecognition`
  - `PyAudio` (only if you want microphone input)
  - `wave` (built-in)

📦 Installation

Install the required libraries using:
pip install -r requirements.txt

How to Use
Place a short .wav audio clip in the project directory and rename it to sample.wav

Run the script:
python speech_to_text.py
