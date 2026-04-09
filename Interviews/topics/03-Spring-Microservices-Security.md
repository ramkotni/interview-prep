# Spring Boot, Microservices, Security

## Must-practice questions
1. Why Spring Boot for microservices?
2. Constructor injection vs field injection
3. API validation and global exception handling
4. JWT/OAuth2 flow and RBAC
5. Idempotency and retries
6. Circuit breaker, bulkhead, timeouts
7. API versioning strategy
8. N+1 query problem handling
9. Saga pattern and compensation
10. Contract testing strategy

## Senior architecture answer pattern
- Service boundaries by business domain
- Sync for immediate reads; async for decoupling
- Secure by design with least privilege
- Operability via health checks and metrics

## Must-not-miss points
- Mention failure path, not only happy path
- Mention backward compatibility policy
- Mention data migration/versioning controls

## Reference
- Detailed Q&A: `Interviews/Senior-FullStack-Daily-Interview-QA.md` (Q46-Q75)
- Coding samples: `Interviews/topics/07-API-Design-Coding-Samples.md`
