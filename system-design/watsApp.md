8 Reasons Why WhatsApp Was Able to Support 50 Billion Messages a Day With Only 32 Engineers
#1: Learn More - Awesome WhatsApp Engineering (6 minutes)
Neo Kim
Aug 27, 2023

Get the powerful template to approach system design for FREE on newsletter sign-up:

This post outlines the incredible story of WhatsApp co-founder Jan Koum. And the engineering techniques used to scale WhatsApp. If you want to learn more, scroll to the bottom and find the references.

Share this post & I'll send you some rewards for the referrals.

January 2008 - California, United States.

Jan Koum, an engineer at Yahoo, applies for work at Facebook - rejected.

It was not the end - he moved on with his life.

He buys an iPhone next year and immediately recognizes the huge potential of the new App Store.

So he decided to build an instant messenger with some of his former coworkers from Yahoo. And named it WhatsApp. The vision behind WhatsApp was to replace the expensive SMS.

With 1 million people signing up each day, the growth rate of WhatsApp was mind-boggling.

WhatsApp was able to support 50 billion messages a day from 450 million daily active users. And they did it with only 32 engineers.

Although explosive product growth is a good problem to have, Jan Koum and the WhatsApp team had to adopt the best engineering practices to overcome the challenges.

WhatsApp Engineering
WhatsApp engineering practices to meet extreme scalability were:

1. Single Responsibility Principle
They put product focus only on the core feature - messaging.

And didn’t bother to build an advertising network or a social media platform.

WhatsApp Engineering; Single responsibility principle
Single Responsibility Principle
Also they eliminated feature creep at all costs.

Feature creep occurs when you add excessive features to a product. And make it difficult to use.

Besides they focused on the reliability of WhatsApp over everything else.

2. Technology Stack
They used Erlang to build the core functionalities of WhatsApp servers. Because it:

Provides high scalability with a tiny footprint

And supports hot-loading

Threads are a native feature of Erlang. But in Java or C++ threads belong to the operating system. So there is no need to save the entire CPU state in Erlang. And this makes context switching cheaper.

Hot loading makes it easier to deploy code changes without a server restart. Or traffic redirection. In simple words, Hot loading offers high availability.

3. Why Reinvent the Wheel?
Don’t reinvent the wheel - either use open source or buy a commercial solution.

WhatsApp Engineering; Do not reinvent the wheel
Don’t Reinvent the Wheel
Ejabberd is an open-source real-time messaging server written in Erlang.

And they built WhatsApp on top of ejabberd. Also they rewrote some of the ejabberd core components to meet their needs.

Besides WhatsApp leveraged third-party services such as Google Push to provide push notifications.

4. Cross-Cutting Concerns
They put huge emphasis on cross-cutting concerns to improve product quality.

Cross-cutting concerns are things that affect many parts of a product. And are hard to separate. For example, monitoring and alerting the health of the services.

WhatsApp engineering; Cross-cutting concerns
Cross-Cutting Concerns
And they improved the software development process with Continuous integration and Continuous delivery.

Continuous integration is the process of merging the code changes regularly into a central repository.

Continuous delivery is the process of code deployment to a testing or production environment.

5. Scalability
WhatsApp used diagonal scaling to keep the costs and operational complexity low.

Horizontal scaling is the process of increasing the number of machines in the resource pool.

Vertical scaling is the process of increasing the capacity of an existing machine, such as the CPU or memory.

And diagonal scaling is a hybrid of horizontal and vertical scaling. The computing resources get added both vertically and horizontally.

WhatsApp engineering; Scalability
Scalability
They ran WhatsApp servers on the FreeBSD operating system. Because they had previous experience with FreeBSD while working at Yahoo. Besides FreeBSD offered a reliable network stack.

Also they fine-tuned FreeBSD to accommodate 2 million+ connections per server. And modified kernel parameters such as files and sockets.

They overprovisioned servers to handle sudden traffic spikes and keep headroom for failures. For example, failures such as network partitions or hardware faults.

6. Flywheel Effect
They measured the metrics such as CPU, context switches, and system calls. Then identified and eliminated the bottlenecks. And they did this at regular intervals.

WhatsApp Engineering; Continuous feedback cycle
Continuous Feedback Cycle
The continuous feedback cycle tremendously improved the performance of WhatsApp.

7. Quality
They used load testing to identify single points of failure.

Load testing is the process of measuring the performance of the system under the anticipated load.

WhatsApp Engineering; Load testing
Load Testing
And they used artificial production traffic and DNS configuration changes for load testing.

8. Small Team Size
The communication paths between engineers increase quadratically as the team size grows. This is a recipe for degraded productivity.

WhatsApp Engineering; Communication paths between engineers
Communication Paths Between Engineers
So they kept the team size small - 32 engineers.

WhatsApp is one of the most successful instant messengers in the market.

In 2014, the same Facebook that rejected Jan Koum acquired WhatsApp for a whopping 19 billion USD.

According to Forbes, Jan Koum has a net worth of 14 billion USD in 2023.

