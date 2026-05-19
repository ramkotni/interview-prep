Yes. Since your laptop has 8 GB RAM and Core i5-7200U, the best free option is to use local AI models with [Ollama](https://ollama.com/?utm_source=chatgpt.com) instead of OpenAI API.

You can run everything fully offline and free.

For your laptop, these models work well:

| Model         | RAM Needed | Good For                     |
| ------------- | ---------- | ---------------------------- |
| `gemma3:1b`   | ~2 GB      | Fast/simple email generation |
| `phi3:mini`   | ~4 GB      | Better quality               |
| `tinyllama`   | ~2 GB      | Very lightweight             |
| `llama3.2:1b` | ~3 GB      | Good balance                 |

I recommend:

```bash
phi3:mini
```

or

```bash
gemma3:1b
```

---

# Step 1: Install Ollama

Download:

[Ollama Download](https://ollama.com/download?utm_source=chatgpt.com)

Install and restart laptop.

---

# Step 2: Pull Free AI Model

Open Command Prompt:

```bash
ollama run phi3:mini
```

OR

```bash
ollama run gemma3:1b
```

First download takes few minutes.

---

# Step 3: Install Python Library

```bash
pip install ollama pandas scikit-learn
```

---

# Step 4: Full Working Python Code (FREE AI)

```python
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
    model='phi3:mini',
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
```

---

# Example Output

Dear John,

Congratulations! Based on your attendance, study hours, and previous scores, our system predicts that you are likely to PASS the exam.

Keep up the hard work and continue your preparation with confidence.

Best Regards,
Student Evaluation Team

---

# Step 5: Run Program

```bash
python app.py
```

---

# If Ollama Not Working

Start Ollama manually:

```bash
ollama serve
```

Then run Python program again.

---

# Best Model For Your Laptop

I strongly recommend:

```bash
ollama run phi3:mini
```

because:

* Works on 8 GB RAM
* Faster on older CPUs
* Good email generation
* Free forever

---

# Later Improvements

You can later add:

* Flask API
* Angular frontend
* Spring Boot backend
* Gmail email sender
* Real student database
* PDF report generation
* Docker deployment
