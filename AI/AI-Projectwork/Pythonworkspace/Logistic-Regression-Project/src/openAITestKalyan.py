import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Initialize client (reads OPENAI_API_KEY from .env)
client = OpenAI()

# Correct JSON data
data = {
    "asset": "solar panel",
    "recepient": "kalyan",
    "date": "05-20-2026",
    "subject": "generator failure",
    "action": "check your connectivity or any issues"
}

# Build prompt
system_content = "You are an email assistant."
user_content = f"""
Generate a polite 3-line email using the JSON below.
Include the date when the issue was noticed.

JSON:
{json.dumps(data, indent=2)}
"""

# API call (UPDATED MODEL)
response = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {"role": "system", "content": system_content},
        {"role": "user", "content": user_content}
    ]
)

# Output result
print(response.choices[0].message.content)