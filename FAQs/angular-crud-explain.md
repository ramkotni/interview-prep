 Objective:
Build a basic Angular app to manage a list of books with:

Add a new book

View all books

Update a book

Delete a book

🧱 Angular Components in a CRUD App
1. book.model.ts – 📦 Define the structure of a book
ts
Copy
Edit
export interface Book {
  id: number;
  title: string;
  author: string;
  price: number;
}
Think of this as a blueprint for what a book looks like in your app.

2. book.service.ts – 🔁 Make HTTP calls to the backend
ts
Copy
Edit
@Injectable({ providedIn: 'root' })
export class BookService {
  private apiUrl = 'http://localhost:8080/api/books';

  constructor(private http: HttpClient) {}

  getBooks(): Observable<Book[]> {
    return this.http.get<Book[]>(this.apiUrl);
  }

  addBook(book: Book): Observable<Book> {
    return this.http.post<Book>(this.apiUrl, book);
  }

  updateBook(book: Book): Observable<Book> {
    return this.http.put<Book>(`${this.apiUrl}/${book.id}`, book);
  }

  deleteBook(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
The service is where all API communication happens.

.get() → fetch all books

.post() → add new

.put() → update

.delete() → remove

3. book-list.component.ts – 📃 Show all books + actions
ts
Copy
Edit
export class BookListComponent implements OnInit {
  books: Book[] = [];

  constructor(private bookService: BookService) {}

  ngOnInit() {
    this.getBooks();
  }

  getBooks() {
    this.bookService.getBooks().subscribe({
      next: data => this.books = data,
      error: err => console.error('Error', err)
    });
  }

  deleteBook(id: number) {
    this.bookService.deleteBook(id).subscribe(() => this.getBooks());
  }
}
This component displays a table/list of books, and allows deleting them.

4. book-list.component.html – 🖥️ Show in HTML
html
Copy
Edit
<table>
  <tr *ngFor="let book of books">
    <td>{{ book.title }}</td>
    <td>{{ book.author }}</td>
    <td>{{ book.price }}</td>
    <td>
      <button (click)="editBook(book)">Edit</button>
      <button (click)="deleteBook(book.id)">Delete</button>
    </td>
  </tr>
</table>
This is the UI view of your book list.

5. book-form.component.ts – 📝 Add or edit a book
ts
Copy
Edit
export class BookFormComponent implements OnInit {
  @Input() book: Book = { id: 0, title: '', author: '', price: 0 };

  constructor(private bookService: BookService) {}

  ngOnInit() {}

  saveBook() {
    if (this.book.id) {
      this.bookService.updateBook(this.book).subscribe();
    } else {
      this.bookService.addBook(this.book).subscribe();
    }
  }
}
This is the form component used to create or update a book.

6. book-form.component.html – 📥 Form HTML
html
Copy
Edit
<form (ngSubmit)="saveBook()">
  <input type="text" [(ngModel)]="book.title" name="title" required>
  <input type="text" [(ngModel)]="book.author" name="author" required>
  <input type="number" [(ngModel)]="book.price" name="price" required>
  <button type="submit">Save</button>
</form>
This form uses two-way binding to bind input fields to the book model.

🔄 Full CRUD Flow Summary
Operation	Where it happens	Angular method used
Read	book-list.component.ts → getBooks()	http.get()
Create	book-form.component.ts → addBook()	http.post()
Update	book-form.component.ts → updateBook()	http.put()
Delete	book-list.component.ts → deleteBook()	http.delete()

🧠 How HTTP & Observables Work Here
BookService uses HttpClient to send HTTP requests.

The methods (getBooks, addBook) return Observables.

Components call subscribe() to listen for results.

Inside subscribe(), we handle success (next), failure (error), or completion (complete).

💡 Real-World Use Cases
Admin panel to manage products, books, or users.

Employee dashboard to manage HR records.

Student app to maintain subjects, grades, and profiles.

