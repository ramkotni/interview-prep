from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_ollama import ChatOllama
from tools import calculator, get_payment_data

llm = ChatOllama(model="llama3.2", temperature=0)

# -------- STATE --------
class State(TypedDict):
    question: str
    decision: str
    answer: str

# -------- NODE 1: DECIDE --------
def decide(state: State):
    prompt = f"""
    You are an AI agent.

    Decide what to do:
    - "calc" if math problem
    - "data" if business/payment data
    - "llm" for normal question

    Question: {state['question']}
    """

    result = llm.invoke(prompt)

    return {"decision": result.content.strip().lower()}

# -------- NODE 2: TOOL EXECUTION --------
def tool_node(state: State):

    if "calc" in state["decision"]:
        result = calculator("100+200+50")
        return {"answer": f"Calculation Result: {result}"}

    if "data" in state["decision"]:
        data = get_payment_data()
        return {"answer": f"Payment Data: {data}"}

    return {"answer": ""}

# -------- NODE 3: FINAL LLM --------
def final_node(state: State):

    prompt = f"""
    Question: {state['question']}
    Context: {state['answer']}

    Give a clear final answer.
    """

    response = llm.invoke(prompt)

    return {"answer": response.content}

# -------- BUILD GRAPH --------
builder = StateGraph(State)

builder.add_node("decide", decide)
builder.add_node("tool", tool_node)
builder.add_node("final", final_node)

builder.set_entry_point("decide")

builder.add_edge("decide", "tool")
builder.add_edge("tool", "final")
builder.add_edge("final", END)

graph = builder.compile()