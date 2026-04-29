# STAR Incident Table

| Incident | Situation | Task | Action | Result |
|---|---|---|---|---|
| Latency spike | API latency jumped | Restore SLA | Fallback, query tuning, reduce sync chain | Latency normalized |
| Kafka lag | Consumer lag increased | Catch up safely | Partition analysis, key fix, scale consumers, DLQ | Lag reduced to minutes |
| OOM restarts | Service crash loop | Stabilize service | Heap/GC analysis, bounded cache, lifecycle fix | Restart loop stopped |
| Bad deployment | Critical regression | Recover quickly | Rollback, patch, contract tests | Impact minimized |
