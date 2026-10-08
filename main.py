import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

apikey = os.environ.get("GEMINI_API_KEY")

print("API KEY FOUND:", apikey is not None)

client = genai.Client(api_key=apikey)

def get(prompt):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        input=prompt
    )

    return interaction.output_text