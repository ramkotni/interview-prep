import ollama

def generate_report(state):

    df = state["df"]

    total_transactions = len(df)

    high_risk = len(
        df[df["FAILURE_PROBABILITY"] > 0.80]
    )

    prompt = f"""
    Generate executive monthly
    ERCOT payment intelligence report.

    Total Transactions:
    {total_transactions}

    High Risk Transactions:
    {high_risk}

    Root Causes:
    {state['root_causes']}

    Recommendations:
    {state['recommendations']}
    """

    response = ollama.chat(
        model="gemma3:1b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    state["executive_report"] = (
        response["message"]["content"]
    )

    print("Executive report generated")

    return state