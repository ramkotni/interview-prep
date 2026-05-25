from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Load model
model = joblib.load("ercot_payment_model.pkl")

app = FastAPI()

# Request object
class PaymentRequest(BaseModel):

    credit_score: int
    prior_defaults: int
    missing_documents: int
    duplicate_submission: int
    market_price: float
    application_completion_pct: int
    bank_balance_million: float
    transaction_retry_count: int


@app.post("/predict")
def predict(request: PaymentRequest):

    values = [[
        request.credit_score,
        request.prior_defaults,
        request.missing_documents,
        request.duplicate_submission,
        request.market_price,
        request.application_completion_pct,
        request.bank_balance_million,
        request.transaction_retry_count
    ]]

    probability = model.predict_proba(values)[0][1]

    prediction = "HIGH_RISK"

    if probability < 0.80:
        prediction = "LOW_RISK"

    return {
        "risk_probability": float(probability),
        "prediction": prediction
    }