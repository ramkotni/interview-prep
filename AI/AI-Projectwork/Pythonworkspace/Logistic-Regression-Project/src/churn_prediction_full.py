import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
import matplotlib.pyplot as plt

# ==============================
# LOAD DATASET
# ==============================

data = pd.read_csv("telecom_churn_large.csv")

print("\n========== DATASET ==========\n")
print(data.head())

# ==============================
# FEATURES AND TARGET
# ==============================

X = data[
    [
        'Age',
        'MonthlyBill',
        'ContractMonths',
        'InternetUsageGB',
        'SupportCalls',
        'StreamingSubscription',
        'PaymentDelayDays'
    ]
]

y = data['Churn']

# ==============================
# TRAIN TEST SPLIT
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)

# ==============================
# CREATE MODEL
# ==============================

model = LogisticRegression(max_iter=1000)

# ==============================
# TRAIN MODEL
# ==============================

model.fit(X_train, y_train)

print("\n========== MODEL TRAINED ==========\n")

# ==============================
# PREDICTIONS
# ==============================

predictions = model.predict(X_test)

# ==============================
# ACCURACY
# ==============================

accuracy = accuracy_score(y_test, predictions)

print("\nModel Accuracy:")
print(round(accuracy * 100, 2), "%")

# ==============================
# CONFUSION MATRIX
# ==============================

matrix = confusion_matrix(y_test, predictions)

print("\nConfusion Matrix:")
print(matrix)

# ==============================
# CLASSIFICATION REPORT
# ==============================

report = classification_report(y_test, predictions)

print("\nClassification Report:")
print(report)

# ==============================
# REAL-TIME PREDICTION
# ==============================

print("\n========== REAL-TIME CUSTOMER CHECK ==========\n")

age = int(input("Enter Age: "))
monthly_bill = float(input("Enter Monthly Bill: "))
contract_months = int(input("Enter Contract Months: "))
internet_usage = float(input("Enter Internet Usage GB: "))
support_calls = int(input("Enter Support Calls: "))
streaming = int(input("Streaming Subscription (1=yes,0=no): "))
payment_delay = int(input("Payment Delay Days: "))

new_customer = [[
    age,
    monthly_bill,
    contract_months,
    internet_usage,
    support_calls,
    streaming,
    payment_delay
]]

prediction = model.predict(new_customer)

probability = model.predict_proba(new_customer)

print("\nPrediction Probability:")
print(probability)

if prediction[0] == 1:
    print("\nCustomer is LIKELY TO CHURN.")
else:
    print("\nCustomer is LIKELY TO STAY.")

# ==============================
# FEATURE IMPORTANCE
# ==============================

features = X.columns
coefficients = model.coef_[0]

plt.figure(figsize=(10, 5))
plt.bar(features, coefficients)

plt.xticks(rotation=20)

plt.title("Feature Importance")
plt.xlabel("Features")
plt.ylabel("Coefficient Value")

plt.tight_layout()

plt.show()