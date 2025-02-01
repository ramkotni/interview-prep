Interview 1 - Wipro - Mon Feb 3, 2025 1pm – 2pm (CST) - 12.30 am IST - (Feb 04th early)

1). Java Full Stack

We are looking for someone with the following qualifications:
JAVA Full Stack Developer, with a focus on both front-end and back-end technologies.
Strong proficiency in front-end frameworks such as React.
Solid understanding of database systems (SQL, NoSQL), webservices.
Extensive use of APIs and strong understanding of HTTP(S) and REST architecture.
Strong problem-solving and analytical skills.
Excellent communication.


2). Java Backend

Strong Computer Science background.
Significant experience in designing, implementing & supporting highly scalable systems and services in Java.
Problem solving skills & technical troubleshooting.
Hands-on experience with MongoDB.
Proficiency in Kafka for building real-time streaming applications.
Understanding of AWS cloud services and experience with at least some of the following: EC2, S3, Lambda, DynamoDB, etc.
Strong analytical and problem-solving skills, with a keen attention to detail.
Experience with testing frameworks, continuous integration and build tools.
Demonstrated knowledge of UNIX servers, commands, environments, and tools.
Experience with DAM (Digital Asset Management) preferable.


=======
Detailed Project Explanation for Interview
Project Overview:
As a Java Full Stack Developer with a focus on both front-end and back-end technologies, the goal of this project was to build and deploy a highly scalable, efficient, and user-friendly web application. This application catered to a digital asset management (DAM) system for an organization, ensuring that all their digital assets (images, videos, documents, etc.) were easily accessible, categorized, and available for real-time use.

The system was designed to handle a high volume of assets while ensuring smooth user interaction via both React (front-end) and a robust Java backend built with Spring Boot and integrated with cloud technologies, messaging systems, and databases.

1. Front-End (React) Development:
For the front-end of the application, I used React to ensure an interactive and dynamic user interface.

React Components: Built reusable and modular components using React, ensuring that the UI was scalable and easy to maintain. These components rendered asset lists, search results, asset previews, etc., and were designed with the goal of making the interface intuitive for users to upload, search, and download assets.

State Management with Redux: For efficient state management, Redux was used. This allowed managing the state of the application globally, particularly for handling complex state transitions when assets were uploaded, deleted, or searched across multiple pages.

APIs and HTTP(S) Integration: I extensively used REST APIs to interact with the backend. These APIs were designed to handle asset uploads, downloads, categorization, and search requests. The axios library was used to make API calls, and I ensured efficient handling of HTTP requests, error responses, and loading states to enhance user experience.

Responsive Design: Used CSS3 and Bootstrap for responsive design to ensure that the application was mobile-friendly and provided a seamless experience across different devices and screen sizes.

Authentication: Implemented JWT-based authentication to ensure secure login and session management. Users could log in to the system, which would authenticate them against the backend, providing an access token for further actions within the application.

Use Case Example for Front-End:
In the DAM application, a user might upload a large batch of digital images. The React component allowed the user to drag and drop the images, after which they were uploaded via an API call. As the images were uploading, the application displayed a progress bar and provided real-time feedback about the status of each image in the batch. The images were stored on the backend and cataloged in a database, and users could immediately search and categorize them using the provided UI.

2. Back-End Development (Java with Spring Boot):
On the back-end, I designed and implemented a highly scalable system using Java, Spring Boot, and integrated with multiple technologies like MongoDB, Kafka, and AWS Cloud.

Spring Boot: I used Spring Boot for building RESTful APIs for managing digital assets. These APIs handled asset CRUD operations, including uploading, retrieving, categorizing, and deleting assets. I ensured the application followed best practices for API design and scalability.

MongoDB: The asset metadata, such as file names, types, categories, and creation dates, were stored in MongoDB, a NoSQL database, which provided the flexibility needed to store various unstructured data types (e.g., image metadata, video duration, etc.). I used MongoDB’s aggregation framework to perform complex searches and queries efficiently.

