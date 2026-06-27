# Machine Learning (ML) – One-Page Interview Summary

# What is Machine Learning?

Machine Learning (ML) is a branch of Artificial Intelligence (AI) that enables computers to learn patterns from historical data and make predictions or decisions without being explicitly programmed.

**Traditional Programming**

Input + Rules → Output

**Machine Learning**

Input + Output → Model Learns Rules

Example:

* Input: Payment history
* Output: Payment Success/Failure
* Model learns why payments fail.

---

# Types of Machine Learning

## 1. Supervised Learning

The model learns using labeled data (features + known target).

Example:

| Amount | Customer Age | Payment Status |
| ------ | ------------ | -------------- |
| 100    | 25           | Success        |
| 500    | 45           | Failure        |

Goal:
Predict the target column.

Algorithms:

* Linear Regression
* Logistic Regression
* Decision Tree
* Random Forest
* XGBoost
* Support Vector Machine (SVM)
* Neural Networks

Use Cases:

* Payment Failure Prediction
* Fraud Detection
* Credit Risk
* Customer Churn

---

## 2. Unsupervised Learning

No target column.

Goal:
Discover hidden patterns.

Algorithms:

* K-Means Clustering
* DBSCAN
* Hierarchical Clustering
* PCA (Dimensionality Reduction)

Use Cases:

* Customer Segmentation
* Anomaly Detection
* Recommendation Systems

---

## 3. Reinforcement Learning

An agent learns by interacting with an environment and receiving rewards or penalties.

Examples:

* Self-driving cars
* Robotics
* Game-playing AI
* Dynamic pricing

---

# ML Workflow

1. Collect Data
2. Clean Data
3. Feature Engineering
4. Train Model
5. Validate Model
6. Test Model
7. Deploy Model
8. Monitor Performance
9. Retrain with New Data

---

# Common ML Terminology

Features (X):
Input variables used to make predictions.

Examples:

* Payment Amount
* Customer ID
* Gateway
* Bank
* Payment Type

Target (Y):
The value to predict.

Examples:

* Success / Failure
* Fraud / Not Fraud

Training Data:
Used to teach the model.

Testing Data:
Used to evaluate model performance on unseen data.

Validation Data:
Used for hyperparameter tuning and model selection.

---

# Classification vs Regression

Classification:
Predicts categories.

Examples:

* Payment Failed?
* Fraud?
* Customer Churn?

Algorithms:

* Logistic Regression
* Decision Tree
* Random Forest

Regression:
Predicts continuous values.

Examples:

* House Price
* Sales Forecast
* Payment Amount

Algorithms:

* Linear Regression
* Random Forest Regressor

---

# Common Algorithms

## Linear Regression

Predicts continuous numbers.

Example:
Predict next month's revenue.

---

## Logistic Regression

Predicts probabilities (0–1).

Example:
Probability that a payment will fail.

Output:
0.92 = 92% chance of failure.

---

## Decision Tree

Splits data into decision rules.

Example:
Payment Amount > $10,000?
→ Yes → High Risk
→ No → Continue

Easy to understand but can overfit.

---

## Random Forest

Many decision trees combined.

Advantages:

* Higher accuracy
* Reduces overfitting
* Robust on large datasets

Widely used in production.

---

## XGBoost

Gradient Boosting algorithm.

Advantages:

* High accuracy
* Fast training
* Handles missing values well

Popular in Kaggle competitions and enterprise ML.

---

# Model Evaluation Metrics

Classification:

Accuracy
Percentage of correct predictions.

Precision
Of all predicted positives, how many were correct?

Recall
Of all actual positives, how many were detected?

F1 Score
Balances Precision and Recall.

ROC-AUC
Measures how well the model distinguishes between classes.

Regression:

MAE (Mean Absolute Error)

MSE (Mean Squared Error)

RMSE (Root Mean Squared Error)

R² Score (Coefficient of Determination)

---

# Overfitting vs Underfitting

Overfitting:
The model memorizes training data and performs poorly on new data.

Symptoms:

* Very high training accuracy
* Low test accuracy

Solutions:

* More data
* Cross-validation
* Regularization
* Simpler model

Underfitting:
The model is too simple to capture patterns.

Symptoms:

* Poor performance on both training and testing data

Solutions:

* Add features
* Increase model complexity
* Train longer

---

# Feature Engineering

Transform raw data into useful features.

Examples:

* Payment Month
* Payment Hour
* Failure Count
* Customer Tenure
* Average Transaction Amount

Better features often improve model performance more than changing algorithms.

---

# ML vs Deep Learning vs Generative AI

Machine Learning:
Learns patterns to make predictions.

Deep Learning:
Uses neural networks to solve complex tasks such as image recognition, speech recognition, and NLP.

Generative AI:
Creates new content (text, code, images, audio).

Examples:

* ChatGPT
* Gemini
* Claude
* Llama

---

# Example: Payment Failure Prediction

Problem:
Predict whether a payment will fail before processing.

Features:

* Payment Amount
* Gateway
* Customer Type
* Bank
* Retry Count
* Payment Method

Target:
Payment Status (Success/Failure)

Algorithm:
Logistic Regression or Random Forest

Output:
"Payment has an 87% probability of failure."

Business Benefit:

* Proactive issue detection
* Reduced payment failures
* Improved customer experience
* Lower operational costs

---

# Interview Answer: "Explain Machine Learning"

Machine Learning is a subset of Artificial Intelligence that enables systems to learn patterns from historical data and make predictions without explicit programming. A typical ML pipeline includes data collection, preprocessing, feature engineering, model training, evaluation, deployment, and monitoring. Depending on the problem, we use supervised learning for prediction, unsupervised learning for discovering patterns, or reinforcement learning for decision-making. In my payment intelligence project, ML can be used to predict payment failures, while RAG and LLMs are used to analyze historical reports and answer operational questions.
