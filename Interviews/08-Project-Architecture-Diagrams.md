# Project Architecture Diagrams

## ERCOT
User -> Angular -> Gateway/Auth -> Workflow Service -> Oracle
Workflow Service -> Audit Service -> Audit Store

## Amazon Robotics
Producers -> Kafka -> Processing Services -> Cache/DB -> Downstream
Retry + DLQ for failure isolation

## Biogen
UI/API -> Validation -> DB -> Audit -> Reporting

## Dell
PLM -> Integration Layer -> ERP/MES
Reconciliation + Replay for consistency
