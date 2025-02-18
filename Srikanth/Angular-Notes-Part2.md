
Life Cycle Hooks:
================

- Angular calls lifecycle hook methods on directives and components as it creates, changes and destroys them.

- Angular manages lifecycle of components and directives

- A directive has the same set of lifecycle hooks, minus the hooks that are specific to components contents and views.

- Angular inspects directive and components classes can calls the hook methos if they are defined.

  - ngOnChanges()
  - ngOnInit()
  - ngDoCheck()
  - ngAfterContentInit()
  - ngAfterContentChecked()
  - ngAfterViewInit()
  - ngAfterViewChecked()
  - ngOnDestroy()

  ngOnChanges() of OnChanges

  Respond when Angular re set data bound input properties
  the method received a Simple Changes object of current and prvious property values.
  called before ngOnInit() and whenver one ore more data bound input properties change.

  ngOnInit of OnInit
  - Initialize the directive/component after Angular first display the data boud properties and sets the directive/components input properties.
  - Called once, after the first ngOnChanges()

  ngDoCheck() of DoCheck
  - Detect and act upon changes that Angular canto or wont detect on its own.
  - Called during every change detection run, immediately after ngOnChanges() and ngOnInit().

  ngAfterContentIinit of AfterConentInit

  - Respond after Angular projects external content into the components view.
  - called once after the first ngDoCheck()
  - A component only hook

  ngAfterContentChecked() of AfterContentChecked
   ❑ Respond after Angular checks the content projected into the component.
   ❑ Called after the ngAfterContentInit() and every subsequent ngDoCheck().
  ❑ A component-only hook.

  ngAfterViewInit() of AfterViewInit
    ❑ Respond after Angular initializes the component's views and child views.
   ❑ Called once after the first ngAfterContentChecked().
   ❑ A component-only hook.
  ngAfterViewChecked() of AfterViewChecked
   ❑ Respond after Angular checks the component's views and child views.
   ❑ Called after the ngAfterViewInit and every subsequent ngAfterContentChecked().
   ❑ A component-only hook.
  ngOnDestroy of OnDestroy
   ❑ Cleanup just before Angular destroys the directive/component. 
  ❑ Unsubscribe Observables and detach event handlers to avoid memory leaks.
  ❑ Called just before Angular destroys the directive/component

  Life Cycle Hooks - Example:
  =========================

  import { Component, OnInit, OnDestroy } from '@angular/core';
 @Component({
 selector: 'st-lifecycle',
 template: `<h1>Life Cycle Hooks</h1>`,
 })
 export class LifeCycleComponent implements OnInit, OnDestroy { 
ngOnInit() {
 console.log("Component Initialized!");
 }
 ngOnDestroy() {
 console.log("Component Destroyed!");
 }
 }

 Dependecy Injection:
 ===================

 ❑It is a coding pattern in which a class receives its dependencies from external sources rather than creating them 
itself.
 ❑Angular ships with its own dependency injection framework.
 ❑Decorators @Component, @Directive and @Pipe are subtypes of @Injectable(). 
❑The @Injectable() decorator identifies a class as a target for instantiation by an injector.
 ❑Angular creates an application-wide injector for you during the bootstrap process.
 ❑You do have to configure the injector by registering the providers that create the services the application 
requires. 
❑At runtime, injectors can read class metadata in the transpiled JavaScript code and use the constructor 
parameter type information to determine what things to inject.
 ❑You can either register a provider within an NgModule or in application components using providers property, 
which is an array.
 ❑Any provider registered within an NgModule will be accessible in the entire application

 Services:
 ==========

 ❑A service is a class with a specific purpose.
 ❑It is injected into other components and services that need it.
 ❑It must be declared as injectable using @Injectable decorator.
 ❑In order to refer to a service and get it injected into our component, we have to declare a parameter of service in 
constructor. 
❑Use services as singletons within the same injector. 
❑Use them for sharing data and functionality.
 ❑Services are ideal for sharing stateful in-memory data.
 ❑A service can depend on another service.
 ❑The Angular injector is hierarchical. When providing the service to a top level component, that instance is shared 
and available to all child components of that top level component.
 ❑When two different components need different instances of a service, it would be better to provide the service 
at the component level that needs the new and separate instance

