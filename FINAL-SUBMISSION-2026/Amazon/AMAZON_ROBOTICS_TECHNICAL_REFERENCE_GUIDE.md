# Amazon Robotics: Technical Reference & Architecture Guide

**For:** Senior Full-Stack Engineer Role Assessment  
**Project:** PLM to MES End-to-End Integration Architecture  
**Date:** May 2026

---

## Project Overview

### What is Amazon Robotics PLM-MES Integration?

Amazon Robotics PLM to MES integration is a mission-critical enterprise system that orchestrates the complete product lifecycle for autonomous robotic systems—from initial engineering design through manufacturing execution to warehouse deployment. It bridges Agile PLM (Product Lifecycle Management) as the central source of truth with Manufacturing Execution Systems (MES) that drive actual robot production.

**Scale:**
- 200+ concurrent users (robotics engineers, manufacturing planners, quality teams)
- 10,000+ BOMs (Bills of Materials) processed daily
- 500+ robot product variants managed
- 500+ Amazon fulfillment centers receiving robots
- 99.9% uptime SLA for mission-critical operations

---

## System Architecture

### High-Level Architecture

```
┌──────────────────────────────────────────────────────┐
│ Phase 1: Engineering (PLM)                          │
│ Agile PLM - Product Structures, CAD, BOMs, ECOs    │
└──────────────────────────────────────────────────────┘
            ↓ (Released Product)
┌──────────────────────────────────────────────────────┐
│ Phase 2: Integration Layer                          │
│ Java/Spring Boot Microservices                      │
│ - Extract (REST + SOAP APIs)                        │
│ - Transform (PLM → MES format)                      │
│ - Validate & Enrich                                 │
│ - Publish (Kafka/SQS)                               │
└──────────────────────────────────────────────────────┘
            ↓ (Transformed Data)
┌──────────────────────────────────────────────────────┐
│ Phase 3: Manufacturing (MES)                        │
│ Manufacturing Execution System                       │
│ - Work Order Generation                             │
│ - Assembly Instructions                             │
│ - Component Tracking                                │
│ - Quality Checkpoints                               │
└──────────────────────────────────────────────────────┘
            ↓ (Manufactured Robots)
┌──────────────────────────────────────────────────────┐
│ Phase 4: Warehouse Deployment                       │
│ Amazon Fulfillment Centers                          │
│ - Robot Serialization & Testing                     │
│ - Configuration & Onboarding                        │
│ - WCS Integration (Warehouse Control System)        │
│ - Operational Deployment                            │
└──────────────────────────────────────────────────────┘
```

### Technology Stack

**Frontend:**
- Angular 15+ (responsive dashboards)
- TypeScript (strict typing)
- RxJS (reactive streams)
- NgRx (state management)
- Material Design (enterprise UI)

**Backend:**
- Java 17 (core language)
- Spring Boot 3.x (microservices)
- Spring Data JPA (ORM)
- Spring Cloud (service coordination)
- Spring Security (OAuth2/OIDC)

**Integration:**
- REST APIs (modern systems)
- SOAP services (legacy PLM)
- Apache Kafka (event streaming)
- Amazon SQS (AWS Lambda integration)

**Data:**
- Oracle Database (PLM warehouse)
- Amazon DynamoDB (NoSQL cache)
- Amazon S3 (documents, CAD files)
- Redis (session cache, rate limiting)

**DevOps:**
- Docker (containerization)
- Amazon ECS/EKS (orchestration)
- Terraform (IaC)
- Jenkins/GitHub Actions (CI/CD)
- CloudWatch (monitoring)

---

## Module Breakdown

### Backend Microservices

#### 1. PLM Data Service
**Responsibility:** Extract PLM data and prepare for transformation
```
GET  /api/v1/products              - List released products
GET  /api/v1/products/{id}         - Get product structure (BOM hierarchy)
GET  /api/v1/products/{id}/bom     - Get flattened BOM
GET  /api/v1/ecos                  - Get Engineering Change Orders
GET  /api/v1/releases              - Get release history
POST /api/v1/products/{id}/sync    - Trigger manual sync
```

**Key Features:**
- REST client for PLM SOAP API
- Caching layer (Redis)
- Pagination for large product lists
- Change tracking (what changed since last sync)
- Error handling with retry logic

**Database Queries:**
- `SELECT product_id, name, version FROM products WHERE status = 'RELEASED'`
- `SELECT component_id, qty FROM bom WHERE product_id = ?`
- `SELECT eco_id, change_date FROM ecos WHERE product_id = ?`

