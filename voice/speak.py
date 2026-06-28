import pyttsx3

engine = pyttsx3.init()

engine.setProperty("rate", 220)

voices = engine.getProperty("voices")

if voices:
    engine.setProperty("voice", voices[0].id)


def speak(text):
    print(f"NOVA: {text}")   # Shows what NOVA is saying

    engine.stop()            # Clears any previous speech

    engine.say(text)

    engine.runAndWait()