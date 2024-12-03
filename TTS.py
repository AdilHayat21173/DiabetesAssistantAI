import os
import logging
from deepgram.utils import verboselogs
from dotenv import load_dotenv 


# Load environment variables from .env file
load_dotenv()

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)


filename = "test.mp3"


def TTS(text):
    try:
        SPEAK_TEXT = {"text": text}
        # STEP 1 Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=os.getenv("DG_API_KEY"))

        # STEP 2 Call the save method on the speak property
        options = SpeakOptions(
            model="aura-asteria-en",
        )

        response = deepgram.speak.rest.v("1").save(filename, SPEAK_TEXT, options)
        return filename
    
    except Exception as e:
        print(f"Exception: {e}")

if __name__ == "__main__":
    TTS("Hello this is text")