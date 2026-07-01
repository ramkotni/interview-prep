# Amazon – Senior AI Engineer

**Duration:** 2 Years
Feb 2023 - March 2025

## Project

**Amazon Robotics AI Assistant Platform**

### Business Problem

Amazon fulfillment centers operate thousands of autonomous mobile robots (AMRs) that transport inventory pods between storage locations and picking stations. Operations teams monitored robot health, battery levels, navigation issues, congestion, task assignments, and hardware failures using multiple dashboards and operational logs. Root cause analysis and troubleshooting were manual, slowing issue resolution and impacting warehouse throughput.

### AI Solution

Designed and developed an Agentic AI platform that enabled operations engineers to interact with robotics data using natural language. The platform combined Retrieval-Augmented Generation (RAG), LangGraph, LLMs, and specialized AI agents to analyze robot incidents, explain failures, recommend corrective actions, and summarize warehouse operations.

## Responsibilities

* Designed a modular multi-agent architecture using LangGraph for robotics operations.
* Built an **Intent Agent** to classify user requests into Robot Diagnostics, Fleet Status, Battery Analysis, Navigation Issues, Predictive Maintenance, Task Assignment, and Operational Summary.
* Developed a **Fleet Search Agent** to retrieve historical robot incidents, maintenance logs, and operational events using semantic search.
* Built a **Robot Diagnostics Agent** to identify probable causes for robot failures such as battery degradation, sensor issues, motor faults, barcode scanner errors, Wi-Fi connectivity problems, and navigation exceptions.
* Implemented a **Predictive Maintenance Agent** that analyzed historical maintenance records and generated proactive maintenance recommendations.
* Developed a **Task Optimization Agent** that suggested workload balancing and robot reassignment based on fleet utilization.
* Built an **Operations Summary Agent** to generate daily warehouse health reports and executive summaries.
* Implemented a Retrieval-Augmented Generation (RAG) pipeline to ingest robotics operational logs, maintenance reports, CSV files, and HTML dashboards into a searchable knowledge base.
* Generated embeddings using **nomic-embed-text** and stored vectors in **ChromaDB** for semantic retrieval.
* Integrated local LLMs through Ollama to provide secure enterprise AI capabilities.
* Developed FastAPI REST APIs to expose conversational AI services for warehouse operations.
* Applied Clean Architecture, SOLID principles, structured logging, exception handling, and configuration management to build scalable AI services.
* Containerized AI services using Docker and designed Kubernetes deployment architectures.
* Collaborated with robotics operations teams to validate AI recommendations and improve operational efficiency.

## Technologies

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
* AWS
* GitHub Actions

## Business Impact

* Reduced robotics incident investigation time from approximately **45 minutes to less than 5 minutes** using AI-assisted diagnostics.
* Improved maintenance planning through predictive recommendations based on historical robot failures.
* Enabled natural language search over robotics operational knowledge.
* Automated executive summaries and daily warehouse health reporting.
* Increased operational efficiency by helping engineers identify recurring fleet issues and prioritize maintenance activities.
