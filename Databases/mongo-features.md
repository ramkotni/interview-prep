Here’s a comprehensive guide on MongoDB features, important queries, and a deep dive into the Aggregation Framework, including practical examples and use cases.

📘 MongoDB Overview
MongoDB is a NoSQL, document-oriented database that stores data as JSON-like documents (BSON). It is schema-less, scalable, and ideal for modern applications.

🔷 Key Features of MongoDB
Feature	Description
🧾 Document-Based	Data is stored in flexible, schema-less JSON-like documents
📁 Collections & Databases	Documents are grouped into collections; collections into databases
📈 Scalability	Horizontal scaling using sharding
🧠 Indexing	Supports various indexes (single, compound, text, geo, etc.)
⚙️ Aggregation Framework	Used for data processing and analytics
📤 Replication	High availability via replica sets
🔍 Full-Text Search	Built-in search with stemming, tokenizing, etc.
🧩 Flexible Schema	Allows varied fields in documents within the same collection
🔐 Security	Role-based access, encryption, audit logging
⚡ High Performance	In-memory processing and fast read/write performance

🔧 MongoDB Basic Queries
Let’s cover CRUD operations and common queries:

✅ Insert Documents
js
Copy
Edit
db.users.insertOne({ name: "Alice", age: 30 })
db.users.insertMany([{ name: "Bob" }, { name: "Carol" }])
✅ Find Documents
js
Copy
Edit
db.users.find() // All documents
db.users.find({ age: { $gt: 25 } }) // Age > 25
db.users.find({ name: /A/i }) // Regex (case-insensitive)
✅ Update Documents
js
Copy
Edit
db.users.updateOne({ name: "Alice" }, { $set: { age: 31 } })
db.users.updateMany({}, { $inc: { age: 1 } })
✅ Delete Documents
js
Copy
Edit
db.users.deleteOne({ name: "Bob" })
db.users.deleteMany({ age: { $lt: 20 } })
📊 Aggregation Framework (Powerful Analytics in MongoDB)
The aggregation framework processes documents through stages in a pipeline.

🔁 Common Stages
Stage	Purpose
$match	Filters documents (like WHERE)
$group	Groups and aggregates data
$project	Reshapes documents
$sort	Sorts data
$limit / $skip	Limits/skips records
$lookup	Joins with another collection
$unwind	Deconstructs arrays
$addFields	Adds new computed fields
$count	Counts matching docs
$facet	Run multiple aggregations in parallel

🧠 Example: Group by Department and Count Employees
js
Copy
Edit
db.employees.aggregate([
  { $group: { _id: "$department", count: { $sum: 1 } } }
])
🧠 Example: Filter, Sort, and Limit
js
Copy
Edit
db.products.aggregate([
  { $match: { price: { $gt: 100 } } },
  { $sort: { price: -1 } },
  { $limit: 5 }
])
🧠 Example: Lookup (Join)
js
Copy
Edit
db.orders.aggregate([
  {
    $lookup: {
      from: "customers",
      localField: "customerId",
      foreignField: "_id",
      as: "customerDetails"
    }
  }
])
🧠 Example: Unwind Array
js
Copy
Edit
db.posts.aggregate([
  { $unwind: "$tags" },
  { $group: { _id: "$tags", count: { $sum: 1 } } }
])
🧠 Example: Faceted Search
js
Copy
Edit
db.products.aggregate([
  {
    $facet: {
      priceBuckets: [
        { $bucket: {
          groupBy: "$price",
          boundaries: [0, 100, 500, 1000],
          default: "Other",
          output: { count: { $sum: 1 } }
        }}
      ],
      averagePrice: [
        { $group: { _id: null, avgPrice: { $avg: "$price" } } }
      ]
    }
  }
])
🧩 Advanced Features in Aggregation
Feature	Description	Example
$expr	Use expressions in queries	{ $match: { $expr: { $gt: ["$qty", 100] } } }
$cond	If-else logic	$cond: { if: ..., then: ..., else: ... }
$merge	Save output to collection	$merge: "summary_collection"
$setWindowFields	Analytics over partitions (MongoDB 5+)	Moving averages, ranks, etc.

🛠 Indexing in MongoDB
Types of Indexes:
Single Field: { name: 1 }

Compound: { name: 1, age: -1 }

Text Search: { description: "text" }

Geospatial: { location: "2dsphere" }

Hashed: { _id: "hashed" } (for sharding)

⚡ Performance Tips
Use indexes to speed up queries.

Use $match early in pipeline.

Limit fields returned via $project.

Avoid $unwind on large arrays unless needed.

Use profiler (db.setProfilingLevel(2)) to analyze performance.

🧠 Real-World Use Cases
Use Case	Feature Used
E-commerce analytics	$group, $sort, $match, $facet
Social media post tagging	$unwind, $group, full-text index
User authentication	$lookup (users ↔ sessions)
Location-based apps	2dsphere index + $geoNear
Inventory dashboard	$project, $match, $group, $merge

Would you like me to:

Generate a full MongoDB + Node.js demo app?

Provide cheatsheets (PDF) for aggregation and query syntax?

Build a visual MongoDB pipeline for any of your use cases?

Let me know and I’ll assist further!
