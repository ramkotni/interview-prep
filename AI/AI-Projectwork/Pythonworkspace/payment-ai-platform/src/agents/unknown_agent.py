def unknown_agent(state):

    state["answer"] = {
        "message": (
            "I can only help with payment related questions "
            "such as payment failures, transactions, gateways, "
            "settlement, and payment analytics."
        ),
        "intent": state.get("intent")
    }

    return state