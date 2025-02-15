
Install Node JS, VS Code

what is type script ..

type script sits on top of java script

type script always converted to java script it data types and java script.

dynamic typed langauage ..

Anders Hejisberg (designer of C#) at Microsoft
involved in creation to type script.

Typescript program -- typescript compiler -- java script
-- browser ..

eventually everything is java script, we need to have typescript compiler.

> npm install -g typescript

g stands for global

tsc is typescript compiler --> tsc --version

Version 5.7.3

>tsc hello.ts
>node hello.js

Data types:
typescript - all about datatypes ensuring all values are
assigned properly whereas javascript there is no type checking.
var num : number;
num = 10;
num = "Abc";
java script
var num;

you can use typescripting.org ... playground

first create typescript config file

tsc --init > this will create tsconfig.json

tsconfig.json .. your program convert to target ecma script 2016

java script ES5

--> run the type script in watch mode
tsc --watch
hellouser.ts
function sayHello(person : string) {
 return "Hello, " + person;
 }
 var user = "Srikanth Pragada";
 document.write(sayHello(user));

 ==========
 <!DOCTYPE html>
 <html>
 <head>
 <title>TypeScript Demo</title>
 <script src="hello.js"></script>
 </head>
 <body>
 </body>
 </html>

 Angular:

 Install Angular CLI using NPM as follows: 

 npm install -g @angular/cli

 for demo project
 ng new demo

  Component ngg component my-new-component
 Directive ng g directive my-new-directive
 Pipe ng g pipe my-new-pipe
 Service ng g service my-new-service
 Class ng g class my-new-class
 Guard ng g guard my-new-guard
 Interface ng g interface my-new-interface
 Enum ngg enummy-new-enum
 Module ngg module my-module

 =======

 Server watches your files and rebuilds app whenever you make changes to files in folder.

 ng serve

  Go to browser and navigate to following URL:

  http://localhost:4200


  It is possible to start server on a differ port number
than default ..
ng serve -port 3000

Important files in project folder:

- app/app.module.ts
  Defines app module, the root module that tells angular how to assemble the application. Right now it declares on AppComponent.

  -app/app.component.{ts,html,css,spec.ts}
  Defines the AppComponent along with an HTML Template, CSS style sheet and a unit test. It is the root component of what will become a tree of nested components as the application evolves.

  -index.html
  The main HTML page that is served when someone visits your site. you will never need to edit it, CLI automatically adds all js and css files when building your app, so you never need to add any scripts or tags here manually.

  -main.ts
  The main entry point for your app. Compiles the application with JIT compiler and bootstraps the application root module(AppModule) to run in the browser

  Building Blocks

  Modules, Components, Templates, Metadata, Data binding, Directives, Services and Dependency Injection

  Module:
  ========
  A module is class that is decorated with @NgModule decorator.
  Every application contains at least one module called root module conventionally called as App Module.
  NgModule decorator provide information about module using this properties listed below
   - Declaration - Classes that belong to this module. They may be components,directives, pipes
   - Export - The subset of declarations that should be visible to other modules.
   - Imports - specifies modules whose exported classes are needed in this module.
   - Bootstrap - Specifies the main application view - root component. it is based for the rest of the appliction.

import { NgModule } from '@angular/core'
import { BrowserModule } from '@angular/platform-browser'
import { FirstComponent } from './first.component'

@NgModule({
    imports: [ BrowserModule],
    declarations: [ FirstComponent],
    bootstrap: [ FirstComponet]
})

exports class AppModule {}


Component:

- A component controls a part of the screen called view.
- Every component is a class with its own data and code.
- A component may depend on services that are injected using dependency injection.
- The template, metadata and component together describe a view.
- Components are decorated with @Component decorator through which we specify template, stye and selector(tag) related to component.
- properties like templateUrl,styleUrl and providers can als be used.

import {Component } from '@angular/core'

@Component({
    selector: 'my-first',
    templateUrl : './first.component.html'
})

export class FirstComponent{
    title : string = "Srikant Technologies";
}


Template:

- Components view is defined with its companion template.
- A template is in the form of HTML that tells Angular how to render the component.
- Template is the user interface(UI) of component.
- Template can use the following:
 - HTML
 - Interpolation {{...}}
 - Data binding
 - Template reference varaibles
 - Pipes
        <html>
        <body>
        <h1> {{courseName}}</h1>
        <ul>
            <li *ngFor="let topic of topics"> {{ topic }} </li>
        </ul>
        </body>
        </html>

Interpolation:

- when you put properties in view template using {{}}, it is called interpolation.

- Angular updates the display whenever property changes.

- The context of the expression is component instance that is associated with the view.

- The expression is evaluated, converted to string and then sent to client.

- From the expression, we can call methods of component associated with view

- The target of the template expression may be HTML element, a component or a directive.

- In case of assigning value to a property, template expression may appear in double quotes.

<span [hidden]="isNew">Modified</span>
<img src="{{filename}}"/>


Template Statement:

- A template statement responds to an event raised by a binding target such as element, directive.

- The template statement parser differs from the template expression parse and specially basic assignment(=) and chaining expressions(with; or)

- Template statements cannot refer to anything in the global namespace. Thye can not refer to window or document. they cant call console.log or Math.max.

- the following expressions of Javascript are NOT allowed:
 - new
 - increment and decrement operator, ++ and --
 - operator assignment, such as += and -=
 - the bitwise operators | and &
 - the template expression operators

  <button (click)="calculate()">Calculate</button>
  <button (click)="onSave($event)">Save</button>

Data Binding:

Data binding allows copying values from Component properties to attributes of HTML elements.

- Following are different bindings available:
 - Property Binding
 - Event Binding
 - Attribute binding
 - Class binding
 - Style binding

Property Binding:

- Binds value to a property in HTML element or Angular Component.
- Target property must be a property and not just an attribute in DOM element.

{{expression}}
[targetproperty]="expression"
bind-targetproperty="expression"

<img [src]="heroImageUrl">
<img bind-src="heroImageUrl">
<imge src="{{imageUrl}}">

HTML Attribute Vs. DOM Property

- Attributes are defined by HTML
- Properties are defined by the DOM.
- A few HTML attributes have 1:1 mapping to properties Example: id
- some HTML attributes dont have corresponding properties ex:colspan
- some DOM properties dont have corresponding attributes. ex: innerHTML
- Value of property might change at runtime but value of attribute doesn't change. ex" value.

- Angular Property Bindings deals with DOM propertiey
and  not HTML attributes

Atribute Binding
 - Sets the value of attribute directly.
 Class Binding
  - Add or removes CSS class names from element's class attribute.

Style Binding
 - Sets inline styles.
 Event Binding
 - Event binding syntax consists of a target event name within paraentheses on the left of an equal sign and quoted template statement on the right.

 <button (click)="onSave">Save</button>

 Attribute Directives

 ngClass - add and remove a set of CSS classes
 ngStyle - Add and remove a set of HTML styles
 ngModel - Two-way data binding to HTML form element

 Structure Directives

 - ngIf - Conditionally adds or remvoes and element from DOM
 - ngeFor - Repeats a template for each item in the list
 - ngSwitch - Adds one element from a set of possible elements based on condition. Used with ngSwitchCase and ngSwtichDefault.

 <div *ngIf="condition">Add Divto DOM when condition is true </div>

 <div *ngFor="let topic of topics; let i=index; let first=first;letoddRow=odd">
 <h2 *ngIf="first">List Of Topics</h2>
 <span [class.red]="oddRow">
 {{i+ 1}} -{{topic}} 
</span>    
</div>

 <div [ngSwitch]="mode">
 <h1   *ngSwitchCase="'f'">Flight {{flight}} </h1>
 <h2   *ngSwitchCase="'t'">Train  {{train}}  </h2>
 <h3   *ngSwitchDefault>Private Transport</h3>
 </div>

 Pipes:

 A pipe takes data as input and transforms it to required output.
 ❑Angular provides built-in pipes for many common requirements.
 ❑Pipes are used in template.
 ❑Pipes can also take optional parameters to fine tune output.
 ❑To add parameters to a pipe, follow the pipe name with a colon ( : ) and then the parameter value (such as 
currency : 'EUR'). 
❑If the pipe accepts multiple parameters, separate the values with colons (such as slice:1:5).
 ❑You can chain pipes together so that output of one pipe goes to another pipe as input.
 ✓ DatePipe
 ✓ JsonPipe
 ✓ LowerCasePipe
 ✓ CurrencyPipe
 ✓ DecimalPipe
 ✓ PercentPipe
 ✓ SlicePipe
 ✓ UpperCasePipe
 ✓ TitleCasePipe

 Date Pipe
  -  date_expression | date [:format]

  {{ dateObj | date }}          // output is 'Apr 11, 2017'
 {{ dateObj | date:'medium' }}   // output is 'Apr 11, 2017, 09:43:11 PM' 
{{ dateObj | date:'shortTime’}} // output is '9:43 PM'
 {{ dateObj | date:'mmss' }}     // output is '43:11'


DecimalPipe

    -number_expression | number [:digitInfo]

Currency Pipe
  - number_expression | currency [:currencyCode[:symbolDisplay [:digitInfo]]


Percent Pipe

number_expression | percent [:digitInfo]

{{ .20 | percent }}                 //  results 20%
 {{ 0.125539 | percent:'2.2-3' }}    // results in 12.55

  Slice Pipe

   array_or_string_expression | slice :start [:end]

   {{str | slice:0:4}}
 {{str | slice:-4}}
 {{str | slice:4:0}}

 Custom Pipes:
 ======

 Create a class and decorate it with @Pipe decorator.
 ❑The pipe class implements PipeTransform interface's transform method that accepts an input value followed 
by optional parameters and returns the transformed value.
 ❑There will be one additional argument to the transform method for each parameter passed to the pipe. 
❑The@Pipedecorator allows you to define the pipe name that you'll use within template expressions. It must 
be a valid JavaScript identifier.
 ❑You must include your pipe in the declarations array of the AppModule.

import {Pipe, PipeTransform } from '@angular/core';
 @Pipe({name: 'brackets'})
 export class BracketsPipe implements PipeTransform
 {
 transform(value: string, newcase : string = 'n') {
 if (newcase == 'u')
 value = value.toUpperCase();
 else
 if (newcase == "l")
 value = value.toLowerCase();
 return "[" + value + "]";
 }
 }

pipedemo.component.ts:

 import { Component } from '@angular/core';
 @Component({
 selector: 'my-pipes',
 template: `<h2>Custom Pipes Demo </h2>
 {{ title | brackets }}
 <p></p>
 {{ title | brackets:'u'}}
 `
 })
 export class PipesDemoComponent{ 
title : string = "Srikanth Technologies";
 }

app.module.ts

import { BrowserModule } from '@angular/platform-browser';
 import { NgModule } from '@angular/core';
 import {PipesDemoComponent}  from './pipesdemo.component';
 import {BracketsPipe} from './brackets.pipe'
 @NgModule({
 declarations: [
 PipesDemoComponent, BracketsPipe
 ],
 imports: [
 BrowserModule
 ],
 providers: [],
 bootstrap: [PipesDemoComponent]
 })
 export class AppModule { }

