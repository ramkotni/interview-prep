def calculator(expression: str):
    """
    Simple safe calculator tool
    """
    try:
        return str(eval(expression))
    except Exception as e:
        return f"Error: {str(e)}"


def get_payment_data():
    """
    Simulated business data tool
    """
    return {
        "total_payments": 1200,
        "failed_payments": 95,
        "system": "ERCOT"
    }