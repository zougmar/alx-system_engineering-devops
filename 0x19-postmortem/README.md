Postmortem Report: July 10th, 2024 Authentication Service Outage
Issue Summary
Duration: July 10th, 2024, 14:00 - 16:45 GMT+1 (2 hours 45 minutes)
Impact: The user authentication service was non-operational, affecting approximately 75% of users trying to log in or register. Existing logged-in sessions were unaffected, but new sessions and any logout attempts failed. Users received "Service Unavailable" errors, leading to a significant drop in user activity and an increase in customer support tickets.
Root Cause: A misconfigured load balancer update caused all traffic to be routed to a single instance of the authentication service, leading to service overload and eventual failure.

Timeline
14:00 GMT+1: Monitoring alert triggered indicating high error rates and increased latency on the authentication API.
14:05 GMT+1: On-call engineer investigates and identifies multiple "Service Unavailable" errors related to the login service.
14:20 GMT+1: Initial assumption was a database connectivity issue, leading to a review of database performance metrics (misleading path).
14:35 GMT+1: Incident escalated to the DevOps team after database checks showed no anomalies.
14:50 GMT+1: Analysis of traffic patterns reveals that all login requests are directed to a single server instance instead of being distributed across multiple instances.
15:10 GMT+1: The root cause is identified: a recent load balancer update introduced an incorrect configuration that ignored round-robin traffic distribution.
15:30 GMT+1: DevOps rolls back the load balancer configuration to the previous version, and the affected instance is restarted.
16:00 GMT+1: Service performance stabilizes, and error rates return to normal.
16:45 GMT+1: Full functionality confirmed; incident closed after monitoring for any residual issues.

Root Cause and Resolution
The issue was caused by a misconfigured update to the load balancer’s configuration, which erroneously directed all traffic to a single instance of the authentication service. This overwhelmed the instance, causing it to hit resource limits and fail under the load. The configuration mistake was due to a syntax error in the load balancer rules that bypassed the round-robin distribution logic, leading to unequal load distribution.
The resolution involved rolling back the load balancer configuration to the previous, known-good state and restarting the affected instance to clear any accumulated overload. Once traffic distribution was restored, the system began functioning normally.


