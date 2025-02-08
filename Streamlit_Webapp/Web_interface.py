import streamlit as st
import requests as rq
from google import genai
import config



st.title("TitleName")

client = genai.Client(api_key=config.INFO)

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="who is kylie jenner",
)

print(response.text)

st.html(body)