import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Load dataset
data = pd.read_csv("customer_churn.csv")

print("\nDataset:\n")
print(data)

# Features (input)
X = data[['MonthlyBill', 'ContractMonths',
          'InternetUsageGB', 'SupportCalls']]

# Target (output)
y = data['Churn']

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create logistic regression model
model = LogisticRegression()

# Train model
model.fit(X_train, y_train)

# Predict test data
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("\nPredictions:")
print(predictions)

print("\nActual Values:")
print(y_test.values)

print("\nModel Accuracy:")
print(round(accuracy * 100, 2), "%")

# Real-time custom prediction
print("\n===== Real-Time Customer Prediction =====")

monthly_bill = float(input("Enter Monthly Bill: "))
contract_months = int(input("Enter Contract Months: "))
internet_usage = float(input("Enter Internet Usage (GB): "))
support_calls = int(input("Enter Support Calls: "))

new_customer = [[monthly_bill,
                 contract_months,
                 internet_usage,
                 support_calls]]

result = model.predict(new_customer)

probability = model.predict_proba(new_customer)

print("\nPrediction Probability:")
print(probability)

if result[0] == 1:
    print("\nCustomer will likely CHURN.")
else:
    print("\nCustomer will likely STAY.")