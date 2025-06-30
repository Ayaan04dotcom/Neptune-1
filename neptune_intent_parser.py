#!/usr/bin/env python3
# @raycast.schemaVersion 1
# @raycast.title Neptune Intent Parser
# @raycast.mode fullOutput
# @raycast.packageName Neptune
# @raycast.description Ask Neptune to generate a document
# @raycast.argument1 { "type": "text", "placeholder": "What do you want Neptune to do?" }

import sys
import openai
import pyperclip
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


                                                    
goal = sys.argv[1]

prompt = f"""Write a 1-page well-written document about: {goal}.
Include 2 statistics and format it clearly."""

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}],
    max_tokens=800,
    temperature=0.7
)

result = response["choices"][0]["message"]["content"]
pyperclip.copy(result)

print("✅ Done. Output copied to clipboard.")
