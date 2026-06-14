import os

from dotenv import load_dotenv
from langchain_ollama import ChatOllama

# Load environment variables
load_dotenv()

print("LangSmith Tracing:",
      os.getenv("LANGSMITH_TRACING"))

# Local Ollama model
llm = ChatOllama(
    model="llama3.2",
    temperature=0
)

response = llm.invoke(
    "Explain payment failure prediction in simple terms"
)

print("\nAI Response:\n")
print(response.content)