1. Install Angular CLI
Ensure you have Node.js installed, then install Angular CLI globally:

npm install -g @angular/cli

2. Create a New Angular Project
Run the following command to create a new project:

ng new angular-demo

Choose CSS or any other styling option when prompted.
Navigate to the project directory:

cd angular-demo

3. Serve the Application
Start the development server:

ng serve

Visit http://localhost:4200 in your browser to see the default Angular app.

<hr></hr>
4. Add a Component
Generate a new component:
ng generate component demo

Update the app.component.html to include the new component:

<app-demo></app-demo>

5. Demo Component Example
Update the demo.component.ts:

import { Component } from '@angular/core';

@Component({
  selector: 'app-demo',
  templateUrl: './demo.component.html',
  styleUrls: ['./demo.component.css']
})
export class DemoComponent {
  title = 'Angular Demo';
  items = ['Item 1', 'Item 2', 'Item 3'];

  addItem(newItem: string) {
    if (newItem) {
      this.items.push(newItem);
    }
  }
}

Update the demo.component.html:
<h2>{{ title }}</h2>
<input #newItem type="text" placeholder="Add an item" />
<button (click)="addItem(newItem.value); newItem.value=''">Add</button>
<ul>
  <li *ngFor="let item of items">{{ item }}</li>
</ul>

6. Run the Application
Restart the server if needed:
ng serve

Visit http://localhost:4200 to see your demo project in action.

Routing in Angular:
To set up routing in your Angular demo project, follow these steps:
1. Generate a Routing Module
Run the following command to create a routing module:
ng generate module app-routing --flat --module=app

This creates a file app-routing.module.ts and automatically imports it into app.module.ts.

<hr></hr>
2. Define Routes
Update the app-routing.module.ts file to define your routes:

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { DemoComponent } from './demo/demo.component';

const routes: Routes = [
  { path: '', redirectTo: '/demo', pathMatch: 'full' },
  { path: 'demo', component: DemoComponent },
  { path: '**', redirectTo: '/demo' } // Wildcard route for 404
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}

3. Add Router Outlet
In the app.component.html, add the <router-outlet> directive:
4. Update app.module.ts
Ensure the AppRoutingModule is imported in app.module.ts:
import { AppRoutingModule } from './app-routing.module';

@NgModule({
  declarations: [
    // Your components
  ],
  imports: [
    AppRoutingModule,
    // Other modules
  ],
  bootstrap: [AppComponent]
})
export class AppModule {}
5. Test the Routes
Start the application:

ng serve
Navigate to http://localhost:4200/demo to see the DemoComponent.

To add navigation links to your Angular routing setup, you can use the RouterLink directive in your HTML. Here's how you can do it:
Steps:
Update the app.component.html: Add navigation links using the RouterLink directive.
<nav>
  <a routerLink="/demo" routerLinkActive="active">Demo</a>
  <a routerLink="/another-route" routerLinkActive="active">Another Route</a>
</nav>
<router-outlet></router-outlet>
Add a New Route: Update the routes array in app-routing.module.ts to include the new route.
const routes: Routes = [
  { path: '', redirectTo: '/demo', pathMatch: 'full' },
  { path: 'demo', component: DemoComponent },
  { path: 'another-route', component: AnotherComponent },
  { path: '**', redirectTo: '/demo' }
];
Generate a New Component (if needed): If AnotherComponent doesn't exist, generate it:

ng generate component another
Style Active Links: Add styles for the active class in your CSS file:


a.active {
  font-weight: bold;
  color: blue;
}
Now, clicking the links will navigate between the defined routes.
To implement lazy loading in your Angular project, follow these steps:

1. Create a Feature Module
Generate a new module for the feature you want to lazy load:
ng generate module feature-name --route feature-name --module app.module

This command automatically sets up the routing for the feature module.

<hr></hr>
2. Update the AppRoutingModule
Ensure the feature module is loaded lazily in the app-routing.module.ts:

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  { path: '', redirectTo: '/home', pathMatch: 'full' },
  { path: 'feature-name', loadChildren: () => import('./feature-name/feature-name.module').then(m => m.FeatureNameModule) },
  { path: '**', redirectTo: '/home' } // Wildcard route for 404
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}

3. Set Up the Feature Module
Ensure the feature-name.module.ts has its own routing

import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FeatureNameComponent } from './feature-name.component';

const routes: Routes = [
  { path: '', component: FeatureNameComponent }
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class FeatureNameRoutingModule {}

@NgModule({
  declarations: [FeatureNameComponent],
  imports: [FeatureNameRoutingModule]
})
export class FeatureNameModule {}

<hr></hr>
4. Test the Lazy Loading
Run the application:

Navigate to /feature-name in the browser. The feature module will load only when the route is accessed.































