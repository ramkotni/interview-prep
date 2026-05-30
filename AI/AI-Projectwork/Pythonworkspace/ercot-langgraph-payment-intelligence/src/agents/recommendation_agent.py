import ollama

def generate_recommendations(state):

    prompt = f"""
    Analyze the following payment
    root causes and provide
    operational recommendations.

    Root Causes:
    {state['root_causes']}
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

    state["recommendations"] = (
        response["message"]["content"]
    )

    print("Recommendations generated")

    return state