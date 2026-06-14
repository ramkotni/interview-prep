import time
from langsmith import traceable

@traceable
def timed_call(llm, prompt):
    start = time.time()

    result = llm.invoke(prompt)

    end = time.time()

    return {
        "response": result.content,
        "latency_seconds": end - start
    }