# Java Core and Concurrency (Senior)

## Must-practice questions
1. `HashMap` vs `ConcurrentHashMap`
2. `volatile` vs `synchronized`
3. Deadlock prevention
4. `ExecutorService` and thread pools
5. `CompletableFuture` usage
6. Java Memory Model practical impact
7. Checked vs unchecked exceptions
8. `equals` and `hashCode` contract
9. Streams and parallel streams trade-offs
10. Memory leak diagnosis approach

## Quick answer cues
- Thread safety: visibility + atomicity + contention
- Performance: benchmark, do not assume
- Reliability: defensive coding and clear exception model

## Coding whiteboard prompts
- Thread-safe counter service
- Async fan-out call using `CompletableFuture`
- Retry wrapper with backoff

## Must-not-miss points
- Distinguish CPU-bound vs I/O-bound concurrency
- Mention observability for thread issues
- Mention fail-safe defaults and timeout use

## Reference
- Detailed Q&A: `Interviews/Senior-FullStack-Daily-Interview-QA.md` (Q21-Q45)
