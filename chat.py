from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv(override=True) # This method will load the .env file variables to the environment variables


client = OpenAI()

models = client.models.list().model_dump()

model_ids = [item['id'] for item in models['data']]

for model_id in model_ids:
    print(model_id)
    
history = [
    {"role": "system", "content": "You are a professional debater, and my proposition is that Chat GPT is the best LLM ever."},
]

while True:
    prompt = input("> ")
    history.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",
        messages=history
    )

    assistant_output = completion.choices[0].message.content
    print(assistant_output)
    print()

    print("Used",completion.usage.total_tokens,"tokens")


    history.append({"role": "assistant", "content": assistant_output})

