# ERCOT GINR Feasibility Screening ML Service

> End-to-End Architecture, Business Problem, Solution Design & Interview Explanation

---

# Project Information

## Project Name

**ERCOT Generation Interconnection Request (GINR) Feasibility Screening Machine Learning Service**

---

## Technology Stack

### Programming
- Python
- Scikit-Learn
- Pandas
- NumPy

### Backend
- Flask REST API
- Spring Boot
- REST Services

### Database
- Oracle Database

### ML & Deployment
- Joblib
- Jenkins
- Docker *(Future Enhancement)*

---

# 1. Executive Summary

ERCOT receives a large number of **Generation Interconnection Requests (GINRs)** from renewable and traditional energy providers requesting connection to the Texas power grid.

Engineers manually perform feasibility screening by validating:

- Payment information
- Connectivity details
- Point of Interconnection (POI)
- Thermal constraints
- Network readiness
- Study requirements

The objective of this project was to build a **Machine Learning-based Feasibility Screening Service** capable of predicting whether a GINR submission would pass feasibility screening before engineers begin manual review.

## Benefits

- Faster screening
- Better prioritization
- Reduced manual effort
- Lower operational costs
- Improved engineer productivity

---

# 2. Business Problem

## Existing Process

Every submitted GINR required manual engineering review.

Activities included:

- Payment verification
- Project capacity validation
- Connectivity review
- POI validation
- Thermal constraint review
- Study requirement verification

### Challenges

- High request volume
- Long processing time
- Manual effort
- Engineering bottlenecks
- Delayed approvals
- Incomplete submissions
- No risk-based prioritization

### Business Impact

- Large backlog
- Reduced efficiency
- Delayed customer onboarding
- Increased operational cost

---

# 3. Business Objective

Develop an intelligent ML system capable of:

- Predicting feasibility outcome
- Calculating pass probability
- Generating risk score
- Providing early warning indicators

### Expected Benefits

- Faster processing
- Better prioritization
- Reduced manual effort
- Improved engineer productivity
- Faster customer response

---

# 4. Solution Overview

The ML service learns from historical GINR data and predicts approval probability for new requests.

## Components

- Data Extraction Layer
- Feature Engineering Layer
- Machine Learning Pipeline
- Model Registry
- Prediction API
- Spring Boot Integration
- Monitoring & Drift Detection

---

# 5. High-Level Architecture

```text
Oracle Database
(Historical GINRs)
        │
        ▼
Data Extraction Layer
        │
        ▼
Feature Engineering
        │
        ▼
ML Training Pipeline
        │
        ▼
Model Registry
        │
        ▼
Flask Prediction API
        │
        ▼
Spring Boot Application
        │
        ▼
ERCOT Engineers
```

---

# 6. Step-by-Step Execution Flow

## Step 1 – Data Collection

Historical data extracted from Oracle.

### Sources

- GINR Requests
- Payment Information
- POI Data
- Connectivity Nodes
- Study Results
- Engineering Reports

**Output**

```
Historical Training Dataset
```

---

## Step 2 – Data Cleaning

Problems found

- Missing values
- Duplicate records
- Invalid records
- Inconsistent formats

Activities

- Remove duplicates
- Handle null values
- Normalize fields
- Standardize formats

Output

```
Cleaned Dataset
```

---

## Step 3 – Feature Engineering

### Numerical Features

- Project MW
- POI Voltage
- Thermal Margin
- Months to COD

### Binary Features

- Payment Completed
- Missing Documents
- Node Available

### Categorical Features

- Resource Type
- Lead TDSP
- Interconnection Type

Additional Processing

- One-Hot Encoding
- Scaling
- Missing Value Imputation

Output

```
ML Ready Dataset
```

---

## Step 4 – Model Training

### Algorithm

**Logistic Regression**

### Why Logistic Regression?

- Explainable
- Fast training
- Easy maintenance
- Probability prediction
- Excellent for structured business data

Pipeline

```text
Input Data
      │
      ▼
SimpleImputer
      │
      ▼
OneHotEncoder
      │
      ▼
StandardScaler
      │
      ▼
Logistic Regression
      │
      ▼
Trained Model
```

