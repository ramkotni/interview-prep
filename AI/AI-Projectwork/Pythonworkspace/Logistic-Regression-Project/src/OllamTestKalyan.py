import json
import requests

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# JSON input
data = {
    "asset": "solar panel",
    "recipient": "Kalyan",
    "date": "05-20-2026",
    "subject": "Generator Failure",
    "action": "Check your connectivity or any issues"
}

# Prompt
prompt = f"""
You are an email assistant.

Generate a professional 3-line email using the JSON below.

JSON:
{json.dumps(data, indent=2)}
"""

# Payload
payload = {
    "model": "gemma3:1b",
    "prompt": prompt,
    "stream": False
}

try:
    # API call
    response = requests.post(OLLAMA_URL, json=payload)

    # Convert response
    result = response.json()

    # Print generated email
    print("\nGenerated Email:\n")
    print(result["response"])

except Exception as e:
    print("Error:", e)