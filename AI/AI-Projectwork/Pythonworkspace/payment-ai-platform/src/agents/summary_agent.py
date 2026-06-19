from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3"
)

def summary_agent(state):

    prompt = f"""
    Summarize findings.

    Root Cause:
    {state['root_cause']}

    Recommendation:
    {state['recommendation']}
    """

    response = llm.invoke(prompt)

    state["answer"] = response.content

    return state