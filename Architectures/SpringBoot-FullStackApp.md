Absolutely! Let’s build a simple end-to-end Spring Boot + Angular full-stack application that you can explain easily in an interview. I’ll make it simple, focused on core concepts, and easy to walk through.

We’ll do a “Task Management App” where users can add tasks and view tasks.

1. Backend: Spring Boot
Step 1: Create Spring Boot project

Dependencies:

Spring Web

Spring Data JPA

H2 Database (in-memory for simplicity)

Spring Boot DevTools

Step 2: Define Entity
package com.example.demo.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;

@Entity
public class Task {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;
    private String title;
    private boolean completed;

    // getters and setters
    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getTitle() { return title; }
    public void setTitle(String title) { this.title = title; }
    public boolean isCompleted() { return completed; }
    public void setCompleted(boolean completed) { this.completed = completed; }
}

Step 3: Repository
package com.example.demo.repository;

import com.example.demo.model.Task;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TaskRepository extends JpaRepository<Task, Long> {
}

Step 4: Service
package com.example.demo.service;

import com.example.demo.model.Task;
import com.example.demo.repository.TaskRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TaskService {

    private final TaskRepository repo;

    public TaskService(TaskRepository repo) {
        this.repo = repo;
    }

    public Task saveTask(Task task) {
        return repo.save(task);
    }

    public List<Task> getTasks() {
        return repo.findAll();
    }
}

Step 5: Controller
package com.example.demo.controller;

import com.example.demo.model.Task;
import com.example.demo.service.TaskService;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@CrossOrigin(origins = "http://localhost:4200")
@RequestMapping("/api/tasks")
public class TaskController {

    private final TaskService service;

    public TaskController(TaskService service) {
        this.service = service;
    }

    @GetMapping
    public List<Task> getAllTasks() {
        return service.getTasks();
    }

    @PostMapping
    public Task createTask(@RequestBody Task task) {
        return service.saveTask(task);
    }
}


@CrossOrigin allows Angular frontend to call Spring Boot APIs.

Step 6: Application properties
spring.h2.console.enabled=true
spring.datasource.url=jdbc:h2:mem:taskdb
spring.datasource.driverClassName=org.h2.Driver
spring.datasource.username=sa
spring.datasource.password=
spring.jpa.hibernate.ddl-auto=update

2. Frontend: Angular
Step 1: Create Angular project
ng new task-app
cd task-app
ng generate service task
ng generate component task-list

Step 2: Angular Service
// task.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Task {
  id?: number;
  title: string;
  completed: boolean;
}

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private baseUrl = 'http://localhost:8080/api/tasks';

  constructor(private http: HttpClient) { }

  getTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(this.baseUrl);
  }

  createTask(task: Task): Observable<Task> {
    return this.http.post<Task>(this.baseUrl, task);
  }
}

Step 3: Angular Component
// task-list.component.ts
import { Component, OnInit } from '@angular/core';
import { TaskService, Task } from '../task.service';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.css']
})
export class TaskListComponent implements OnInit {
  tasks: Task[] = [];
  newTask: string = '';

  constructor(private taskService: TaskService) { }

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks() {
    this.taskService.getTasks().subscribe(data => this.tasks = data);
  }

  addTask() {
    if (!this.newTask.trim()) return;
    const task: Task = { title: this.newTask, completed: false };
    this.taskService.createTask(task).subscribe(t => {
      this.tasks.push(t);
      this.newTask = '';
    });
  }
}

Step 4: Angular Template
<!-- task-list.component.html -->
<div>
  <h2>Task List</h2>
  <input type="text" [(ngModel)]="newTask" placeholder="New task">
  <button (click)="addTask()">Add</button>

  <ul>
    <li *ngFor="let task of tasks">
      {{task.title}} - {{task.completed ? 'Done' : 'Pending'}}
    </li>
  </ul>
</div>

Step 5: Enable HttpClientModule and FormsModule
// app.module.ts
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

@NgModule({
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
})
export class AppModule { }

3. How to run

Start Spring Boot backend (mvn spring-boot:run) → runs on localhost:8080.

Start Angular frontend (ng serve) → runs on localhost:4200.

Open http://localhost:4200 → Add tasks → Tasks appear in the list → Stored in H2 database.

