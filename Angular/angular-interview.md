Commonly Used Angular Features:
Components: Building blocks of Angular applications.
Directives: Extend HTML with custom behavior (*ngIf, *ngFor, etc.).
Services and Dependency Injection: Share data and logic across components.
Routing and Navigation: Manage navigation between views.
Forms: Template-driven and reactive forms for user input handling.
Pipes: Transform data in templates (e.g., | date, | uppercase).
Modules: Organize the application into cohesive blocks (@NgModule).
HttpClient: Communicate with backend APIs.
Lifecycle Hooks: Manage component lifecycle (ngOnInit, ngOnDestroy).
Change Detection: Automatically update the DOM when data changes.
<hr></hr>
Angular Interview Questions and Answers:
1. What is Angular?
Angular is a TypeScript-based framework for building single-page web applications (SPAs) developed by Google.
2. What are Angular directives?
Structural Directives: Change the DOM structure (e.g., *ngIf, *ngFor).
Attribute Directives: Change the appearance or behavior of an element (e.g., [ngClass], [ngStyle]).
3. What is the difference between constructor and ngOnInit?
constructor: Used for dependency injection and initializing class members.
ngOnInit: Lifecycle hook called after the component is initialized, used for initialization logic.
4. What is a service in Angular?
A service is a class with reusable logic that can be shared across components using dependency injection.
5. What is the purpose of @Input and @Output?
@Input: Pass data from a parent to a child component.
@Output: Emit events from a child to a parent component.
6. What is Angular's change detection?
A mechanism to track changes in the application state and update the DOM accordingly.
7. What is the difference between Template-driven and Reactive forms?
Template-driven: Simpler, uses directives in the template.
Reactive: More robust, uses FormGroup and FormControl in the component.
8. What is lazy loading in Angular?
A technique to load modules only when they are needed, improving application performance.
9. What is the purpose of ng-content?
Used to project content from a parent component into a child component.
10. What is the Angular CLI?
A command-line interface tool to create, build, and manage Angular projects.
11. What is the difference between Observable and Promise?
Observable: Supports multiple values over time, cancellable, used with RxJS.
Promise: Handles a single asynchronous value, not cancellable.
12. What is the purpose of RouterModule?
Provides routing and navigation functionality in Angular applications.
13. What are Angular lifecycle hooks?
Methods that allow developers to tap into different phases of a component's lifecycle (e.g., ngOnInit, ngOnDestroy, ngAfterViewInit).
14. What is the purpose of zone.js in Angular?
It patches asynchronous operations to trigger Angular's change detection.
15. What is the difference between ViewChild and ContentChild?
ViewChild: Access child components or elements in the component's template.
ContentChild: Access projected content from a parent component.
These are some of the most commonly asked Angular interview questions and features.
