import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

df = pd.read_csv("ercot_generator_payment_data.csv")

encoder = LabelEncoder()

df["payment_method"] = encoder.fit_transform(df["payment_method"])
df["generator_type"] = encoder.fit_transform(df["generator_type"])
df["region"] = encoder.fit_transform(df["region"])

X = df[
    [
        "credit_score",
        "prior_defaults",
        "missing_documents",
        "duplicate_submission",
        "market_price",
        "application_completion_pct",
        "bank_balance_million",
        "transaction_retry_count"
    ]
]

y = df["payment_status"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print("Prediction:", predictions)