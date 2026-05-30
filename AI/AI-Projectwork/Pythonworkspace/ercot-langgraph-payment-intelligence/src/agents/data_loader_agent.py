import pandas as pd

def load_data(state):

    df = pd.read_csv(
        "data/payment_ml_dataset_10000_records.csv"
    )

    state["df"] = df

    print("Dataset loaded")

    return state