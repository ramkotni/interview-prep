import json
import requests

# Ollama API endpoint
OLLAMA_URL = "http://localhost:11434/api/generate"

# Your JSON data
data = {
    "asset": "solar panel",
    "recepient": "kalyan",
    "date": "05-20-2026",
    "subject": "generator failure",
    "action": "check your connectivity or any issues"
}

# Prompt
prompt = f"""
You are an email assistant. Generate a polite 3-line email using the JSON below.
Include the date when the issue was noticed.

JSON:
{json.dumps(data, indent=2)}
"""

# Request payload
payload = {
    "model": "gemma:2b",
    "prompt": prompt,
    "stream": False
}

# Call Ollama
response = requests.post(OLLAMA_URL, json=payload)

# Parse response
result = response.json()

# Output
print(result["response"])