#### 2. Data Transformation Service
**Responsibility:** Transform PLM structures to MES-compatible format
```
POST /api/v1/transform/bom         - Transform BOM for MES
POST /api/v1/transform/batch       - Batch transform 1000+ BOMs
POST /api/v1/validate/bom          - Validate BOM completeness
GET  /api/v1/transform/status      - Transformation job status
```

**Transformation Logic:**
```
PLM Hierarchy        →  MES Flat BOM
Product (Qty: 1)         Part001 (Qty: 1)
├─ Component A (Q: 2)    Part002 (Qty: 2)
├─ Assembly B (Q: 1)     Part003 (Qty: 1)
│  ├─ Sub-C (Q: 3)       Part004 (Qty: 3)
│  └─ Sub-D (Q: 1)       Part005 (Qty: 1)
```

**Features:**
- Recursive traversal algorithm
- Quantity multiplication
- Part number mapping (internal → supplier)
- Attribute enrichment (specs, certifications)
- Validation rules (no missing fields, valid suppliers)

#### 3. MES Integration Service
**Responsibility:** Publish transformed data to MES and receive feedback
```
POST /api/v1/publish/bom           - Publish BOM to MES
POST /api/v1/publish/order         - Create work order
GET  /api/v1/orders/{id}           - Get order status
POST /api/v1/feedback/quality      - Receive quality data
```

**Key Operations:**
- BOM publishing to MES via REST API
- Work order generation
- Message publishing to Kafka
- Error handling with dead letter queues
- Idempotency (prevent duplicate processing)

#### 4. Workflow Orchestration Service
**Responsibility:** Manage product lifecycle and approval workflows
```
POST /api/v1/workflows/release     - Start release workflow
POST /api/v1/workflows/{id}/approve - Approve by next stage
GET  /api/v1/workflows/{id}        - Get workflow status
POST /api/v1/workflows/{id}/reject  - Reject with feedback
```

**Workflow States:**
```
InDesign → InReview → ReadyForRelease → Released → Obsolete
   ↑           ↓
   └─ ReviewRejected
```

**Approval Routing:**
- Engineering sign-off (design verification)
- Quality sign-off (compliance check)
- Manufacturing sign-off (feasibility review)
- Supply chain sign-off (sourcing confirmation)

### Frontend Components

#### 1. PLM Dashboard
- **Product Browser:** Hierarchical tree view of designs
- **BOM Editor:** Live editing with validation
- **Change Management:** Create and track ECOs
- **Release Workflow:** Progress through approval stages
- **Search & Filter:** Find products by name, code, category

#### 2. Manufacturing Dashboard
- **Work Orders:** Active orders with progress tracking
- **Component Status:** Availability and substitutions
- **Quality Events:** Checkpoints and test results
- **Performance Metrics:** KPIs and production analytics
- **Alerts:** Exception notifications for manufacturing issues

#### 3. Admin Console
- **User Management:** RBAC configuration
- **System Health:** Service status and metrics
- **Integration Logs:** Error tracking and debugging
- **Configuration:** Sync schedules, transformation rules
- **Audit Trail:** Complete change history

---

## API Reference

### PLM Data Extraction Endpoints

```
GET /api/v1/products?status=RELEASED&page=1&size=100
Response (200 OK):
{
  "data": [
    {
      "productId": 12345,
      "name": "Mobile Manipulator Unit v2.0",
      "code": "MMU-200",
      "status": "RELEASED",
      "version": "2.0.1",
      "releaseDate": "2026-05-01",
      "components": 145,
      "lastModified": "2026-05-03T10:30:00Z"
    }
  ],
  "pagination": { "total": 523, "page": 1, "pageSize": 100 }
}

GET /api/v1/products/12345/bom
Response (200 OK):
{
  "productId": 12345,
  "bomItems": [
    { "partNumber": "MEC-001", "description": "Motor Controller", "quantity": 2, "supplier": "MotorCorp" },
    { "partNumber": "ARM-002", "description": "Robotic Arm Assembly", "quantity": 1, "supplier": "ArmTech" },
    { "partNumber": "GRP-003", "description": "Gripper Jaw", "quantity": 2, "supplier": "GripperInc" }
  ],
  "totalCost": 15000,
  "leadTime": 45
}
```

### Data Transformation Endpoints

