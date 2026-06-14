from graph import graph
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGSMITH_PROJECT"] = "Local-AI-Agent"
if __name__ == "__main__":

    while True:

        question = input("\nAsk AI Agent: ")

        if question.lower() in ["exit", "quit"]:
            break

        result = graph.invoke({
            "question": question
        })

        print("\nAI ANSWER:\n", result["answer"])