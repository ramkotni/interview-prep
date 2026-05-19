from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd
import ollama

# =========================
# TRAIN MACHINE LEARNING MODEL
# =========================

data = pd.DataFrame({
    'hours': [2,5,7,1,4,6,3],
    'attendance': [60,80,90,50,70,85,65],
    'prev_score': [40,65,70,30,55,68,50],
    'pass_exam': [0,1,1,0,1,1,0]
})

X = data[['hours', 'attendance', 'prev_score']]
y = data['pass_exam']

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

# =========================
# JSON INPUT
# =========================

student_json = {
    "student_name": "John",
    "hours": 5,
    "attendance": 75,
    "prev_score": 60,
    "email": "john@example.com"
}

# =========================
# PREDICT RESULT
# =========================

student_df = pd.DataFrame([{
    "hours": student_json["hours"],
    "attendance": student_json["attendance"],
    "prev_score": student_json["prev_score"]
}])

result = model.predict(student_df)[0]

status = "PASS" if result == 1 else "FAIL"

print("Prediction:", status)

# =========================
# GENERATE EMAIL USING OLLAMA
# =========================

prompt = f"""
Generate a professional email for a student.

Student Name: {student_json['student_name']}
Hours Studied: {student_json['hours']}
Attendance: {student_json['attendance']}
Previous Score: {student_json['prev_score']}
Prediction: {status}

Generate encouraging email.
"""

response = ollama.chat(
    #model='phi3:mini',
    model='gemma3:1b',
    messages=[
        {
            'role': 'user',
            'content': prompt
        }
    ]
)

email_content = response['message']['content']

print("\n===== AI GENERATED EMAIL =====\n")
print(email_content)