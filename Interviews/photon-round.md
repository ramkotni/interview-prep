Question: Can you describe your team structure and methodology?
Answer:
Yes, our team uses Agile methodology, and we follow a two-week sprint cycle, around 15 days. For each sprint, we create story points and allocate them to the respective team members. Business analysts create the requirements, which are then turned into user stories for the developers. We have a DevOps team that handles infrastructure, cloud services, and Terraform scripts. Our testing team includes three members—one automation tester and two manual testers. We also have one business analyst in the testing team. Additionally, there is a scrum master, myself as the architect, and a senior architect. The remaining team members are developers, including two UI developers and three full-stack developers.

Question: Are stakeholders involved in the project?
Answer:
Yes, we do involve stakeholders, such as the DevOps team (with two DevOps engineers), the testing team, and the business analyst. They all play a role in ensuring smooth communication and collaboration.

Question: Can you explain your project?
Answer:
We are working on an Amazon Robotics application that involves a delivery tracking system. We pull data from an ERP system, assign it to delivery partners, and track the processing of goods on a daily basis. The goal is to assess vendor performance, check which vendor is processing the fastest, and identify any delays or issues in the process. We use Apache Flink to connect our warehouse data to vendor systems. Some services faced downtime due to latency issues, but we're working to stabilize and improve the application.

Question: Did you face any issues with the application during peak times?
Answer:
Yes, during peak periods, some of the services faced downgrades due to issues with the auto-scaling group. It wasn’t functioning properly, and the system couldn't handle high traffic, leading to slower data loading times. We reported this to the DevOps team, and they are working on resolving it.

Question: How did you handle a situation where the severity of an issue wasn't understood?
Answer:
There was a scenario where some of the junior team members were retrieving unnecessary data from the database, which led to performance issues. I took the initiative to review and prioritize the APIs, ensuring they retrieved only necessary data. I also documented the process in Confluence for future reference. Even though it wasn't directly part of my role, I stepped in to improve the situation by identifying and resolving the issue.

Question: Can you explain how you applied your senior-level experience in this situation?
Answer:
In the previous project, I noticed that some API requests were pulling unnecessary data, causing problems in the application. As a senior team member, I identified this issue and worked on prioritizing the APIs, ensuring that only the required data was retrieved. I guided my junior team members and took the responsibility of documenting the changes in Confluence, making sure everyone understood the new approach and why it was necessary. This was an example of how I applied my senior-level experience to manage and improve the project.
