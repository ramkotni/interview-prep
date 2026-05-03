# RARF Project: Technical Reference & Architecture Guide

**For:** Senior Full-Stack Engineer Role Assessment  
**Project:** ERCOT RARF (Renewable Energy Resources & Facilities)  
**Date:** May 2026

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Technology Stack](#technology-stack)
4. [Module Breakdown](#module-breakdown)
5. [API Reference](#api-reference)
6. [Database Architecture](#database-architecture)
7. [Deployment & DevOps](#deployment--devops)
8. [Key Workflows](#key-workflows)
9. [Performance Considerations](#performance-considerations)
10. [Production Runbooks](#production-runbooks)

---

## Project Overview

### What is RARF?
RARF (Renewable Energy Resources & Facilities) is a web-based SaaS platform enabling Market Participants to register, manage, and track renewable energy assets across ERCOT's grid. It supports a complex lifecycle from initial interconnection requests (INRs) through asset staging, validation, and graduation to production operations.

### Key Stakeholders
- **Market Participants:** 100+ renewable energy companies
- **Grid Operators:** ERCOT operations team managing asset integration
- **Regulators:** NERC for compliance, CIP security standards
- **End Users:** Asset managers, engineers, compliance officers

### Business Value
- Streamlined asset registration reducing time-to-market
- Automated validation preventing grid stability issues
- Complete audit trail for compliance requirements
- Real-time visibility into renewable energy portfolio

---

## System Architecture

### High-Level Architecture

```
┌──────────────────────────────────────────────────────┐
│                    Market Participant                 │
│                    Browser (Chrome)                   │
└──────────────────────────────────────────────────────┘
                           ↓ HTTPS
┌──────────────────────────────────────────────────────┐
│              Angular SPA (19.2.8)                     │
│  - Dashboard, Asset Forms, Change Requests, Reports  │
│  - Auth0 OAuth2, Role-Based UI Rendering             │
│  - Akita State Management                            │
└──────────────────────────────────────────────────────┘
                           ↓ REST/JSON
┌──────────────────────────────────────────────────────┐
│         Tomcat 9 Application Server (JVM)            │
│                                                       │
│  ┌────────────────────────────────────────────────┐  │
│  │ Jersey REST Framework (50+ Endpoints)          │  │
│  │ - AssetsResource, SubstationsResource, etc.    │  │
│  └────────────────────────────────────────────────┘  │
│                       ↓                              │
│  ┌────────────────────────────────────────────────┐  │
│  │ Service Layer (30+ Services)                   │  │
│  │ - Validation, Graduation, Migration            │  │
│  │ - Business Logic Orchestration                 │  │
│  └────────────────────────────────────────────────┘  │
│                       ↓                              │
│  ┌────────────────────────────────────────────────┐  │
│  │ Persistence Layer (100+ Repositories)          │  │
│  │ - Hibernate ORM, JPA Queries                   │  │
│  └────────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────────┘
                           ↓ JDBC
┌──────────────────────────────────────────────────────┐
│         Oracle 19c Database (Three Schemas)          │
│                                                       │
│  ┌──────────┐  ┌─────────────┐  ┌──────────┐       │
│  │  GINR    │  │  RARFSTG    │  │  RARF    │       │
│  │ Request  │→ │  Staging    │→ │Production│       │
│  │  Schema  │  │   Schema    │  │  Schema  │       │
│  └──────────┘  └─────────────┘  └──────────┘       │
└──────────────────────────────────────────────────────┘
```

### Three-Schema Strategy

**GINR (Interconnection Schema)**
- Stores INR requests from market participants
- Tracks request status (ACK, SUB, MOD, PRC, CAN)
- Maintains INR-to-substation mapping (SUBSTATION_REFERENCE table)
- Read-only integration point for grid operations

**RARFSTG (Staging Schema)**
- Intermediate consolidation zone
- Stores staged asset data before graduation
- Supports multi-tech substation consolidation
- Houses pre-graduation validation results

**RARF (Production Schema)**
- Final production asset records
- Complete asset hierarchy with all child objects
- Used by grid operations, EMS/SCADA integration
- Ownership-based multi-tenancy model

---

## Technology Stack

### Frontend
```
Angular 19.2.8
├── @angular/core (routing, dependency injection)
├── @angular/forms (reactive forms, validators)
├── @angular/common (HTTPClient, pipes)
├── @angular/router (lazy loading, route guards)
├── RxJS (7.x) - observables, operators, subscriptions
├── Akita (6.x) - entity store, state management
├── Bootstrap (ng-bootstrap) - UI components
├── Font Awesome (icons)
└── TypeScript 5.7 (strict mode)
```

### Backend
```
Java 17 + Spring/Jakarta EE
├── Jersey 2.35 (REST framework, @Path, @GET/POST)
├── Hibernate 5.2.12 (ORM, JPA)
├── Oracle JDBC (database connectivity)
├── Quartz (scheduler, cron jobs)
├── SLF4J + Logback (logging)
├── JUnit + Mockito (testing)
└── Maven 3.8+ (build automation)
```

### Database
```
Oracle 19c
├── JDBC Connection Pooling (Tomcat DBCP)
├── Three operational schemas (GINR, RARFSTG, RARF)
├── 100+ entity tables
├── Complex views (V$SESSION monitoring)
└── Stored procedures (ETL, data migration)
```

### DevOps & Infrastructure
```
Docker & Containerization
├── Base: tomcat:9-jdk11
├── Multi-stage build (Maven → WAR → Docker)
└── docker-compose.yaml (local development)

Kubernetes (Production)
├── Rolling deployments (zero-downtime)
├── Service mesh integration
├── ConfigMaps (environment configuration)
└── PersistentVolumes (data persistence)

CI/CD Pipeline
├── Git triggers (push to main)
├── Maven build (compile, test, package)
├── Docker image build & registry push
├── Kubernetes manifest update
└── Automated deployment
```

---

## Module Breakdown

### Frontend Modules (Angular)

#### 1. App Module (Root)
- Application initialization
- Authentication setup (Auth0)
- Shared services, interceptors, guards
- Global error handling

#### 2. Dashboard Module
- INR status tracking
- Multi-filter search (INR ID, company, status)
- ERCOT vs. Market Participant views
- Real-time update subscriptions

#### 3. Asset Management Module
- Solar Generator registration form
- Wind Generator configuration
- Combined Cycle setup
- ESR/Battery configuration
- Transformer & breaker inventory

#### 4. Change Request Module
- CR creation workflow
- Validation state tracking
- Approval routing
- Before/after value comparison

#### 5. SODG Module
- Settlement-Only Generator management
- Ownership tracking
- Graduation workflow
- Status transitions

#### 6. Shared Module
- Reusable form components
- Custom validators (async ESIID check)
- Pipe filters (date, currency, enum)
- HTTP interceptors (JWT injection, CORS)

### Backend Services (Java)

#### 1. Resource Layer (50+ Controllers)
**SubstationsResource**
- GET /staged, /processed, /inrId, /inrId/before
- POST /substations (create)
- PUT /substations/{id} (update)

**AssetsResource**
- GET /solar-generators, /wind-generators
- GET /combined-cycle, /conventional-generators
- CRUD operations for each asset type

**ChangeRequestsResource**
- GET /change-requests, /change-request/{id}
- POST /change-requests (submit)
- PUT /change-requests/{id}/approve
- Workflow transition endpoints

**EsrChargingDetailsResource**
- GET /esrChargingDetails/substation/{id}
- Deduplication handling for multiple owners

#### 2. Service Layer (30+ Services)
**SubstationsService**
- Substation CRUD, multi-tech consolidation
- Ownership resolution based on user DUNS
- Query filtering by record status (staged vs. processed)

**LSGGraduationService**
- Graduation orchestration (7,600+ LOC)
- 40+ asset type processing
- Parent-child relationship handling
- Pre-graduation validation
- Transaction rollback on failure

**MigrationService**
- RARFSTG → RARF migration logic
- Pre-migration validation
- Duplicate detection & resolution
- Migration status tracking

**ChangeRequestService**
- CR lifecycle management
- Validation state tracking
- Approval workflow orchestration

**ValidationService**
- Business rule enforcement
- Field-level validation
- Cross-field validation (dependent validations)
- Error collection & reporting

#### 3. Persistence Layer (100+ Repositories)
**SubstationsRepository**
- findByCode, findByAssetId
- Custom queries for multi-schema joins
- Pagination support

**AssetRepositories** (per asset type)
- BatteryUnitsRepository, TransformersRepository, etc.
- Type-specific queries, filtering
- Ownership-based result sets

**All repositories extend BaseRepository**
- Common CRUD methods
- Transaction management
- Entity lifecycle handling

---

## API Reference

### Core Endpoints

#### Substations Endpoints
```
# Staged (recordStatus = 1) - For INR registration
GET    /substations/staged                    200 OK - List all staged
GET    /substations/staged?id={id}            200 OK - Get single staged
POST   /substations                           201 Created - Create new
PUT    /substations/{id}                      200 OK - Update staged
DELETE /substations/{id}                      204 No Content - Delete

# Processed (recordStatus = 2) - After graduation
GET    /substations/processed                 200 OK - List processed
GET    /substations/processed?id={id}         200 OK - Get single processed
GET    /substations/processed?id={id}&ginrRequestId={gid}  INR-specific

# INR-Specific Views
GET    /substations/inrId/{inrId}             200 OK - By INR ID
GET    /substations/inrId/{inrId}/before      200 OK - Pre-graduation version
```

#### Change Requests Endpoints
```
# CRUD Operations
GET    /change-requests                       200 OK - List all CRs
GET    /change-request/{id}                   200 OK - Get CR with data
POST   /change-requests                       201 Created - Submit new CR
PUT    /change-requests/{id}                  200 OK - Update CR

# Workflow Transitions
POST   /change-requests/{id}/approve          200 OK - Approve CR
POST   /change-requests/{id}/reject           200 OK - Reject CR
POST   /change-requests/{id}/submit-for-approval  200 OK - Submit to ERCOT

# Change Request Data
GET    /change-request/{crId}/data            200 OK - Get all CR line items
GET    /change-request/{crId}/data/{dataId}   200 OK - Get specific line item
```

#### Assets Endpoints
```
# Solar Generators
GET    /solar-generators?substationId={id}    200 OK - List by substation
GET    /solar-generators/{id}                 200 OK - Get details
POST   /solar-generators                      201 Created - Create
PUT    /solar-generators/{id}                 200 OK - Update

# Wind Generators
GET    /wind-generators?substationId={id}
GET    /wind-generators/{id}
POST   /wind-generators
PUT    /wind-generators/{id}

# Combined Cycle
GET    /combined-cycle/configurations?substationId={id}
GET    /combined-cycle/generators?substationId={id}
GET    /combined-cycle/trains?substationId={id}

# Energy Storage Resources
GET    /esrChargingDetails/substation/{id}    # Deduplication applied
GET    /esrConnectivity/substation/{id}
GET    /esrInverters/substation/{id}
```

#### Graduation Endpoints
```
POST   /graduation/substation/{id}            202 Accepted - Trigger graduation
GET    /graduation/status/{id}                200 OK - Check graduation status
GET    /graduation/results/{inrId}            200 OK - View graduation results
```

#### Validation Endpoints
```
GET    /meters/checkEsiid/{type}/{id}/{esiid}     200 OK - Validate ESI ID
POST   /validate/substations/{id}                 200 OK - Full validation
GET    /ui-validation-state/{substationId}        200 OK - Panel errors
```

### Response Format

**Success Response (200 OK)**
```json
{
  "status": "success",
  "data": {
    "id": 12345,
    "code": "SUBSTATION_CODE",
    "name": "Substation Name",
    "substationId": 369,
    "recordStatusId": 2,
    "assets": [...]
  },
  "messages": []
}
```

**Error Response (400/500)**
```json
{
  "status": "error",
  "data": null,
  "messages": [
    {
      "severity": "ERROR",
      "message": "Substation not found: ID 999",
      "code": "SUBSTATION_NOT_FOUND"
    }
  ]
}
```

**Validation Error Response (422)**
```json
{
  "status": "validation_error",
  "data": {
    "panelErrors": {
      "unit-details": [
        "MAX_MW must be > 0",
        "ESIID is required"
      ],
      "connectivity": [
        "At least one connectivity node required"
      ]
    }
  },
  "messages": []
}
```

---

## Database Architecture

### Three-Schema Model

#### GINR Schema (Interconnection Requests)
```
GINR_REQUEST
├── ID (PK)
├── INR_ID (unique, e.g., "23INR0408")
├── PROJECT_NAME
├── TECHNOLOGY_TYPE (SOLAR, WIND, ESR, etc.)
├── MAX_GEN_MW
├── POI (Point of Interconnection)
├── ID_APPLICATION_STATUS (PLN, ACK, SUB, MOD, PRC, CAN)
├── ID_COMPANY (DUNS lookup)
└── timestamps (CREATED, UPDATED)

SUBSTATION_REFERENCE
├── ID (PK)
├── ID_GINR_REQUEST (FK → GINR_REQUEST)
├── SUBSTATION_ID (FK → RARFSTG.SUBSTATIONS)
├── ID_RARF_STATUS (ACK, SUB, MOD, PRC, CAN)
├── TARGET_DATE
└── PREGRAD_STATUS, GRADUATION_STATUS
```

#### RARFSTG Schema (Staging)
```
SUBSTATIONS
├── ID (PK)
├── CODE (unique, e.g., "CMPD_SL2")
├── NAME
├── ASSET_ID (FK → ASSETS)
├── ID_RARF (FK → RARF.SUBSTATIONS after graduation)
├── RECORD_STATUS_ID (1=staged, 2=graduated)
├── ADDRESS, CITY, COUNTY, STATE, ZIP
├── LATITUDE, LONGITUDE
├── SERVICE_START, SERVICE_STOP
└── timestamps

[Child tables - same structure for all asset types]
SOLAR_GENERATORS
├── ID (PK)
├── NAME, CODE
├── SUBSTATION_ID (FK → SUBSTATIONS)
├── REAL_POWER_RATING_MW
├── ID_RARF (after graduation)
└── timestamps

ENERGY_STORAGE_RESOURCES
├── ID (PK)
├── SUBSTATION_ID
├── NAME
├── UNIT_START, UNIT_END
├── ID_RARF
└── child objects (ESR_CHARGING_DETAILS, ESR_INVERTERS, etc.)

TRANSFORMERS
├── ID (PK)
├── SUBSTATION_ID (or EXTERNAL_SUBSTATION_ID for non-local)
├── NAME, CODE
├── [50+ technical parameters]
├── ID_RARF
└── child: TRANSFORMER_TAPS

LINES
├── ID (PK)
├── SUBSTATION_ID_FROM, SUBSTATION_ID_TO
├── EXTERNAL_SUBSTATION_ID
├── LINE_RATING
├── ID_RARF
└── timestamps
```

#### RARF Schema (Production)
```
[Identical structure to RARFSTG for graduated records]

OWNERSHIP
├── ID (PK)
├── ASSET_ID (FK → ASSETS)
├── COMPANY_ID (FK → COMPANIES)
├── PERCENTAGE (ownership %)
├── MASTER_OWNER (Y/N)
├── BEGIN (start date)
├── END (end date - NULL = active)
└── timestamps

[For multi-tenant filtering]
User DUNS (1190850713000)
  → OWNERSHIP.COMPANY_ID
  → OWNERSHIP.ASSET_ID
  → Substation/Asset linked to ASSET_ID
  → Filter API response by ownership
```

### Critical Queries

**Find Substation by INR ID**
```sql
SELECT s.* FROM rarf.substations s
JOIN rarfstg.substations stg ON s.id_rarfstg = stg.id
JOIN ginr.substation_reference sr ON sr.substation_id = stg.id
JOIN ginr.ginr_request gr ON gr.id = sr.id_ginr_request
WHERE gr.inr_id = '23INR0408';
```

**Find Assets by User DUNS (Multi-Tenant)**
```sql
SELECT DISTINCT s.id, s.code, s.name FROM rarf.substations s
JOIN rarf.asset_ownership_vw v ON s.id = v.substation_id
JOIN rarf.ownership o ON o.asset_id = v.asset_id
WHERE o.company_id = (
  SELECT id FROM rarf.companies WHERE duns = '1190850713000'
)
AND o.master_owner = 1
AND (o.begin IS NULL OR o.begin <= SYSDATE)
AND (o.end IS NULL OR o.end >= SYSDATE);
```

**Find Duplicate Ownership**
```sql
SELECT asset_id, COUNT(*) as active_owner_count, SUM(percentage) as total_pct
FROM rarf.ownership
WHERE (begin IS NULL OR begin <= SYSDATE)
  AND (end IS NULL OR end >= SYSDATE)
GROUP BY asset_id
HAVING COUNT(*) > 1 OR SUM(percentage) <> 1;
```

---

## Deployment & DevOps

### Local Development Setup

**Prerequisites:**
- Docker Desktop with Compose V2
- Maven 3.8+
- Java 17 JDK
- Node.js 18+

**Build & Run Locally:**
```bash
# Clone repository
git clone ssh://git@git.ercot.com:7999/mpo/rarf.git
cd rarf

# Build Maven modules
mvn clean install -DskipTests

# Build Docker images
docker-compose build

# Start services
docker-compose up

# Access application
http://localhost:8080/rioo-rs
```

### CI/CD Pipeline

**Git → Bitbucket → Jenkins → Docker Registry → Kubernetes**

```
1. Developer Commits Code
   └→ Git push to main branch

2. Jenkins CI Trigger
   ├→ Maven clean build
   ├→ Compile Java source
   ├→ Run JUnit tests
   ├→ Build Angular (prod mode)
   ├→ Package WAR with embedded frontend
   └→ Execute SonarQube code analysis

3. Docker Build
   ├→ Multi-stage Dockerfile
   ├→ Stage 1: Maven build (rarf-model, rarf-rest-api, rarf-webapp)
   ├→ Stage 2: Tomcat container with WAR deployment
   └→ Tag image: rarf:1.10.3-SNAPSHOT

4. Push to Registry
   └→ Private Docker registry (artifactory)

5. Deploy to Kubernetes
   ├→ Update deployment manifest with new image tag
   ├→ Rollout strategy: RollingUpdate (zero-downtime)
   ├→ Health checks: liveness probe, readiness probe
   └→ Service mesh integration

6. Post-Deployment
   ├→ Run smoke tests
   ├→ Monitor application metrics
   ├→ Verify database connectivity
   └→ Notify deployment team
```

### Container Configuration

**Dockerfile**
```dockerfile
FROM tomcat:9-jdk11
RUN rm -rf /usr/local/tomcat/webapps/*
COPY ./web-app/target/rioo-rs.war /usr/local/tomcat/webapps/
COPY ./web-app/config/rioo-rs.properties /app/ercot/conf/
COPY ./web-app/config/context.xml /usr/local/tomcat/conf/
EXPOSE 8080
CMD ["catalina.sh", "run"]
```

**docker-compose.yaml** (Local Development)
```yaml
version: '3.8'
services:
  tomcat:
    build: .
    ports:
      - "8080:8080"
      - "5005:5005"  # Debug port
    environment:
      - JAVA_OPTS=-Xmx4g -Xms2g -agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=*:5005
    volumes:
      - ./web-app/config/rioo-rs.properties:/app/ercot/conf/rioo-rs.properties
      - ./web-app/config/context.xml:/usr/local/tomcat/conf/Catalina/localhost/rioo-rs.xml
    depends_on:
      - oracle-db
    networks:
      - rarf-network

  oracle-db:
    image: oracle/database:19c
    ports:
      - "1521:1521"
    environment:
      - ORACLE_SID=ORCL
      - ORACLE_PDB=ORCLPDB1
    volumes:
      - oracle-data:/opt/oracle/oradata
    networks:
      - rarf-network

networks:
  rarf-network:
    driver: bridge
```

---

## Key Workflows

### 1. INR Registration Workflow (Initial Asset Entry)

```
User (Market Participant)
  ↓ Create INR
GINR.GINR_REQUEST (status=ACK/SUB)
GINR.SUBSTATION_REFERENCE (tracks INR)
  ↓ (Background job or manual)
RARFSTG.SUBSTATIONS (staged, recordStatus=1)
  ├ RARFSTG.SOLAR_GENERATORS
  ├ RARFSTG.TRANSFORMERS
  ├ RARFSTG.METERS
  └ RARFSTG.POIB_DATA
  ↓ (Validation passes)
Pre-Graduation: Validate all child objects
  ↓ (Graduation triggered)
RARF.SUBSTATIONS (recordStatus=2)
  ├ RARF.SOLAR_GENERATORS (id_rarf populated)
  ├ RARF.TRANSFORMERS
  ├ RARF.METERS
  └ RARF.POIB_DATA
  ↓
Grid Operations Integration (SCADA/EMS)
```

### 2. Multi-Tech Consolidation Workflow

```
Scenario: 5 substations (2422, 2423, 2424, 2426, 2427) need consolidation

Step 1: Data Analysis
├─ Identify target substation (2427 - latest update date)
├─ Analyze child objects across all 5 substations
└─ Detect conflicts/duplicates

Step 2: Update Assets
├─ UPDATE SOLAR_GENERATORS SET SUBSTATION_ID = 2427 WHERE SUBSTATION_ID IN (2422,2423,2424,2426)
├─ UPDATE TRANSFORMERS SET SUBSTATION_ID = 2427 WHERE SUBSTATION_ID IN (...)
├─ UPDATE ENERGY_STORAGE_RESOURCES SET SUBSTATION_ID = 2427 WHERE SUBSTATION_ID IN (...)
└─ [Repeat for 30+ asset tables]

Step 3: Update References
├─ UPDATE INR_REFERENCE SET SUBSTATION_ID = 2427 WHERE SUBSTATION_ID IN (2422,2423,2424,2426)
└─ UPDATE SUBSTATION_REFERENCE SET SUBSTATION_ID = 2427 WHERE SUBSTATION_ID IN (...)

Step 4: Delete Old Records
├─ DELETE FROM SUBSTATIONS WHERE ID IN (2422,2423,2424,2426)
└─ Verify referential integrity

Result: All assets now under single substation 2427 (multi-tech)
```

### 3. Change Request Workflow

```
User creates Change Request
  ↓
CR created with status=DRAFT
CHANGE_REQUESTS table + CHANGE_REQUEST_DATA line items
  ↓
User submits CR
  ↓
CR status → PENDING_REVIEW
Validation checks run (form validation, business rules)
  ↓ (Validation passes)
CR available for ERCOT review
  ↓
ERCOT approves CR
  ↓
CR status → APPROVED
  ↓ (Implementation triggered)
Apply changes to backend data
  ↓
CR status → IMPLEMENTED
  ↓
CR status → COMPLETED
Change logged to audit trail
```

### 4. Graduation Workflow

```
Trigger: Graduation scheduler job (daily 2 AM)
  ↓
Pre-Graduation Validation
├─ Check all child objects exist
├─ Verify ASSET_ID references
├─ Validate constraint compliance
└─ Record failures in GRADUATION_RESULTS

For each validating substation:
  ↓
LSGGraduationService.graduate()
├─ Read RARFSTG records
├─ Create RARF entities (id_rarf populated)
├─ Copy all child objects (SOLAR_GENERATORS, etc.)
├─ Process 40+ asset types
└─ Commit transaction

Update Status
├─ RARFSTG.SUBSTATION_REFERENCE.GRADUATION_STATUS = COMPLETED
├─ RARFSTG.SUBSTATION_REFERENCE.ID_RARF_STATUS = PRC
└─ Log graduation_results

Result: Assets now in RARF production schema
```

---

## Performance Considerations

### Database Optimization

**Connection Pool Tuning:**
```
maxTotal=20              # Maximum concurrent connections
maxIdle=10               # Connections to keep idle
maxWaitMillis=-1         # Wait indefinitely for available connection
initialSize=5            # Initial pool size
testOnBorrow=true        # Validate connection on checkout
testWhileIdle=true       # Background validation
```

**Query Optimization Techniques:**
1. **DISTINCT for ownership deduplication**
   - Remove duplicate rows from ownership JOIN
   - 2 active owners → 1 unique result row

2. **Pagination for large result sets**
   - Fetch 100 records per page
   - Use offset-based pagination or cursor-based

3. **Index on frequently joined columns**
   - SUBSTATION_ID on all asset tables
   - ASSET_ID on OWNERSHIP table
   - ID_GINR_REQUEST on SUBSTATION_REFERENCE

4. **Lazy loading vs. eager loading**
   - Fetch parent first, lazy-load children on demand
   - Avoid N+1 queries with Hibernate batch fetching

### Frontend Performance

**Angular Optimization:**
- Virtual scrolling for 1000+ row tables
- OnPush change detection strategy
- Lazy-loaded modules (Dashboard, AssetMgmt, etc.)
- RxJS unsubscribe in ngOnDestroy

**API Response Optimization:**
- VO selective field loading (don't fetch all child objects)
- Pagination for list endpoints
- HTTP cache headers for static data

**Build Optimization:**
```bash
# Production build with tree-shaking
ng build --configuration production --named-chunks
# Output: 10+ JavaScript chunks (lazy loaded)
# Gzip compression: 5 MB → 1.2 MB
```

---

## Production Runbooks

### Issue: Graduation Failures

**Symptoms:**
- Graduation job completes with 0 successful records
- Errors in graduation_results table

**Diagnosis:**
```sql
SELECT * FROM rarfstg.graduation_results WHERE status = 'Failed' ORDER BY graduation_lastrun_date DESC;
-- Check error_details column for specific failures
```

**Common Causes & Fixes:**

1. **Constraint Violation (ORA-02290)**
   - Cause: NULL required field in child object
   - Fix: Update null fields with valid data
   ```sql
   UPDATE rarfstg.meters SET esiid = 'ESI_ID' WHERE esiid IS NULL;
   ```

2. **Record Already Exists (ORA-00001)**
   - Cause: Duplicate in RARF already graduated
   - Fix: Check id_rarf column, mark as already graduated
   ```sql
   UPDATE rarfstg.substations SET id_rarf = 12345, graduated = 'YES' WHERE id = 122;
   ```

3. **Missing Reference (ORA-02291)**
   - Cause: Parent object not found
   - Fix: Validate parent exists before graduation
   ```sql
   SELECT * FROM rarfstg.substations WHERE id = 122;
   ```

### Issue: Duplicate API Response Rows

**Symptoms:**
- API returns same object twice
- ESR charging details showing duplicate rows

**Diagnosis:**
```sql
SELECT cd.id, COUNT(*) FROM rarf.esr_charging_details cd
JOIN rarf.energy_storage_resources esr ON esr.id = cd.energy_storage_resource_id
JOIN rarf.ownership o ON o.asset_id = esr.asset_id
GROUP BY cd.id HAVING COUNT(*) > 1;
```

**Root Cause:**
- Multiple active ownership records (2 owners with 100% each)
- JOIN multiplying rows

**Fix:**
- Add DISTINCT to JPA query
- Verify single active owner with 100% ownership
- Update stale ownership end_date

```sql
-- Inactivate stale ownership
UPDATE rarf.ownership SET "END" = TRUNC(SYSDATE)-1 WHERE id = 46131;
```

### Issue: High API Latency (>1000ms)

**Symptoms:**
- Slow dashboard load
- Timeout on complex queries

**Diagnosis:**
```sql
-- Check slow queries
SELECT sql_text, executions, buffer_gets FROM v$sql 
WHERE parsing_user_id = (SELECT user_id FROM dba_users WHERE username='RARF') 
  AND elapsed_time/1000000 > 1 -- > 1 second
ORDER BY elapsed_time DESC;

-- Check execution plan
EXPLAIN PLAN FOR SELECT ... FROM rarf.substations s
JOIN rarf.asset_ownership_vw v ON ...;
SELECT * FROM TABLE(dbms_xplan.display);
```

**Optimization Steps:**
1. Add missing indexes on join columns
2. Use DISTINCT to eliminate row multiplication
3. Implement pagination for large result sets
4. Cache frequently accessed lookup tables

---

**End of Technical Reference Guide**

*For questions or clarifications, contact the RARF development team.*