---

## Step 5 – Model Evaluation

### Metrics

| Metric | Purpose |
|---------|----------|
| Accuracy | Overall correctness |
| Precision | Failure prediction accuracy |
| Recall | Detect actual failures |
| ROC-AUC | Overall model quality |

### Business Priority

**Recall**

Reason:

Missing a problematic request is far more expensive than reviewing an additional request.

---

## Step 6 – Model Versioning

Example

```
ginr_model_v1.0.joblib
ginr_model_v1.1.joblib
```

Stored Metadata

- Training Date
- Feature List
- Evaluation Metrics
- Dataset Version

Benefits

- Rollback
- Auditability
- Governance

---

## Step 7 – Prediction API

### Endpoints

```http
GET /api/v1/health
```

```http
POST /api/v1/score
```

```http
POST /api/v1/score/batch
```

```http
GET /api/v1/model/info
```

```http
GET /api/v1/drift
```

---

## Step 8 – Real-Time Prediction Flow

```text
User submits GINR
        │
        ▼
Spring Boot
        │
        ▼
Flask Prediction API
        │
        ▼
Payload Validation
        │
        ▼
Feature Engineering
        │
        ▼
ML Prediction
        │
        ▼
Risk Classification
        │
        ▼
Response
```

Example Response

```json
{
  "prediction": "PASS",
  "probability": 0.89,
  "risk": "LOW"
}
```

---

## Step 9 – Risk Categorization

| Probability | Risk |
|-------------|------|
| >80% | LOW |
| 50–80% | MEDIUM |
| <50% | HIGH |

Purpose

Engineers prioritize reviews based on risk.

---

## Step 10 – Monitoring & Drift Detection

Monitor

- Feature distribution
- New resource types
- Data quality
- Prediction trends

If drift exceeds threshold

- Alert generated
- Retraining initiated

---

# 7. Deployment Architecture

## Training

```text
Oracle Database
      │
      ▼
Python Training Pipeline
      │
      ▼
Model Artifact
      │
      ▼
Model Registry
```

## Production

```text
RARF UI
      │
      ▼
Spring Boot
      │
      ▼
REST API
      │
      ▼
Flask ML Service
      │
      ▼
Prediction Response
```

---

# 8. Business Benefits

## Before

- Manual screening
- Slow processing
- Large backlog
- No prioritization

## After

- Automated risk assessment
- Faster processing
- Reduced engineering effort
- Better prioritization
- Improved turnaround time

### Expected Improvements

- 40–60% reduction in manual review effort
- Faster approval cycle
- Better engineering utilization
- Improved customer satisfaction

---

# 9. My Role

As Senior Software Engineer / AI Engineer

Responsibilities

- Business requirement analysis
- Historical data analysis
- ML architecture design
- Feature engineering
- Model training
- Model evaluation
- Flask API development
- Spring Boot integration
- Monitoring implementation
- Model versioning
- Deployment support
- Testing

---

# 10. Interview Explanation (5 Minutes)

ERCOT processes hundreds of Generation Interconnection Requests from renewable and traditional energy providers seeking connection to the Texas power grid.

The original feasibility screening process was completely manual, requiring engineers to review payment information, connectivity details, Point of Interconnection (POI), and network constraints. This resulted in delays, high operational costs, and limited scalability.

To improve efficiency, we developed a Machine Learning-based Feasibility Screening Service using Python and Scikit-Learn. Historical GINR data was extracted from Oracle and transformed into machine learning features such as payment status, project size, POI voltage, connectivity information, and thermal margins.

The solution uses a preprocessing pipeline consisting of SimpleImputer, OneHotEncoder, StandardScaler, and Logistic Regression. The trained model is deployed as a Flask REST API and integrated with a Spring Boot application.

Whenever a new request is submitted, the application calls the ML service to obtain a pass probability and risk classification, enabling engineers to prioritize high-risk requests and significantly reduce manual effort.

Additional capabilities such as model versioning, monitoring, and drift detection ensure long-term reliability and governance.

---