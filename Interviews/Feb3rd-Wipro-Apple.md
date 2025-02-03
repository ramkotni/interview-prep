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


===Mongo DB ==

MongoDB Basic Interview Questions
MongoDB Basic Interview Questions focus on foundational knowledge, helping you understand how MongoDB operates as a NoSQL database. These questions typically cover key concepts like the differences between SQL and NoSQL databases, how MongoDB structures and stores data, and basic operations like CRUD (Create, Read, Update, Delete).

1. What is MongoDB, and How Does It Differ from Traditional SQL Databases?
MongoDB is a NoSQL database which means it does not use the traditional table-based relational database structure. Instead of it uses a flexible and document-oriented data model that stores data in BSON (Binary JSON) format.
Unlike SQL databases that use rows and columns, MongoDB stores data as JSON-like documents, making it easier to handle unstructured data and providing greater flexibility in terms of schema design.
2. Explain BSON and Its Significance in MongoDB.
BSON (Binary JSON) is a binary-encoded serialization format used by MongoDB to store documents. BSON extends JSON by adding support for data types such as dates and binary data and it is designed to be efficient in both storage space and scan speed. The binary format allows MongoDB to be more efficient with data retrieval and storage compared to text-based JSON.

3. Describe the Structure of a MongoDB Document.
A MongoDB document is a set of key-value pairs similar to a JSON object. Each key is a string and the value can be a variety of data types including strings, numbers, arrays, nested documents and more.

Example:

{
  "_id": ObjectId("507f1f77bcf86cd799439011"),
  "name": "Alice",
  "age": 25,
  "address": {
    "street": "123 Main St",
    "city": "Anytown",
    "state": "CA"
  },
  "hobbies": ["reading", "cycling"]
}
4. What are Collections And Databases In MongoDB?
Database: A container for collections, equivalent to a database in SQL.
Collection: A group of documents, similar to tables in SQL, but schema-less.
For example, a users collection can be part of the mydatabase database.
5. How Does MongoDB Ensure High Availability and Scalability?
MongoDB ensures high availability and scalability through its features like replica sets and sharding.
Replica sets provide redundancy and failover capabilities by ensuring that data is always available.
Sharding distributes data across multiple servers, enabling horizontal scalability to handle large volumes of data and high traffic loads.
6. Explain the Concept of Replica Sets in MongoDB.
A replica set in MongoDB is a group of mongod instances that maintain the same data set.
A replica set consists of a primary node and multiple secondary nodes.
The primary node receives all write operations while secondary nodes replicate the primary's data and can serve read operations.
If the primary node fails, an automatic election process selects a new primary to maintain high availability.
7. What are the Advantages of Using MongoDB Over Other Databases?
Flexibility: MongoDB's document-oriented model allows for dynamic schemas.
Scalability: Built-in sharding enables horizontal scaling.
High Availability: Replica sets provide redundancy and automatic failover.
Performance: Efficient storage and retrieval with BSON format.
Ease of Use: JSON-like documents make it easier for developers to interact with data.
8. How to Create a New Database and Collection in MongoDB?
To create a new database and collection in MongoDB, you can use the mongo shell:

