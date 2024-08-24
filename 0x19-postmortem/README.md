0. My first postmortem
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

1. Make people want to read your postmortem
Postmortem Report: The Day Our Login Service Decided to Play Hide-and-Seek
Issue Summary
Duration: July 10th, 2024, 14:00 - 16:45 GMT+1 (2 hours 45 minutes)
Impact: Picture this: 75% of our users trying to log in, only to be greeted with “Service Unavailable” instead of their dashboard. Not fun. For nearly three hours, logging in was more like finding the last piece of a jigsaw puzzle—it rarely worked. Users who were already logged in got lucky, but new logins? Nope. And our support inbox? Flooded.
Root Cause: A load balancer misconfiguration made our login requests pack their bags and all head to the same server, which couldn’t handle the crowd and crashed spectacularly.

Timeline (A Dramatic Retelling)
14:00 GMT+1: Our monitoring system starts waving red flags. Error rates spike, and the login service feels like it’s moving through molasses.
14:05 GMT+1: Our on-call engineer steps in, coffee in hand, to investigate. “Service Unavailable” errors flood the logs.
14:20 GMT+1: The first assumption? Maybe the database is being grumpy again. (Spoiler: It wasn’t.)
14:35 GMT+1: DevOps gets involved after we realize the database is innocent. The real culprit is hiding somewhere else.
14:50 GMT+1: Traffic analysis reveals the horror: All login requests are huddled around a single server like it’s Black Friday.
15:10 GMT+1: We find out the new load balancer config had one job and failed—no proper traffic distribution.
15:30 GMT+1: A rollback brings things back to normal. The overworked server breathes a sigh of relief.
16:00 GMT+1: Error rates drop, and login speeds are back to being smooth as butter.
16:45 GMT+1: We declare victory and give the system a clean bill of health. (And maybe take a nap.)

Root Cause and Resolution
This all started because someone decided to “improve” our load balancer setup, but instead of balancing traffic, the new configuration created a one-way street, sending all requests to a single server. It didn’t take long for that server to throw in the towel and stop responding altogether. The misconfiguration was due to a small syntax error that bypassed round-robin load distribution—imagine turning off all the lights in a nightclub except for one spotlight, and now everyone’s on that tiny dance floor.
The fix was straightforward: roll back to the previous configuration and give the overloaded server a break by restarting it. Once we got the traffic flowing correctly, it was smooth sailing.


