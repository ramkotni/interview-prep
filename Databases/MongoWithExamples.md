MongoDB Overview
MongoDB is a NoSQL database that stores data in flexible, JSON-like documents (BSON - Binary JSON). It is a popular database used for its scalability, flexibility, and ease of use. MongoDB is schema-less, meaning you can store documents with different structures in the same collection.

Key Features of MongoDB:
Document-Oriented: Data is stored in JSON-like documents, making it easy to store and query.
Scalable: MongoDB can handle large amounts of data, and supports horizontal scaling through sharding.
Flexible Schema: Documents in a collection don't need to have the same structure.
High Performance: MongoDB provides indexing, in-memory processing, and other features that make it fast for both read and write operations.
Java MongoDB Connection
To connect to MongoDB from Java, you need the MongoDB Java driver. The most commonly used driver is the official mongo-java-driver. Below are the steps to set up the connection.

Step 1: Add MongoDB Dependencies to Your Project
If you're using Maven to manage your Java project dependencies, add the following to your pom.xml file:

<dependencies>
    <!-- MongoDB Java driver -->
    <dependency>
        <groupId>org.mongodb</groupId>
        <artifactId>mongo-java-driver</artifactId>
        <version>4.5.0</version>
    </dependency>
</dependencies>

For Gradle, you can add this dependency in your build.gradle file:

dependencies {
    implementation 'org.mongodb:mongo-java-driver:4.5.0'
}

Step 2: Establish Connection
Once the dependency is added, you can connect to MongoDB using the following steps:

Code for MongoDB Connection

import com.mongodb.client.MongoClients;
import com.mongodb.client.MongoClient;
import com.mongodb.client.MongoDatabase;

public class MongoDBConnection {
    public static void main(String[] args) {
        // Create a MongoClient instance and connect to the MongoDB server
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            // Connect to the database
            MongoDatabase database = mongoClient.getDatabase("testdb");  // "testdb" is the name of the database
            System.out.println("Connected to MongoDB successfully!");
        } catch (Exception e) {
            System.out.println("Failed to connect to MongoDB: " + e.getMessage());
        }
    }
}

MongoClient.create("mongodb://localhost:27017"): This creates a client that connects to MongoDB on localhost (default MongoDB port: 27017).
getDatabase("testdb"): This retrieves the database named testdb.
Step 3: CRUD Operations in MongoDB
After establishing a connection to the database, you can perform CRUD operations.

CRUD Operations in MongoDB Using Java
Create (Insert a document)
To insert data into a MongoDB collection:

import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.InsertOneModel;
import org.bson.Document;

public class MongoDBCRUD {
    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase database = mongoClient.getDatabase("testdb");
            MongoCollection<Document> collection = database.getCollection("users");

            // Create a new document (insert one)
            Document newUser = new Document("name", "John Doe")
                .append("age", 30)
                .append("email", "john@example.com");

            collection.insertOne(newUser);
            System.out.println("Document inserted successfully.");
        }
    }
}
Read (Query for documents)
To retrieve documents from a collection:

import com.mongodb.client.MongoCollection;
import org.bson.Document;
import com.mongodb.client.MongoCursor;

public class MongoDBCRUD {
    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase database = mongoClient.getDatabase("testdb");
            MongoCollection<Document> collection = database.getCollection("users");

            // Query all documents in the collection
            MongoCursor<Document> cursor = collection.find().iterator();

            while (cursor.hasNext()) {
                System.out.println(cursor.next().toJson());
            }
        }
    }
}

Update (Modify a document)
To update a document in the collection:

import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import com.mongodb.client.model.Updates;
import org.bson.Document;

public class MongoDBCRUD {
    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase database = mongoClient.getDatabase("testdb");
            MongoCollection<Document> collection = database.getCollection("users");

            // Update a document
            collection.updateOne(
                Filters.eq("name", "John Doe"),   // Filter: find the document where name is "John Doe"
                Updates.set("age", 31)            // Update: set the age to 31
            );

            System.out.println("Document updated successfully.");
        }
    }
}

Delete (Remove a document)
To delete a document:

import com.mongodb.client.MongoCollection;
import com.mongodb.client.model.Filters;
import org.bson.Document;

public class MongoDBCRUD {
    public static void main(String[] args) {
        try (MongoClient mongoClient = MongoClients.create("mongodb://localhost:27017")) {
            MongoDatabase database = mongoClient.getDatabase("testdb");
            MongoCollection<Document> collection = database.getCollection("users");

            // Delete a document where the name is "John Doe"
            collection.deleteOne(Filters.eq("name", "John Doe"));

            System.out.println("Document deleted successfully.");
        }
    }
}

Explanation of CRUD Operations:
Insert: The insertOne() method is used to add a single document to a collection. We create a Document object that holds key-value pairs, and use insertOne() to insert it.
Find (Read): The find() method retrieves documents from the collection. You can use queries to filter results. The iterator() allows you to loop through the results.
Update: The updateOne() method is used to modify a single document. The Filters.eq() method is used to specify the query criteria, and Updates.set() is used to specify the update operation.
Delete: The deleteOne() method deletes a single document matching the criteria.
Conclusion
To connect MongoDB to Java, you need the official MongoDB Java driver. Once the connection is established, you can perform CRUD operations using MongoDB's Java API. The process involves connecting to the MongoDB server, selecting the database and collection, and then performing the desired operation (insert, find, update, delete).

These basic operations are the foundation of interacting with MongoDB in Java. Depending on the use case, you can extend this logic by adding more complex queries, aggregation pipelines, and handling errors and performance optimization.