use mydatabase
db.createCollection("mycollection")
This command switches to mydatabase (creating it if it doesn't exist) and creates a new collection named mycollection.

9. What is Sharding, and How Does It Work in MongoDB?
Sharding is a method for distributing data across multiple servers in MongoDB. It allows for horizontal scaling by splitting large datasets into smaller, more manageable pieces called shards.

Each shard is a separate database that holds a portion of the data.
MongoDB automatically balances data and load across shards, ensuring efficient data distribution and high performance.
10. Explain the Basic Syntax of MongoDB CRUD Operations.
CRUD operations in MongoDB are used to create, read, update, and delete documents.

Create: db.collection.insertOne({ name: "Alice", age: 25 })
Read: db.collection.find({ name: "Alice" })
Update: db.collection.updateOne({ name: "Alice" }, { $set: { age: 26 } })
Delete: db.collection.deleteOne({ name: "Alice" })
11. How to Perform Basic Querying in MongoDB?
Basic querying in MongoDB involves using the find method to retrieve documents that match certain criteria.

Example:

db.collection.find({ age: { $gte: 20 } })
This query retrieves all documents from the collection where the age field is greater than or equal to 20.

12. What is an Index in MongoDB, and How to Create One?
An index in MongoDB is a data structure that improves the speed of data retrieval operations on a collection. You can create an index using the createIndex method.

For example, to create an index on the name field:

db.collection.createIndex({ name: 1 })
13. How Does MongoDB Handle Data Consistency?
MongoDB provides several mechanisms to ensure data consistency:

Journaling: MongoDB uses write-ahead logging to maintain data integrity.
Write Concerns: It specify the level of acknowledgment requested from MongoDB for write operations (e.g., acknowledgment from primary only, or acknowledgment from primary and secondaries).
Replica Sets: Replication ensures data is consistent across multiple nodes, and read concerns can be configured to ensure data consistency for read operations.
14. How to Perform Data Import and Export in MongoDB?
To perform data import and export in MongoDB, you can use the mongoimport and mongoexport tools. These tools allow you to import data from JSON, CSV or TSV files into MongoDB and export data from MongoDB collections to JSON or CSV files.

Import Data:

mongoimport --db mydatabase --collection mycollection --file data.json
This command imports data from data.json into the mycollection collection in the mydatabase database.

Export Data:

mongoexport --db mydatabase --collection mycollection --out data.json
This command exports data from the mycollection collection in the mydatabase database to data.json.

15. What are MongoDB Aggregation Pipelines and How are They Used?
The aggregation pipeline is a framework for data aggregation, modeled on the concept of data processing pipelines. Documents enter a multi-stage pipeline that transforms the documents into aggregated results. Each stage performs an operation on the input documents and passes the results to the next stage.

db.orders.aggregate([
  { $match: { status: "A" } },           // Stage 1: Filter documents by status
  { $group: { _id: "$cust_id", total: { $sum: "$amount" } } },  // Stage 2: Group by customer ID and sum the amount
  { $sort: { total: -1 } }               // Stage 3: Sort by total in descending order
])
In this example:

Stage 1 ($match) filters documents by status "A".
Stage 2 ($group) groups documents by customer ID and calculates the total amount for each group.
Stage 3 ($sort) sorts the results by total amount in descending order.
Aggregation pipelines are powerful and flexible, enabling complex data processing tasks to be executed within MongoDB.

MongoDB Intermediate Interview Questions
MongoDB Intermediate Interview Questions explore advanced concepts and features, such as schema design, aggregation pipelines, indexing strategies, and transaction management. These questions help gauge your ability to utilize MongoDB efficiently in more complex scenarios.

1. Describe the Aggregation Framework in MongoDB
The Aggregation Framework in MongoDB is a powerful tool for performing data processing and transformation on documents within a collection.
It works by passing documents through a multi-stage pipeline, where each stage performs a specific operation on the data, such as filtering, grouping, sorting, reshaping and computing aggregations.
This framework is particularly useful for creating complex data transformations and analytics directly within the database.
2. How to Perform Aggregation Operations Using MongoDB?
Aggregation operations in MongoDB are performed using the aggregate method. This method takes an array of pipeline stages, each stage representing a step in the data processing pipeline.

Example: Calculate total sales for each product:
db.sales.aggregate([
  { $match: { status: "completed" } },  // Filter completed sales
  { $group: { _id: "$product", totalSales: { $sum: "$amount" } } },  // Group by product and sum the sales amount
  { $sort: { totalSales: -1 } }  // Sort by total sales in descending order
])
3. Explain the Concept of Write Concern and Its Importance in MongoDB
Write Concern in MongoDB refers to the level of acknowledgment requested from MongoDB for write operations. It determines how many nodes must confirm the write operation before it is considered successful. Write concern levels range from "acknowledged" (default) to "unacknowledged," "journaled," and various "replica acknowledged" levels.

The importance of write concern lies in balancing between data durability and performance. Higher write concern ensures data is safely written to disk and replicated, but it may impact performance due to the added latency.

4. What are TTL Indexes, and How are They Used in MongoDB?
TTL (Time To Live) Indexes in MongoDB are special indexes that automatically remove documents from a collection after a certain period. They are commonly used for data that needs to expire after a specific time, such as session information, logs, or temporary data. To create a TTL index, you can specify the expiration time in seconds

Example: Remove documents 1 hour after createdAt:
db.sessions.createIndex({ "createdAt": 1 }, { expireAfterSeconds: 3600 })
This index will remove documents from the sessions collection 1 hour (3600 seconds) after the createdAt field's value.

5. How to Handle Schema Design and Data Modeling in MongoDB?
Schema design and data modeling in MongoDB involve defining how data is organized and stored in a document-oriented database. Unlike SQL databases, MongoDB offers flexible schema design, which can be both an advantage and a challenge. Key considerations for schema design include:

Embedding vs. Referencing: Deciding whether to embed related data within a single document or use references between documents.
Document Structure: Designing documents that align with application query patterns for efficient read and write operations.
Indexing: Creating indexes to support query performance.
Data Duplication: Accepting some level of data duplication to optimize for read performance.
Sharding: Designing the schema to support sharding if horizontal scaling is required.
6. What is GridFS, and When is it Used in MongoDB?
GridFS is a specification for storing and retrieving large files in MongoDB. It is used when files exceed the BSON-document size limit of 16 MB or when you need to perform efficient retrieval of specific file sections.

GridFS splits a large file into smaller chunks and stores each chunk as a separate document within two collections: fs.files and fs.chunks. This allows for efficient storage and retrieval of large files, such as images, videos, or large datasets.

7. Explain the Differences Between WiredTiger and MMAPv1 Storage Engines
Feature	WiredTiger	MMAPv1
Concurrency	Document-level concurrency, allowing multiple operations simultaneously.	Collection-level concurrency, limiting performance under heavy write operations.
Compression	Supports data compression, reducing storage requirements.	Does not support data compression.
Performance	Generally offers better performance and efficiency for most workloads.	Limited performance, especially under heavy workloads.
Journaling	Uses write-ahead logging for better data integrity.	Basic journaling; less advanced than WiredTiger.
Status	Modern and default storage engine.	Legacy engine, deprecated in favor of WiredTiger.
Implementation	Advanced implementation with additional features.	Simple implementation but lacks advanced features.
8. How to Handle Transactions in MongoDB?
MongoDB supports multi-document ACID transactions by allowing us to perform a series of read and write operations across multiple documents and collections in a transaction. This ensures data consistency and integrity. To use transactions we typically start a session, begin a transaction, perform the operations and then commit or abort the transaction.

Example in JavaScript:

const session = client.startSession();

session.startTransaction();

try {
  db.collection1.insertOne({ name: "Alice" }, { session });
  db.collection2.insertOne({ name: "Bob" }, { session });
  session.commitTransaction();
} catch (error) {
  session.abortTransaction();
} finally {
  session.endSession();
}
9. Describe the MongoDB Compass Tool and Its Functionalities
MongoDB Compass is a graphical user interface (GUI) tool for MongoDB that provides an easy way to visualize, explore, and manipulate your data. It offers features such as:

Schema Visualization: View and analyze your data schema, including field types and distributions.
Query Building: Build and execute queries using a visual interface.
Aggregation Pipeline: Construct and run aggregation pipelines.
Index Management: Create and manage indexes to optimize query performance.
Performance Monitoring: Monitor database performance, including slow queries and resource utilization.
Data Validation: Define and enforce schema validation rules to ensure data integrity.
Data Import/Export: Easily import and export data between MongoDB and JSON/CSV files.
10. What is MongoDB Atlas, and How Does it Differ From Self-Hosted MongoDB?
MongoDB Atlas is a fully managed cloud database service provided by MongoDB. It offers automated deployment, scaling, and management of MongoDB clusters across various cloud providers (AWS, Azure, Google Cloud). Key differences from self-hosted MongoDB include:

Managed Service: Atlas handles infrastructure management, backups, monitoring, and upgrades.
Scalability: Easily scale clusters up or down based on demand.
Security: Built-in security features such as encryption, access controls, and compliance certifications.
Global Distribution: Deploy clusters across multiple regions for low-latency access and high availability.
Integrations: Seamless integration with other cloud services and MongoDB tools.
11. How to Implement Access Control and User Authentication in MongoDB?
Access control and user authentication in MongoDB are implemented through a role-based access control (RBAC) system. You create users and assign roles that define their permissions. To set up access control:

Enable Authentication: Configure MongoDB to require authentication by starting the server with --auth or setting security.authorization to enabled in the configuration file.
Create Users: Use the db.createUser method to create users with specific roles.
db.createUser({
  user: "admin",
  pwd: "password",
  roles: [{ role: "userAdminAnyDatabase", db: "admin" }]
});
Assign Roles: Assign roles to users that define their permissions, such as read, write, or admin roles for specific databases or collections.
12. What are Capped Collections, and When are They Useful?
Capped collections in MongoDB are fixed-size collections that automatically overwrite the oldest documents when the specified size limit is reached. They maintain insertion order and are useful for scenarios where you need to store a fixed amount of recent data, such as logging, caching, or monitoring data.

Example of creating a capped collection:

db.createCollection("logs", { capped: true, size: 100000 });
13. Explain the Concept of Geospatial Indexes in MongoDB
Geospatial indexes in MongoDB are special indexes that support querying of geospatial data, such as locations and coordinates. They enable efficient queries for proximity, intersections, and other spatial relationships. MongoDB supports two types of geospatial indexes: 2d for flat geometries and 2dsphere for spherical geometries.

Example of creating a 2dsphere index:

db.places.createIndex({ location: "2dsphere" });
14. How to Handle Backups and Disaster Recovery in MongoDB?
Handling backups and disaster recovery in MongoDB involves regularly creating backups of your data and having a plan for restoring data in case of failure. Methods include:

Mongodump/Mongorestore: Use the mongodump and mongorestore utilities to create and restore binary backups.
File System Snapshots: Use file system snapshots to take consistent backups of the data files.
Cloud Backups: If using MongoDB Atlas, leverage automated backups provided by the service.
Replica Sets: Use replica sets to ensure data redundancy and high availability. Regularly test the failover and recovery process.
15. Describe the Process of Upgrading MongoDB to a Newer Version
Upgrading MongoDB to a newer version involves several steps to ensure a smooth transition:

Check Compatibility: Review the release notes and compatibility changes for the new version.
Backup Data: Create a backup of your data to prevent data loss.
Upgrade Drivers: Ensure that your application drivers are compatible with the new MongoDB version.
Upgrade MongoDB: Follow the official MongoDB upgrade instructions, which typically involve stopping the server, installing the new version, and restarting the server.
Test Application: Thoroughly test your application with the new MongoDB version to identify any issues.
Monitor: Monitor the database performance and logs to ensure a successful upgrade.
16. What are Change Streams in MongoDB, and How are They Used?
Change Streams in MongoDB allow applications to listen for real-time changes to data in collections, databases, or entire clusters. They provide a powerful way to implement event-driven architectures by capturing insert, update, replace, and delete operations. To use Change Streams, you typically open a change stream cursor and process the change events as they occur.

Example:

const changeStream = db.collection('orders').watch();
changeStream.on('change', (change) => {
  console.log(change);
});
This example listens for changes in the orders collection and logs the change events.

17. Explain the Use of Hashed Sharding Keys in MongoDB
Hashed Sharding Keys in MongoDB distribute data across shards using a hashed value of the shard key field. This approach ensures an even distribution of data and avoids issues related to data locality or uneven data distribution that can occur with range-based sharding. Hashed sharding is useful for fields with monotonically increasing values, such as timestamps or identifiers.

Example:

db.collection.createIndex({ _id: "hashed" });
sh.shardCollection("mydb.mycollection", { _id: "hashed" });
18. How to Optimize MongoDB Queries for Performance?
Optimizing MongoDB queries involves several strategies:

Indexes: Create appropriate indexes to support query patterns.
Query Projections: Use projections to return only necessary fields.
Index Hinting: Use index hints to force the query optimizer to use a specific index.
Query Analysis: Use the explain() method to analyze query execution plans and identify bottlenecks.
Aggregation Pipeline: Optimize the aggregation pipeline stages to minimize data processing and improve efficiency.
19. Describe the Map-Reduce Functionality in MongoDB
Map-Reduce in MongoDB is a data processing paradigm used to perform complex data aggregation operations. It consists of two phases: the map phase processes each input document and emits key-value pairs, and the reduce phase processes all emitted values for each key and outputs the final result.

Example:

db.collection.mapReduce(
  function() { emit(this.category, this.price); },
  function(key, values) { return Array.sum(values); },
  { out: "category_totals" }
);
This example calculates the total price for each category in a collection.

20. What is the Role of Journaling in MongoDB, and How Does It Impact Performance?
Journaling in MongoDB ensures data durability and crash recovery by recording changes to the data in a journal file before applying them to the database files. This mechanism allows MongoDB to recover from unexpected shutdowns or crashes by replaying the journal. While journaling provides data safety, it can impact performance due to the additional I/O operations required to write to the journal file.

21. How to Implement Full-Text Search in MongoDB?
Full-Text Search in MongoDB is implemented using text indexes. These indexes allow you to perform text search queries on string content within documents.

Example:

db.collection.createIndex({ content: "text" });
db.collection.find({ $text: { $search: "mongodb" } });
In this example, a text index is created on the content field, and a text search query is performed to find documents containing the word "mongodb."

22. What are the Considerations for Deploying MongoDB in a Production Environment?
Considerations for deploying MongoDB in a production environment include:

Replication: Set up replica sets for high availability and data redundancy.
Sharding: Implement sharding for horizontal scaling and to distribute the load.
Backup and Recovery: Establish a robust backup and recovery strategy.
Security: Implement authentication, authorization, and encryption.
Monitoring: Use monitoring tools to track performance and detect issues.
Capacity Planning: Plan for adequate storage, memory, and CPU resources.
Maintenance: Regularly update MongoDB to the latest stable version and perform routine maintenance tasks.
23. Explain the Concept of Horizontal Scalability and Its Implementation in MongoDB
Horizontal Scalability in MongoDB refers to the ability to add more servers to distribute the load and data. This is achieved through sharding, where data is partitioned across multiple shards.
Each shard is a replica set that holds a subset of the data. Sharding allows MongoDB to handle large datasets and high-throughput operations by distributing the workload.
24. How to Monitor and Troubleshoot Performance Issues in MongoDB?
Monitoring and troubleshooting performance issues in MongoDB involve:

Monitoring Tools: Use tools like MongoDB Cloud Manager, MongoDB Ops Manager, or third-party monitoring solutions.
Logs: Analyze MongoDB logs for errors and performance metrics.
Profiling: Enable database profiling to capture detailed information about operations.
Explain Plans: Use the explain() method to understand query execution and identify bottlenecks.
Index Analysis: Review and optimize indexes based on query patterns and usage.
Resource Utilization: Monitor CPU, memory, and disk I/O usage to identify resource constraints.
25. Describe the Process of Migrating Data from a Relational Database to MongoDB
Migrating data from a relational database to MongoDB involves several steps:

Schema Design: Redesign the relational schema to fit MongoDB's document-oriented model. Decide on embedding vs. referencing, and plan for indexes and collections.
Data Export: Export data from the relational database in a format suitable for MongoDB (e.g., CSV, JSON).
Data Transformation: Transform the data to match the MongoDB schema. This can involve converting data types, restructuring documents, and handling relationships.
Data Import: Import the transformed data into MongoDB using tools like mongoimport or custom scripts.
Validation: Validate the imported data to ensure consistency and completeness.
Application Changes: Update the application code to interact with MongoDB instead of the relational database.
Testing: Thoroughly test the application and the database to ensure everything works as expected.
Go Live: Deploy the MongoDB database in production and monitor the transition.
MongoDB Query Based Interview Questions
MongoDB Query-Based Interview Questions focus on your ability to write efficient and optimized queries to interact with databases. These tasks include retrieving specific data using filters, sorting and paginating results, and utilizing projections to select desired fields. Below is a sample dataset we'll use to demonstrate various queries.

Sample Dataset
The following dataset represents a collection named employees, containing documents about employees in an organization. Each document includes details such as the employee's name, age, position, salary, department, and hire date.

"[
    {
        ""_id"": 1,
        ""name"": ""John Doe"",
        ""age"": 28,
        ""position"": ""Software Engineer"",
        ""salary"": 80000,
        ""department"": ""Engineering"",
        ""hire_date"": ISODate(""2021-01-15"")
    },
    {
        ""_id"": 2,
        ""name"": ""Jane Smith"",
        ""age"": 34,
        ""position"": ""Project Manager"",
        ""salary"": 95000,
        ""department"": ""Engineering"",
        ""hire_date"": ISODate(""2019-06-23"")
    },
    {
        ""_id"": 3,
        ""name"": ""Emily Johnson"",
        ""age"": 41,
        ""position"": ""CTO"",
        ""salary"": 150000,
        ""department"": ""Management"",
        ""hire_date"": ISODate(""2015-03-12"")
    },
    {
        ""_id"": 4,
        ""name"": ""Michael Brown"",
        ""age"": 29,
        ""position"": ""Software Engineer"",
        ""salary"": 85000,
        ""department"": ""Engineering"",
        ""hire_date"": ISODate(""2020-07-30"")
    },
    {
        ""_id"": 5,
        ""name"": ""Sarah Davis"",
        ""age"": 26,
        ""position"": ""UI/UX Designer"",
        ""salary"": 70000,
        ""department"": ""Design"",
        ""hire_date"": ISODate(""2022-10-12"")
    }
]"
1. Find all Employees Who Work in the "Engineering" Department.
Query:

