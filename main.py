'''example completion with openai > 1.1'''
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()  # This line brings all environment variables from .env into os.environ
OPEN_AI_KEY = os.environ['OPEN_AI_KEY']
client = OpenAI(api_key=OPEN_AI_KEY)

while True:
    prompt = input("Type your propmt: ")
    response = client.completions.create(
        prompt=prompt,
        model="gpt-3.5-turbo-instruct",
        top_p=0.5, max_tokens=1500,
        stream=True)

    res = ""
    for part in response:
        res+=part.choices[0].text + " "
    print(res)