Steps to create and use Service:
===============================

Create a class with @Injectable() decorator.
 ❑Provide required methods in this class.
 ❑Register service class with Module or a Component by listing it in providers array of @NgModule or 
@Component decorators.
 ❑In component, inject service into a property by using  a private parameter in constructor which is of service type.


 Provider Property
 =================

 ❑A service is to be registered before it is used. 
❑A service provider is to be registered with the injector, or it won't know how to create the service.
 ❑The providers property of @Component or @NgModule decorators is used to list services to be registered with 
the component or module.
 ❑When a service is registered using module it is available to all components of that module.


 log.service.ts
 ==============

  import {Injectable} from "@angular/core";
 @Injectable()
 export class LogService {
 log(msg: string ) : void {
 console.log(msg);      
}
 }


uselog.component.ts
==================

 import { Component } from '@angular/core';
 import { LogService} from './log.service';
 @Component({
 selector: 'test-log',
 templateUrl : 'app/uselog.component.html',
 providers : [ LogService ]
 })
 export class UseLogComponent {
 // Injects LogService into logService property
 constructor(private logService : LogService) {
 }
 logMessage(msg : string) : void
 {
 this.logService.log(msg);
 }
 }

Optional dependency:
===================

When a service is optional, inform Angular that the dependency is optional by annotating the constructor 
argument with@Optional().
 import { Optional} from '@angular/core';
 constructor(@Optional() private logger: LogService) {
 if(this.logger) {
 this.logger.logMessage(some_message);
 }
 }


Component Interactions:
=====================

❑Passing data from parent to child using @Input() decorator.
 ❑Sending event from child to parent using @Output() decorator.
 ❑Parent and child communicating via a service

 Input property:
 ==============
 ❑In order to send data from parent component, a property in child component must be declared as input 
property.
 ❑Input property receives data.
 ❑Input property is marked with  @Input() decorator.
 ❑It is also possible to mark input properties using  inputs array in @Component() decorator

 @Input() Example
================

course.component.ts

import { Component, Input } from '@angular/core';
 import { Course } from './Course';
 @Component({
 selector: 'course',
 templateUrl: './course.component.html'
 })
 export class CourseComponent {
 @Input() course : Course;
 }

 course.component.html

 <h2>{{course.title}}</h2>
 <h3>{{course.duration}} </h3>
 <h3>{{course.fee}} </h3>

 courses-list.component.html

  <div *ngFor="let course of courses">   
<course [course]="course"></course>
 </div>

 Parent listens to child event:
 ============================

❑Child component can emit an event to communicate with parent.
 ❑Child declares EventEmitter as an output property using @Output() decorator.
 ❑Using EventEmitter child emits event so that parent can respond to event

chile sending event to parent example

  import { Component, Input, Output, EventEmitter} from '@angular/core';
 import { Course } from './Course';
 @Component({
 selector: 'course',
 templateUrl : './course.component.html'
 })
 export class CourseComponent{
 @Output() deleteCourse = new EventEmitter<string>();
 delete() {   
this.deleteCourse.emit(this.course.title);
 } 
}

Forms:
======

 ❑An Angular form coordinates a set of data-bound user controls, tracks changes, validates input, and presents 
errors.
 ❑Angular supports two types of forms – Template Driven and Reactive


 Template Driven:
 ================
 ❑These forms are built by creating templates using Angular template syntax with form-specific directives.
 ❑Create properties that are to be bound to controls in the form. 
❑Use two-way data binding with ngModel directive.
 ❑In the application root module import FormsModule from @angular/forms.
 ❑List FormsModule in imports array of the module.
 ❑Specify form name using ngForm directive to the <form> tag.
 ❑The ngFormdirective supplements the form element with additional features. It holds the controls you created 
for the elements with an ngModel directive and name attribute, and monitors their properties, including their 
validity. It also has its own valid property which is true only if every contained control is valid.
 ❑Internally, Angular creates FormControl instances and registers them with an NgForm directive that Angular 
attached to the <form> tag. 
❑Each FormControl is registered under the name you assigned to the name attribute.
 ❑The NgModeldirective doesn't just track state; it updates the control with special Angular CSS classes that reflect 