db.employees.find({ department: "Engineering" })
Output:

[
    {
        "_id": 1,
        "name": "John Doe",
        "age": 28,
        "position": "Software Engineer",
        "salary": 80000,
        "department": "Engineering",
        "hire_date": ISODate("2021-01-15")
    },
    {
        "_id": 2,
        "name": "Jane Smith",
        "age": 34,
        "position": "Project Manager",
        "salary": 95000,
        "department": "Engineering",
        "hire_date": ISODate("2019-06-23")
    },
    {
        "_id": 4,
        "name": "Michael Brown",
        "age": 29,
        "position": "Software Engineer",
        "salary": 85000,
        "department": "Engineering",
        "hire_date": ISODate("2020-07-30")
    }
]
Explanation: This query finds all employees whose department field is "Engineering".

2. Find the Employee with the Highest Salary.
Query:

db.employees.find().sort({ salary: -1 }).limit(1)
Output:

[
    {
        "_id": 3,
        "name": "Emily Johnson",
        "age": 41,
        "position": "CTO",
        "salary": 150000,
        "department": "Management",
        "hire_date": ISODate("2015-03-12")
    }
]
Explanation: This query sorts all employees by salary in descending order and retrieves the top document, which is the employee with the highest salary.

3. Update the Salary of "John Doe" to 90000.
Query:

