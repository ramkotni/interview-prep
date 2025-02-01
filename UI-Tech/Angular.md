Creating a full end-to-end Angular application connected to a Spring Boot backend involves several steps. Below, I'll provide a simple example to demonstrate this flow. The flow will include:

Spring Boot Backend: A REST API with a simple controller.
Angular Frontend: A basic Angular service that communicates with the backend.
1. Spring Boot Backend (REST API)
First, create a Spring Boot application that will serve as your backend. You can create the project using Spring Initializr: https://start.spring.io/, and add dependencies like Spring Web and Spring Boot DevTools.

Application Setup:

Project: Maven
Language: Java
Dependencies: Spring Web
After generating the project, extract it and open it in your favorite IDE (IntelliJ IDEA, Eclipse, etc.).

Backend Code:

Controller Class (src/main/java/com/example/demo/controller/ItemController.java):
java
Copy
package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import com.example.demo.model.Item;
import java.util.Arrays;
import java.util.List;

@RestController
public class ItemController {

    @GetMapping("/api/items")
    public List<Item> getItems() {
        return Arrays.asList(
                new Item(1, "Item 1", 10.0),
                new Item(2, "Item 2", 15.5),
                new Item(3, "Item 3", 20.0)
        );
    }
}
Item Model (src/main/java/com/example/demo/model/Item.java):
java
Copy
package com.example.demo.model;

public class Item {

    private int id;
    private String name;
    private double price;

    // Constructor, Getters, and Setters
    public Item(int id, String name, double price) {
        this.id = id;
        this.name = name;
        this.price = price;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}
Application Class (src/main/java/com/example/demo/DemoApplication.java):
java
Copy
package com.example.demo;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class DemoApplication {

    public static void main(String[] args) {
        SpringApplication.run(DemoApplication.class, args);
    }
}
Now, run the Spring Boot application, and the backend API will be available at http://localhost:8080/api/items.

2. Angular Frontend
Now, let’s create an Angular application that consumes the Spring Boot API.

You can create a new Angular application by running the following command:

bash
Copy
ng new angular-demo
cd angular-demo
ng serve
Next, create a service to fetch the data from the Spring Boot backend.

Item Service (src/app/item.service.ts):
typescript
Copy
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

interface Item {
  id: number;
  name: string;
  price: number;
}

@Injectable({
  providedIn: 'root',
})
export class ItemService {
  private apiUrl = 'http://localhost:8080/api/items';

  constructor(private http: HttpClient) {}

  getItems(): Observable<Item[]> {
    return this.http.get<Item[]>(this.apiUrl);
  }
}
Item Component (src/app/item/item.component.ts):
typescript
Copy
import { Component, OnInit } from '@angular/core';
import { ItemService } from '../item.service';

@Component({
  selector: 'app-item',
  templateUrl: './item.component.html',
  styleUrls: ['./item.component.css'],
})
export class ItemComponent implements OnInit {
  items = [];

  constructor(private itemService: ItemService) {}

  ngOnInit(): void {
    this.itemService.getItems().subscribe((data) => {
      this.items = data;
    });
  }
}
Item Component HTML (src/app/item/item.component.html):
html
Copy
<div class="item-list">
  <h2>Items</h2>
  <ul>
    <li *ngFor="let item of items">
      {{ item.name }} - ${{ item.price }}
    </li>
  </ul>
</div>
App Module (src/app/app.module.ts):
typescript
Copy
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { ItemComponent } from './item/item.component';

@NgModule({
  declarations: [AppComponent, ItemComponent],
  imports: [BrowserModule, HttpClientModule],
  providers: [],
  bootstrap: [AppComponent],
})
export class AppModule {}
App Component HTML (src/app/app.component.html):
html
Copy
<app-item></app-item>
3. Running the Application
Spring Boot Backend: Make sure the Spring Boot backend is running (http://localhost:8080).
Angular Frontend: Open the Angular project in your terminal, run the following command:
bash
Copy
ng serve
Now, navigate to http://localhost:4200 in your browser, and you should see a list of items fetched from the Spring Boot API.

4. CORS Configuration
Since the Angular frontend and Spring Boot backend are running on different ports (4200 for Angular and 8080 for Spring Boot), you might run into CORS (Cross-Origin Resource Sharing) issues.

To resolve this, add a CORS configuration to your Spring Boot application:

CORS Configuration (src/main/java/com/example/demo/config/WebConfig.java):
java
Copy
package com.example.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/api/**")
                .allowedOrigins("http://localhost:4200")
                .allowedMethods("GET", "POST", "PUT", "DELETE")
                .allowedHeaders("*")
                .allowCredentials(true);
    }
}
Conclusion
Now, you have a working Angular frontend and a Spring Boot backend communicating via RESTful APIs. When you open http://localhost:4200, the Angular app will show the list of items fetched from the Spring Boot backend.

