from dotenv import load_dotenv
import os

load_dotenv()

print("API Key:", os.getenv("LANGSMITH_API_KEY"))
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))