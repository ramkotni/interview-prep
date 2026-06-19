from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3"
)

def recommendation_agent(state):

    prompt = f"""
    Based on root cause:

    {state['root_cause']}

    Provide recommendations.
    """

    response = llm.invoke(prompt)

    state["recommendation"] = response.content

    return state