from langsmith import traceable

@traceable(
    metadata={
        "project": "payment-demo",
        "env": "local-ollama",
        "model": "llama3.2"
    }
)
def run_llm(llm, prompt):
    return llm.invoke(prompt)