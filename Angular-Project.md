Creating an Angular project from scratch involves setting up Angular CLI, generating components, services, routing, and implementing basic functionality. In this example, we will build a simple Task Management application where you can:

Add tasks
View tasks
Delete tasks
Here’s an end-to-end implementation of an Angular project:

1. Set Up the Angular Project
First, make sure that you have Node.js and Angular CLI installed.

Install Angular CLI globally if you don't have it already:
bash
Copy
npm install -g @angular/cli
Create a new Angular project:
bash
Copy
ng new task-manager
This will prompt you to choose whether to add routing and which CSS style to use. Choose "Yes" for routing and select your preferred CSS option (e.g., SCSS, CSS, etc.).

Navigate to your project directory:
bash
Copy
cd task-manager
Start the development server:
bash
Copy
ng serve
By default, the app will run at http://localhost:4200.

2. Project Structure
The basic structure of the Angular app will look like this:

arduino
Copy
task-manager/
 ├── src/
 │    ├── app/
 │    │    ├── components/
 │    │    │    ├── task-list/
 │    │    │    ├── task-item/
 │    │    ├── services/
 │    │    │    ├── task.service.ts
 │    │    ├── app.component.ts
 │    │    ├── app.module.ts
 ├── assets/
 ├── environments/
 └── styles.css
3. Create the Task Model
We will start by creating a simple Task model.

Create a new file src/app/models/task.ts and define the Task interface:
typescript
Copy
// src/app/models/task.ts
export interface Task {
  id: number;
  title: string;
  completed: boolean;
}
4. Create the Task Service
The service will handle the logic for managing tasks (add, delete, fetch).

Generate a service using Angular CLI:
bash
Copy
ng generate service services/task
Define the service in src/app/services/task.service.ts:
typescript
Copy
// src/app/services/task.service.ts
import { Injectable } from '@angular/core';
import { Task } from '../models/task';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private tasks: Task[] = [
    { id: 1, title: 'Learn Angular', completed: false },
    { id: 2, title: 'Build a task manager', completed: false }
  ];

  constructor() { }

  getTasks(): Task[] {
    return this.tasks;
  }

  addTask(title: string): void {
    const newTask: Task = {
      id: this.tasks.length + 1,
      title: title,
      completed: false
    };
    this.tasks.push(newTask);
  }

  deleteTask(id: number): void {
    this.tasks = this.tasks.filter(task => task.id !== id);
  }

  toggleTaskCompletion(id: number): void {
    const task = this.tasks.find(t => t.id === id);
    if (task) {
      task.completed = !task.completed;
    }
  }
}
5. Create the Task List Component
Now, we will create a component that displays the list of tasks.

Generate a component using Angular CLI:
bash
Copy
ng generate component components/task-list
In src/app/components/task-list/task-list.component.ts, use the TaskService to fetch and display tasks:
typescript
Copy
// src/app/components/task-list/task-list.component.ts
import { Component, OnInit } from '@angular/core';
import { TaskService } from '../../services/task.service';
import { Task } from '../../models/task';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {
  tasks: Task[] = [];

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.tasks = this.taskService.getTasks();
  }

  deleteTask(id: number): void {
    this.taskService.deleteTask(id);
    this.tasks = this.taskService.getTasks();  // Re-fetch tasks after deletion
  }

  toggleCompletion(id: number): void {
    this.taskService.toggleTaskCompletion(id);
    this.tasks = this.taskService.getTasks();  // Re-fetch tasks after toggling completion
  }
}
6. Create the Task Item Component
Next, let’s create a component for each individual task.

Generate the component:
bash
Copy
ng generate component components/task-item
In src/app/components/task-item/task-item.component.ts, display individual task details and provide buttons to delete and toggle completion:
typescript
Copy
// src/app/components/task-item/task-item.component.ts
import { Component, Input, Output, EventEmitter } from '@angular/core';
import { Task } from '../../models/task';

@Component({
  selector: 'app-task-item',
  templateUrl: './task-item.component.html',
  styleUrls: ['./task-item.component.css']
})
export class TaskItemComponent {
  @Input() task!: Task;  // Input from parent component (task list)
  @Output() delete = new EventEmitter<number>();  // Output for delete action
  @Output() toggle = new EventEmitter<number>();  // Output for toggle completion

  onDelete() {
    this.delete.emit(this.task.id);
  }

  onToggleCompletion() {
    this.toggle.emit(this.task.id);
  }
}
7. Update Templates for Components
Now, let's update the HTML templates for the components.

task-list.component.html - List of tasks with add, delete, and toggle options:
html
Copy
<!-- src/app/components/task-list/task-list.component.html -->
<div>
  <h2>Task Manager</h2>
  <ul>
    <li *ngFor="let task of tasks">
      <app-task-item
        [task]="task"
        (delete)="deleteTask($event)"
        (toggle)="toggleCompletion($event)"
      ></app-task-item>
    </li>
  </ul>

  <input type="text" #newTaskTitle />
  <button (click)="addTask(newTaskTitle.value)">Add Task</button>
</div>
task-item.component.html - Each individual task with delete and toggle options:
html
Copy
<!-- src/app/components/task-item/task-item.component.html -->
<div>
  <span [style.textDecoration]="task.completed ? 'line-through' : 'none'">
    {{ task.title }}
  </span>
  <button (click)="onToggleCompletion()">Toggle Completion</button>
  <button (click)="onDelete()">Delete</button>
</div>
8. Update the App Component
Now, let’s add the TaskListComponent to the app.component.html so it is rendered when the app starts.

In src/app/app.component.html, include the task-list component:
html
Copy
<!-- src/app/app.component.html -->
<app-task-list></app-task-list>
9. Adding Styles (Optional)
You can style the application as per your needs. Let’s add a basic style in src/styles.css:

css
Copy
/* src/styles.css */
body {
  font-family: Arial, sans-serif;
  padding: 20px;
}

h2 {
  color: #333;
}

ul {
  padding-left: 20px;
}

li {
  margin-bottom: 10px;
}

button {
  margin-left: 10px;
  padding: 5px 10px;
  cursor: pointer;
}

input {
  margin-right: 10px;
  padding: 5px;
}
10. Run the Application
With everything set up, start the Angular development server again (if not already running):

bash
Copy
ng serve
Visit http://localhost:4200 to see your Task Management App in action!

11. Conclusion
Here’s a quick summary of what we built:

Task Model: Defined a simple Task interface with properties like id, title, and completed.
Task Service: Created a service that handles the logic for managing tasks (adding, deleting, toggling completion).
Components: Built a TaskListComponent to display tasks, and a TaskItemComponent to represent each individual task.
Event Handling: Set up event binding to allow task deletion and completion toggling.
This is just the beginning. You can extend this app further by adding features like:

Persisting tasks with a backend API.
Implementing authentication and authorization.
Adding advanced task filtering and sorting options.
Let me know if you have any questions or need further clarification on any part of the project!