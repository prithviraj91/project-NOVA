import os
import tempfile

from dotenv import load_dotenv
from openai import OpenAI
from playsound import playsound

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def speak(text):
    print(f"NOVA: {text}")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_path = temp_audio.name

    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="alloy",
        input=text,
    ) as response:
        response.stream_to_file(temp_path)

    playsound(temp_path)

    os.remove(temp_path)