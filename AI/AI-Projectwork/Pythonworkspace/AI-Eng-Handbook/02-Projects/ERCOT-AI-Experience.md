# ERCOT – Senior AI Engineer (Agentic AI)

**Duration:** 1.5 Years

April 2025 to current date - 1 year 2 months

## Project

**AI-Powered Payment Operations Intelligence Platform**

### Business Problem

The payment operations team managed thousands of payment transactions and settlement records daily. Support engineers manually analyzed payment failures, duplicate payments, validation errors, synchronization issues, and missing fee transactions by reviewing reports, logs, and historical records. Root cause analysis was time-consuming, and generating executive summaries required significant manual effort.

### Solution

Designed and implemented an Agentic AI platform that combined Retrieval-Augmented Generation (RAG), LangGraph, and multiple specialized AI agents to automate payment failure investigation, root cause analysis, trend analysis, recommendations, and conversational search over historical payment reports.

### Responsibilities

* Designed a multi-agent architecture using LangGraph for payment operations intelligence.
* Built an **Intent Agent** to classify user requests into Root Cause Analysis (RCA), Trend Analysis, Recommendation, Summary, and Search workflows.
* Developed a **Search Agent** to retrieve relevant historical payment incidents from a ChromaDB vector store using semantic search.
* Implemented an **RCA Agent** to analyze similar historical failures and identify probable causes.
* Developed a **Recommendation Agent** to suggest operational actions based on previous incident resolutions and business rules.
* Built a **Trend Analysis Agent** to identify recurring payment failure patterns, severity trends, and monthly operational metrics.
* Implemented a **Summary Agent** to generate executive-ready summaries for operations teams and management.
* Built a Retrieval-Augmented Generation (RAG) pipeline to ingest CSV and HTML payment monitoring reports and convert them into searchable embeddings.
* Generated embeddings using **nomic-embed-text** and stored vectors in **ChromaDB** for semantic retrieval.
* Integrated local LLMs through Ollama to provide secure, enterprise-ready AI capabilities.
* Developed FastAPI REST APIs for conversational AI, incident analysis, and operational reporting.
* Applied Clean Architecture, SOLID principles, structured logging, exception handling, and configuration management to build production-ready AI services.
* Containerized AI services using Docker and designed deployment-ready architectures for Kubernetes.
* Worked with operations and business stakeholders to validate AI recommendations and improve investigation workflows.

### Technologies

* Python
* FastAPI
* LangGraph
* LangChain
* Ollama
* Llama
* ChromaDB
* RAG
* Prompt Engineering
* Pandas
* PostgreSQL
* Docker
* Kubernetes
* GitHub Actions
* AWS

### Business Impact

* Reduced payment failure investigation time from approximately **30–60 minutes to under 5 minutes** by enabling AI-assisted retrieval and root cause analysis.
* Automated operational summaries and recommendations, reducing manual effort for support teams.
* Improved knowledge reuse by making historical payment incidents searchable through semantic search.
* Increased consistency in incident analysis and operational reporting across payment support teams.