```
POST /api/v1/transform/bom
Request:
{
  "productId": 12345,
  "sourceFormat": "PLM",
  "targetFormat": "MES"
}

Response (200 OK):
{
  "transformationId": "TXN-98765",
  "status": "COMPLETED",
  "sourceBom": { "components": 145, "lines": 543 },
  "targetBom": { "flatItems": 543, "totalQuantity": 2100 },
  "validationErrors": [],
  "processingTime": "892ms"
}
```

### MES Publishing Endpoints

```
POST /api/v1/publish/bom
Request:
{
  "bomId": "TXN-98765",
  "target": "MES",
  "scheduleDate": "2026-05-04T06:00:00Z"
}

Response (202 Accepted):
{
  "publishId": "PUB-54321",
  "status": "QUEUED",
  "estimatedDelivery": "2026-05-04T06:15:00Z",
  "destination": "MES_PROD"
}

GET /api/v1/publish/PUB-54321
Response (200 OK):
{
  "publishId": "PUB-54321",
  "status": "DELIVERED",
  "deliveryTime": "2026-05-04T06:05:23Z",
  "acknowledgedBy": "MES_PROD",
  "messagesPublished": 543,
  "errors": 0
}
```

### Workflow Endpoints

```
POST /api/v1/workflows/release
Request:
{
  "productId": 12345,
  "targetDate": "2026-05-10",
  "releaseNotes": "Production ready v2.0.1"
}

Response (201 Created):
{
  "workflowId": "WF-11111",
  "productId": 12345,
  "currentStage": "ENGINEERING_APPROVAL",
  "approvers": ["eng@amazon.com", "quality@amazon.com", "mfg@amazon.com"],
  "createdAt": "2026-05-03T10:00:00Z"
}

POST /api/v1/workflows/WF-11111/approve
Request:
{
  "approvedBy": "quality@amazon.com",
  "comments": "Quality review passed. No concerns."
}

Response (200 OK):
{
  "workflowId": "WF-11111",
  "previousStage": "QUALITY_APPROVAL",
  "currentStage": "MFG_APPROVAL",
  "nextApprover": "mfg@amazon.com",
  "approvalChain": [
    { "stage": "ENGINEERING_APPROVAL", "status": "APPROVED", "approvedAt": "2026-05-03T10:15:00Z" },
    { "stage": "QUALITY_APPROVAL", "status": "APPROVED", "approvedAt": "2026-05-03T10:25:00Z" }
  ]
}
```

---

## Database Architecture

### PLM Database (Oracle)

```sql
-- Products Table
CREATE TABLE products (
  product_id NUMBER PRIMARY KEY,
  name VARCHAR2(255),
  code VARCHAR2(50) UNIQUE,
  version VARCHAR2(20),
  status VARCHAR2(20),  -- INDESIGN, INREVIEW, RELEASED, OBSOLETE
  release_date DATE,
  created_date DATE,
  modified_date DATE,
  created_by VARCHAR2(100),
  modified_by VARCHAR2(100)
);

-- BOM Items (Hierarchical)
CREATE TABLE bom_items (
  item_id NUMBER PRIMARY KEY,
  product_id NUMBER REFERENCES products,
  parent_item_id NUMBER REFERENCES bom_items,
  part_number VARCHAR2(50),
  description VARCHAR2(255),
  quantity NUMBER,
  supplier_id NUMBER,
  unit_cost NUMBER,
  lead_time_days NUMBER
);

-- Engineering Change Orders
CREATE TABLE ecos (
  eco_id NUMBER PRIMARY KEY,
  product_id NUMBER REFERENCES products,
  eco_number VARCHAR2(50) UNIQUE,
  description VARCHAR2(1000),
  impact_area VARCHAR2(100),
  status VARCHAR2(20),  -- DRAFT, APPROVED, IMPLEMENTED
  created_date DATE,
  effective_date DATE
);

-- Approvals & Workflows
CREATE TABLE workflow_approvals (
  approval_id NUMBER PRIMARY KEY,
  workflow_id NUMBER,
  stage VARCHAR2(50),
  approver_email VARCHAR2(100),
  status VARCHAR2(20),  -- PENDING, APPROVED, REJECTED
  comments VARCHAR2(1000),
  approved_at DATE
);
```

### Integration Database (Oracle)

