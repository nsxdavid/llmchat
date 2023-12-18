from dotenv import load_dotenv
import os
from openai import OpenAI
import json

load_dotenv(override=True) # This method will load the .env file variables to the environment variables


client = OpenAI()

# models = client.models.list().model_dump()
# model_ids = [item['id'] for item in models['data']]
# for model_id in model_ids:
#     print(model_id)
    
history = [
    {"role": "system", "content": "You are smarter than you look, but your responses must always sound like like a hillbilly."},
]

print("Howdy, I hear you want to jaw about something. Well whatcha got on your mind?")

while True:
    prompt = input("> ")
    history.append({"role": "user", "content": prompt})

    completion = client.chat.completions.create(
        model="gpt-4-1106-preview",  # Chat-GPT4-Turbo Preview (update this as necessary)
        messages=history
    )

    assistant_output = completion.choices[0].message.content
    print(assistant_output)
    print()

    history.append({"role": "assistant", "content": assistant_output})