4. Key points to explain in interview
Layer	Role
Angular UI	Sends HTTP requests, displays task list
Angular Service	Calls Spring Boot REST APIs via HttpClient
Spring Boot Controller	Receives API calls, delegates to service layer
Spring Boot Service	Business logic (save and retrieve tasks)
Spring Boot Repository	Persists data to database (H2 in-memory)

When a task is added, the backend publishes a Kafka event.

A Kafka consumer receives the event and logs it (simulating another microservice).

1. Add Kafka Dependencies (Spring Boot)

Add to pom.xml:

<dependency>
    <groupId>org.springframework.kafka</groupId>
    <artifactId>spring-kafka</artifactId>
</dependency>

2. Configure Kafka

Add in application.properties:

spring.kafka.bootstrap-servers=localhost:9092
spring.kafka.producer.key-serializer=org.apache.kafka.common.serialization.StringSerializer
spring.kafka.producer.value-serializer=org.apache.kafka.common.serialization.StringSerializer
spring.kafka.consumer.group-id=task-group
spring.kafka.consumer.key-deserializer=org.apache.kafka.common.serialization.StringDeserializer
spring.kafka.consumer.value-deserializer=org.apache.kafka.common.serialization.StringDeserializer


Make sure Kafka is running locally (or via Docker).

3. Create Kafka Producer
package com.example.demo.kafka;

import org.springframework.kafka.core.KafkaTemplate;
import org.springframework.stereotype.Service;

@Service
public class TaskProducer {

    private final KafkaTemplate<String, String> kafkaTemplate;
    private static final String TOPIC = "tasks";

    public TaskProducer(KafkaTemplate<String, String> kafkaTemplate) {
        this.kafkaTemplate = kafkaTemplate;
    }

    public void sendTaskEvent(String taskJson) {
        kafkaTemplate.send(TOPIC, taskJson);
        System.out.println("Sent task event to Kafka: " + taskJson);
    }
}

4. Update Task Service to publish event
package com.example.demo.service;

import com.example.demo.kafka.TaskProducer;
import com.example.demo.model.Task;
import com.example.demo.repository.TaskRepository;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TaskService {

    private final TaskRepository repo;
    private final TaskProducer producer;
    private final ObjectMapper objectMapper;

    public TaskService(TaskRepository repo, TaskProducer producer, ObjectMapper objectMapper) {
        this.repo = repo;
        this.producer = producer;
        this.objectMapper = objectMapper;
    }

    public Task saveTask(Task task) {
        Task saved = repo.save(task);
        try {
            String taskJson = objectMapper.writeValueAsString(saved);
            producer.sendTaskEvent(taskJson); // send event to Kafka
        } catch (Exception e) {
            e.printStackTrace();
        }
        return saved;
    }

    public List<Task> getTasks() {
        return repo.findAll();
    }
}

5. Create Kafka Consumer
package com.example.demo.kafka;

import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;

@Component
public class TaskConsumer {

    @KafkaListener(topics = "tasks", groupId = "task-group")
    public void consumeTask(String taskJson) {
        System.out.println("Kafka Consumer received task event: " + taskJson);
        // Here you can simulate another service processing the task
    }
}

6. Testing the flow

Start Kafka broker (localhost:9092).

Start Spring Boot backend.

Start Angular frontend (ng serve).

Add a task via the Angular UI.

You will see two logs in the Spring Boot console:

Task saved in DB

Task event sent to Kafka

Kafka consumer receives the task event

7. Flow Diagram (Text)
Angular UI (Add Task) ---> Spring Boot REST API ---> Save in DB ---> Send event to Kafka ---> Kafka Consumer (Other Service)


Producer: Spring Boot TaskService

Event: JSON representation of the task

Kafka Topic: tasks

Consumer: Spring Boot TaskConsumer (simulates another microservice)

8. Key points for interview
Concept	Explanation
Event	Task added message ({"id":1,"title":"Buy milk","completed":false})
Producer	Spring Boot publishes event to Kafka topic
Kafka Topic	Stores events (tasks) and allows multiple consumers
Consumer	Spring Boot TaskConsumer (simulates another service)
Decoupling	Angular → Backend → DB → Kafka → Consumer. Each can scale independently

✅ This simple app now demonstrates:

Full-stack Spring Boot + Angular

Event-driven architecture

Kafka producer → topic → consumer flow

Decoupling of services using Kafka events

Flow: Angular → REST API → Spring Boot → H2 → Spring Boot → Angular

Can easily add Kafka: Producer in Spring Boot, Consumers in other services.