```sql
-- Transformation Log
CREATE TABLE transformation_log (
  txn_id NUMBER PRIMARY KEY,
  product_id NUMBER,
  source_format VARCHAR2(20),
  target_format VARCHAR2(20),
  status VARCHAR2(20),  -- INPROGRESS, COMPLETED, FAILED
  source_count NUMBER,
  target_count NUMBER,
  processing_time_ms NUMBER,
  created_at DATE,
  error_message CLOB
);

-- Publishing History
CREATE TABLE publish_history (
  publish_id NUMBER PRIMARY KEY,
  txn_id NUMBER REFERENCES transformation_log,
  destination VARCHAR2(50),  -- MES_PROD, MES_QA, etc.
  status VARCHAR2(20),  -- QUEUED, DELIVERED, FAILED
  message_count NUMBER,
  delivery_time DATE,
  acknowledged_at DATE
);

-- Event Log (for Kafka publishing)
CREATE TABLE event_log (
  event_id NUMBER PRIMARY KEY,
  event_type VARCHAR2(50),  -- ProductReleased, BomChanged, etc.
  product_id NUMBER,
  payload CLOB,
  status VARCHAR2(20),  -- PUBLISHED, CONSUMED, FAILED
  published_at DATE,
  consumed_at DATE
);
```

### Cache Database (Redis)

```
Key: products:{product_id}
Value: {
  "productId": 12345,
  "name": "Mobile Manipulator Unit",
  "bom": { "components": 145, "hash": "abc123" }
}
TTL: 1 hour

Key: bom:{product_id}
Value: Flat BOM list (cached transformation result)
TTL: 24 hours

Key: workflow:{workflow_id}
Value: Current workflow state and approvers
TTL: 7 days (until workflow completes)
```

---

## Deployment & DevOps

### Docker Container Structure

```dockerfile
FROM openjdk:17-slim
WORKDIR /app
COPY --chown=appuser:appuser build/libs/plm-mes-service.jar app.jar
EXPOSE 8080
CMD ["java", "-Xmx1g", "-Xms512m", "-jar", "app.jar"]
```

### Kubernetes Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: plm-data-service
  namespace: robotics
spec:
  replicas: 3
  selector:
    matchLabels:
      app: plm-data-service
  template:
    metadata:
      labels:
        app: plm-data-service
    spec:
      containers:
      - name: plm-data-service
        image: robotics/plm-data-service:1.0.0
        ports:
        - containerPort: 8080
        env:
        - name: ORACLE_HOST
          valueFrom:
            configMapKeyRef:
              name: db-config
              key: oracle-host
        resources:
          requests:
            memory: "512Mi"
            cpu: "250m"
          limits:
            memory: "1Gi"
            cpu: "500m"
        livenessProbe:
          httpGet:
            path: /actuator/health
            port: 8080
          initialDelaySeconds: 30
          periodSeconds: 10
```

### CI/CD Pipeline

```
1. Code Commit → GitHub
2. GitHub Actions Trigger
   ├─ Maven: mvn clean install
   ├─ Tests: ./mvnw test
   ├─ SonarQube: Code quality scan
   └─ Build: Docker image build
3. Docker Registry: Push image (ECR)
4. Terraform: Update infrastructure
5. Kubernetes: Rolling update
   ├─ Health checks
   ├─ Canary deployment (5% traffic)
   └─ Gradual rollout (100%)
6. Smoke Tests: Verify deployment
7. Notification: Slack alert
```

---

## Key Workflows

### Release Workflow

```
1. Engineer creates product & BOM in PLM
2. Submits for engineering review
3. Engineering team reviews design
4. If rejected: feedback loop
5. If approved: moves to Quality review
6. Quality verifies compliance
7. If rejected: ECO created
8. If approved: moves to Manufacturing
9. Manufacturing feasibility check
10. If rejected: feedback
11. If approved: Product released
12. Integration service detects release
13. Extracts product data from PLM
14. Transforms to MES format
15. Publishes to MES via Kafka
16. MES generates work orders
17. Manufacturing begins
```

### Data Sync Workflow

```
1. Scheduler triggers sync (hourly)
2. Query PLM for modified products
3. Cache check (skip if unchanged)
4. Extract product structure
5. Validate BOM completeness
6. Transform to MES format
7. Compare with previous version (delta detection)
8. If changed: publish event to Kafka
9. Log transformation result
10. Update cache with new data
11. Alert manufacturing if critical changes
12. Archive previous version
```

### Error Handling Workflow

```
1. Error detected (constraint violation, transformation failure, API error)
2. Log error details with stack trace
3. Send alert (CloudWatch → PagerDuty)
4. Retry logic:
   - Transient error: exponential backoff (1s, 2s, 4s, 8s)
   - Permanent error: escalate to human
