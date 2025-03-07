# Angular Interview Questions and Answers

## 1. What is Angular?

### **Answer:**
Angular is a platform and framework for building single-page client applications using HTML and TypeScript. It is developed and maintained by Google and is widely used for developing dynamic, responsive web applications. Angular uses a component-based architecture and offers features like two-way data binding, dependency injection, modularization, and routing.

---

## 2. What are Components in Angular?

### **Answer:**
In Angular, a component is a building block of the application that controls a part of the user interface. Each component has:
- **Template**: Defines the HTML structure for the component’s view.
- **Class**: Contains the logic and data for the component, written in TypeScript.
- **Metadata**: Decorators like `@Component` that provide configuration for the component (e.g., template, selector).
- **Styles**: The CSS that applies to the component.

Components are responsible for handling user interactions and rendering dynamic content in the view.

---

## 3. What is Data Binding in Angular?

### **Answer:**
Data binding in Angular is the mechanism that allows communication between the component and its template. There are four types of data binding:

1. **Interpolation**: `{{ value }}` — used to bind data from the component to the template.
2. **Property Binding**: `[property]="value"` — binds an element's property to a component property.
3. **Event Binding**: `(event)="method()"` — binds events like click, change, etc., to component methods.
4. **Two-way Binding**: `[(ngModel)]="value"` — binds both the property and event, allowing the component to synchronize with the view and vice versa.

---

## 4. What is Dependency Injection (DI) in Angular?

### **Answer:**
Dependency Injection (DI) is a design pattern used in Angular to manage the dependencies of services and components. It allows objects (like services) to be injected into components or other services rather than creating instances directly within the components. DI helps in writing modular, reusable, and testable code.

- **Injectable Services**: Use `@Injectable` decorator to mark a class as injectable.
- **Providers**: Used to define how services are provided to the components.

---

## 5. What is the difference between `ngOnInit()` and `constructor()` in Angular?

### **Answer:**
- **constructor()**: The constructor is a special method in a class used for initialization. It is called when the component is created but before the Angular lifecycle hooks are called. It is typically used for dependency injection.
  
- **ngOnInit()**: This is a lifecycle hook in Angular, called after the constructor and once Angular has initialized the component’s inputs. It is used for component initialization, such as fetching data from APIs or setting up other logic.

---

## 6. What is Routing in Angular?

### **Answer:**
Routing in Angular is a mechanism that allows navigation between different views or pages within a single-page application (SPA). Angular’s Router helps in defining routes, navigating between them, and protecting routes (e.g., authentication).

- **RouterModule**: A module that needs to be imported into the application to enable routing.
- **Routes**: Defines the paths and components to be rendered for each route.
- **RouterLink**: Directive used in templates to link to routes.
- **ActivatedRoute**: Provides access to information about a route and its parameters.

---

## 7. What is Angular CLI?

### **Answer:**
Angular CLI (Command Line Interface) is a tool to automate common Angular development tasks like creating components, services, modules, building, and testing the application. It simplifies the process of creating and managing Angular projects and automates the workflow.

Example commands:
- `ng new my-app`: Creates a new Angular project.
- `ng serve`: Builds the app and starts the development server.
- `ng generate component my-component`: Generates a new component.
- `ng test`: Runs unit tests.

---

## 8. What is the Angular Lifecycle Hooks?

### **Answer:**
Angular Lifecycle Hooks are special methods that are called at different stages of a component’s life. Some common lifecycle hooks are:

1. **ngOnChanges()**: Called when an input property of a component changes.
2. **ngOnInit()**: Called once, after the first `ngOnChanges()`.
3. **ngDoCheck()**: Called during every change detection run.
4. **ngAfterContentInit()**: Called after the component's content is projected into the view.
5. **ngAfterViewInit()**: Called after the component's view has been initialized.
6. **ngOnDestroy()**: Called just before the component is destroyed, useful for cleanup.

---

## 9. What is RxJS in Angular?

### **Answer:**
RxJS (Reactive Extensions for JavaScript) is a library for handling asynchronous programming using observable sequences. It is extensively used in Angular for managing asynchronous data streams like HTTP requests, events, and user inputs.

Key RxJS operators:
- `map()`: Transforms emitted values.
- `filter()`: Filters emitted values based on a condition.
- `mergeMap()`: Flattens the emitted observables.
- `switchMap()`: Cancels the previous observable and subscribes to a new one.

---

## 10. What is an Angular Module?

### **Answer:**
An Angular Module (`@NgModule`) is a container for a related set of components, services, pipes, and other modules. It helps organize and group related code, making the application modular.

- **Declarations**: Defines the components, directives, and pipes that belong to the module.
- **Imports**: Imports other Angular modules that are needed by the components in this module.
- **Providers**: Defines the services that are available throughout the module.
- **Bootstrap**: Specifies the root component to be bootstrapped when the application starts.

---

## 11. What is a Pipe in Angular?

### **Answer:**
A Pipe in Angular is a way to transform data for display in the template. Angular has several built-in pipes like `date`, `uppercase`, `lowercase`, `currency`, etc. You can also create custom pipes to handle custom transformations.

