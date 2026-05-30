import joblib
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def predict_risk(state):

    print("Starting prediction agent...")

    df = state["df"]

    # ==================================================
    # SAME FEATURES USED DURING TRAINING
    # ==================================================

    features = [
        'TOTAL_AMOUNT',
        'PRIOR_ATTEMPTS_SAME_REQUEST',
        'TOTAL_FAILURES_SAME_CARD',
        'DAYS_SUBMIT_TO_PAY',
        'ACCOUNT_TYPE',
        'ID_FUEL_TYPE',
        'ID_APPLICATION_SIZE',
        'MAX_GEN_MW',
        'POI_VOLTAGE',
        'FIS_FEE_PAID',
        'SS_FEE_PAID',
        'ANALYSIS_FEE_PAID'
    ]

    X = df[features].copy()

    # ==================================================
    # ENCODE CATEGORICAL COLUMNS
    # ==================================================

    categorical_columns = [
        'ACCOUNT_TYPE',
        'ID_FUEL_TYPE',
        'ID_APPLICATION_SIZE'
    ]

    for column in categorical_columns:

        encoder = LabelEncoder()

        X[column] = encoder.fit_transform(
            X[column].astype(str)
        )

    # ==================================================
    # LOAD TRAINED MODEL
    # ==================================================

    model = joblib.load(
        "models/logistic_model.pkl"
    )

    # ==================================================
    # PREDICT PROBABILITY
    # ==================================================

    probabilities = model.predict_proba(X)

    df["FAILURE_PROBABILITY"] = probabilities[:,1]

    # ==================================================
    # CREATE RISK LEVEL
    # ==================================================

    def risk_level(prob):

        if prob >= 0.80:
            return "HIGH"

        elif prob >= 0.30:
            return "MEDIUM"

        else:
            return "LOW"

    df["RISK_LEVEL"] = df[
        "FAILURE_PROBABILITY"
    ].apply(risk_level)

    # ==================================================
    # PREDICTED STATUS
    # ==================================================

    df["PREDICTED_STATUS"] = (
        df["FAILURE_PROBABILITY"] >= 0.5
    ).astype(int)

    # ==================================================
    # SAVE OUTPUT CSV
    # ==================================================

    df.to_csv(
        "data/output/payment_risk_predictions.csv",
        index=False
    )

    state["df"] = df

    state["predictions_done"] = True

    print("Predictions completed successfully")

    return state