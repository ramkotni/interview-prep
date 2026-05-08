# OBSERVABILITY & MONITORING - COMPREHENSIVE INTERVIEW Q&A

## CloudWatch, Prometheus, ELK Stack, Splunk

---

## Q1: Observability Three Pillars

**A:** Complete visibility into system behavior and performance.

### Three Pillars:
```
1. LOGS - Detailed record of events, errors, warnings
2. METRICS - Numerical time-series data (CPU, memory, latency)
3. TRACES - Request flow through distributed systems
```

---

## Q2: CloudWatch (AWS Native)

**A:** AWS monitoring and logging service.

### CloudWatch Logs:
```java
@Configuration
public class CloudWatchLoggingConfig {
    
    @Bean
    public IEventPublisher cloudWatchPublisher(
        AWSLogs awsLogs) {
        return new CloudWatchLogsAppender(awsLogs);
    }
}

// Application logging
@Slf4j
@Service
public class OrderService {
    
    @Autowired
    private CloudWatchClient cloudwatch;
    
    public void processOrder(Order order) {
        log.info("Processing order: {}", order.getId());
        
        try {
            // Process order
            log.debug("Order items: {}", order.getItems());
            
        } catch (Exception e) {
            log.error("Failed to process order: {}", order.getId(), e);
            // Publish metric for error
            putMetric("OrderProcessingErrors", 1);
        }
    }
    
    private void putMetric(String metricName, double value) {
        MetricDatum datum = MetricDatum.builder()
            .metricName(metricName)
            .value(value)
            .timestamp(Instant.now())
            .unit(StandardUnit.COUNT)
            .build();
        
        PutMetricDataRequest request = PutMetricDataRequest.builder()
            .namespace("MyApp/Orders")
            .metricData(datum)
            .build();
        
        cloudwatch.putMetricData(request);
    }
}
```

### CloudWatch Alarms:
```bash
# Alarm for high API latency
aws cloudwatch put-metric-alarm \
  --alarm-name HighAPILatency \
  --alarm-description "Alert when API p99 latency > 1000ms" \
  --metric-name APILatencyP99 \
  --namespace MyApp \
  --statistic Average \
  --period 300 \
  --threshold 1000 \
  --comparison-operator GreaterThanThreshold \
  --evaluation-periods 2 \
  --alarm-actions arn:aws:sns:region:account:topic

# Alarm for error rate
aws cloudwatch put-metric-alarm \
  --alarm-name HighErrorRate \
  --metric-name Errors \
  --statistic Sum \
  --period 60 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold \
  --alarm-actions arn:aws:sns:region:account:topic
```

### CloudWatch Dashboards:
```bash
# Create JSON dashboard
{
  "widgets": [
    {
      "type": "metric",
      "properties": {
        "metrics": [
          ["AWS/EC2", "CPUUtilization", {"stat": "Average"}],
          ["MyApp", "RequestCount", {"stat": "Sum"}],
          ["MyApp", "APILatencyP99", {"stat": "p99"}]
        ],
        "period": 300,
        "stat": "Average",
        "region": "us-east-1",
        "title": "Application Metrics"
      }
    }
  ]
}
```

---

## Q3: Prometheus (Time-Series Database)

**A:** Open-source monitoring and time-series database.

### Prometheus Metrics in Spring Boot:
```java
@Configuration
public class MetricsConfig {
    
    @Bean
    public MeterRegistry meterRegistry() {
        return new PrometheusMeterRegistry(PrometheusConfig.DEFAULT);
    }
}

@RestController
@RequestMapping("/api/orders")
public class OrderController {
    
    @Autowired
    private MeterRegistry meterRegistry;
    
    @PostMapping
    public ResponseEntity<OrderDTO> createOrder(@RequestBody CreateOrderRequest req) {
        Timer.Sample sample = Timer.start(meterRegistry);
        
        try {
            // Process order
            Order order = orderService.createOrder(req);
            
            // Record custom metrics
            meterRegistry.counter("order.created", "type", req.getType()).increment();
            meterRegistry.gauge("order.total_amount", new AtomicInteger((int)req.getAmount()));
            
            sample.stop(Timer.builder("order.creation.time")
                .description("Time to create order")
                .publishPercentiles(0.5, 0.99)
                .register(meterRegistry));
            
            return ResponseEntity.ok(convert(order));
            
        } catch (Exception e) {
            meterRegistry.counter("order.creation.errors").increment();
            throw e;
        }
    }
}

// application properties
management.endpoints.web.exposure.include=prometheus
management.endpoint.metrics.enabled=true
management.metrics.export.prometheus.enabled=true
```

### Prometheus Configuration:
```yaml
# prometheus.yml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'spring-boot-app'
    metrics_path: '/actuator/prometheus'
    static_configs:
      - targets: ['localhost:8080']

  - job_name: 'kubernetes-pods'
    kubernetes_sd_configs:
      - role: pod
    relabel_configs:
      - source_labels: [__meta_kubernetes_pod_annotation_prometheus_io_scrape]
        action: keep
        regex: 'true'
```

### Prometheus Queries (PromQL):
```promql
# Current request rate
rate(http_requests_total[5m])

# Percentage of errors
(rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m])) * 100

# P99 latency
histogram_quantile(0.99, http_request_duration_seconds_bucket)

# Memory usage
container_memory_usage_bytes / 1024 / 1024

# Pod restart count
kube_pod_container_status_restarts_total
```

---

## Q4: ELK Stack (Elasticsearch, Logstash, Kibana)

**A:** Log aggregation and visualization.

