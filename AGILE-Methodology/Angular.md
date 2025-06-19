Angular Concepts Explained (with Examples)
🔹 1. Modules
What: Organize code into cohesive blocks.

Syntax:

ts
Copy
Edit
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent]
})
export class AppModule {}
🔹 2. Components
What: Building blocks of the UI.

Example:

ts
Copy
Edit
@Component({
  selector: 'app-hello',
  template: `<h1>Hello {{name}}</h1>`
})
export class HelloComponent {
  name = 'Angular';
}
🔹 3. Templates
What: HTML with Angular syntax (interpolation, directives, etc.)

Example:

html
Copy
Edit
<div *ngIf="isVisible">Visible!</div>
🔹 4. Data Binding
Types:

Interpolation: {{ title }}

Property binding: [src]="imgUrl"

Event binding: (click)="handleClick()"

Two-way binding: [(ngModel)]="name"

🔹 5. Directives
Structural (*ngIf, *ngFor): Change DOM layout.

Attribute (e.g. ngClass, custom): Change appearance/behavior.

html
Copy
Edit
<div *ngFor="let user of users">{{ user.name }}</div>
🔹 6. Services & Dependency Injection
What: Business logic and reusable code.

Example:

ts
Copy
Edit
@Injectable()
export class UserService {
  getUsers() { return ['John', 'Jane']; }
}
🔹 7. Routing
What: Navigate between components/pages.

Example:

ts
Copy
Edit
const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent }
];
🔹 8. Forms
Template-Driven:

html
Copy
Edit
<form #f="ngForm">
  <input name="email" ngModel>
</form>
Reactive Forms:

ts
Copy
Edit
this.form = this.fb.group({ email: [''] });
🔹 9. Pipes
What: Transform data in templates.

Example:

html
Copy
Edit
{{ birthday | date:'longDate' }}
Custom Pipe:

ts
Copy
Edit
@Pipe({name: 'capitalize'})
export class CapitalizePipe implements PipeTransform {
  transform(value: string) { return value.toUpperCase(); }
}
🔹 10. Lifecycle Hooks
Key Hooks:

ngOnInit(): Called once component is initialized.

ngOnDestroy(): Cleanup on destroy.

ngOnChanges(): On input changes.

🔹 11. HTTP Client
What: Communicate with REST APIs.

Example:

ts
Copy
Edit
this.http.get<User[]>('/api/users')
  .subscribe(data => this.users = data);
🔹 12. State Management (Optional Advanced)
Services with Observables or use libraries like:

NgRx (Redux for Angular)

Akita

NgXs

🔹 13. Testing
Tools: Jasmine, Karma.

Example:

ts
Copy
Edit
it('should create component', () => {
  const fixture = TestBed.createComponent(AppComponent);
  expect(fixture.componentInstance).toBeTruthy();
});
🛠️ DEMO APP: User Management Dashboard
Features:
View list of users

Add/edit/delete user (Reactive Forms)

Navigation between pages

Fetch data from mock API (JSON-server)

Pipes for formatting

Custom directive to highlight active user

Lifecycle usage in child component

Components:
UserListComponent – Displays user list.

UserFormComponent – Add/edit user.

NavbarComponent – Navigation bar.

AppComponent – Root container.

Would you like:

A ready-to-run GitHub repo for the demo app?

A step-by-step Angular project setup guide?

Angular + Spring Boot full-stack version?

Sure! I'll give you a simple Angular + Spring Boot demo project example with the following:

Angular frontend that fetches a list of items from the backend.

Spring Boot backend that exposes a REST API to serve the list.

1. Spring Boot Backend (Java)
Step 1: Create a Spring Boot project (using Spring Initializr or your IDE)
Dependencies: Spring Web

Step 2: Create a simple REST Controller
java
Copy
Edit
package com.example.demo;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.Arrays;
import java.util.List;

@RestController
@CrossOrigin(origins = "http://localhost:4200")  // Allow Angular dev server CORS access
public class ItemController {

    @GetMapping("/api/items")
    public List<String> getItems() {
        return Arrays.asList("Item 1", "Item 2", "Item 3", "Item 4");
    }
}
Step 3: Run your Spring Boot app
Runs on default port 8080.

The endpoint is: http://localhost:8080/api/items

2. Angular Frontend
Step 1: Create a new Angular project
bash
Copy
Edit
ng new demo-angular-spring
cd demo-angular-spring
Step 2: Create a service to fetch items
Generate a service:

bash
Copy
Edit
ng generate service item
Edit src/app/item.service.ts:

typescript
Copy
Edit
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ItemService {

  private apiUrl = 'http://localhost:8080/api/items';

  constructor(private http: HttpClient) { }

  getItems(): Observable<string[]> {
    return this.http.get<string[]>(this.apiUrl);
  }
}
Step 3: Use the service in a component
Modify src/app/app.component.ts:

typescript
Copy
Edit
import { Component, OnInit } from '@angular/core';
import { ItemService } from './item.service';

@Component({
  selector: 'app-root',
  template: `
    <h1>Items List</h1>
    <ul>
      <li *ngFor="let item of items">{{ item }}</li>
    </ul>
  `
})
export class AppComponent implements OnInit {
  items: string[] = [];

  constructor(private itemService: ItemService) { }

  ngOnInit() {
    this.itemService.getItems().subscribe(data => {
      this.items = data;
    });
  }
}
Step 4: Enable HTTP Client Module
In src/app/app.module.ts, import HttpClientModule:

typescript
Copy
Edit
import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
Step 5: Run Angular app
bash
Copy
Edit
ng serve
Angular app runs on http://localhost:4200 and calls Spring Boot API on http://localhost:8080/api/items.

Summary
Spring Boot backend exposes GET /api/items returning JSON list.

Angular frontend calls this API and shows the list.
