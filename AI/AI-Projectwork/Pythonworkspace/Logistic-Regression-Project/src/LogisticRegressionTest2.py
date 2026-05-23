import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
data = {
    'Hours_Studied': [1,2,3,4,5,6,7,8],
    'Attendance': [50,60,65,70,75,80,85,90],
    'Pass': [0,0,0,0,1,1,1,1]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Hours_Studied', 'Attendance']]
y = df['Pass']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, predictions))