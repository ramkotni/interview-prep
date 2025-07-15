🔷 1. Components
✅ What:
The basic building block of Angular applications. Each view is a component.

🧠 Example:
ts
Copy
Edit
@Component({
  selector: 'app-user',
  template: `<h2>{{ name }}</h2>`
})
export class UserComponent {
  name = 'John Doe';
}
💼 Use Case:
Create reusable UI blocks like user cards, headers, or login forms.

🔷 2. Modules
✅ What:
A logical grouping of components, services, pipes, etc.

🧠 Example:
ts
Copy
Edit
@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule],
  bootstrap: [AppComponent]
})
export class AppModule {}
💼 Use Case:
Split app features like UserModule, AdminModule, etc., for lazy loading and maintainability.

🔷 3. Templates and Data Binding
✅ Types:
Interpolation: {{ value }}

Property Binding: [src]="imgUrl"

Event Binding: (click)="submit()"

Two-Way Binding: [(ngModel)]="username"

🧠 Example:
html
Copy
Edit
<input [(ngModel)]="name">
<p>Hello, {{ name }}</p>
💼 Use Case:
Form inputs, showing dynamic data in UI.

🔷 4. Directives
✅ What:
Used to manipulate DOM.

🧠 Types:
Structural: *ngIf, *ngFor

Attribute: ngClass, ngStyle

🧠 Example:
html
Copy
Edit
<div *ngIf="isLoggedIn">Welcome</div>
<ul>
  <li *ngFor="let item of items">{{ item }}</li>
</ul>
💼 Use Case:
Conditionally show elements, loop over arrays, dynamic styling.

🔷 5. Services and Dependency Injection
✅ What:
Shared logic, reusable APIs, injected into components.

🧠 Example:
ts
Copy
Edit
@Injectable()
export class AuthService {
  login() { return true; }
}

@Component({...})
export class LoginComponent {
  constructor(private auth: AuthService) {}
}
💼 Use Case:
Login services, data APIs, caching logic.

🔷 6. Routing and Navigation
✅ What:
Single Page Application (SPA) routing.

🧠 Example:
ts
Copy
Edit
const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'about', component: AboutComponent }
];
html
Copy
Edit
<a routerLink="/home">Home</a>
<router-outlet></router-outlet>
💼 Use Case:
Navigate between pages like dashboard, profile, etc., without reloading the page.

🔷 7. Forms
✅ Types:
Template-driven

Reactive forms

🧠 Template-driven Example:
html
Copy
Edit
<form #f="ngForm" (ngSubmit)="submit(f)">
  <input name="email" ngModel required>
</form>
🧠 Reactive Example:
ts
Copy
Edit
this.form = new FormGroup({
  email: new FormControl('', Validators.required)
});
💼 Use Case:
User input, form validations (login, registration, surveys).

🔷 8. Pipes
✅ What:
Transform data in templates.

🧠 Built-in Example:
html
Copy
Edit
{{ price | currency }}
{{ today | date:'longDate' }}
🧠 Custom Pipe:
ts
Copy
Edit
@Pipe({name: 'capitalize'})
export class CapitalizePipe {
  transform(value: string): string {
    return value.charAt(0).toUpperCase() + value.slice(1);
  }
}
💼 Use Case:
Format data in the UI like currency, dates, and text transformation.

🔷 9. Lifecycle Hooks
✅ Common Hooks:
ngOnInit(): After component initialized.

ngOnChanges(): On input change.

ngOnDestroy(): Cleanup.

🧠 Example:
ts
Copy
Edit
ngOnInit() {
  this.loadData();
}
💼 Use Case:
Fetch data after component loads, unsubscribe to avoid memory leaks.

🔷 10. HTTP Client (API Calls)
✅ What:
Make REST API calls using Angular's HttpClient.

🧠 Example:
ts
Copy
Edit
this.http.get('https://api.example.com/users').subscribe(data => {
  this.users = data;
});
💼 Use Case:
Communicate with backend, fetch/post data.

🔷 11. Guards (Route Protection)
✅ What:
Prevent access to routes based on logic (auth, roles, etc.)

🧠 Example:
ts
Copy
Edit
canActivate(): boolean {
  return this.authService.isLoggedIn();
}
💼 Use Case:
Protect dashboard, admin routes, or routes requiring login.

🔷 12. Interceptors
✅ What:
Intercept HTTP requests and responses.

🧠 Example:
ts
Copy
Edit
intercept(req: HttpRequest<any>, next: HttpHandler) {
  const cloned = req.clone({ headers: req.headers.set('Auth', 'token') });
  return next.handle(cloned);
}
💼 Use Case:
Attach JWT tokens, show loading spinners, handle errors globally.

🔷 13. Lazy Loading
✅ What:
Load feature modules only when needed.

🧠 Example:
ts
Copy
Edit
{ path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) }
💼 Use Case:
Boost performance, especially in large apps.

🔷 14. State Management (NgRx or Services)
✅ What:
Manage complex state across components.

🧠 Use case:
Use service-based state for small apps.

Use NgRx for large-scale apps with centralized state.

🔷 15. Animations
✅ What:
Add motion to elements.

🧠 Example:
ts
Copy
Edit
animations: [
  trigger('fade', [
    transition(':enter', [style({ opacity: 0 }), animate(500, style({ opacity: 1 }))])
  ])
]
💼 Use Case:
Fade in modals, slide transitions, button feedback.

🔷 16. Standalone Components (Angular 14+)
✅ What:
Components without modules.

🧠 Example:
ts
Copy
Edit
@Component({
  standalone: true,
  imports: [CommonModule],
  selector: 'app-profile',
  templateUrl: './profile.component.html'
})
export class ProfileComponent {}
💼 Use Case:
Simplify modularity for small, reusable components or libraries.

🔷 17. Signals (Angular 16+)
✅ What:
Fine-grained reactivity (alternative to RxJS in some cases)

🧠 Example:
ts
Copy
Edit
import { signal } from '@angular/core';

const counter = signal(0);
counter.set(counter() + 1);
💼 Use Case:
Reactive state without RxJS for local component logic.

Want More?
Let me know if you’d like:

A demo Angular app using all features ✅

Interview questions based on these features 🎯

Angular vs React feature comparison 🆚

