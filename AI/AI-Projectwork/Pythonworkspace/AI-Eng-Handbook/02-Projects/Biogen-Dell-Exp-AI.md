# AI Experience Summary

## Dell Technologies (6 Years 11 months)
## June 2015 - May 2022

1 year May 2021 to May 2022 - AI

### Machine Learning Engineer / Senior Software Engineer

**Project: AI Feasibility Prediction Platform**

### Business Problem

Enterprise architects manually analyzed new project requests to estimate feasibility, cost, effort, risks, and timelines. The process was slow, inconsistent, and dependent on senior architects.

### Solution

Designed and implemented a Machine Learning solution using Logistic Regression to predict project feasibility based on historical project data. The ML prediction was integrated into an AI workflow that generated explainable recommendations and executive summaries.

### Responsibilities

* Developed end-to-end Machine Learning pipelines using Python and Scikit-learn.
* Built a Logistic Regression model to predict project feasibility.
* Performed feature engineering using project complexity, budget, timeline, technology readiness, resource availability, and dependency data.
* Cleaned, transformed, and validated structured datasets using Pandas and NumPy.
* Split datasets into training and testing sets and evaluated models using Accuracy, Precision, Recall, F1 Score, ROC-AUC, and Confusion Matrix.
* Tuned model parameters and compared multiple algorithms before selecting Logistic Regression for its interpretability.
* Exposed model inference through FastAPI REST APIs.
* Integrated ML predictions into business workflows for automated feasibility analysis.
* Collaborated with architects and business stakeholders to validate model outputs.
* Implemented logging, monitoring, and exception handling for production readiness.

**Technologies**

Python, Scikit-learn, Pandas, NumPy, Logistic Regression, FastAPI, PostgreSQL, Docker, Kubernetes, Git

---

## Biogen (1 Year) - June 2022 - June 2023

### Senior Software Engineer – Generative AI Integration

**Project: Enterprise Knowledge Assistant**

### Business Problem

Business users spent significant time searching through internal documents, SOPs, and knowledge repositories to answer operational questions.

### Solution

Integrated LLM capabilities into internal applications to provide conversational access to enterprise knowledge using Retrieval-Augmented Generation (RAG).

### Responsibilities

* Integrated Llama-based models with enterprise applications using REST APIs.
* Designed prompt templates for document summarization and question answering.
* Built document ingestion pipelines for PDF, Word, HTML, and CSV sources.
* Generated embeddings and indexed enterprise documents in ChromaDB.
* Implemented semantic search for knowledge retrieval.
* Developed FastAPI services to expose AI capabilities.
* Improved prompt quality through prompt engineering and iterative evaluation.
* Added citation-aware responses based on retrieved context.
* Worked with business users to validate response quality.

**Technologies**

Python, FastAPI, Llama, Ollama, LangChain, ChromaDB, Embeddings, Prompt Engineering, RAG

---

## Amazon (2 Years) - June 2023 - April 2025

### Senior AI Engineer – Agentic AI Platform

**Project: Payment Failure Intelligence Platform**

### Business Problem

Operations teams manually investigated payment failures by reviewing historical reports, logs, and operational dashboards. Root cause analysis and trend identification required significant manual effort.

### Solution

Designed a production-oriented Agentic AI platform that combines RAG, LangGraph, and multiple specialized AI agents to automate payment failure analysis, root cause identification, trend analysis, and recommendations.

### Responsibilities

* Designed LangGraph workflows for enterprise AI orchestration.
* Built an Intent Agent to classify user requests into RCA, Trend Analysis, Summary, Recommendation, and Search categories.
* Developed Search, RCA, Recommendation, Trend Analysis, and Executive Summary agents.
* Built a RAG pipeline using CSV and HTML payment reports.
* Generated embeddings with nomic-embed-text and stored vectors in ChromaDB.
* Implemented semantic retrieval for historical payment incidents.
* Integrated local LLMs using Ollama for secure enterprise deployments.
* Developed FastAPI APIs for conversational AI services.
* Implemented configurable routing, logging, monitoring, and exception handling.
* Containerized applications using Docker and designed Kubernetes deployment architecture.
* Applied Clean Architecture and SOLID principles to build modular, scalable AI services.

**Technologies**

Python, LangGraph, LangChain, FastAPI, Ollama, Llama, ChromaDB, RAG, Docker, Kubernetes, PostgreSQL, GitHub Actions