### Logstash Pipeline Configuration:
```
# logstash.conf

input {
  tcp {
    port => 5000
    codec => json
  }
  file {
    path => "/var/log/myapp/*.log"
    start_position => "beginning"
  }
}

filter {
  # Parse logs
  if [type] == "app" {
    grok {
      match => {
        "message" => "%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{DATA:logger} - %{GREEDYDATA:msg}"
      }
    }
    
    # Parse JSON logs
    json {
      source => "message"
      target => "parsed"
    }
    
    # Add metadata
    mutate {
      add_field => { "environment" => "production" }
      add_field => { "service" => "order-service" }
    }
    
    # Filter sensitive data
    mutate {
      gsub => ["parsed_password", ".", "*"]
      gsub => ["parsed_token", ".", "*"]
    }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "myapp-%{+YYYY.MM.dd}"
    codec => json
  }
}
```

### Java Application Logging to Logstash:
```xml
<!-- logback-spring.xml -->
<configuration>
    <appender name="LOGSTASH" class="net.logstash.logback.appender.LogstashTcpSocketAppender">
        <destination>localhost:5000</destination>
        <encoder class="net.logstash.logback.encoder.LogstashEncoder">
            <customFields>
                {"service":"order-service","environment":"prod"}
            </customFields>
        </encoder>
    </appender>
    
    <root level="INFO">
        <appender-ref ref="LOGSTASH" />
    </root>
</configuration>
```

### Kibana Queries (KQL):
```
# Find errors in order service
level: ERROR AND service: "order-service"

# Errors in last hour
level: ERROR AND @timestamp >= now - 1h

# Status distribution
status: * | stats count() by status

# Response time percentiles
response_time: * | stats percentiles(response_time, 50, 95, 99)

# Top errors
level: ERROR | top 10 error_message
```

### Kibana Dashboard Example:
```json
{
  "title": "Order Service Monitoring",
  "panels": [
    {
      "type": "metric",
      "title": "Error Rate",
      "query": "level: ERROR | stats count() as errors | stats avg(errors)"
    },
    {
      "type": "line",
      "title": "Request Rate Over Time",
      "query": "request_id: * | timechart count() by service"
    },
    {
      "type": "table",
      "title": "Recent Errors",
      "query": "level: ERROR | sort @timestamp desc | limit 100"
    }
  ]
}
```

---

## Q5: Splunk (Enterprise Monitoring)

**A:** Enterprise-grade log management and analytics.

### Splunk Search Queries:
```spl
# Basic search
sourcetype=spring-log ERROR | table timestamp, message, trace_id

# Real-time monitoring
index=myapp sourcetype=app ERROR | head 100

# Error rates by service
index=myapp level=ERROR | stats count as error_count by service

# Performance metrics
index=myapp response_time=* | stats avg(response_time), max(response_time), p95(response_time) by endpoint

# Failed transactions
index=myapp transaction_status="FAILED" | stats count by reason

# Business metrics
index=myapp event_type="ORDER_CREATED" | stats count(order_value) as revenue sum(order_value)

# Drill-down analysis
index=myapp user_id="123" | transaction request_id | table timestamp, endpoint, response_time, status
```

### Splunk Alerts:
```
Search: index=myapp level=ERROR | stats count as error_count

Alert Trigger:
- When error_count > 10 in last 5 minutes

Actions:
- Send email to team@example.com
- Create incident in JIRA
- Trigger PagerDuty
```

---

## Q6: Distributed Tracing with Jaeger

**A:** Trace requests across microservices.

### Spring Cloud Sleuth + Jaeger:
```xml
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-sleuth</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-sleuth-otel-autoconfigure</artifactId>
</dependency>
<dependency>
    <groupId>io.opentelemetry.exporter</groupId>
    <artifactId>opentelemetry-exporter-jaeger</artifactId>
</dependency>
```

### Jaeger Configuration:
```properties
# application.properties
spring.cloud.sleuth.enabled=true
otel.exporter.jaeger.endpoint=http://localhost:16686

# Trace ID will automatically appear in logs
logging.pattern.level=[%X{traceId}] %5p
```

### Making Traces:
```java
@Service
public class OrderTraceService {
    
    @Autowired
    private Tracer tracer;
    
    public Order processOrder(CreateOrderRequest req) {
        // Create span
        try (var scope = tracer.buildSpan("processOrder")
            .withTag("order.type", req.getType())
            .withTag("order.amount", req.getAmount())
            .startActive(true)) {
            
            Span span = scope.span();
            
            // Nested span for inventory check
            try (var invScope = tracer.buildSpan("checkInventory")
                .asChildOf(span)
                .startActive(true)) {
                
                inventoryService.checkStock(req.getItems());
            }
            
            // Nested span for payment
            try (var payScope = tracer.buildSpan("processPayment")
                .asChildOf(span)
                .startActive(true)) {
                
                paymentService.processPayment(req.getAmount());
            }
        }
    }
}
```

---

## Q7: Monitoring Best Practices

✅ **Key Metrics (Use 4 Golden Signals):**
1. **Latency:** How long requests take
2. **Traffic:** Request rate and throughput
3. **Errors:** Error rate and types
4. **Saturation:** Resource utilization (CPU, memory, disk)

✅ **Alerting Strategy:**
- Alert on symptoms, not causes
- Avoid alert fatigue
- Set appropriate thresholds
- Test alert procedures

✅ **Log Management:**
- Structured logging (JSON)
- Include correlation IDs
- Don't log sensitive data
- Appropriate log levels

✅ **Dashboard Design:**
- Show business metrics
- Show system health
- Fast to scan
- Actionable insights

---

**Last Updated:** May 8, 2026


