from dotenv import load_dotenv
import os

import google.generativeai as genai

load_dotenv()

print()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])


while True:
	user_input = input("> ")
	response = chat.send_message(user_input)
	print(response.text)
