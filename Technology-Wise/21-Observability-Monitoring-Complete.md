# OBSERVABILITY, MONITORING & INCIDENT RESPONSE — COMPLETE Q&A
## CloudWatch, Prometheus, Grafana, Dynatrace | Sr Cloud Platform Engineer
---
## SECTION 1: OBSERVABILITY FUNDAMENTALS
### Q1: Explain the 3 pillars of observability.
**A:**
| Pillar | What | Tools | Use |
|---|---|---|---|
| **Metrics** | Numeric measurements over time | Prometheus, CloudWatch | Dashboards, alerting, SLOs |
| **Logs** | Timestamped text records of events | CloudWatch Logs, ELK Stack, Splunk | Debugging, audit trails |
| **Traces** | Request flow across services | AWS X-Ray, Jaeger, Zipkin | Latency root cause, service map |
**Why all three matter:**
- Metrics tell you WHAT is wrong (error rate 5%)
- Logs tell you WHY (NullPointerException in OrderService)
- Traces tell you WHERE (bottleneck in PaymentService.validate() taking 3sec)
---
### Q2: How do you set up Prometheus and Grafana on Kubernetes?
**A:**
```bash
# Install kube-prometheus-stack (includes Prometheus, Grafana, AlertManager, node-exporter)
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring \
  --create-namespace \
  --set prometheus.prometheusSpec.retention=15d \
  --set prometheus.prometheusSpec.storageSpec.volumeClaimTemplate.spec.resources.requests.storage=50Gi \
  --set grafana.adminPassword=$GRAFANA_ADMIN_PASSWORD \
  --set alertmanager.config.global.slack_api_url=$SLACK_WEBHOOK_URL
```
**Custom application metrics (Java/Spring Boot):**
```java
@Configuration
public class MetricsConfig {
    @Bean
    MeterRegistryCustomizer<MeterRegistry> metricsCommonTags() {
        return registry -> registry.config()
            .commonTags("application", "warehouse-api",
                       "environment", "production",
                       "region", "us-east-1");
    }
}
@RestController
public class OrderController {
    private final Counter orderCounter;
    private final Timer orderProcessingTimer;
    private final Gauge activeOrdersGauge;
    public OrderController(MeterRegistry registry) {
        this.orderCounter = Counter.builder("orders.total")
            .tag("status", "created")
            .description("Total orders created")
            .register(registry);
        this.orderProcessingTimer = Timer.builder("order.processing.duration")
            .description("Order processing time")
            .percentiles(0.5, 0.95, 0.99)
            .register(registry);
        this.activeOrdersGauge = Gauge.builder("orders.active", orderRepository, 
            r -> r.countByStatus("PROCESSING"))
            .description("Currently processing orders")
            .register(registry);
    }
    @PostMapping("/orders")
    public Order createOrder(@RequestBody OrderRequest request) {
        return orderProcessingTimer.record(() -> {
            Order order = orderService.process(request);
            orderCounter.increment();
            return order;
        });
    }
}
```
**Prometheus scrape annotations in K8s deployment:**
```yaml
spec:
  template:
    metadata:
      annotations:
        prometheus.io/scrape: "true"
        prometheus.io/path: "/actuator/prometheus"
        prometheus.io/port: "8080"
```
---
### Q3: Show key Prometheus queries you use for monitoring.
**A:**
```promql
# --- API Performance ---
# Request rate (requests per second)
sum(rate(http_server_requests_seconds_count{namespace="logistics"}[5m])) by (uri, method)
# P99 latency
histogram_quantile(0.99,
  sum(rate(http_server_requests_seconds_bucket{namespace="logistics"}[5m])) by (le, uri)
)
# Error rate (5xx / total)
sum(rate(http_server_requests_seconds_count{status=~"5.."}[5m]))
  / sum(rate(http_server_requests_seconds_count[5m])) * 100
# --- JVM / Application ---
# JVM heap usage %
jvm_memory_used_bytes{area="heap"} / jvm_memory_max_bytes{area="heap"} * 100
# GC pause time
rate(jvm_gc_pause_seconds_sum[5m])
# Thread count
jvm_threads_live_threads
# --- Kubernetes Workloads ---
# Pod CPU usage vs limit
sum(rate(container_cpu_usage_seconds_total{namespace="logistics"}[5m])) by (pod)
  / sum(kube_pod_container_resource_limits{resource="cpu", namespace="logistics"}) by (pod) * 100
# Pod memory usage
sum(container_memory_working_set_bytes{namespace="logistics"}) by (pod)
# Pod restart count (alert trigger)
increase(kube_pod_container_status_restarts_total{namespace="logistics"}[1h]) > 3
# Deployment availability
kube_deployment_status_replicas_available{namespace="logistics"}
  / kube_deployment_spec_replicas{namespace="logistics"} < 0.75
# --- Kafka ---
# Consumer lag
kafka_consumer_group_lag{namespace="kafka-system"} > 10000
# Broker disk usage
kafka_log_log_size / kafka_log_log_size_max * 100 > 70
```
---
### Q4: How do you configure CloudWatch alarms and metrics?
**A:**
```hcl
# API error rate alarm
resource "aws_cloudwatch_metric_alarm" "api_errors" {
  alarm_name          = "api-5xx-rate-high"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 3
  metric_name         = "5xxErrorRate"
  namespace           = "ERCOT/API"
  period              = 60
  statistic           = "Average"
  threshold           = 1.0     # 1% error rate
  alarm_description   = "API 5xx error rate above 1% for 3 minutes"
  treat_missing_data  = "notBreaching"
  alarm_actions       = [aws_sns_topic.pagerduty.arn]
  ok_actions          = [aws_sns_topic.slack_ok.arn]
}
# Composite alarm (reduce noise — both metrics must be bad)
resource "aws_cloudwatch_composite_alarm" "service_degraded" {
  alarm_name = "service-degraded"
  alarm_rule = "ALARM(${aws_cloudwatch_metric_alarm.api_errors.alarm_name}) AND ALARM(${aws_cloudwatch_metric_alarm.api_latency.alarm_name})"
}
# Custom metric from application logs
resource "aws_cloudwatch_log_metric_filter" "payment_errors" {
  name           = "payment-errors"
  pattern        = "[timestamp, requestId, level=ERROR, message=\"Payment*\"]"
  log_group_name = "/ercot/rioo-is/application"
  metric_transformation {
    name      = "PaymentErrors"
    namespace = "ERCOT/Business"
    value     = "1"
    unit      = "Count"
  }
}
```
**CloudWatch Logs Insights queries I use daily:**
```sql
-- Find slow API requests
fields @timestamp, responseTime, endpoint, statusCode
| filter responseTime > 1000
| stats percentile(responseTime, 99) as p99, count(*) as count by endpoint
| sort p99 desc | limit 20
-- Error frequency by service
fields @timestamp, level, service, message
| filter level = "ERROR"
| stats count(*) as errors by service, bin(5m)
| sort errors desc
-- Lambda cold start analysis
fields @timestamp, @message
| filter @message like /Init Duration/
| stats avg(@initDuration), max(@initDuration) by functionName
```
---
### Q5: How does Dynatrace APM work? How did you use it?
**A:**
**Dynatrace at ERCOT/Amazon Robotics:**
- Full-stack APM: JVM metrics, database calls, external service calls
- OneAgent auto-instrumentation (no code changes needed)
- AI-powered root cause detection (Davis AI)
- Service-level baselining — automatically detects anomalies vs normal
**Dynatrace vs Prometheus/Grafana:**
| Feature | Dynatrace | Prometheus + Grafana |
|---|---|---|
| **Setup** | OneAgent auto-instructs | Requires code instrumentation |
| **Cost** | $$ (commercial) | Open source |
| **AI features** | Davis AI auto-RCA | Manual analysis |
| **Code tracing** | Full method-level traces | Depends on custom spans |
| **Infrastructure** | Auto-discovery | Requires manual scrape config |
**How I used Dynatrace:**
- Configured custom SLOs in Dynatrace (availability + response time)
- Set up anomaly detection: alert when metric deviates from baseline (vs fixed threshold)
- Used service flow map to trace cascade failures in warehouse pipeline
- Created management zones per team for RBAC on dashboards
---
### Q6: How do you implement distributed tracing?
**A:**
**AWS X-Ray with Spring Boot (ERCOT setup):**
```xml
<!-- pom.xml -->
<dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-spring</artifactId>
</dependency>
<dependency>
    <groupId>com.amazonaws</groupId>
    <artifactId>aws-xray-recorder-sdk-aws-sdk-v2</artifactId>
</dependency>
```
```java
@Configuration
public class XRayConfig {
    @Bean
    public Filter TracingFilter() {
        return new AWSXRayServletFilter("warehouse-api");
    }
}
@Service
public class OrderService {
    public Order processOrder(OrderRequest request) {
        // Create subsegment for database call
        return AWSXRay.createSubsegment("OrderRepository.save", subsegment -> {
            subsegment.putMetadata("orderId", request.getOrderId());
            subsegment.putAnnotation("customerId", request.getCustomerId());
            return orderRepository.save(request);
        });
    }
}
```
**OpenTelemetry (vendor-agnostic, used at Amazon Robotics):**
```yaml
# OpenTelemetry Collector deployment
apiVersion: opentelemetry.io/v1alpha1
kind: OpenTelemetryCollector
metadata:
  name: otel-collector
spec:
  config: |
    receivers:
      otlp:
        protocols:
          grpc:
            endpoint: 0.0.0.0:4317
          http:
            endpoint: 0.0.0.0:4318
    processors:
      batch:
        timeout: 1s
        send_batch_size: 1000
    exporters:
      awsxray:
        region: us-east-1
      jaeger:
        endpoint: jaeger-collector:14250
    service:
      pipelines:
        traces:
          receivers: [otlp]
          processors: [batch]
          exporters: [awsxray, jaeger]
```
---
## SECTION 2: INCIDENT RESPONSE
### Q7: Explain your incident response process with a real example.
**A:**
**P1 Incident — Amazon Robotics (MTTR: 28 minutes):**
```
10:02 AM: CloudWatch alarm fires — warehouse-api error rate 15% (SLO threshold: 0.05%)
          PagerDuty pages on-call engineer
10:04 AM: Engineer acknowledges alert
          Creates #incident-20240315 Slack channel
          Posts initial assessment: "Investigating warehouse-api 5xx spike"
10:05 AM: Checks Grafana dashboard
          Error rate 15%, P99 latency 8sec (normal: 200ms)
          Correlation: started 10:02 AM, 45 minutes after deployment
10:08 AM: kubectl rollout history deployment/warehouse-api -n production
          Shows deployment v2.1.3 at 09:17 AM
          kubectl logs warehouse-api-xxx --previous -n production
          Errors: "HikariPool-Connection timeout waiting for connection from pool"
10:10 AM: Root cause identified:
          New feature in v2.1.3 adds N+1 query pattern
          Each API call making 50+ DB queries vs 5 before
          DB connection pool (20 connections) exhausted
10:15 AM: Mitigation: kubectl rollout undo deployment/warehouse-api -n production
          Error rate starts dropping within 30 seconds
          10:17 AM: Error rate back to <0.05%
10:30 AM: All-clear posted to stakeholders
          P1 resolved — MTTR: 28 minutes
24 hours later: RCA Document
  Root cause: N+1 query in OrderService.getOrderWithDetails()
  Why not caught:
    - Integration tests use in-memory DB (doesn't reveal N+1)
    - Performance test not run before production deploy
  Action items:
    1. Add DB query count metric to Grafana dashboard (Owner: Ram, Due: 1 week)
    2. Add connection pool utilization alarm (Owner: Ram, Due: 3 days)
    3. Run load test for all PRs touching DB layer (Owner: Dev lead, Due: 2 weeks)
    4. Enable Hibernate SQL logging in staging (Owner: Ram, Due: 3 days)
```
---
### Q8: How do you create effective Grafana dashboards?
**A:**
**Dashboard I built at ERCOT (Warehouse API):**
```
Row 1: SERVICE HEALTH (RED METHOD)
  Panel 1: Request Rate    (rate(http_requests_total[5m]))
  Panel 2: Error Rate %    (5xx / total * 100)
  Panel 3: P99 Latency     (histogram_quantile(0.99, ...))
  Panel 4: Active Pods     (kube_deployment_status_replicas_available)
Row 2: JVM HEALTH
  Panel 5: Heap Usage %    (jvm_memory_used / jvm_memory_max * 100)
  Panel 6: GC Pause Time   (rate(jvm_gc_pause_seconds_sum[5m]))
  Panel 7: Thread Count    (jvm_threads_live_threads)
  Panel 8: DB Pool Usage   (hikaricp_connections_active / hikaricp_connections_max)
Row 3: KAFKA
  Panel 9: Consumer Lag     (kafka_consumer_group_lag per topic)
  Panel 10: Produce Rate    (kafka_producer_record_send_rate)
  Panel 11: Broker Disk     (kafka_log_log_size / total * 100)
Row 4: INFRASTRUCTURE
  Panel 12: CPU Utilization (container_cpu_usage / limits * 100)
  Panel 13: Memory Usage    (container_memory_working_set / limits * 100)
  Panel 14: Pod Restarts    (increase(kube_pod_container_status_restarts_total[1h]))
Row 5: BUSINESS METRICS
  Panel 15: Orders Created/min
  Panel 16: Orders Failed/min
  Panel 17: Order Processing Time (custom metric)
```
**Grafana alerting:**
```yaml
# alert rules in Grafana (provisioned via ConfigMap)
groups:
  - name: warehouse-api
    rules:
    - alert: HighErrorRate
      expr: |
        sum(rate(http_server_requests_seconds_count{status=~"5..",job="warehouse-api"}[5m]))
          / sum(rate(http_server_requests_seconds_count{job="warehouse-api"}[5m])) > 0.01
      for: 3m
      labels:
        severity: critical
        team: warehouse
      annotations:
        summary: "warehouse-api error rate above 1%"
        runbook: "https://wiki.ercot.internal/runbooks/warehouse-api-errors"
    - alert: PodCrashLooping
      expr: increase(kube_pod_container_status_restarts_total{namespace="logistics"}[15m]) > 3
      for: 1m
      labels:
        severity: warning
      annotations:
        summary: "Pod {{ $labels.pod }} is crash looping"
```
---
### Q9: How do you implement ELK Stack for log management?
**A:**
**ELK at Biogen (supply chain system):**
```yaml
# Filebeat DaemonSet — collect container logs from all nodes
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: filebeat
  namespace: logging
spec:
  selector:
    matchLabels:
      app: filebeat
  template:
    spec:
      containers:
      - name: filebeat
        image: elastic/filebeat:8.10.0
        args: ["-c", "/etc/filebeat/filebeat.yml", "-e"]
        env:
        - name: ELASTICSEARCH_HOST
          value: "elasticsearch-master.logging.svc:9200"
        volumeMounts:
        - name: filebeat-config
          mountPath: /etc/filebeat
        - name: varlog
          mountPath: /var/log
        - name: varlibdockercontainers
          mountPath: /var/lib/docker/containers
          readOnly: true
      volumes:
      - name: varlog
        hostPath:
          path: /var/log
      - name: varlibdockercontainers
        hostPath:
          path: /var/lib/docker/containers
```
**Filebeat configuration:**
```yaml
# filebeat.yml
filebeat.inputs:
- type: container
  paths:
    - /var/lib/docker/containers/*/*.log
  processors:
  - add_kubernetes_metadata:
      host: ${NODE_NAME}
      matchers:
      - logs_path:
          logs_path: "/var/log/containers/"
processors:
- drop_fields:
    fields: ["agent", "ecs", "host"]  # Remove noisy fields
output.elasticsearch:
  hosts: ["${ELASTICSEARCH_HOST}"]
  index: "k8s-logs-%{+yyyy.MM.dd}"
  pipeline: "k8s-log-enrichment"
# JSON log parsing for structured logs
- decode_json_fields:
    fields: ["message"]
    target: ""
    overwrite_keys: true
```
**Kibana saved queries I use:**
```
# Find all errors in last 1 hour
kubernetes.namespace: "logistics" AND level: "ERROR"
# Slow HTTP requests
kubernetes.labels.app: "warehouse-api" AND responseTime > 1000
# Specific user activity for audit
userId: "USR-12345" AND action: "ORDER_*"
# Correlation by requestId (trace across services)
requestId: "req-abc-123"
```
---
*File: 21-Observability-Monitoring-Complete.md | Created: June 2026 | Role: Sr Cloud Platform Engineer*
