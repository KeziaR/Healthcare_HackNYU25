import requests as rq
from google import genai
import config


client = genai.Client(api_key=INFO.config)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="Explain how AI works",
)

print(response.text)