db.employees.updateOne({ name: "John Doe" }, { $set: { salary: 90000 } })
Output:

{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
Explanation: This query updates the salary of the employee named "John Doe" to 90000.

4. Count the Number of Employees in Each Department.
Query:

db.employees.aggregate([
    { $group: { _id: "$department", count: { $sum: 1 } } }
])
Output:

[
    { "_id": "Engineering", "count": 3 },
    { "_id": "Management", "count": 1 },
    { "_id": "Design", "count": 1 }
]
Explanation: This query groups the employees by the department field and counts the number of employees in each department.

5. Add a New Field Bonus to All Employees in the "Engineering" Department with a Value of 5000.
Query:

db.employees.updateMany({ department: "Engineering" }, { $set: { bonus: 5000 } })
Output:

{ "acknowledged" : true, "matchedCount" : 3, "modifiedCount" : 3 }
Explanation: This query adds a new field bonus with a value of 5000 to all employees in the "Engineering" department.

6. Retrieve All Documents in the Employees Collection and Sort Them by the Length of Their Name in Descending Order.
Query:

db.employees.aggregate([
    { $addFields: { nameLength: { $strLenCP: "$name" } } },
    { $sort: { nameLength: -1 } },
    { $project: { nameLength: 0 } }
])
Output:

[
    {
        "_id": 2,
        "name": "Jane Smith",
        "age": 34,
        "position": "Project Manager",
        "salary": 95000,
        "department": "Engineering",
        "hire_date": ISODate("2019-06-23")
    },
    {
        "_id": 3,
        "name": "Emily Johnson",
        "age": 41,
        "position": "CTO",
        "salary": 150000,
        "department": "Management",
        "hire_date": ISODate("2015-03-12")
    },
    {
        "_id": 1,
        "name": "John Doe",
        "age": 28,
        "position": "Software Engineer",
        "salary": 80000,
        "department": "Engineering",
        "hire_date": ISODate("2021-01-15")
    },
    {
        "_id": 4,
        "name": "Michael Brown",
        "age": 29,
        "position": "Software Engineer",
        "salary": 85000,
        "department": "Engineering",
        "hire_date": ISODate("2020-07-30")
    },
    {
        "_id": 5,
        "name": "Sarah Davis",
        "age": 26,
        "position": "UI/UX Designer",
        "salary": 70000,
        "department": "Design",
        "hire_date": ISODate("2022-10-12")
    }
]
Explanation: This query calculates the length of each employee's name, sorts the documents by this length in descending order, and removes the temporary nameLength field from the output.

7. Find the Average Salary of Employees in the "Engineering" Department.
Query:

db.employees.aggregate([
    { $match: { department: "Engineering" } },
    { $group: { _id: null, averageSalary: { $avg: "$salary" } } }
])
Output:

[
    { "_id": null, "averageSalary": 86666.66666666667 }
]
Explanation: This query filters employees to those in the "Engineering" department and calculates the average salary of these employees.

8. Find the Department with the Highest Average Salary.
Query:

db.employees.aggregate([
    { $group: { _id: "$department", averageSalary: { $avg: "$salary" } } },
    { $sort: { averageSalary: -1 } },
    { $limit: 1 }
])
Output:

[
    { "_id": "Management", "averageSalary": 150000 }
]
Explanation: This query groups employees by department, calculates the average salary for each department, sorts these averages in descending order, and retrieves the department with the highest average salary.

9. Find the Total Number of Employees Hired in Each Year.
Query:

db.employees.aggregate([
    { $group: { _id: { $year: "$hire_date" }, totalHired: { $sum: 1 } } }
])
Output:

[
    { "_id": 2015, "totalHired": 1 },
    { "_id": 2019, "totalHired": 1 },
    { "_id": 2020, "totalHired": 1 },
    { "_id": 2021, "totalHired": 1 },
    { "_id": 2022, "totalHired": 1 }
]
Explanation: This query groups employees by the year they were hired, which is extracted from the hire_date field, and counts the total number of employees hired each year.

10. Find the Highest and Lowest Salary in the "Engineering" Department.
Query:

db.employees.aggregate([
    { $match: { department: "Engineering" } },
    {
        $group: {
            _id: null,
            highestSalary: { $max: "$salary" },
            lowestSalary: { $min: "$salary" }
        }
    }
])
Output:

[
    { "_id": null, "highestSalary": 95000, "lowestSalary": 80000 }
]
Explanation: This query filters employees to those in the "Engineering" department, then calculates the highest and lowest salary within this group.

Conclusion
Preparing for a MongoDB interview becomes much simpler with the right resources. This guide has provided a detailed collection of MongoDB interview questions, covering fundamental concepts, advanced topics, and real-world applications. By practicing these questions, you'll enhance your knowledge of MongoDB, strengthen your problem-solving skills, and build the confidence needed to excel in your interview. Stay consistent in your preparation, and you'll be ready to tackle any MongoDB challenge that comes your way!

======
Questions on React

React Interview Questions and Answers
Last Updated : 27 Jan, 2025
React is an efficient, flexible, and open-source JavaScript library that allows developers to create simple, fast, and scalable web applications. Jordan Walke, a software engineer who was working for Facebook created React. It was first deployed on Facebook’s news feed in 2011 and on Instagram in 2012. Developers with a Javascript background can easily develop web applications with React.

React is used by top IT companies such as Facebook, Dropbox, Instagram, WhatsApp, Atlassian, and Meta because of its Virtual DOM, Components, State and Props, JSX, Hooks, and Routing. So, to get developer roles in these companies, you need to complete these Top React interview questions which can make you seem like an expert in front of the interviewer.

In This Top React Interview Questions article, we’ve covered the Interview Questions of React that cover everything from basic to advanced React concepts such as Virtual DOM, Components, State and Props, JSX, Hooks, Routing, and more. Whether you are a fresher or an experienced professional with 2 – 10 years of experience, these React Interview Questions give you all the confidence you need to ace your next technical interview.

Table of Content

React Interview Questions For Freshers
React Intermediate Interview Questions
React Interview Questions For Experienced
React Interview Questions and Answers – FAQ’s
React Interview Questions For Freshers
1. What is ReactJS?
ReactJS is a JavaScript library used to build reusable components for the view layer in MVC architecture. It is highly efficient and uses a virtual DOM to render components. It works on the client side and is written in JSX.

Important Features of React:

Virtual DOM: React uses a virtual DOM to efficiently update and render components, ensuring fast performance by minimizing direct DOM manipulations.
Component-Based Architecture: React builds UI using reusable, isolated components, making code more modular, maintainable, and scalable.
Hooks: React hooks allow functional components to manage state and side effects, making them powerful and more flexible.
2. Explain the MVC architecture.
The Model-View-Controller (MVC) framework is an architectural/design pattern that separates an application into three main logical components Model, View, and Controller. Each architectural component is built to handle specific development aspects of an application. It isolates the business, logic, and presentation layer from each other

3. Explain the building blocks of React.
The five main building blocks of React are:

Components: These are reusable blocks of code that return HTML.
JSX: It stands for JavaScript and XML and allows you to write HTML in React.
Props and State: props are like function parameters and State is similar to variables.
Context: This allows data to be passed through components as props in a hierarchy.
Virtual DOM: It is a lightweight copy of the actual DOM which makes DOM manipulation easier.
4. Explain props and state in React with differences
Props are used to pass data from one component to another. The state is local data storage that is local to the component only and cannot be passed to other components.

Here is the difference table of props and state In react

PROPS

STATE

The Data is passed from one component to another.	The Data is passed within the component only.
It is Immutable (cannot be modified).	It is Mutable ( can be modified).
Props can be used with state and functional components.	The state can be used only with the state components/class component (Before 16.0).
Props are read-only.	The state is both read and write.
5. What is virtual DOM in React?
The Virtual DOM in React is an in-memory representation of the actual DOM. It helps React efficiently update and render the user interface by comparing the current and previous virtual DOM states using a process called diffing.

How Virtual DOM Works

Efficient Rendering: The Virtual DOM is an in-memory representation of the actual DOM that React uses to optimize the process of updating and rendering UI changes.
Diffing Algorithm: React compares the current and previous versions of the Virtual DOM using a diffing algorithm, identifying the minimal set of changes required to update the real DOM.
Batch Updates: Instead of updating the real DOM immediately, React batches multiple changes to reduce unnecessary re-renders, improving performance.
Faster Updates: Since updating the real DOM is slow, React minimizes direct DOM manipulations by only making updates where necessary after comparing the Virtual DOM.
Declarative UI: With the Virtual DOM, React allows developers to write code in a declarative style, letting React handle when and how to efficiently update the UI.
6. What is JSX?
JSX is basically a syntax extension of regular JavaScript and is used to create React elements. These elements are then rendered to the React DOM. All the React components are written in JSX. To embed any JavaScript expression in a piece of code written in JSX we will have to wrap that expression in curly braces {}. 

Example of JSX: The name written in curly braces { } signifies JSX

const name = "Learner";

const element = (
    <h1>
        Hello,
        {name}.Welcome to GeeksforGeeks.
    </h1>
);
7. What are components and their type in React?
A Component is one of the core building blocks of React. In other words, we can say that every application you will develop in React will be made up of pieces called components. Components make the task of building UIs much easier. 

 In React, we mainly have two types of components: 

Functional Components: Functional components are simply javascript functions. We can create a functional component in React by writing a javascript function. 
Class Components: The class components are a little more complex than the functional components. The functional components are not aware of the other components in your program whereas the class components can work with each other. We can pass data from one class component to another class component.
8. How do browsers read JSX?
In general, browsers are not capable of reading JSX and only can read pure JavaScript. The web browsers read JSX with the help of a transpiler. Transpilers are used to convert JSX into JavaScript. The transpiler used is called Babel

9. Explain the steps to create a react application and print Hello World?
To install React, first, make sure Node is installed on your computer. After installing Node. Open the terminal and type the following command.

npx create-react-app <<Application_Name>>
Navigate to the folder.

cd <<Application_Name>>
This is the first code of ReactJS Hello World!


import React from "react";
import "./App.css";
function App() {
    return <div className="App">Hello World !</div>;
}
export default App;
Type the following command to run the application

npm start
10. How to create an event in React?
To create an event in React, attach an event handler like onClick, onChange, etc., to a JSX element. Define the handler function to specify the action when the event is triggered, such as updating state or executing logic.


function Component() {
    doSomething(e);
    {
        e.preventDefault();
        // Some more response to the event
    }
    return <button onEvent={doSomething}></button>;
}
11. Explain the creation of a List in react?
Lists are very useful when it comes to developing the UI of any website. Lists are mainly used for displaying menus on a website, for example, the navbar menu. To create a list in React use the map method of array as follows.


import React from "react";
import ReactDOM from "react-dom";

const numbers = [1, 2, 3, 4, 5];

const updatedNums = numbers.map((number) => {
    return <li>{number}</li>;
});

ReactDOM.render(<ul>{updatedNums}</ul>, document.getElementById("root"));
12. What is a key in React?
A “key” is a special string attribute you need to include when creating lists of elements in React. Keys are used in React to identify which items in the list are changed, updated, or deleted. In other words, we can say that keys are used to give an identity to the elements in the lists.

13. How to write a comment in React?
There are two ways to write comments in React.

Multi-line comment: We can write multi-line comments in React using the asterisk format /* */.
Single line comment: We can write single comments in React using the double forward slash //.
14. Explain the difference between React and Angular?
Field
React.js
Angular
Used as	
React.js is a JavaScript library. As it indicates react js updates only the virtual DOM is present and the data flow is always in a single direction.

Angular is a framework. Angular updates the Real DOM and the data flow is ensured in the architecture in both directions.

Architecture	
React.js is more simplified as it follows MVC ie., Model View Control.

The architecture is complex as it follows MVVM models ie., Model View-ViewModel. 

Scalability	It is highly scalable.	It is less scalable than React JS.
Data Binding	It supports Uni-directional data binding which is one-way data binding.	It supports Bi-directional data binding which is two way data binding.
DOM	It has a virtual DOM.	It has regular DOM.
15. Explain the use of render method in React?
React renders HTML to the web page by using a function called render(). The purpose of the function is to display the specified HTML code inside the specified HTML element. In the render() method, we can read props and state and return our JSX code to the root component of our app.

16. What is state in React?
The state is an instance of React Component Class that can be defined as an object of a set of observable properties that control the behaviour of the component. In other words, the State of a component is an object that holds some information that may change over the lifetime of the component.

17. Explain props in React?
React allows us to pass information to a Component using something called props (which stands for properties). Props are objects which can be used inside a component

We can access any props inside from the component’s class to which the props is passed. The props can be accessed as shown below:

this.props.propName;
18. What is higher-order component in React?
Higher-order components or HOC is the advanced method of reusing the component functionality logic. It simply takes the original component and returns the enhanced component. HOC are beneficial as they are easy to code and read. Also, helps to get rid of copying the same logic in every component.

19. Explain the difference between functional and class component in React?
Here we have difference table of functional and class component in React

Functional Components                  	                         Class Components                
A functional component is just a plain JavaScript pure function that accepts props as an argument 	A class component requires you to extend from React. Component and create a render function 
No render method used	It must have the render() method returning JSX 
Also known as Stateless components 	Also known as Stateful components
React lifecycle methods (for example, componentDidMount) cannot be used in functional components.	React lifecycle methods can be used inside class components (for example, componentDidMount).
Constructors are not used.	Constructor is used as it needs to store state. 
20. Explain one way data binding in React?
ReactJS uses one-way data binding which can be Component to View or View to Component. It is also known as one-way data flow, which means the data has one, and only one way to be transferred to other parts of the application. In essence, this means child components are not able to update the data that is coming from the parent component. It is easy to debug and less prone to errors.

React Intermediate Interview Questions
Here, we cover all intermediate level react interview questions with answers, that recommeded for freshers as well as for experienced professionals having 1 – 2 years of experience.

21. What is conditional rendering in React?
Conditional rendering in React involves selectively rendering components based on specified conditions. By evaluating these conditions, developers can control which components are displayed, allowing for dynamic and responsive user interfaces in React applications.

Let us look at this sample code to understand conditional rendering. 

{isLoggedIn == false ? <DisplayLoggedOut /> : <DisplayLoggedIn />}
Here if the boolean isLoggedIn is false then the DisplayLoggedOut component will be rendered otherwise DisplayLoggedIn component will be rendered.

22. What is react router?
React Router is a standard library for routing in React. It enables the navigation among views of various components in a React Application, allows changing the browser URL, and keeps the UI in sync with the URL.

To install react router type the following command.

npm i react-router-dom
23. Explain the components of a react-router
The main components of a react-router are:

Router(usually imported as BrowserRouter):  It is the parent component that is used to store all of the other components. Everything within this will be part of the routing functionality
Switch: The switch component is used to render only the first route that matches the location rather than rendering all matching routes.
Route: This component checks the current URL and displays the component associated with that exact path. All routes are placed within the switch components.
Link: The Link component is used to create links to different routes.
24. Explain the lifecycle methods of components
A React Component can go through four stages of its life as follows. 

Initialization: This is the stage where the component is constructed with the given Props and default state. This is done in the constructor of a Component Class.
Mounting: Mounting is the stage of rendering the JSX returned by the render method itself.
Updating: Updating is the stage when the state of a component is updated and the application is repainted.
Unmounting: As the name suggests Unmounting is the final step of the component lifecycle where the component is removed from the page.
25. Explain the methods used in mounting phase of components
Mounting is the phase of the component lifecycle when the initialization of the component is completed and the component is mounted on the DOM and rendered for the first time on the webpage. he mounting phase consists of two such predefined functions as described below

componentWillMount() Function: This function is invoked right before the component is mounted on the DOM.
componentDidMount() Function: This function is invoked right after the component is mounted on the DOM.
26. What is this.setState function in React?
We use the setState() method to change the state object. It ensures that the component has been updated and calls for re-rendering of the component. The state object of a component may contain multiple attributes and React allows using setState() function to update only a subset of those attributes as well as using multiple setState() methods to update each attribute value independently.

27.  What is the use of ref in React?
Refs are a function provided by React to access the DOM element and the React element that you might have created on your own. They are used in cases where we want to change the value of a child component, without making use of props and all. They have wide functionality as we can use callbacks with them.

The syntax to use ref is

const node = this.myCallRef.current;
28. What are hooks in React?
 Hooks are a new addition in React 16.8. They let developers use state and other React features without writing a class. Hooks doesn’t violate any existing React concepts. Instead, Hooks provide a direct API to react concepts such as props, state, context, refs and life-cycle

29. Explain the useState hook in React?
The most used hook in React is the useState() hook. Using this hook we can declare a state variable inside a function but only one state variable can be declared using a single useState() hook. Whenever the useState() hook is used, the value of the state variable is changed and the new variable is stored in a new cell in the stack.

When you use useState(), you declare a state variable and a function to update that state. React then manages this state internally and triggers a re-render of the component when the state changes. This allows functional components to maintain and update their internal state over time.

We have to import this hook in React using the following syntax

import {useState} from 'react'
30. Explain the useEffect hook in react?
The useEffect hook in React eliminates the side effect of using class based components. It is used as an alternative to componentDidUpdate() method. The useEffect hook accepts two arguments where second argument is optional. 

useEffect(function, dependency)
The dependency decides when the component will be updated again after rendering.

31. What is React Fragments?
when we are trying to render more than one root element we have to put the entire content inside the ‘div’ tag which is not loved by many developers. So since React 16.2 version, Fragments were introduced, and we use them instead of the extraneous ‘div’ tag. The following syntax is used to create fragment in react.

<React.Fragment>  
    <h2>Child-1</h2>   
    <p> Child-2</p>   
</React.Fragment>  
32. What is a react developer tool?
React Developer Tools is a Chrome DevTools extension for the React JavaScript library. A very useful tool, if you are working on React.js applications. This extension adds React debugging tools to the Chrome Developer Tools. It helps you to inspect and edit the React component tree that builds the page, and for each component, one can check the props, the state, hooks, etc.

33. How to use styles in ReactJS?
CSS modules are a way to locally scope the content of your CSS file. We can create a CSS module file by naming our CSS file as App.modules.css and then it can be imported inside App.js file using the special syntax mentioned below.

Syntax:

import styles from './App.module.css';
34. Explain styled components in React?
Styled-component Module allows us to write CSS within JavaScript in a very modular and reusable way in React. Instead of having one global CSS file for a React project, we can use styled-component for enhancing the developer experience. It also removes the mapping between components and styles – using components as a low-level styling construct

The command to install styled components is

npm i styled-components
Using the below code we can custom style a button in React


import styled from 'styled-components'

const Button = styled.div`
    width : 100px ;
    cursor: pointer ;
    text-decoration : none;
`
export default Button;
35. What is prop drilling and its disadvantages?
Prop drilling is basically a situation when the same data is being sent at almost every level due to requirements in the final level. The problem with Prop Drilling is that whenever data from the Parent component will be needed, it would have to come from each level, Regardless of the fact that it is not needed there and simply needed in last.

For further reading, check out our dedicated article on Intermediate ReactJS Intermediate Interview Questions. Inside, you’ll discover over 20 questions with detailed answers.


React Interview Questions For Experienced
Here, we cover advanced react interview questions with answers for experienced professionals, who have over 5+ years of experience.

36. What is custom hooks in React?
Custom hooks are normal JavaScript functions whose names start with “use” and they may call other hooks. We use custom hooks to maintain the DRY concept that is Don’t Repeat Yourself. It helps us to write a logic once and use it anywhere in the code.

37. How to optimize a React code?
We can improve our react code by following these practices:

Using binding functions in constructors
Eliminating the use of inline attributes as they slow the process of loading
Avoiding extra tags by using React fragments
Lazy loading
38. What is the difference between useref and createRef in React ?
Here is the difference table of useref and createRef in React

useRef

createRef

It is a hook.	It is a function.
It uses the same ref throughout.	It creates a new ref every time.
It saves its value between re-renders in a functional component.	It creates a new ref for every re-render.
It returns a mutable ref object.	It returns a read-only ref object.
The refs created using the useRef can persist for the entire component lifetime.	The refs created using the createRef can be referenced throughout the component.
It is used in functional components.	It is used in class components.
39. What is react-redux?
React-redux is a state management tool which makes it easier to pass these states from one component to another irrespective of their position in the component tree and hence prevents the complexity of the application. As the number of components in our application increases it becomes difficult to pass state as props to multiple components. To overcome this situation we use react-redux

40. What are benefits of using react-redux?
They are several benfits of using react-redux such as:

It provides centralized state management i.e. a single store for whole application
It optimizes performance as it prevents re-rendering of component
Makes the process of debugging easier
Since it offers persistent state management therefore storing data for long times become easier
41. Explain the core components of react-redux?
There are four fundamental concepts of redux in react which decide how the data will flow through components

Redux Store: It is an object that holds the application state
Action Creators: These are functions that return actions (objects).
Actions: Actions are simple objects which conventionally have two properties- type and payload 
Reducers: Reducers are pure functions that update the state of the application in response to actions
42. How can we combine multiple reducers in React?
When working with Redux we sometimes require multiple reducers. In many cases, multiple actions are needed, resulting in the requirement of multiple reducers. However, this can become problematic when creating the Redux store. To manage the multiple reducers we have function called combineReducers in the redux. This basically helps to combine multiple reducers into a single unit and use them.

Syntax: 

import { combineReducers } from "redux";
const rootReducer = combineReducers({
    books: BooksReducer,
    activeBook: ActiveBook
});
43. What is context API?
Context API is used to pass global variables anywhere in the code. It helps when there is a need for sharing state between a lot of nested components. It is light in weight and easier to use, to create a context just need to call React.createContext(). It eliminates the need to install other dependencies or third-party libraries like redux for state management. It has two properties Provider and Consumer. 

44. Explain provider and consumer in ContextAPI?
A provider is used to provide context to the whole application whereas a consumer consume the context provided by nearest provider. In other words The Provider acts as a parent it passes the state to its children whereas the Consumer uses the state that has been passed. 

45. Explain CORS in React?
In ReactJS, Cross-Origin Resource Sharing (CORS) refers to the method that allows you to make requests to the server deployed at a different domain. As a reference, if the frontend and backend are at two different domains, we need CORS there.

We can setup CORS evironment in frontend using two methods:

axios
fetch
46. What is axios and how to use it in React?
Axios, which is a popular library is mainly used to send asynchronous HTTP requests to REST endpoints. This library is very useful to perform CRUD operations.

This popular library is used to communicate with the backend. Axios supports the Promise API, native to JS ES6.
Using Axios we make API requests in our application. Once the request is made we get the data in Return, and then we use this data in our project. 
To install aixos package in react use the following command.

npm i axios
47. Write a program to create a counter with increment and decrement?

import React, { useState } from "react";

const App = () => {


    const [counter, setCounter] = useState(0)

    const handleClick1 = () => {


        setCounter(counter + 1)
    }

    const handleClick2 = () => {

        setCounter(counter - 1)
    }

    return (
        <div>
            <div>
                {counter}
            </div>
            <div className="buttons">
                <button onClick={handleClick1}>
                    Increment
                </button>
                <button onClick={handleClick2}>
                    Decrement
                </button>
            </div>
        </div>
    )
}

export default App
48. Explain why and how to update state of components using callback?
It is advised to use a callback-based approach to update the state using setState because it solves lots of bugs upfront that may occur in the future.We can use the following syntax to update state using callback

this.setState(st => {
    return(
        st.stateName1 = state1UpdatedValue,
        st.stateName2 = state2UpdatedValue
    )
})
49. What is React-Material UI?
React Material UI is an open-source React component library, offering prebuilt components for creating React applications. Developed by Google in 2014, it’s compatible with JavaScript frameworks like Angular.js and Vue.js. Renowned for its quality designs and easy customization, it’s favored by developers for rapid development.

50. What is flux architecture in redux?
Flux architecture in Redux is a design pattern used for managing application state in a unidirectional data flow. In this architecture, actions are dispatched to modify the store, which holds the entire application state. The store sends the updated state to the view (UI), and the cycle repeats when new actions are triggered. Redux follows this structure to ensure a predictable and maintainable state management system for large applications.

Conclusion
This React Interview Questions and Answers covers a wide range of topics, from basic concepts to advanced techniques. Whether you’re a beginner or an experienced developer, mastering these questions will enhance your readiness for React interviews and boost your confidence.

For further reading, check out our dedicated article on Advanced ReactJS Intermediate Interview Questions. Inside, you’ll discover over 20 questions with detailed answers.


React Interview Questions and Answers 2025

React Interview Questions and Answers – FAQ’s
What are the most commonly asked React interview questions for 2025?
Some common React interview questions for 2025 focus on hooks like useState and useEffect, React lifecycle methods, state management with Redux, and performance optimization techniques such as memoization and lazy loading. Expect questions about new features in React as well.


Why is React’s virtual DOM often discussed in interviews?
React’s virtual DOM is a key reason for its fast performance. It allows React to minimize actual DOM manipulations by comparing the virtual DOM with the real DOM and only updating the necessary parts. Interviewers ask about this to see if you understand how React optimizes rendering.


How can you optimize the performance of a React application?
To optimize a React app, you can use techniques such as memoization with React.memo and useMemo, lazy loading components with React.lazy, and using keys correctly in lists. Additionally, you can minimize re-renders by avoiding unnecessary state changes.


What are some advanced React interview questions you might face in 2025?
Advanced questions may include topics like React Fiber architecture, server-side rendering (SSR) with Next.js, building custom hooks, error boundaries, handling higher-order components (HOCs), and using React in microservices architectures.


What should you focus on when preparing for a React interview?
Focus on understanding hooks, lifecycle methods, state management, performance optimizations, error handling, and newer React features. It’s also important to work on real-world projects to demonstrate your knowledge in practical applications during the interview.



