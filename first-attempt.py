from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()

# Accessing variables
api_key = f"{os.getenv("API_KEY")}"

from google import genai
import os

clientAi = genai.Client(api_key=api_key)

def aiDoYourThing(client, text):
    standard = ". Give me a response that a person in conversation would give with a quick response like a assistant that just quickly looked something up and summerized it but only summerize when needed."
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=text+standard
    )

    ## voice response
    from gtts import gTTS
    gTTS(text=response.text, lang="en", slow=False).save("response.mp3")
    os.system("response.mp3")

## loop until you hear voice command
command="boy"

import speech_recognition as sr
# open the file

r = sr.Recognizer()

while 1:
    with sr.Microphone() as source:
        # listen for the data (load audio to memory)
        r.adjust_for_ambient_noise(source, duration=0.1)
        audio_data = r.listen(source)
        # recognize (convert from speech to text)
        try:
            text = r.recognize_google(audio_data)
            if command in text:
                aiDoYourThing(client=clientAi, text=text.replace("boy", ""))
        except: 
            pass

# ## get response
