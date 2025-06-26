MongoDB Features:
Document-Oriented: MongoDB stores data in flexible, JSON-like documents, making it easy to model complex data structures.
Schema Flexibility: No fixed schema; fields can vary between documents, allowing for dynamic and evolving data models.
Scalability: Supports horizontal scaling through sharding, distributing data across multiple servers.
Indexing: Provides powerful indexing options to optimize query performance.
Aggregation Framework: Allows advanced data processing and transformation using pipelines.
Replication: Ensures high availability with replica sets, providing data redundancy.
ACID Transactions: Supports multi-document ACID transactions for reliable operations.
Geospatial Queries: Enables location-based queries with geospatial indexing.
High Performance: Optimized for read and write operations, suitable for real-time applications.
Rich Query Language: Supports a wide range of queries, including filtering, sorting, and projections.
<hr></hr>
Demo Project: MongoDB with Node.js
Objective: Build a simple REST API to manage a "Books" collection.
Steps:
Setup MongoDB:


Install MongoDB and start the server.
Create a database named library and a collection named books.
Initialize Node.js Project:


mkdir mongodb-demo
cd mongodb-demo
npm init -y
npm install express mongoose body-parser
Create the Project Structure:


mongodb-demo/
├── app.js
├── models/
│   └── book.js
└── routes/
    └── books.js
Code Implementation:


app.js: Main entry point.


const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const booksRoutes = require('./routes/books');

const app = express();
app.use(bodyParser.json());

mongoose.connect('mongodb://localhost:27017/library', {
  useNewUrlParser: true,
  useUnifiedTopology: true,
}).then(() => console.log('MongoDB connected'))
  .catch(err => console.error(err));

app.use('/api/books', booksRoutes);

app.listen(3000, () => console.log('Server running on port 3000'));
models/book.js: Book schema.


const mongoose = require('mongoose');

const bookSchema = new mongoose.Schema({
  title: { type: String, required: true },
  author: { type: String, required: true },
  publishedYear: { type: Number },
  genre: { type: String },
});

module.exports = mongoose.model('Book', bookSchema);
routes/books.js: CRUD routes for books.


const express = require('express');
const Book = require('../models/book');
const router = express.Router();

// Create a new book
router.post('/', async (req, res) => {
  try {
    const book = new Book(req.body);
    await book.save();
    res.status(201).json(book);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Get all books
router.get('/', async (req, res) => {
  try {
    const books = await Book.find();
    res.json(books);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get a book by ID
router.get('/:id', async (req, res) => {
  try {
    const book = await Book.findById(req.params.id);
    if (!book) return res.status(404).json({ error: 'Book not found' });
    res.json(book);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update a book
router.put('/:id', async (req, res) => {
  try {
    const book = await Book.findByIdAndUpdate(req.params.id, req.body, { new: true });
    if (!book) return res.status(404).json({ error: 'Book not found' });
    res.json(book);
  } catch (err) {
    res.status(400).json({ error: err.message });
  }
});

// Delete a book
router.delete('/:id', async (req, res) => {
  try {
    const book = await Book.findByIdAndDelete(req.params.id);
    if (!book) return res.status(404).json({ error: 'Book not found' });
    res.json({ message: 'Book deleted' });
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

module.exports = router;
Run the Application:


node app.js
Test the API: Use tools like Postman or curl to test the endpoints:
POST /api/books: Add a new book.
GET /api/books: Retrieve all books.
GET /api/books/:id: Retrieve a book by ID.
PUT /api/books/:id: Update a book.
DELETE /api/books/:id: Delete a book

MongoDB Interview Questions and Answers
1. What is MongoDB?
MongoDB is a NoSQL, document-oriented database that stores data in JSON-like flexible documents. It is designed for scalability, high performance, and ease of development.

<hr></hr>
2. What are the key features of MongoDB?
Document-Oriented: Stores data in BSON (Binary JSON) format.
Schema Flexibility: No fixed schema; fields can vary between documents.
Scalability: Supports horizontal scaling using sharding.
Indexing: Provides powerful indexing for faster query execution.
Replication: Ensures high availability with replica sets.
Aggregation Framework: Allows advanced data processing and transformation.
Geospatial Queries: Supports location-based queries.
<hr></hr>
3. What is a replica set in MongoDB?
A replica set is a group of MongoDB servers that maintain the same data set, providing redundancy and high availability. It consists of:


Primary: Handles all write operations.
Secondary: Replicates data from the primary.
Arbiter: Participates in elections but does not store data.
<hr></hr>
4. What is sharding in MongoDB?
Sharding is a method of distributing data across multiple servers to handle large datasets and high throughput. MongoDB uses a shard key to partition data into chunks and distribute them across shards.

<hr></hr>
5. What is the difference between MongoDB and a relational database?
Feature
MongoDB
Relational Database
Data Model
Document-Oriented
Table-Based
Schema
Flexible
Fixed
Joins
Not supported (use embedding or referencing)
Supported
Scalability
Horizontal (Sharding)
Vertical
Transactions
Limited (multi-document ACID supported)
Fully Supported
<hr></hr>
6. What is the Aggregation Framework in MongoDB?
The Aggregation Framework processes data and performs operations like filtering, grouping, and sorting. It uses a pipeline of stages such as $match, $group, $sort, $project, etc.

Example:
db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
]);

db.orders.aggregate([
  { $match: { status: "completed" } },
  { $group: { _id: "$customerId", total: { $sum: "$amount" } } },
  { $sort: { total: -1 } }
]);

db.users.updateOne({ _id: 1 }, { $set: { age: 30 }, $unset: { address: "" } });

<hr></hr>
12. What is the difference between deleteOne() and deleteMany()?
deleteOne(): Deletes the first document matching the query.
deleteMany(): Deletes all documents matching the query.
<hr></hr>
13. What is the purpose of the ObjectId in MongoDB?
ObjectId is a unique identifier for documents. It contains:


Timestamp
Machine ID
Process ID
Counter
<hr></hr>
14. How do you perform a backup and restore in MongoDB?
Backup: Use mongodump to create a backup.
mongodump --db database_name --out /backup/path
Restore: Use mongorestore to restore data.
mongorestore --db database_name /backup/path
<hr></hr>
15. What is the difference between embedded documents and referenced documents?
Embedded Documents: Store related data within the same document.
Referenced Documents: Store related data in separate documents and link them using references.
<hr></hr> These are some common MongoDB interview questions and answers to help you prepare.