Example of a custom pipe:
```typescript
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'reverse'
})
export class ReversePipe implements PipeTransform {
  transform(value: string): string {
    return value.split('').reverse().join('');
  }
}


12. How can you optimize performance in Angular applications?
Answer:
Here are some strategies to optimize Angular applications:

Lazy Loading: Load modules only when needed to reduce the initial loading time.
Change Detection Strategy: Use OnPush change detection to minimize unnecessary checks.
Track By in ngFor: Use trackBy to optimize the rendering of lists by tracking items uniquely.
AOT Compilation: Use Ahead-of-Time (AOT) compilation to reduce the bundle size and improve app performance.
Service Workers: Use service workers for caching and offline support to improve performance.
13. What are Guards in Angular?
Answer:
Guards in Angular are used to control access to routes. They can prevent navigation to a route based on certain conditions like user authentication or roles.

Types of guards:

CanActivate: Decides if a route can be activated.
CanActivateChild: Decides if a child route can be activated.
CanDeactivate: Decides if a route can be deactivated.
Resolve: Resolves data before a route is activated.
CanLoad: Decides if a module can be loaded.
14. What is the difference between ngIf and ngFor in Angular?
Answer:
ngIf: A structural directive used to conditionally include or remove an element from the DOM based on a given condition.

html
Copy
<div *ngIf="isVisible">This will be shown if isVisible is true.</div>
ngFor: A structural directive used to iterate over a collection (array or list) and display an element for each item.

html
Copy
<div *ngFor="let item of items">{{ item.name }}</div>
15. What is the role of @Injectable() decorator in Angular?
Answer:
The @Injectable() decorator is used to mark a class as available for dependency injection. It tells Angular that the class can be injected into other classes, like components or services. The @Injectable() decorator is typically used in services.

Example:

typescript
Copy
@Injectable({
  providedIn: 'root'
})
export class MyService {
  constructor() { }
}


5. What is a component in Angular?
Answer:
A component in Angular is a basic unit of the user interface. It is a TypeScript class that contains:

Template: Defines the HTML view.
Class: Contains the logic, properties, and methods.
Decorator: @Component provides metadata like the selector, template, and styles.
Styles: Defines CSS that applies to the component.
6. What is the role of @NgModule?
Answer:
@NgModule is a decorator that defines a module in Angular. It helps to organize related components, directives, pipes, and services into cohesive blocks. It includes:

Declarations: Defines components, directives, and pipes.
Imports: Imports other modules.
Providers: Specifies services that will be available in the module.
Bootstrap: Specifies the root component to launch the application.
7. What is Dependency Injection in Angular?
Answer:
Dependency Injection (DI) is a design pattern in Angular used to manage the services and their dependencies. It allows Angular to automatically provide an instance of a service to the component or service that requires it. DI makes the application more modular and testable.

8. What is @Injectable() in Angular?
Answer:
@Injectable() is a decorator used to define a service or class as available for dependency injection. It marks a class as injectable, making it available for Angular's DI system. By default, services are provided in the root module unless specified otherwise.

Example:

typescript
Copy
@Injectable({
  providedIn: 'root'
})
export class MyService {
  constructor() { }
}
9. What is two-way data binding in Angular?
Answer:
Two-way data binding in Angular refers to the synchronization of data between the component class and the view (UI). Any change in the model updates the view, and any change in the view is reflected in the model. It is achieved using [(ngModel)].

Example:

html
Copy
<input [(ngModel)]="name">
<p>{{ name }}</p>
10. What are Angular lifecycle hooks?
Answer:
Angular lifecycle hooks are methods that are called during different stages of a component's life. Common lifecycle hooks include:

ngOnInit: Called once after the component is initialized.
ngOnChanges: Called when input properties change.
ngDoCheck: Called during every change detection cycle.
ngAfterViewInit: Called after the component's view is initialized.
ngOnDestroy: Called just before the component is destroyed.
11. What is ngIf in Angular?
Answer:
ngIf is a structural directive used to conditionally include or remove an element from the DOM. It is typically used with a condition that is evaluated at runtime.

Example:

html
Copy
<div *ngIf="isVisible">This element is visible if isVisible is true</div>
12. What are Directives in Angular?
Answer:
Directives are special markers on DOM elements that allow you to extend HTML functionality. There are three types of directives:

Structural Directives: Modify the structure of the DOM (e.g., ngIf, ngFor).
Attribute Directives: Change the appearance or behavior of an element (e.g., ngClass, ngStyle).
Component Directives: Directives that define a view and its logic (i.e., Angular components).
13. What is the purpose of @ViewChild() in Angular?
Answer:
@ViewChild() is a decorator used to get a reference to a DOM element, directive, or child component in the template. It allows a parent component to directly access the properties and methods of its child components.

Example:

typescript
Copy
@ViewChild('myDiv') divElement: ElementRef;

ngAfterViewInit() {
  console.log(this.divElement.nativeElement);
}
14. What are Forms in Angular?
Answer:
Angular provides two types of forms:

Template-driven forms: Forms defined and managed in the template. Simple to use for basic forms.
Reactive forms: Forms defined and managed in the component class. More scalable and flexible for complex forms and validation.
15. What is ngOnInit() in Angular?
Answer:
ngOnInit() is a lifecycle hook in Angular that is called after Angular has initialized all the data-bound properties of a component. It is commonly used for initialization tasks like fetching data from APIs.

Example:

typescript
Copy
ngOnInit() {
  this.fetchData();
}
16. What is Lazy Loading in Angular?
Answer:
Lazy loading is a design pattern that helps improve the application's performance by loading modules only when needed, instead of loading all modules upfront. This reduces the initial load time of the application.

Example:

typescript
Copy
const routes: Routes = [
  { path: 'feature', loadChildren: () => import('./feature/feature.module').then(m => m.FeatureModule) }
];
17. What is Angular Router?
Answer:
Angular Router is a library that allows for navigation between views or pages in a single-page application (SPA). It enables route configuration, navigation, and route guards.

Key features include:

Defining routes.
Navigation with routerLink.
Route guards for protecting routes.
Route parameters for passing data between components.
18. What are the different types of binding in Angular?
Answer:
In Angular, there are four types of binding:

Interpolation: {{ value }} for binding data to the view.
Property Binding: [property]="value" for binding an element property to a component property.
Event Binding: (event)="method()" for binding an event to a component method.
Two-way Binding: [(ngModel)]="value" for syncing data between the model and the view.
19. What is a Service in Angular?
Answer:
A service is a class in Angular that provides business logic, data storage, and shared functionality that can be injected into components or other services. Services are typically used to interact with external APIs, manage state, and encapsulate reusable logic.

20. How can you handle HTTP requests in Angular?
Answer:
Angular provides the HttpClient module to make HTTP requests. It supports methods like GET, POST, PUT, DELETE for interacting with REST APIs.

Example of a GET request:

typescript
Copy
import { HttpClient } from '@angular/common/http';

constructor(private http: HttpClient) {}

getData() {
  this.http.get('https://api.example.com/data').subscribe(response => {
    console.log(response);
  });
}
21. What is the difference between ngModel and formControl?
Answer:
ngModel: Used for template-driven forms and supports two-way data binding.
formControl: Used for reactive forms to bind a control to an input element and track its state and validity.
22. What are Guards in Angular?
Answer:
Guards in Angular are used to protect routes and control access based on certain conditions. Common types of guards are:

CanActivate: Checks if a route can be activated.
CanActivateChild: Checks if a child route can be activated.
CanDeactivate: Checks if a route can be deactivated.
CanLoad: Checks if a lazy-loaded module can be loaded.
23. What is a Pipe in Angular?
Answer:
A pipe is a way to transform data in the view template. Angular provides built-in pipes like date, uppercase, currency, etc. You can also create custom pipes to perform specific transformations.

Example:

typescript
Copy
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'reverse'
})
export class ReversePipe implements PipeTransform {
  transform(value: string): string {
    return value.split('').reverse().join('');
  }
}
24. What is @Input() and @Output() in Angular?
Answer:
@Input(): A decorator used to pass data from a parent component to a child component.
@Output(): A decorator used to emit events from a child component to a parent component.
Example:

typescript
Copy
// Parent Component
<app-child [childInput]="parentData" (childOutput)="parentMethod($event)"></app-child>

// Child Component
@Input() childInput: string;
@Output() childOutput = new EventEmitter<string>();
25. How can you optimize Angular applications?
Answer:
To optimize Angular applications:

Lazy Loading: Load modules only when needed.
OnPush Change Detection: Use OnPush strategy to reduce unnecessary change detection.
Track By: Use trackBy with ngFor to optimize list rendering.
AOT Compilation: Use Ahead-of-Time (AOT) compilation for faster startup and smaller bundles.
Service Workers: Use service workers for caching and offline functionality.
26. What is ngOnChanges() in Angular?
Answer:
ngOnChanges() is a lifecycle hook that is called whenever an input property of the component changes. It provides the previous and current values of the input property.

Example:

typescript
Copy
ngOnChanges(changes: SimpleChanges) {
  console.log(changes);
}
27. What is a module in Angular?
Answer:
A module in Angular is a cohesive block of code that encapsulates related functionality. It includes components, services, pipes, and other modules. Every Angular application has at least one module: the root module (typically AppModule).

28. What is the purpose of ngOnDestroy() in Angular?
Answer:
ngOnDestroy() is a lifecycle hook called just before Angular destroys a component. It is used for cleanup tasks like unsubscribing from observables, detaching event listeners, and releasing resources.

29. What are Observables in Angular?
Answer:
Observables are a core concept in Angular and RxJS. They represent asynchronous data streams that can be observed and subscribed to. Observables are used to handle events, HTTP requests, and other asynchronous operations.

30. How do you perform form validation in Angular?
Answer:
Angular provides both template-driven and reactive forms for validation.

Template-driven forms: Use directives like ngModel, required, minlength, maxlength, etc.
Reactive forms: Use FormControl and Validators to apply validation rules.
Example:

typescript
Copy
const username = new FormControl('', [Validators.required, Validators.minLength(4)]);
31. How do you create a service in Angular?
Answer:
To create a service in Angular, use the Angular CLI:

bash
Copy
ng generate service my-service
Example service:

typescript
Copy
@Injectable({
  providedIn: 'root'
})
export class MyService {
  constructor() {}
}

# Angular Interview Questions and Answers

| **Question**                                                                 | **Answer**                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. What is Angular?**                                                        | Angular is a platform and framework for building single-page applications using HTML and TypeScript. Developed by Google, it follows a component-based architecture.                                                                                                                            |
| **2. What are the key features of Angular?**                                   | 1. Component-based architecture<br> 2. Two-way data binding<br> 3. Dependency Injection (DI)<br> 4. RxJS for async operations<br> 5. Routing for navigation<br> 6. Directives<br> 7. Forms handling<br> 8. HTTP Client<br> 9. Angular CLI<br> 10. AOT Compilation.                                 |
| **3. What is the difference between AngularJS and Angular?**                   | AngularJS is built with JavaScript, whereas Angular (2+) is built with TypeScript. Angular has a more robust architecture, better performance, mobile support, and enhanced dependency injection.                                                                                              |
| **4. What is the use of `ngFor` in Angular?**                                  | `ngFor` is a structural directive that repeats a set of elements for each item in a collection.                                                                                                                                                                                                |
| **5. What is a component in Angular?**                                         | A component is the fundamental building block of Angular applications, consisting of a class (with logic), a template (HTML), and a decorator (`@Component`).                                                                                                                                |
| **6. What is the role of `@NgModule`?**                                        | `@NgModule` organizes components, directives, pipes, and services into cohesive blocks. It includes declarations, imports, providers, and bootstrap information for Angular modules.                                                                                                          |
| **7. What is Dependency Injection in Angular?**                               | DI is a design pattern where Angular automatically provides services or objects that a class requires. It helps with decoupling and promotes modularity in Angular apps.                                                                                                                        |
| **8. What is `@Injectable()` in Angular?**                                     | `@Injectable()` decorator marks a class as available for dependency injection. It provides services across components or other services.                                                                                                                                                         |
| **9. What is two-way data binding in Angular?**                                | Two-way data binding synchronizes data between the component and the view. Changes in the model update the view and vice-versa. It’s achieved using `[(ngModel)]`.                                                                                                                             |
| **10. What are Angular lifecycle hooks?**                                      | Lifecycle hooks like `ngOnInit`, `ngOnChanges`, `ngOnDestroy`, etc., are methods called at different stages of a component's lifecycle. They allow you to handle logic during initialization, change detection, and cleanup.                                                                        |
| **11. What is `ngIf` in Angular?**                                             | `ngIf` is a structural directive that conditionally includes or removes an HTML element from the DOM based on an expression's result.                                                                                                                                                          |
| **12. What are Directives in Angular?**                                        | Directives are used to extend HTML functionality. They are of three types: Structural (`ngIf`, `ngFor`), Attribute (`ngClass`, `ngStyle`), and Component directives (components themselves).                                                                                                      |
| **13. What is the purpose of `@ViewChild()` in Angular?**                      | `@ViewChild()` allows a parent component to access and manipulate child components, directives, or DOM elements.                                                                                                                                                                                 |
| **14. What are Forms in Angular?**                                             | Forms in Angular can be handled in two ways: Template-driven forms (simple, HTML-centric) and Reactive forms (dynamic and complex, managed in the component class).                                                                                                                            |
| **15. What is `ngOnInit()` in Angular?**                                       | `ngOnInit()` is a lifecycle hook called once the component is initialized, often used for initialization logic such as fetching data from APIs.                                                                                                                                                  |
| **16. What is Lazy Loading in Angular?**                                       | Lazy loading is a design pattern where modules are loaded only when needed, improving application performance.                                                                                                                                                                                 |
| **17. What is Angular Router?**                                                | Angular Router enables navigation within a single-page application. It allows the management of URL paths and routes, making it easy to navigate between components.                                                                                                                            |
| **18. What are the different types of binding in Angular?**                    | 1. Interpolation: `{{ value }}`<br>2. Property Binding: `[property]="value"`<br>3. Event Binding: `(event)="method()"`<br>4. Two-way Binding: `[(ngModel)]="value"`                                                                                                                             |
| **19. What is a Service in Angular?**                                          | A service is a class that provides logic, data, or functionalities to components and other services. Services are typically used to interact with APIs, manage state, and encapsulate reusable logic.                                                                                              |
| **20. How can you handle HTTP requests in Angular?**                           | Angular uses the `HttpClient` module for making HTTP requests, like `GET`, `POST`, `PUT`, and `DELETE`.                                                                                                                                                                                           |
| **21. What is the difference between `ngModel` and `formControl`?**             | `ngModel` is used in template-driven forms for two-way data binding, while `formControl` is used in reactive forms to bind form controls to component data.                                                                                                                                       |
| **22. What are Guards in Angular?**                                            | Guards are used to protect routes and control access based on conditions. Types include `CanActivate`, `CanActivateChild`, `CanDeactivate`, and `CanLoad`.                                                                                                                                         |
| **23. What is a Pipe in Angular?**                                             | A pipe is used to transform data in Angular templates. Angular has built-in pipes like `date`, `currency`, `uppercase`, and custom pipes can be created to perform specific transformations.                                                                                                       |
| **24. What is `@Input()` and `@Output()` in Angular?**                         | `@Input()` allows passing data from a parent to a child component, while `@Output()` allows emitting events from a child component to a parent.                                                                                                                                                  |
| **25. How can you optimize Angular applications?**                             | To optimize Angular apps, you can use lazy loading, `OnPush` change detection, trackBy with `ngFor`, AOT compilation, and implement service workers for caching and offline capabilities.                                                                                                          |
| **26. What is `ngOnChanges()` in Angular?**                                    | `ngOnChanges()` is a lifecycle hook that is called when any input property of a component changes, providing the previous and current values of the property.                                                                                                                                |
| **27. What is a module in Angular?**                                           | A module is a cohesive block of related functionality. It groups components, directives, pipes, and services together. Every Angular application has at least one module (the root module).                                                                                                         |
| **28. What is the purpose of `ngOnDestroy()` in Angular?**                      | `ngOnDestroy()` is a lifecycle hook called just before Angular destroys the component. It is used for cleanup tasks like unsubscribing from observables or detaching event listeners.                                                                                                             |
| **29. What are Observables in Angular?**                                       | Observables are used to handle asynchronous data streams. RxJS is used to manage observables for operations like HTTP requests, events, or streams of data.                                                                                                                                    |
| **30. How do you perform form validation in Angular?**                         | Angular provides template-driven forms and reactive forms for validation. Template-driven uses `required`, `minlength`, etc., while reactive forms use `Validators` like `Validators.required`, `Validators.minLength()`.                                                                         |
| **31. How do you create a service in Angular?**                                 | Use Angular CLI: `ng generate service my-service`. A basic service is created with an `@Injectable()` decorator, allowing it to be used across components.                                                                                                                                       |
| **32. What is `ng-content` in Angular?**                                        | `ng-content` is used for projecting content into a component's template. It allows the insertion of dynamic content into a component.                                                                                                                                                           |
| **33. How do you implement routing in Angular?**                               | Routing is configured in the `app-routing.module.ts` file. Define routes with path and component and use `<router-outlet>` in the template to display the routed views.                                                                                                                        |
| **34. What is the role of `ngOnChanges()` in Angular?**                         | `ngOnChanges()` is called when any of the component's `@Input()` properties change. It receives a `SimpleChanges` object containing the current and previous values of the properties.                                                                                                          |
| **35. How can you share data between components in Angular?**                  | Data can be shared between components using services, `@Input()` for parent-to-child communication, and `@Output()` for child-to-parent communication.                                                                                                                                         |
| **36. What is `ngAfterViewInit()` in Angular?**                                 | `ngAfterViewInit()` is a lifecycle hook that is called after Angular initializes the component's view and child views. It is useful for accessing and manipulating child components or DOM elements.                                                                                               |
| **37. What is `ngAfterViewChecked()` in Angular?**                              | `ngAfterViewChecked()` is called after Angular checks the component's view for changes. It can be used to perform actions after the view has been checked for changes.                                                                                                                           |
| **38. What is a `Subject` in RxJS?**                                            | A `Subject` in RxJS is both an Observable and an Observer. It allows multicasting to multiple subscribers, and can emit values to them.                                                                                                                                                          |
| **39. How can you handle errors in Angular HTTP requests?**                    | You can handle errors using the `catchError` operator in RxJS or by subscribing to the observable and handling errors in the error callback.                                                                                                                                                    |
| **40. What is the `Renderer2` in Angular?**                                     | `Renderer2` is an Angular service that provides an abstraction layer for DOM manipulation. It allows the application to work across different platforms like server-side rendering.                                                                                                              |
| **41. How do you navigate programmatically in Angular?**                        | You can use Angular's `Router` to navigate programmatically by calling `router.navigate()` or `router.navigateByUrl()`.                                                                                                                                                                        |

---

# Angular Interview Questions and Answers

| **Question**                                                                 | **Answer**                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **42. What is an Angular service worker?**                                    | Service workers in Angular provide the ability to manage caching, handle background data synchronization, and enable offline capabilities for your Angular application.                                                                                                                            |
| **43. How do you enable lazy loading in Angular?**                            | Lazy loading in Angular is enabled by configuring the Angular router with `loadChildren` to load modules only when needed.                                                                                                                                                                         |
| **44. What is the use of `ngOnChanges()` lifecycle hook?**                    | `ngOnChanges()` is a lifecycle hook that is called whenever the value of any input property changes in a component. It allows you to react to these changes by processing the new and previous values.                                                                                           |
| **45. What is the purpose of `ngOnInit()` lifecycle hook in Angular?**         | `ngOnInit()` is used to initialize the component after Angular first displays the component’s view. It is a good place to initialize data or call services to load data.                                                                                                                        |
| **46. What is `ngAfterViewInit()` in Angular?**                                | `ngAfterViewInit()` is a lifecycle hook that is called after the Angular framework initializes the component’s views and child views. It’s a good place for interacting with child components or DOM elements.                                                                                       |
| **47. What is `ngAfterViewChecked()` in Angular?**                             | `ngAfterViewChecked()` is a lifecycle hook that is called after Angular has checked the component's view for changes. It’s a useful place to perform additional actions after Angular’s change detection runs.                                                                                        |
| **48. What is `ngOnDestroy()` lifecycle hook used for?**                      | `ngOnDestroy()` is called just before Angular destroys the component. It is used to clean up resources like unsubscribing from observables, clearing timers, or detaching event listeners.                                                                                                        |
| **49. What is `ngDoCheck()` in Angular?**                                     | `ngDoCheck()` is a lifecycle hook that is called during every change detection cycle. It is used for custom change detection logic that cannot be done by Angular’s built-in change detection.                                                                                                     |
| **50. What is a `Pure` Pipe in Angular?**                                      | A `Pure` pipe is only executed when the input data to the pipe changes. Angular’s default behavior for pipes is pure pipes, where they only run if the data changes.                                                                                                                             |
| **51. What is an `Impure` Pipe in Angular?**                                   | An `Impure` pipe is executed whenever Angular’s change detection runs, even if the input data hasn’t changed. This behavior is slower but allows for more complex data transformations.                                                                                                            |
| **52. What is `@Inject()` in Angular?**                                        | `@Inject()` is used for specifying a dependency to be injected into the constructor. It is used when the type of the dependency cannot be inferred by Angular.                                                                                                                                   |
| **53. What is `ngFor` directive used for in Angular?**                         | `ngFor` is a structural directive that is used to repeat a template for each item in an array or a list. It iterates over a collection and renders the template for each item.                                                                                                                |
| **54. What is `ngClass` directive in Angular?**                               | `ngClass` is used to dynamically add or remove CSS classes from an element. It can be used with an object, array, or string to apply styles conditionally based on component data.                                                                                                              |
| **55. What is `ngStyle` directive in Angular?**                               | `ngStyle` is used to dynamically set CSS styles on an element. It can take an object or expression to bind styles.                                                                                                                          |
| **56. What are Observables and how are they used in Angular?**                | Observables represent a collection of future values or events. They are used extensively in Angular for handling asynchronous operations such as HTTP requests, user inputs, or WebSocket events.                                                                                                    |
| **57. What is RxJS in Angular?**                                               | RxJS (Reactive Extensions for JavaScript) is a library for reactive programming that enables the use of Observables. It is used in Angular for handling asynchronous tasks, such as HTTP requests, event streams, and handling multiple values over time.                                                 |
| **58. What is `async` pipe in Angular?**                                       | The `async` pipe subscribes to an Observable and renders the latest emitted value in the template. It also automatically unsubscribes when the component is destroyed.                                                                                                                               |
| **59. What is the difference between `subscribe` and `async` pipe?**           | `subscribe` is used explicitly in the component’s TypeScript file to handle Observables, while `async` pipe handles subscription and unsubscription automatically in the template.                                                                                                                |
| **60. What are the differences between `@Input()` and `@Output()`?**           | `@Input()` allows passing data from a parent component to a child component, while `@Output()` allows emitting events from the child component to the parent.                                                                                                                             |
| **61. How do you create a custom pipe in Angular?**                            | To create a custom pipe, use Angular CLI: `ng generate pipe customPipe`. The custom pipe should implement `PipeTransform` and define the `transform()` method to modify input data.                                                                                                            |
| **62. What is `ngSwitch` directive in Angular?**                              | `ngSwitch` is a structural directive that works similarly to the `switch` statement in JavaScript. It displays different templates based on the value of an expression.                                                                                                                           |
| **63. What is the purpose of `ngModel` in Angular?**                           | `ngModel` is used for two-way data binding in Angular forms. It synchronizes the view and model. It’s often used in template-driven forms.                                                                                                                                                         |
| **64. What is a `FormGroup` in Angular?**                                     | A `FormGroup` is a collection of `FormControl` instances in reactive forms. It is used to track the state and values of the form controls as a group.                                                                                                                                        |
| **65. What is a `FormControl` in Angular?**                                   | A `FormControl` represents a single form input element in Angular's reactive forms. It tracks the value and validation state of that input.                                                                                                                                                       |
| **66. What is `FormBuilder` in Angular?**                                      | `FormBuilder` is a service provided by Angular to simplify the creation of reactive forms. It is used to create `FormGroup` and `FormControl` instances with less boilerplate code.                                                                                                           |
| **67. How do you perform form validation in Angular?**                         | You can use built-in validators like `Validators.required`, `Validators.minLength`, or create custom validators. In template-driven forms, use `ngModel` to bind data, and in reactive forms, use `FormControl` or `FormGroup` with validators.                                                       |
| **68. What is the difference between `ngOnChanges()` and `ngDoCheck()` in Angular?** | `ngOnChanges()` is triggered when an input property changes, while `ngDoCheck()` is called during every change detection cycle.                                                                                                                                                               |
| **69. How do you prevent Angular’s change detection from running on a component?** | You can use `ChangeDetectionStrategy.OnPush` to optimize performance by limiting the checks to only when the component's inputs change or when an event is triggered.                                                                                                                             |
| **70. What are interceptors in Angular?**                                      | HTTP interceptors are used to intercept HTTP requests and responses to modify them. They can be used for logging, error handling, or adding authentication headers.                                                                                                                            |
| **71. How can you handle HTTP errors in Angular?**                             | You can handle HTTP errors by using `catchError()` in RxJS operators or by subscribing to the observable and handling errors in the `error` callback.                                                                                                                                           |
| **72. What is the role of `@Injectable()` in Angular?**                        | `@Injectable()` decorator marks a service class as injectable, allowing Angular’s DI system to provide an instance of it to components and other services.                                                                                                                                         |
| **73. What is `ChangeDetectorRef` in Angular?**                                | `ChangeDetectorRef` is used to explicitly control change detection in Angular. You can use methods like `markForCheck()` or `detectChanges()` to manually trigger change detection in certain scenarios.                                                                                             |
| **74. What is `ngOnChanges()` and how is it used in Angular?**                 | `ngOnChanges()` is a lifecycle hook that is triggered when any of the component's input properties change. It’s often used to respond to property changes or perform additional logic.                                                                                                           |
| **75. What is the role of `ngModel` in template-driven forms?**                | `ngModel` creates two-way data binding between a form input element and the component model. It updates the component when the user changes the input and vice versa.                                                                                                                           |
| **76. How does Angular handle HTTP requests?**                                 | Angular uses the `HttpClient` module to make HTTP requests. It provides methods like `get()`, `post()`, `put()`, and `delete()` to interact with RESTful APIs.                                                                                                                                |
| **77. What is an Angular CLI?**                                                | Angular CLI (Command Line Interface) is a tool for automating common development tasks such as creating components, services, generating tests, and serving the application.                                                                                                                     |
| **78. How do you create a new Angular component using Angular CLI?**           | You can create a new component using Angular CLI by running the following command: `ng generate component my-component`.                                                                                                               |
| **79. What is `@NgModule()` in Angular?**                                      | `@NgModule()` is a decorator that defines a module in Angular. It organizes components, directives, pipes, and services into cohesive blocks of functionality.                                                                                                                                |
| **80. How do you pass data from a child component to a parent component in Angular?** | You can use the `@Output()` decorator to emit events from the child to the parent component. The parent component listens for these events and processes the data.                                                                                                                            |
| **81. What is the purpose of `RouterOutlet` in Angular?**                      | `RouterOutlet` is a directive that serves as a placeholder for rendering the routed components in Angular's routing system.                                                                                                                                                                      |
| **82. What is `ActivatedRoute` in Angular?**                                   | `ActivatedRoute` provides access to information about the currently active route. It allows you to get parameters, query parameters, and route data associated with the route.                                                                                                                  |
| **83. What is the `RouterModule` in Angular?**                                 | `RouterModule` is an Angular module that provides routing functionality to your application. It is used to configure and enable navigation between different views in the application.                                                                                                            |
| **84. What is `ng-template` in Angular?**                                      | `ng-template` is used to define template content that can be reused or rendered conditionally using directives like `ngIf`, `ngFor`, and `ngSwitch`.                                                                                                                                             |
| **85. What is `ng-content` in Angular?**                                       | `ng-content` is used for content projection. It allows you to pass content from a parent component into a child component's template.                                                                                                                                                             |
| **86. What is `ngIf` and how is it used in Angular?**                          | `ngIf` is a structural directive used to conditionally include or remove elements from the DOM based on the value of a given expression.                                                                                                                                                         |
| **87. How do you create an Angular pipe?**                                     | You can create an Angular pipe by using Angular CLI: `ng generate pipe custom-pipe`. Then, implement the `PipeTransform` interface and define the `transform()` method to manipulate data.                                                                                                      |
| **88. What is a route guard in Angular?**                                      | A route guard is a service that is used to protect routes from unauthorized access. Guards can be used to allow or deny navigation to a particular route based on conditions.                                                                                                                      |
| **89. What is a `Subject` in RxJS?**                                           | A `Subject` is a type of Observable that allows values to be multicasted to many Observers. It can also be used to manually emit values.                                                                                                                                                        |
| **90. What is `async` pipe in Angular?**                                       | The `async` pipe subscribes to an observable and renders the latest value emitted. It also automatically unsubscribes when the component is destroyed.                                                                                                                                             |

---

The list is now covering 90 questions. Would you like me to continue generating all the questions in similar format, or is there a particular section you would like to focus on?
# Angular Interview Questions and Answers (Continued)

| **Question**                                                                 | **Answer**                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **91. What is a `BehaviorSubject` in RxJS?**                                  | A `BehaviorSubject` is a type of `Subject` that holds the current value and emits that value to new subscribers immediately upon subscription. It is useful for representing "state" in your application.                                                                                       |
| **92. How do you implement routing in Angular?**                              | Routing in Angular is implemented by configuring the `RouterModule` in your application module, defining routes, and using the `<router-outlet></router-outlet>` directive in templates. The `routerLink` directive is used for navigation.                                                        |
| **93. How do you implement navigation between pages in Angular?**             | You can implement navigation between pages by using `routerLink` directive to specify the path in the template, or by using `router.navigate()` programmatically in the component class.                                                                                                         |
| **94. What is `lazy loading` in Angular and how is it implemented?**          | Lazy loading is a technique to load modules only when needed, rather than at the application startup. It can be implemented by using `loadChildren` in the routing module.                                                                                                                     |
| **95. How do you manage authentication and authorization in Angular?**       | Authentication and authorization in Angular can be handled using route guards. A guard can prevent unauthorized users from accessing routes by checking authentication status using services.                                                                                                  |
| **96. What is the purpose of `HttpInterceptor` in Angular?**                   | An `HttpInterceptor` is used to intercept and modify HTTP requests and responses. Common use cases include adding authentication tokens to requests, logging HTTP traffic, or handling errors globally.                                                                                           |
| **97. How do you define environment-specific variables in Angular?**          | Environment-specific variables can be defined in the `src/environments` folder. Angular provides `environment.ts` for development and `environment.prod.ts` for production. These variables can be accessed via `environment.[variableName]`.                                                       |
| **98. What is the difference between `ng serve` and `ng build` in Angular?**  | `ng serve` compiles the application and serves it in a local development server, while `ng build` compiles the application into static files that are ready for production deployment.                                                                                                         |
| **99. What is `ngOnChanges` lifecycle hook used for?**                        | `ngOnChanges` is a lifecycle hook called whenever an input property changes. It allows you to react to changes in the component's inputs and take necessary actions accordingly.                                                                                                              |
| **100. What is `ngAfterContentInit` lifecycle hook in Angular?**              | `ngAfterContentInit` is called after Angular projects external content into the component’s view, such as content passed via `ng-content`. It’s typically used for working with projected content.                                                                                                |
| **101. How do you make HTTP calls in Angular?**                               | HTTP calls in Angular are made using the `HttpClient` service. You can use methods like `get()`, `post()`, `put()`, and `delete()` to interact with REST APIs.                                                                                                                                |
| **102. What is `HttpClientModule` in Angular?**                               | `HttpClientModule` is an Angular module that provides a simplified API for making HTTP requests. It needs to be imported in the root application module to enable HTTP communication.                                                                                                         |
| **103. How do you prevent XSS attacks in Angular?**                            | Angular automatically sanitizes untrusted values, such as URLs, styles, and HTML content, using the `DomSanitizer`. Avoid inserting raw HTML content using `innerHTML` or other unsafe methods. Use Angular's built-in mechanisms to protect against XSS. |
| **104. What is the purpose of `trackBy` in `ngFor`?**                         | `trackBy` is used in `ngFor` to optimize performance by providing a unique identifier for each element in the list. It helps Angular identify which items have changed, reducing unnecessary DOM manipulations.                                                                                  |
| **105. What are form controls in Angular?**                                   | Form controls represent individual form input elements, tracking their value and state (valid, invalid, touched, dirty, etc.). These are used in reactive forms to bind user inputs to the component model.                                                                                   |
| **106. What are template-driven forms in Angular?**                           | Template-driven forms in Angular are forms where the form model is driven by the template, and the validation logic is written in the template. These forms are easier to work with for simple scenarios but less flexible than reactive forms.                                                      |
| **107. What are reactive forms in Angular?**                                  | Reactive forms in Angular are forms where the form model is explicitly defined in the component class using `FormGroup` and `FormControl`. They offer better scalability and flexibility for complex forms with more powerful validation and control.                                                  |
| **108. What is the purpose of `ng-content` in Angular?**                      | `ng-content` is used for content projection, where content is passed from a parent component to a child component. The child component renders the passed content within its template.                                                                                                         |
| **109. What is an Angular directive?**                                        | Directives are classes in Angular that add behavior to elements in the DOM. There are structural directives (e.g., `ngIf`, `ngFor`) and attribute directives (e.g., `ngClass`, `ngStyle`).                                                                                                         |
| **110. What is `ngIf` directive in Angular?**                                 | `ngIf` is a structural directive that conditionally adds or removes elements from the DOM based on the expression value. If the expression evaluates to `true`, the element is added; otherwise, it is removed.                                                                                 |
| **111. How do you create custom directives in Angular?**                       | Custom directives in Angular can be created using the Angular CLI (`ng generate directive`) or manually by implementing the `Directive` decorator and defining the `ngOnInit` or `ngOnChanges` lifecycle hooks.                                                                                |
| **112. What is the `ngFor` directive in Angular?**                            | `ngFor` is a structural directive used to iterate over an array or list of items and repeat an HTML element for each item in the array.                                                                                                                        |
| **113. How do you use dynamic data binding in Angular?**                       | Dynamic data binding in Angular is done using interpolation (`{{ value }}`), property binding (`[property]="value"`), or event binding (`(event)="handler()"`) to bind component data to the view dynamically.                                                                                   |
| **114. What is a `Service` in Angular?**                                      | A service in Angular is a class that is used to perform data operations, business logic, or handle HTTP requests. It is typically injected into components, other services, or directives using Angular's Dependency Injection system.                                                                 |
| **115. How do you handle multiple HTTP requests in Angular?**                 | You can use RxJS operators like `forkJoin`, `concat`, `merge`, or `combineLatest` to handle multiple HTTP requests concurrently or sequentially in Angular.                                                                                                                                    |
| **116. What is `async` and `await` in Angular?**                              | `async` and `await` are JavaScript keywords used to handle asynchronous operations in a more readable manner. `async` marks a function as asynchronous, while `await` pauses execution until the promise resolves. Angular uses this for async operations in services.                               |
| **117. How do you handle errors in Angular?**                                 | Errors in Angular can be handled using `catchError` RxJS operator or by handling errors explicitly in the `subscribe` method of an observable. Global error handling can also be implemented with `HttpInterceptor`.                                                                             |
| **118. What is the purpose of `ChangeDetectionStrategy.OnPush` in Angular?**    | `ChangeDetectionStrategy.OnPush` tells Angular to check for changes only when an input property changes or when an event is triggered, making the application more efficient by reducing unnecessary change detection cycles.                                                                          |
| **119. What is `ngStyle` directive in Angular?**                              | `ngStyle` is an attribute directive that allows you to set inline styles dynamically on an element. It accepts an object or an expression representing the styles to be applied.                                                                                                                   |
| **120. What is `ngClass` directive in Angular?**                              | `ngClass` is an attribute directive used to conditionally apply CSS classes to an HTML element based on the evaluation of an expression.                                                                                                           |
| **121. How do you create dynamic components in Angular?**                      | Dynamic components can be created using `ViewContainerRef` to dynamically add components to a view at runtime. You can also use `ComponentFactoryResolver` to instantiate a component dynamically.                                                                                              |
| **122. What is `Renderer2` in Angular?**                                       | `Renderer2` is a service provided by Angular that allows safe interaction with the DOM. It provides methods for manipulating elements without directly accessing the native DOM.                                                                                                               |
| **123. What is the purpose of `@HostListener` in Angular?**                    | `@HostListener` is a decorator that allows you to listen to events on the host element of the directive or component. It is commonly used to listen for native events like clicks or mouse movements.                                                                                              |
| **124. What is `@HostBinding` in Angular?**                                    | `@HostBinding` is a decorator used to bind properties or attributes to the host element. It can be used to set styles, classes, or other properties dynamically based on component data.                                                                                                          |
| **125. How do you add custom event binding in Angular?**                       | Custom event binding in Angular is done using `@Output` and `EventEmitter`. The component emits an event using `EventEmitter`, and the parent component listens to it using event binding (`(event)="handler()"`).                                                                                 |
| **126. What is `ngModel` in Angular?**                                         | `ngModel` is a directive used for two-way data binding in Angular forms. It binds the form control's value to the component property, automatically updating both the view and model when one changes.                                                                                           |
| **127. What is `angular.json` file?**                                          | `angular.json` is a configuration file used by Angular CLI to configure various aspects of the Angular project such as build settings, assets, environment variables, and much more.                                                                                                            |
| **128. What are `webpack` and its role in Angular?**                           | Webpack is a module bundler used by Angular CLI to bundle and optimize the application code, assets, and dependencies for deployment. It helps in the process of compiling and optimizing assets for production.                                                                                  |

---

Let me know if you would like me to continue with more questions, or if you need further modifications!

# Angular Interview Questions and Answers (Continued)

| **Question**                                                                 | **Answer**                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **129. What is the purpose of `ngSwitch` in Angular?**                         | `ngSwitch` is a directive in Angular that allows for conditionally rendering a set of elements based on an expression. It's similar to a switch-case statement in programming.                                                                                                                    |
| **130. What is `ngFor` used for in Angular?**                                  | `ngFor` is a structural directive that is used to repeat a set of elements in the DOM for each item in an iterable (array, object, etc.). It can be used to display lists of data dynamically.                                                                                                   |
| **131. What is the difference between `ngIf` and `ngSwitch`?**                 | `ngIf` conditionally includes or excludes an element from the DOM, while `ngSwitch` is used to display different elements based on matching values (similar to switch-case).                                                                                                                     |
| **132. How do you optimize the performance of an Angular application?**       | Performance can be optimized in Angular by using lazy loading, `OnPush` change detection strategy, avoiding unnecessary re-renders, using trackBy with `ngFor`, reducing the size of bundles, and using `ChangeDetectorRef` to manually control change detection.                                      |
| **133. How do you handle routing errors in Angular?**                          | You can handle routing errors in Angular using route guards (`CanActivate`, `CanDeactivate`, etc.) and the `RouterModule`'s `errorHandler` function. Additionally, you can catch routing errors using `catchError` in an `Observable`.                                                             |
| **134. What is the purpose of `@Injectable` decorator in Angular?**            | The `@Injectable` decorator is used to mark a class as available for dependency injection. It ensures that Angular knows how to create an instance of the class when needed and allows for it to be injected into other services or components.                                                       |
| **135. What is `ngOnInit` used for in Angular?**                               | `ngOnInit` is a lifecycle hook that is called once the component's input properties have been initialized. It’s a good place to perform initialization tasks, such as data fetching or setting up component state.                                                                                 |
| **136. What is `ngAfterViewInit` used for in Angular?**                        | `ngAfterViewInit` is a lifecycle hook called after Angular initializes the component's view and its child views. It is used to perform initialization tasks related to the component's view.                                                                                                      |
| **137. What is `ngOnDestroy` in Angular?**                                     | `ngOnDestroy` is a lifecycle hook called when a component or directive is destroyed. It is commonly used to clean up resources, such as unsubscribing from observables or detaching event handlers.                                                                                                 |
| **138. What is a `module` in Angular?**                                        | A module in Angular is a container that holds a cohesive block of code, which can include components, directives, services, pipes, and other modules. It helps organize and structure an application, making it more modular and easier to maintain.                                                |
| **139. What is the purpose of `app.module.ts`?**                               | `app.module.ts` is the root module of an Angular application. It declares all the components, directives, pipes, and services needed in the application and imports other modules required for functionality.                                                                                      |
| **140. What is the role of `angular-cli.json`?**                               | `angular-cli.json` (or `angular.json` in recent versions) is a configuration file used by Angular CLI to specify build options, file paths, assets, and other project-level settings. It helps configure how the application is built, served, and deployed.                                               |
| **141. What is `ngOnChanges` in Angular?**                                     | `ngOnChanges` is a lifecycle hook that is called when there is a change in the input properties of a component. It allows you to track and respond to changes in input data.                                                                                                                      |
| **142. What is the role of `ngModel` in Angular?**                             | `ngModel` is used for two-way data binding in Angular forms. It binds the input fields to the component's properties and updates both the view and the model whenever one of them changes.                                                                                                          |
| **143. What is the difference between `ngOnInit` and `ngAfterViewInit`?**       | `ngOnInit` is called after the component's input properties are set, while `ngAfterViewInit` is called after the component’s view (and its children) is initialized. `ngAfterViewInit` is useful for accessing and manipulating child components or views.                                           |
| **144. What is `ngAfterViewChecked` used for?**                               | `ngAfterViewChecked` is a lifecycle hook that is called after every check of the component's view and child views. It can be used to detect and respond to changes in the view, though its use should be minimized to avoid performance issues.                                                       |
| **145. What is `ngAfterContentChecked` in Angular?**                           | `ngAfterContentChecked` is called after the content that is projected into the component via `ng-content` is checked. It is similar to `ngAfterViewChecked` but is for content projection.                                                                                                        |
| **146. What is the difference between `ngOnInit` and `constructor`?**          | The constructor is called when the component is instantiated, while `ngOnInit` is called after the component’s input properties are initialized. `ngOnInit` is typically used for setup tasks that require input properties to be set.                                                              |
| **147. What is the difference between template-driven and reactive forms?**    | Template-driven forms are declarative and defined in the HTML template, while reactive forms are programmatically defined in the component class using `FormGroup` and `FormControl`. Reactive forms provide more control and flexibility for complex scenarios.                                      |
| **148. What is the purpose of `FormGroup` in Angular?**                        | `FormGroup` is used to represent a collection of form controls. It allows you to group related form controls together and manage their validation, status, and value.                                                                                                                            |
| **149. What is the difference between `ngOnInit` and `ngOnChanges`?**           | `ngOnInit` is called once after the component's input properties are initialized, while `ngOnChanges` is called whenever any of the input properties of the component change.                                                                                                                     |
| **150. What is the purpose of `ngModelChange` in Angular?**                    | `ngModelChange` is an event emitted when the value of a bound form control changes. It is used for capturing changes and reacting to them, often used with `ngModel` for two-way data binding.                                                                                                    |
| **151. What are Angular services used for?**                                   | Angular services are classes used to handle business logic, interact with APIs, manage application state, or share data between components. They are typically injected into components, other services, or directives via Angular's Dependency Injection system.                                         |
| **152. How do you share data between components in Angular?**                  | Data can be shared between components in Angular using services, `@Input()` and `@Output()`, or by using a shared store (like Redux or NgRx). Services are the most common and recommended approach.                                                                                               |
| **153. How do you perform form validation in Angular?**                        | Form validation can be performed using both template-driven and reactive forms. Template-driven forms use validation directives like `required`, `minlength`, and `maxlength`, while reactive forms use `Validators` in the component class to define validation rules.                                 |
| **154. How do you handle multiple form validations in Angular?**               | In Angular, you can use multiple validators on form controls by passing an array of validators. This can be done in both template-driven and reactive forms by chaining multiple validators together.                                                                                             |
| **155. What are `ngIf` and `ngFor` directives used for?**                      | `ngIf` is used to conditionally include or exclude an HTML element from the DOM based on a boolean condition. `ngFor` is used to repeat an HTML element for each item in an iterable, such as an array or list.                                                                                   |
| **156. What is the role of `ng-content` in Angular?**                          | `ng-content` is used for content projection in Angular. It allows the parent component to pass content to the child component's template, where it will be rendered inside the `ng-content` element.                                                                                                |
| **157. What is the purpose of `ngClass` in Angular?**                          | `ngClass` is an attribute directive used to conditionally apply or remove CSS classes on an HTML element based on an expression. It can accept a string, an array, or an object representing the classes to be applied.                                                                          |
| **158. How do you handle routing with query parameters in Angular?**            | You can handle query parameters in Angular by using the `ActivatedRoute` service to access route parameters. Use `this.route.snapshot.queryParams` to retrieve query parameters in a component.                                                                                                 |
| **159. How do you pass data to routes in Angular?**                             | Data can be passed to routes using `route.data` property in the route configuration. It can be accessed within components using `ActivatedRoute`'s `data` property.                                                                                                                                |
| **160. What is the purpose of `@Input` and `@Output` in Angular?**              | `@Input` allows a component to accept data from its parent, while `@Output` allows a component to emit events to its parent. These are used for communication between parent and child components.                                                                                                 |

---

This concludes the list of 160 Angular interview questions and answers. Let me know if you need additional information or further assistance!
# Angular Interview Questions and Answers (Continued)

| **Question**                                                                 | **Answer**                                                                                                                                                                                                                                                                                      |
|-------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **161. What is `ngOnChanges` lifecycle hook in Angular?**                      | `ngOnChanges` is a lifecycle hook that gets called whenever there is a change in an input-bound property (`@Input`). It is useful for responding to changes in the component's input data.                                                                                                     |
| **162. What is `ngAfterContentInit` lifecycle hook in Angular?**              | `ngAfterContentInit` is called once Angular initializes all of the content projected into the component. It is useful for performing any initialization tasks related to content projection.                                                                                                    |
| **163. What is `ngAfterViewInit` lifecycle hook in Angular?**                 | `ngAfterViewInit` is called after Angular initializes the component’s view and its child views. This is often used to access and modify the view once it is fully initialized.                                                                                                                  |
| **164. How does Angular handle form validation?**                              | Angular provides built-in validators like `required`, `minlength`, `maxlength`, and `pattern` for template-driven forms. For reactive forms, the validation is handled using `Validators` in the component class. You can also create custom validators.                                         |
| **165. What is a custom validator in Angular?**                                | A custom validator in Angular is a function that takes a control as an argument and returns an error object if the control is invalid. This allows you to define validation logic that is not provided by Angular's built-in validators.                                                        |
| **166. How do you create a custom pipe in Angular?**                           | A custom pipe in Angular is created by implementing the `PipeTransform` interface and defining the `transform()` method. You can register the pipe using the `@Pipe` decorator.                                                                                                                 |
| **167. What is the purpose of `@Pipe` decorator in Angular?**                  | The `@Pipe` decorator is used to define a custom pipe in Angular. It allows you to transform data within the template (such as date formatting or text transformation). The `transform()` method is the logic that defines how the data is transformed.                                            |
| **168. How do you implement routing with parameters in Angular?**              | Routing with parameters is implemented by defining a route with dynamic parameters, e.g., `{ path: 'product/:id', component: ProductComponent }`. In the component, parameters can be accessed using `ActivatedRoute` service (`this.route.snapshot.paramMap.get('id')`).                           |
| **169. What is the difference between `snapshot` and `observable` in Angular routing?** | `snapshot` provides a static snapshot of the current route at the time the component is initialized, while `observable` is a dynamic stream that listens to changes in the route over time. `observable` is preferred for detecting changes in route parameters.                                 |
| **170. How can you implement lazy loading in Angular?**                        | Lazy loading in Angular is implemented by defining feature modules with `loadChildren` in the routing module. For example, `{ path: 'admin', loadChildren: () => import('./admin/admin.module').then(m => m.AdminModule) }`. It loads the module only when the route is visited.                      |
| **171. What is the purpose of `@Inject` in Angular?**                          | `@Inject` is used in Angular's Dependency Injection system to explicitly specify which dependency to inject into the constructor when the class doesn't have a direct type. It helps with providing tokens for dependencies.                                                                       |
| **172. How can you prevent an Angular component from being destroyed?**       | You can prevent a component from being destroyed by using route guards like `CanDeactivate` to prevent navigation. You can also use `ngOnDestroy` to clean up resources and prevent automatic destruction in specific scenarios.                                                                 |
| **173. What is the difference between `ngFor` and `ngForOf`?**                  | `ngFor` is an alias for `ngForOf`. Both are used to iterate over lists, but `ngForOf` is the correct directive. `ngFor` is the shorthand for using `ngForOf`.                                                                                                                                    |
| **174. How can you access DOM elements in Angular?**                          | You can access DOM elements in Angular using `@ViewChild` or `@ViewChildren` decorators, or by using `Renderer2` for safe DOM manipulation. `@ViewChild` allows direct access to a single child element, while `@ViewChildren` is used for accessing multiple elements.                            |
| **175. What is the `Renderer2` in Angular used for?**                          | `Renderer2` is a service that provides an abstraction for interacting with the DOM. It helps to avoid direct manipulation of the DOM, ensuring that Angular can handle updates in a platform-independent manner.                                                                                   |
| **176. What is the purpose of `ngModel` in Angular?**                          | `ngModel` is used for two-way data binding in Angular forms. It binds the value of an input field to a component property and updates both the view and the component's data when one changes.                                                                                                    |
| **177. What is `async` pipe in Angular?**                                      | The `async` pipe is used to subscribe to an observable or promise and return the latest value. It automatically handles subscribing and unsubscribing, reducing boilerplate code.                                                                                                                 |
| **178. How do you handle HTTP errors globally in Angular?**                    | HTTP errors can be handled globally using an `HttpInterceptor`. The interceptor can catch HTTP errors and handle them, such as displaying an error message or redirecting the user.                                                                                                               |
| **179. How do you optimize Angular change detection performance?**             | Change detection performance can be optimized by using `ChangeDetectionStrategy.OnPush`, which checks for changes only when input properties change, or when an event is triggered. Additionally, minimizing the use of two-way data binding and reducing the number of watchers can help.                |
| **180. What is the `HttpClient` in Angular used for?**                         | The `HttpClient` is used for making HTTP requests in Angular. It provides methods for sending GET, POST, PUT, and DELETE requests to REST APIs, and it returns an `Observable` that can be subscribed to for handling responses.                                                                 |
| **181. How do you handle authorization and authentication in Angular?**       | Authorization and authentication in Angular can be handled by using route guards like `CanActivate`, `CanLoad`, and `CanDeactivate` to protect routes. For authentication, token-based systems (e.g., JWT) can be used along with HTTP interceptors to add tokens to requests.                        |
| **182. What is the `ActivatedRoute` in Angular?**                              | `ActivatedRoute` is a service that provides access to the current route information, such as route parameters, query parameters, and data associated with the route. It is often used for retrieving parameters or resolving data before rendering a component.                                          |
| **183. What is the `@Output` decorator in Angular?**                           | `@Output` is a decorator that is used to define custom events in Angular components. It is typically used in combination with an `EventEmitter` to send data from the child component to the parent component.                                                                                      |
| **184. What is the `@Input` decorator in Angular?**                            | `@Input` is a decorator used to define input properties in Angular components. It allows data to be passed from a parent component to a child component.                                                                                                                                            |
| **185. What is `ngOnChanges` used for in Angular?**                            | `ngOnChanges` is called when any data-bound input property changes. It allows components to respond to changes in the values of input properties passed from the parent component.                                                                                                                 |
| **186. What is the role of `ngAfterViewChecked` in Angular?**                  | `ngAfterViewChecked` is a lifecycle hook that is called after Angular has checked the component's view and its child views. It is useful for detecting changes in the DOM after Angular has updated the view.                                                                                         |
| **187. What is the `ng-content` used for in Angular?**                         | `ng-content` is used to insert dynamic content into a component's template. It allows content projection, enabling you to pass content from a parent component to a child component.                                                                                                               |
| **188. What is a module in Angular and why is it important?**                  | A module in Angular is a logical unit of code that can contain components, services, directives, pipes, and other modules. It is used to organize the application and helps Angular to manage dependencies, lazy loading, and the overall structure.                                                |
| **189. How does `ngFor` work in Angular?**                                     | `ngFor` is a structural directive used for iterating over a list of items. It repeats an HTML element for each item in the iterable. For example, it can be used to generate a list of HTML elements dynamically based on an array of data.                                                         |
| **190. What is the difference between `ngOnInit` and `ngAfterViewInit`?**       | `ngOnInit` is called once after the component's inputs have been set, while `ngAfterViewInit` is called after Angular has fully initialized the component's view and its child views. `ngAfterViewInit` is used when you need to interact with child components after they have been initialized.  |
| **191. How does Angular handle dependency injection?**                         | Angular's Dependency Injection (DI) system allows components and services to declare dependencies. These dependencies are injected by Angular through constructors or other mechanisms. DI enables a modular, testable, and maintainable structure in Angular applications.                           |
| **192. What is `ngModel` used for in Angular forms?**                          | `ngModel` is used for two-way data binding in Angular forms. It binds the form control's value to a property in the component, ensuring the model and view are kept in sync.                                                                                                                        |
| **193. How can you test Angular components?**                                  | Angular components can be tested using Angular's testing utilities like `TestBed` and `ComponentFixture`. You can write unit tests for individual components, using tools like Jasmine and Karma for running tests, and mocking dependencies using services like `HttpClientTestingModule`.                 |
| **194. What is the `ngIf` directive in Angular?**                              | `ngIf` is a structural directive used to conditionally include or exclude an HTML element from the DOM based on the value of a boolean expression. It can be used to dynamically control the visibility of elements.                                                                                 |
| **195. How do you use reactive forms in Angular?**                             | Reactive forms in Angular are used by importing `ReactiveFormsModule` in the application module. You create form controls and groups programmatically in the component class using `FormControl`, `FormGroup`, and `FormArray`. Validation is also defined in the class using Angular's `Validators`.    |
| **196. What are observables in Angular?**                                      | Observables in Angular are a key part of the RxJS library. They are used to manage asynchronous data streams, such as HTTP requests or user input events. Observables allow you to subscribe to data, handle asynchronous operations, and chain operators like `map()`, `filter()`, and `catchError()`.       |
| **197. What is `ngIf else` in Angular?**                                        | `ngIf else` is used to conditionally display an alternative view when a condition is false. You can provide an `else` block with an HTML template to be rendered when the condition doesn't match.                                                                                                   |
| **198. What is the role of `ngClass` in Angular?**                             | `ngClass` is used to dynamically add or remove CSS classes from an HTML element based on an expression. It can accept a string, array, or object to represent the CSS classes.                                                                                                                        |
| **199. How do you pass parameters to routes in Angular?**                      | Parameters can be passed to routes in Angular by using dynamic path segments in the route
| **200. How do you handle lazy-loaded routes in Angular?**                      | Lazy-loaded routes are handled by using `loadChildren` in the route configuration. The modules for lazy-loaded routes are only fetched when the route is activated, reducing the initial loading time of the application.                                                                            |



