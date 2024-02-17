import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()

while True:

    try:

        with sr.Microphone() as mic:
            
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            txt = recognizer.recognize_whisper(audio)
            txt = txt.lower()

            print(f"{txt}")
    except sr.UnknownValueError():
        recognizer = sr.Recognizer()
        continue