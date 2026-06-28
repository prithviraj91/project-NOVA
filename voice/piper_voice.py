import subprocess
import os
import winsound

PIPER_EXE = "piper/piper.exe"
VOICE_MODEL = "piper/voices/en_US-amy-medium.onnx"
OUTPUT_FILE = "piper/output.wav"


def speak(text):
    print(">>> speaker called",text)
    command = [
        PIPER_EXE,
        "--model",
        VOICE_MODEL,
        "--output_file",
        OUTPUT_FILE
    ]

    subprocess.run(
        command,
        input=text,
        text=True
    )

    winsound.PlaySound(
        OUTPUT_FILE,
        winsound.SND_FILENAME
    )

    if os.path.exists(OUTPUT_FILE):
        os.remove(OUTPUT_FILE)