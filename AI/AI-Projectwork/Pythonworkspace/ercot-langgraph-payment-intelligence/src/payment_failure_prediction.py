import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)

import joblib

# ==================================================
# STEP 1 - LOAD DATASET
# ==================================================

print("Loading dataset...")

df = pd.read_csv(
    "data/payment_ml_dataset_10000_records.csv"
)

print(df.head())

# ==================================================
# STEP 2 - CREATE TARGET VARIABLE
# ==================================================

# FAILED = 1
# SUCCESS = 0

df['TARGET'] = df['PAYMENT_STATUS'].apply(
    lambda x: 1 if x == 'FAILED' else 0
)

# ==================================================
# STEP 3 - SELECT FEATURES
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
y = df['TARGET']

# ==================================================
# STEP 4 - HANDLE CATEGORICAL DATA
# ==================================================

categorical_columns = [
    'ACCOUNT_TYPE',
    'ID_FUEL_TYPE',
    'ID_APPLICATION_SIZE'
]

encoders = {}

for column in categorical_columns:

    encoder = LabelEncoder()

    X[column] = encoder.fit_transform(
        X[column].astype(str)
    )

    encoders[column] = encoder

# ==================================================
# STEP 5 - TRAIN TEST SPLIT
# ==================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ==================================================
# STEP 6 - TRAIN LOGISTIC REGRESSION MODEL
# ==================================================

print("Training model...")

model = LogisticRegression(
    max_iter=2000
)

model.fit(X_train, y_train)

# ==================================================
# STEP 7 - PREDICT
# ==================================================

predictions = model.predict(X_test)

probabilities = model.predict_proba(X_test)

# Probability of FAILED
failure_probability = probabilities[:, 1]

# ==================================================
# STEP 8 - CREATE RISK LEVEL
# ==================================================

def risk_level(prob):

    if prob >= 0.7:
        return "HIGH"

    elif prob >= 0.3:
        return "MEDIUM"

    else:
        return "LOW"

# ==================================================
# STEP 9 - CREATE OUTPUT DATAFRAME
# ==================================================

results = X_test.copy()

results['ACTUAL_STATUS'] = y_test.values

results['PREDICTED_STATUS'] = predictions

results['FAILURE_PROBABILITY'] = failure_probability

results['RISK_LEVEL'] = results[
    'FAILURE_PROBABILITY'
].apply(risk_level)

# ==================================================
# STEP 10 - SAVE CSV OUTPUT
# ==================================================

output_file = "data/output/payment_risk_predictions.csv"

results.to_csv(
    output_file,
    index=False
)

print(f"\nPrediction file saved: {output_file}")

# ==================================================
# STEP 11 - MODEL ACCURACY
# ==================================================

accuracy = accuracy_score(
    y_test,
    predictions
)

print("\nModel Accuracy:")
print(accuracy)

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions
    )
)

print("\nConfusion Matrix:")
print(
    confusion_matrix(
        y_test,
        predictions
    )
)

# ==================================================
# STEP 12 - SAVE MODEL
# ==================================================

joblib.dump(
    model,
    "models/logistic_model.pkl"
)

print("\nModel saved successfully.")

print("\nProgram completed.")