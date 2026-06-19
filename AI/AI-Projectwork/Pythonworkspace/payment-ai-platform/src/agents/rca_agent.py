from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3"
)

def rca_agent(state):

    prompt = f"""
    Analyze payment failure.

    Context:
    {state['context']}

    Question:
    {state['question']}

    Identify root cause.
    """

    response = llm.invoke(prompt)

    state["root_cause"] = response.content

    return state