Kafka: To manage real-time asset-related events, such as notifications when assets are uploaded, deleted, or updated, I integrated Kafka for event streaming. Kafka was set up as the messaging queue that published asset events (e.g., “asset uploaded”, “asset deleted”) and allowed downstream services or microservices to consume them.

REST API: I created a REST API with CRUD operations for the digital assets. These operations were exposed to the front-end to facilitate easy interaction. This included authentication via JWT, error handling, and response codes, ensuring smooth integration between front-end and back-end.

AWS Cloud Integration:

S3: Digital assets, such as images and videos, were stored on Amazon S3 to take advantage of its scalable, durable, and secure object storage. This ensured that assets were easily accessible and could be served directly to users with minimal delay.
EC2: Deployed the Spring Boot application on EC2 instances to ensure scalability and availability.
Lambda: Used AWS Lambda to handle certain asynchronous tasks, such as resizing images or processing video files upon upload. These tasks were triggered based on certain events in the S3 bucket.
DynamoDB: For some lightweight, non-relational data storage needs (e.g., user sessions or temporary metadata), I utilized DynamoDB, which provided fast read and write operations at scale.
Use Case Example for Back-End:
When a user uploads a new image through the front-end React interface, the following happens:

The image is first uploaded to S3.
A Kafka producer sends an event to a Kafka topic indicating that a new asset has been uploaded.
A Kafka consumer processes the event and stores the asset's metadata (file name, size, type, etc.) in MongoDB.
If any processing (such as resizing or thumbnail generation) is needed, AWS Lambda is triggered to handle the image processing asynchronously.
3. Integration with Digital Asset Management (DAM):
The application was specifically designed to manage large volumes of digital assets (images, documents, videos) and included the following key features:

Search & Categorization: Built a search engine using MongoDB's powerful query features, allowing users to search assets by different criteria (name, type, category).

Asset Preview: Implemented functionality to preview assets directly from the interface before users decide to download or categorize them.

Version Control: To track updates or modifications to assets, I implemented a basic version control system, allowing users to upload new versions of an asset while keeping track of the old ones.

Security: Ensured that only authenticated users could access and perform actions on assets. Implemented role-based access control (RBAC) to restrict certain actions (e.g., asset deletion, modification) to privileged users only.

4. Testing & Continuous Integration:
Unit Testing: Used JUnit and Mockito for unit testing individual components of the application, ensuring that each component (both front-end and back-end) performed correctly and met requirements.

Integration Testing: I wrote integration tests for the RESTful APIs to ensure that the front-end and back-end communicated seamlessly.

CI/CD Pipeline: Set up a Jenkins-based CI/CD pipeline for continuous integration and delivery. The pipeline was designed to automatically run tests, build the application, and deploy it to a staging environment whenever code changes were made.

5. Monitoring and Troubleshooting:
Logging and Monitoring: Integrated AWS CloudWatch for monitoring application logs and performance metrics. I used it to track server health, API request times, and detect any unusual behavior or performance degradation.

Error Handling: Ensured robust error handling on both the front-end (React) and back-end (Java). Any unhandled errors or system failures were logged and provided with meaningful error messages for troubleshooting.

Summary of Technologies Used:
Front-End: React, Redux, HTML, CSS, Bootstrap
Back-End: Java, Spring Boot, RESTful APIs, MongoDB, Kafka
Cloud: AWS (EC2, S3, Lambda, DynamoDB)
Messaging: Apache Kafka
CI/CD: Jenkins, Git
Testing: JUnit, Mockito, Postman for API testing
Version Control: GitHub
This project involved a combination of Java Full Stack skills, integrating both React for the front-end and Spring Boot for the back-end, while leveraging cloud services such as AWS for scalability and storage. The system was designed to handle high volumes of digital assets while ensuring security, efficiency, and seamless user interaction.

The result was a scalable, secure, and highly available Digital Asset Management platform that met both business and technical requirements while providing an excellent user experience.