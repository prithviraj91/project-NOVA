import speech_recognition as sr

recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=0.1)

        recognizer.pause_threshold = 2.0
        recognizer.non_speaking_duration = 1.0
        recognizer.dynamic_energy_threshold = True

        audio = recognizer.listen(
            source,
            timeout=2,
            phrase_time_limit=10
        )

    try:
        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text

    except sr.UnknownValueError:
        print("I couldn't understand you.")
        return ""

    except sr.RequestError:
        print("Speech recognition service unavailable.")
        return ""