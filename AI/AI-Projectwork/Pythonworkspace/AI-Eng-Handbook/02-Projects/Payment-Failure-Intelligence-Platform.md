# Payment Failure Intelligence Platform

> **Production-Ready Agentic AI + RAG Solution for ERCOT GINR Operations**

---

# Project Overview

## Project Name

**Payment Failure Intelligence Platform**

## Domain

ERCOT Generation Interconnection Request (GINR) Operations

## Objective

Build an AI-powered conversational platform that enables operations teams to investigate payment failures, identify root causes, analyze trends, retrieve historical resolutions, and generate executive insights using natural language.

---

# Business Problem

ERCOT processes thousands of payment transactions related to:

- Full Interconnection Study (FIS)
- Scoping Study (SS)
- Change Requests
- Analysis Fees
- Generation Interconnection Requests

Operations teams relied on manually reviewing:

- CSV Reports
- HTML Reports
- Excel Reports
- Email Notifications

to answer questions like:

- Why did GINR-12345 fail?
- Has this issue occurred before?
- What is the recommended resolution?

### Challenges

- Manual investigations
- Slow root cause analysis
- No historical intelligence
- Limited operational visibility
- Time-consuming report analysis
- No conversational interface

---

# Business Objectives

The platform should:

- Read historical payment reports
- Store operational knowledge
- Answer natural language questions
- Identify root causes
- Recommend corrective actions
- Generate executive summaries
- Analyze payment trends

---

# Proposed Solution

Build a Retrieval-Augmented Generation (RAG) platform using:

- LangGraph
- LangChain
- Ollama
- ChromaDB
- FastAPI

The platform transforms historical payment reports into searchable knowledge, allowing users to ask operational questions in plain English.

Example Questions

```text
Why did GINR123 fail?

Show duplicate payments.

What are the top payment failures this month?

Which payment failures are increasing?

Generate quarterly executive summary.
```

---

# High-Level Architecture

```text
                     User
                       │
                       ▼
                FastAPI REST API
                       │
                       ▼
              LangGraph Workflow
                       │
     ┌────────────┬─────────────┬─────────────┬─────────────┐
     │            │             │             │
     ▼            ▼             ▼             ▼
 Search Agent   RCA Agent   Recommendation   Summary Agent
                                 Agent
                       │
                       ▼
                    Ollama
                       │
                       ▼
                  ChromaDB
                       │
                       ▼
          Historical Payment Reports
             CSV / HTML Documents
```

---

# Technology Stack

## Backend

- Python 3.12
- FastAPI

## AI Framework

- LangGraph
- LangChain

## LLM

- Ollama
- Llama 3

## Embeddings

- nomic-embed-text

## Vector Database

- ChromaDB

## Data Sources

- CSV Reports
- HTML Reports
- Oracle Database *(Future Integration)*

## Deployment

- Docker
- Kubernetes

## Monitoring

- Prometheus
- Grafana

---

# System Components

## 1. Payment Monitor

Generates daily operational reports.

Example

```text
2025-01-payment-report.csv

2025-01-summary.html

2025-02-payment-report.csv

2025-02-summary.html
```

---

## 2. Ingestion Pipeline

Responsibilities

- Read reports
- Extract records
- Create LangChain documents
- Generate embeddings

---

## 3. Embedding Service

Model

```
nomic-embed-text
```

Converts text into vector embeddings.

---

## 4. Vector Database

**ChromaDB**

Stores

- Payment failures
- Severity
- Root causes
- Resolutions
- Project information

---

## 5. LangGraph Agents

Responsible for intelligent orchestration.

---

## 6. FastAPI

Provides REST endpoints for conversational AI.

---

# End-to-End Data Flow

## Step 1

Payment Monitor generates reports.

↓

## Step 2

Ingestion job executes.

```bash
python -m rag.ingest
```

↓

## Step 3

CSV and HTML files loaded.

↓

## Step 4

Documents created.

Example

```text
Project ID : GINR123

Failure Type : FIS Fee Missing

Severity : Critical

Resolution : Contact Customer
```

↓

## Step 5

Embeddings generated.

↓

## Step 6

Vectors stored in ChromaDB.

↓

## Step 7

User asks question.

↓

## Step 8

Retriever searches vector database.

↓

## Step 9

Relevant incidents retrieved.

↓

## Step 10

LangGraph workflow executes.

↓

## Step 11

Final response generated.

---

# LangGraph Architecture

## Why LangGraph?

Traditional Applications

```text
A → B → C
```

LangGraph

```text
User Question
      │
      ▼
 Search Agent
      │
      ▼
 Root Cause Agent
      │
      ▼
 Recommendation Agent
      │
      ▼
 Summary Agent
      │
      ▼
 Final Response
```

Advantages

- Stateful workflows
- Conditional routing
- Multi-agent orchestration
- Complex AI workflows

---

# Agent Responsibilities

## Search Agent

Purpose

Retrieve relevant incidents from ChromaDB.