the state.
 ❑We can leverage those class names to change the appearance of the control

 Example:

 <form (ngSubmit)="onSubmit(loginForm)" #loginForm="ngForm">
 Username <br>
 <input type="text" #uname="ngModel" [(ngModel)]="username" 
name="username"  minlength="4"   required>
 <span *ngIf="uname.dirty && uname.errors">
 <span *ngIf="uname.errors.required">Username is required! </span>
 <span *ngIf="uname.errors.minlength">Enter at least 4 chars</span>
 </span>
 <p></p>
 ...
 <button  [disabled]= "!loginForm.valid">Login</button>
 <button  [hidden]="!loginForm.dirty" type="reset">Reset</button>
 </form>

 NgForm properties:
 =================

 ❑NgForm directive creates a top-level FormGroup and binds it to form to track form values and validation status.
 ❑Associate a local template variable with ngForm directive.  Ex :   #loginForm =“ngForm”.
 ❑This template variable provides access to properties related to form and child controls.
 ❑To register child controls with the form, we have to use NgModel with name attribute. 
❑Internally, Angular creates FormControl instances and registers them with an NgForm directive that Angular 
attached to the <form> tag. 
❑Each FormControl is registered under the name you assigned to the name attribute.

controls
 dirty
 errors
 invalid
 valid
 value
 touched
 submitted

 Reactive Forms (Model Driven Forms)
 ===================================

  ❑In this we create a tree of Angular form control objects in the component class and bind them to native form. 
control elements in the component template.
 ❑You create and manipulate form control objects directly in the component class.
 ❑Here are steps to create Reactive Form:
 ✓ Create data model
 ✓ Create reactive form component like FormGroup and FormControl
 ✓ Create template - html
 ✓ Import ReactiveFormsModule and include in modules array of Module

 Making Ajax calls with HttpClient Module:
 ===============================

  ❑The AngularHttpclient communicates with the server using a familiar HTTP request/response protocol. 
❑TheHttpclient is one of a family of services in the Angular HTTP library -@angular/common/http.
 ❑Before you can use theHttpclient, you need to register it as a service provider with the dependency injection 
system.
 import { HttpClientModule} from '@angular/common/http';
 @NgModule({
 imports: [
 BrowserModule,
 HttpClientModule
 ],
 })
 export class AppModule {
 }

Using Promise:
==============

import { Component } from '@angular/core';
 import { Book } from './Book';
 import { HttpClient, Response } from '@angular/common/http';
 @Component({
 selector: 'st-books',  templateUrl: 'books.component.html'
 })
 export class BooksPromiseComponent {
 books: Book[];
 constructor(private http: HttpClient) {
 }
 ngOnInit() {
 this.http.get("assets/books.json")
 .toPromise()
 .then( response => this.books = response.json());
 }
 }

======
Observable:

❑Angular uses Observables to connect to backend servers.
 ❑Observable is a concept introduced in a library called Reactive extensions – reactivex.io.
 ❑An Observable represents an asynchronous data stream where data arrives asynchronously.
 ❑An observer (subscriber or watcher) subscribes to an Observable. 
❑Observer reacts to whatever item or sequence of items the Observable emits


A publisher creates an Observable instance that defined a subscriber function.
 ❑Subscriber function is executed when a consumer calls subscribe() method.
 ❑To begin receiving notifications, we need to call subscribe() method. 
