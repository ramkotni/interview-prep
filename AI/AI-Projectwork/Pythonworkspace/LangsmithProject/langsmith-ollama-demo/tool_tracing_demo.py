from dotenv import load_dotenv
load_dotenv()

from langsmith import traceable
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.2")

@traceable(run_type="tool")
def get_payment_stats():
    return {
        "total_payments": 1000,
        "failed_payments": 75
    }

@traceable
def analyze_payments():

    data = get_payment_stats()

    prompt = f"""
    Total Payments: {data['total_payments']}
    Failed Payments: {data['failed_payments']}

    Calculate failure percentage.
    """

    response = llm.invoke(prompt)

    return response.content

print(analyze_payments())