Input

```
Why did GINR123 fail?
```

Output

Relevant payment records.

---

## Root Cause Analysis Agent

Purpose

Analyze retrieved incidents.

Output

```
Root Cause:
FIS Fee Missing
```

---

## Recommendation Agent

Purpose

Suggest corrective actions.

Output

```
Contact customer and request payment.
```

---

## Summary Agent

Purpose

Generate human-readable response.

Example

```
GINR123 failed because the Full Interconnection Study fee was not received.
```

---

# State Flow

```text
Initial State
{ question }

        │
        ▼

Search Agent
{ question + context }

        │
        ▼

RCA Agent
{ question + context + root_cause }

        │
        ▼

Recommendation Agent
{ recommendation }

        │
        ▼

Summary Agent
{ final_answer }
```

---

# Project Structure

```text
payment-ai-platform/

├── api/
│   ├── main.py
│   ├── routes.py
│
├── agents/
│   ├── search_agent.py
│   ├── rca_agent.py
│   ├── recommendation_agent.py
│   └── summary_agent.py
│
├── rag/
│   ├── ingest.py
│   ├── retriever.py
│   ├── embeddings.py
│   └── graph.py
│
├── data/
│   ├── 2025/
│   └── 2026/
│
├── chroma_db/
│
├── requirements.txt
│
└── README.md
```

---

# REST APIs

## Health Check

```http
GET /health
```

Response

```json
{
  "status":"UP"
}
```

---

## Ask Question

```http
POST /ask
```

Request

```json
{
  "question":"Why did GINR123 fail?"
}
```

Response

```json
{
  "answer":"FIS Fee Missing"
}
```

---

# Installation

## Clone Repository

```bash
git clone payment-ai-platform

cd payment-ai-platform
```

---

## Create Virtual Environment

```bash
python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Start Ollama

```bash
ollama serve
```

---

## Pull Models

```bash
ollama pull llama3

ollama pull nomic-embed-text
```

---

## Verify Models

```bash
ollama list
```

---

## Load Reports

```bash
python -m rag.ingest
```

Example

```text
Found 24 files

Loaded 3500 records

ChromaDB Created Successfully
```

---

## Start FastAPI

```bash
uvicorn api.main:app --reload
```

Swagger

```
http://localhost:8000/docs
```

---

# Sample Questions

Operational

- Why did GINR123 fail?
- Show duplicate payments.
- Show payment synchronization failures.
- Show all critical failures.

Management

- Show trends for last three months.
- Which failure type is increasing?
- Show monthly failure distribution.

Executive

- Generate quarterly summary.
- Show risk areas.
- Recommend operational improvements.

---

# Production Deployment

```text
Docker Container
       │
       ▼
Kubernetes
       │
       ▼
Load Balancer
       │
       ▼
FastAPI Pods
       │
       ▼
ChromaDB
       │
       ▼
Ollama
       │
       ▼
Persistent Storage
```

---

# Monitoring

## Prometheus

Collects

- API Requests
- Latency
- Token Usage
- Embedding Time

## Grafana Dashboards

- API Health
- Agent Performance
- Question Volume
- Failure Trends

---

# Resume Description

Designed and developed an AI-powered **Payment Failure Intelligence Platform** using **LangGraph, LangChain, Ollama, ChromaDB, and FastAPI**. Implemented Retrieval-Augmented Generation (RAG) pipelines to ingest historical payment reports, perform semantic search, identify root causes, generate recommendations, and provide conversational analytics. Built a multi-agent architecture consisting of Search, Root Cause Analysis, Recommendation, and Summary agents, enabling faster incident investigation and improved operational visibility.

---

# Interview Explanation (5 Minutes)

The business problem was that ERCOT operations teams manually investigated payment failures using CSV, HTML, and Excel reports. As report volumes increased, identifying historical incidents and root causes became increasingly difficult.

To solve this problem, we designed an AI-powered Payment Failure Intelligence Platform using LangGraph, LangChain, Ollama, ChromaDB, and FastAPI.

Historical reports are ingested through a RAG pipeline, converted into embeddings using the **nomic-embed-text** model, and stored in ChromaDB.

When users ask operational questions, a LangGraph workflow orchestrates multiple AI agents:

- Search Agent
- Root Cause Analysis Agent
- Recommendation Agent
- Summary Agent

These agents retrieve relevant historical incidents, analyze root causes, recommend corrective actions, and generate human-readable responses.

The platform enables conversational access to operational knowledge, significantly reducing manual investigation effort while improving operational visibility and decision-making.

---

# Key Features

- Retrieval-Augmented Generation (RAG)
- LangGraph Multi-Agent Workflow
- LangChain Integration
- ChromaDB Vector Search
- Ollama LLM
- FastAPI REST APIs
- Semantic Search
- Root Cause Analysis
- AI Recommendations
- Executive Summaries
- Production Deployment
- Monitoring with Prometheus & Grafana
- Kubernetes Ready

---