5. Dead letter queue: store failed messages
6. Manual review queue: for investigation
7. RCA process: document root cause
8. Prevention: implement safeguard
9. Redeploy fix
10. Reprocess failed messages
```

---

## Production Troubleshooting

### Issue: PLM Data Extraction Timeout

**Symptoms:**
- Transformation jobs timing out after 30 seconds
- PLM REST API calls returning 504 Gateway Timeout
- Integration logs: "Connection timeout to PLM API"

**Root Cause Analysis:**
```sql
-- Check PLM query performance
SELECT * FROM v$session WHERE sql_text LIKE '%BOM%' AND status = 'ACTIVE';
EXPLAIN PLAN FOR SELECT * FROM bom_items WHERE product_id = 12345;
SELECT * FROM TABLE(dbms_xplan.display);
```

**Solution:**
1. Add index on product_id, modified_date
2. Implement pagination (fetch 1000 items at a time)
3. Cache frequently accessed BOMs
4. Increase PLM API timeout from 30s to 60s

**Prevention:**
- Monitor query execution time
- Alert if transformation takes >5 seconds
- Implement circuit breaker (fail fast after 3 retries)

### Issue: Message Queue Backlog

**Symptoms:**
- Consumer lag increasing
- Kafka topics backing up
- Manufacturing delays due to work order delays
- Dashboard showing "QUEUED" for hours

**Root Cause Analysis:**
```
-- Check Kafka consumer group status
kafka-consumer-groups --bootstrap-server localhost:9092 --group mes-integration-group --describe

-- Output shows:
TOPIC     PARTITION  CURRENT-OFFSET  LOG-END-OFFSET  LAG
mes-data  0          50000           100000          50000  ← LAGGING
```

**Solution:**
1. Increase consumer thread count (4 → 8 threads)
2. Increase batch size (500 → 1000 messages)
3. Optimize transformation logic (from 2s → 500ms)
4. Add additional consumer instances (1 → 2 pods)

**Prevention:**
- Set alarm threshold (LAG > 10000)
- Scale consumers based on CPU/memory
- Monitor transformation performance continuously

### Issue: Data Discrepancy Between PLM and MES

**Symptoms:**
- Manufacturing reports missing components
- Work orders contain wrong quantities
- Quality checks finding component mismatches

**Root Cause Analysis:**
```sql
-- Compare PLM BOM with MES records
SELECT plm.part_number, plm.qty, mes.qty
FROM plm_bom plm
LEFT JOIN mes_bom mes ON plm.part_number = mes.part_number
WHERE plm.qty <> mes.qty OR mes.qty IS NULL;
```

**Solution:**
1. Check transformation logic for edge cases
2. Verify supplier code mapping is correct
3. Review schema version compatibility
4. Implement checksum validation before publish

**Prevention:**
- Data validation rules in transformation service
- Automated reconciliation reports (daily)
- Early alert if transformation errors exceed 0.1%

---

## Performance Optimization Strategies

### Database Optimization
```sql
-- Add indexes on frequently queried columns
CREATE INDEX idx_products_status ON products(status);
CREATE INDEX idx_bom_items_product ON bom_items(product_id);
CREATE INDEX idx_bom_items_modified ON bom_items(modified_date);

-- Partition large tables by product category
ALTER TABLE bom_items PARTITION BY LIST(category) ...

-- Monitor long-running queries
SELECT * FROM v$sql WHERE elapsed_time > 1000000 ORDER BY elapsed_time DESC;
```

### Caching Strategy
```
L1 Cache (Local): In-memory cache (1 minute TTL)
L2 Cache (Redis): Distributed cache (1 hour TTL)
L3 Cache (DB): Source of truth (Oracle)

Product structure: 100MB across all products
Hit rate target: >85%
```

### API Optimization
```
-- Response compression
gzip: enabled (>1KB responses)

-- Connection pooling
Min: 10, Max: 50
Timeout: 30 seconds

-- Rate limiting
Per-user: 1000 requests/minute
Per-IP: 10000 requests/minute
```

---

## Monitoring & Alerting

### Key Metrics
```
Transformation Success Rate: >99.5%
API Response Time (p95): <500ms
Kafka Consumer Lag: <10,000 messages
System Availability: 99.9%
Data Accuracy: 99.8%
```

### Alerts
```
CRITICAL:
- Transformation failure rate > 1%
- API response time > 2 seconds (p95)
- Kafka lag > 50,000 messages
- System downtime

WARNING:
- Transformation failure rate > 0.5%
- API response time > 1 second (p95)
- Kafka lag > 10,000 messages
- Approaching capacity limits
```

---

**End of Technical Reference Guide**

*For questions or clarifications, contact the Amazon Robotics development team.*

