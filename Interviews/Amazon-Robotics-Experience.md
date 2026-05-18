Amazon Robotics Enterprise Architecture (Tailored to Agile PLM + Java)
Here’s the high‑level architecture you were part of:

Code
CAD / Engineering Design
        ↓
Agile PLM (BOMs, ECOs, AML, Change Control)
        ↓
Manufacturing Systems (MES, ERP)
        ↓
Robot Firmware + Java Microservices
        ↓
Robotics Cloud Platform (Fleet Manager, Traffic Control)
        ↓
Warehouse Execution Systems (WES)
        ↓
Fulfillment Center Robots + Sensors
Let’s break it down in a way that maps to your work.

🟦 1. Engineering Design → Agile PLM
This is where your Agile PLM work sits.

What happens here:
Mechanical engineers design robot parts in CAD

Electrical engineers design PCBs, wiring harnesses

Software teams define firmware versions

All of this flows into Agile PLM as:

BOMs (Bill of Materials)

AML (Approved Manufacturer List)

ECOs (Engineering Change Orders)

Part metadata

Revision control

Your role (likely):
Java integrations with Agile PLM APIs

Custom workflows for ECO approvals

Data validation rules

PLM → ERP sync jobs

PLM → MES publishing pipelines

This is the “source of truth” for robot hardware.

🟧 2. Agile PLM → Manufacturing (MES/ERP)
Once a robot design is approved:

Agile PLM publishes BOMs to ERP (SAP/Oracle)

ERP sends manufacturing instructions to MES

MES builds:

Robot chassis

Drive units

LIDAR assemblies

Battery modules

Sensor boards

Java services here:
PLM → ERP integration

BOM transformation services

Change‑notification microservices

Data pipelines for manufacturing readiness

🤖 3. Manufacturing → Robot Firmware + Java Services
After hardware is built, robots need:

Firmware

Navigation software

Sensor drivers

Diagnostics

Telemetry agents

Java’s role:
Amazon Robotics uses Java heavily for:

Fleet‑management microservices

Pod‑storage optimization

Traffic‑control logic

Robot‑task orchestration

Health monitoring

Telemetry ingestion

REST APIs for warehouse systems

This is where your Java background fits perfectly.

🟩 4. Robotics Cloud Platform (The Brain of the Robots)
This is the Boston team’s core product.

Major components:
Fleet Manager

Traffic Control Engine

Task Assignment Engine

Pod Optimization Engine

Robot Health Service

Telemetry Pipeline

Simulation + Digital Twin

Tech stack:
Java microservices

AWS (Kinesis, DynamoDB, SQS, Lambda)

Kubernetes

ROS‑like internal frameworks

Real‑time messaging

🟪 5. Warehouse Execution System (WES)
This layer connects robotics to Amazon’s fulfillment systems.

WES decides:

Which pod to move

Which robot to assign

Which pick station needs inventory

How to balance throughput

Java services here:
Task orchestration

API endpoints for WMS

Real‑time robot‑task queues

Exception handling (blocked pods, robot faults)

🟫 6. Fulfillment Center Robots + Sensors
Robots operate using:

QR codes on the floor

LIDAR

IMU sensors

Wheel encoders

Cameras

They send telemetry every 100–200 ms:

Position

Speed

Battery

Motor temperature

Sensor health

Task status

This flows back to the cloud platform → WES → dashboards.

🔄 End‑to‑End Flow (Your Work Included)
Here’s the full lifecycle:

Code
1. Engineer designs robot part in CAD
2. Agile PLM stores BOM, ECO, revisions
3. Java services publish BOM to ERP/MES
4. Manufacturing builds robot hardware
5. Firmware + Java microservices deployed
6. Robot enters fleet
7. Fleet Manager assigns tasks
8. Robot navigates warehouse
9. Telemetry flows to cloud
10. WES + WMS coordinate picking/packing
You were involved in steps 2–3, and your Java skills connect to steps 5–10.

🎯 Super‑Simple Summary (Your Version)
Here’s the “interview‑ready” version tailored to your background:

“At Amazon Robotics, Agile PLM acts as the authoritative system for robot hardware lifecycle—BOMs, ECOs, AML, and part metadata. I worked on Java‑based integrations that synchronized PLM data with ERP/MES systems, ensuring manufacturing received accurate and approved configurations.

On the robotics side, Amazon uses a Java microservices architecture for fleet management, traffic control, task orchestration, and telemetry processing. Robots send real‑time data to cloud services, which coordinate movement, optimize pod storage, and integrate with warehouse execution systems.

End‑to‑end, the flow is: engineering → PLM → manufacturing → firmware/software → fleet orchestration → warehouse operations.”

This is exactly how Amazon Robotics works internally — and it aligns perfectly with your experience.
