from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

# Sample dataset
data = pd.DataFrame({
    'hours': [2,5,7,1,4,6,3],
    'attendance': [60,80,90,50,70,85,65],
    'prev_score': [40,65,70,30,55,68,50],
    'pass_exam': [0,1,1,0,1,1,0]
})

X = data[['hours', 'attendance', 'prev_score']]
y = data['pass_exam']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
# print(X_train)
#
# print(X_test)
#
# print(y_train)
#
# print(y_test)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

print(model.coef_)

print(model.classes_)

# Predict
pred = model.predict(X_test)

# Evaluate
print("Accuracy:", accuracy_score(y_test, pred))