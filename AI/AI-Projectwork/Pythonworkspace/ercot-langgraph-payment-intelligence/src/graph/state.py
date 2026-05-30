from typing import TypedDict
import pandas as pd

class PaymentState(TypedDict):

    df: pd.DataFrame

    predictions_done: bool

    root_causes: str

    recommendations: str

    executive_report: str