❑We can call unsubscribe() method to stop receiving notification.
 ❑Data published by an observable is known as a stream.


  import { Component } from '@angular/core';
 import { Observable } from 'rxjs';
 @Component({
 selector: 'st-time',
 template: `<h1>{{time}}</h1> <button (click)="stopTimer()">Stop Timer</button> 
<button (click)="startTimer()">Start Timer</button>`})
 export class TimeComponent {
 time : string;
 subscriber : any;
 timeObservable = Observable.create( 
function(observer) {
 const interval = setInterval(() => observer.next(new Date().toString()),1000);
 // returns process to clean up resources 
return () => clearInterval(interval); } 
)

Http class is used to make AJAX calls using methods like get(), post(), delete() and put().
 ❑In order to use HttpClient, we need to import it from @angular/common/http.
 ❑Inject HttpClient into our component using DI mechanism in Angular, i.e. as a parameter to constructor.
 ❑Use get() method of HttpClient class and provide URL of the endpoint. 
❑Return type of get() is  Observable<any>.
 ❑Client should consume the value coming from Observable by subscribing to Observable using subscribe() 
method.
 ❑It is possible to perform operations on Observable using operators provided by RxJS library.  
❑Each code file in RxJS should add the operators it needs by importing from an RxJS library.
 ❑Response object contains data coming from server that is already converted to JSON.

  get(url: string, options?: RequestOptionsArgs) : Observable<any>
 post(url: string, body: any, options?: RequestOptionsArgs) : Observable<any>
 put(url: string, body: any, options?: RequestOptionsArgs) : Observable<any>
 delete(url: string, options?: RequestOptionsArgs) : Observable<any>

 list-books.component.ts:
 =======================

  import { Component } from '@angular/core';
 import { OnInit } from '@angular/core';
 import { Book } from './Book';
 import { HttpClient} from '@angular/common/http';
 @Component({
 selector: 'st-books',
 templateUrl: 'app/http/list-books.component.html'
 })
 export class ListBooksComponent implements OnInit {
 books: Book[];
 constructor(private http: HttpClient) {
 }
 ngOnInit() {
 this.http.get<Book[]>("assets/books.json")
 .subscribe( resp => this.books = resp);
 }
 }


 <html>
 <head>
 <title>Books</title>
 </head>
 <body>
 <h1>Books</h1>
 <table border="1" style="width:100%">
 <tr>
 <th>Title</th>
 <th>Author</th>
 <th>Price</th>
 </tr>
 <tr *ngFor="let b of books">
 <td> {{ b.title }} </td>
 <td> {{ b.author }} </td>
 <td> {{ b.price }} </td>
 </tr>
 </table>
 </body>
 </html>

Routing:
=========

Routing allows users to move from one view to another view using different URLs in the client.
 ❑The Angular router is an external, optional Angular NgModule called RouterModule. 
❑The router is a combination of multiple provided services (RouterModule), multiple directives (RouterOutlet, 
RouterLink, RouterLinkActive), and a configuration (Routes).
 ❑Router can interpret a browser URL as an instruction to navigate to a client-generated view. 
❑It can pass optional parameters along to view component.

Route Configuration:
====================

 ❑A routed Angular application has one singleton instance of theRouterservice. 
❑When the browser's URL changes, that router looks for a correspondingRoutefrom which it can determine 
the component to display.
 ❑A router has no routes until you configure it.
 ❑We need to pass the array of Routes objects to RouterModule.forRoot() to configure the router.
 ❑EachRoutemaps a URLpathto a component. There areno leading slashesin thepath. The router parses 
and builds the final URL for you, allowing you to use both relative and absolute paths when navigating 
between application views.
 @NgModule(
 { declarations: [AuthorsListComponent, AuthorDetailsComponent, MainComponent],
 imports: [RouterModule.forRoot(appRoutes)],
 providers: [],
 bootstrap: [MainComponent]
 })
 export class AppModule {

 }

const appRoutes: Routes = [ 
{ path: 'list', component: AuthorsListComponent }, 
{ path: 'details/:id', component:  AuthorDetailsComponent },  
{ path: '', component : HomeComponent, pathMatch : 'full'},  
{ path: '**', component: HomeComponent}
 ];

 ❑The:idin the third route is a token for a route parameter. In a URL such as/details/1, "1" is the value of 
theidparameter.  
❑Thedataproperty in route is a place to store arbitrary data associated with this specific route. The data 
property is accessible within each activated route. Use it to store items such as page titles, breadcrumb text, 
and other read-only,staticdata.
 ❑Theempty path represents the default path for the application, the place to go when the path in the URL is 
empty
❑The**path in the last route is a wildcard. The router will select this route if the requested URL doesn't match 
any paths for routes defined earlier in the configuration.
 ❑The order of the routes in the configuration matters and this is by design. The router uses a first-match 
wins strategy when matching routes, so more specific routes should be placed above less specific routes.
 ❑A redirect route requires a pathMatch property to tell the router how to match a URL to the path of a 
route. Value full means the entire URL must match the given string. 

Given this configuration, when the browser URL for this application becomes /list, the router matches that URL 
to the route path /list and displays AuthorsListComponent in RouterOutlet that you've placed in the host view's 
HTML

<router-outlet></router-outlet>

❑Most of the time you navigate as a result of some user action such as the click of an anchor tag.
 ❑TheRouterLink directives on the anchor tags give the navigation.
 ❑TheRouterLinkActive directive on each anchor tag helps visually distinguish the anchor for the currently 
selected "active" route. 
❑The router adds the active CSS class to the element when the associated RouterLink becomes active. 
[<a routerLink="/home" routerLinkActive="active">Home</a>]
 [<a routerLink="/list" routerLinkActive="active">List Authors</a>]

  ❑Route parameters are used to pass data to a page.
 ❑Parameters are prefixed with : (colon) in URL.
 ❑For example, in URL /details/:id, id is route parameter.
 ❑We can have multiple parameters each separated with /. 
❑For example, if we have a URL /author/:id/:subject then actual URL is /author/10/angular.
 ❑You need to pass values to parameters using routerLink directive as shown below:
 <a [routerLink]="['/details', author.id]"> {{author.name}}</a>

  ❑In order to receive values of route parameters we need to inject ActivatedRoute object into our component and 
then read route parameter using params collection of snapshot of route.
 ❑It is also possible to subscribe to params observable.
 export class AuthorDetailsComponent {
 constructor(private route: ActivatedRoute, private router : Router) { 
}
 ngOnInit(): void {
 this.route.params.subscribe( params => {
 this.id =  params["id"];
 });

 // alternatively we can read param from snapshot
 this.id = this.route.snapshot.params["id"]; 
}
 // rest of code 
}

Route Guard
===========

A Route Guard is used to check whether navigation to route or from route is allowed.
 ❑A guard can navigate elsewhere, cancelling the current navigation.
 ❑A guard returns true or false. True will allow navigation process to continue and false stops navigation.
 ❑The following are available guards : 
✓ CanActivate to mediate navigation to a route.
 ✓ CanActivateChild to mediate navigation to a child route.
 ✓ CanDeactivate to mediate navigation away from the current route.
 ✓ Resolve to perform route data retrieval before route activation.
 ✓ CanLoadto mediate navigation to a feature module loaded asynchronously

Create Route Guard:
==================

❑Create a class that implements interface related to Route Guard.
 ❑Use @Injectable() decorator with class.
 ❑Define method declared in interface and return either true or false from that method.
 import { Injectable }     from '@angular/core';
 import { CanActivate }    from '@angular/router';
 @Injectable()
 export class AuthGuard implements CanActivate {
 canActivate() {
 If (ok_to_allow_user)
 return true;
 else {
 // take action like redirecting user to login page
 return false;
 }
 }
 }

Associate Guard with Route Guard:
================================

const appRoutes: Routes = [
 { path: 'admin', 
component: AdminComponent, 
canActivate: [AuthGuard]
 },
 …
 ]


 Declare Route Guard in Providers Array:
 ======================================

  @NgModule({
 declarations: 
[ . . .],
 imports:
 [BrowserModule, FormsModule, HttpModule,
 RouterModule.forRoot(appRoutes)],
 providers:
 [AuthGuard],
 bootstrap: 
[MainComponent]
 })
 export class AppModule { }

 Deployment:
 ===========

 ❑Making Angular application available to a server running remotely.
 ❑When run in production, we need to optimize application size and performance. 
❑Not all files in development are needed in production environment.

AOT - Ahead of time - compilation ..
====================================

❑The Angular Ahead-of-Time compiler pre-compiles application components and their templates during the 
build process.
 ❑Apps compiled with AOT launch faster for following reasons: 
✓ Application components execute immediately, without client-side compilation.
 ✓ Templates are embedded as code within their components, so there is no client-side request for template 
files.
 ✓ You don't download the Angular compiler, which is pretty big on its own.
 ✓ The compiler discards unused Angular directives that a tree-shaking tool can then exclude

Build projected
===============

❑Use ng build to build project for deployment.
 ❑Artifacts built by ng build are stored in distfolder of the project. 
❑Must be run from the folder in which angular cli placed project artifacts.
 ❑Build can be either for production (--prod) or development  (--dev) environment.
 ❑All builds make use of bundling and limited tree-shaking, while --prod builds also run limited dead code 
elimination via UglifyJS.


ng build --prod













