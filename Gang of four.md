Gang of Four (GoF) Design Patterns
The Gang of Four (GoF) refers to the authors of the book Design Patterns: Elements of Reusable Object-Oriented Software — Erich Gamma, Richard Helm, Ralph Johnson, and John Vlissides. This book outlines 23 design patterns that have become essential tools for object-oriented design and software development.

These patterns are divided into three categories:

Creational Patterns – deal with object creation mechanisms.
Structural Patterns – focus on how classes and objects are composed to form larger structures.
Behavioral Patterns – deal with object interaction and responsibility delegation.
Let’s go through the key Gang of Four design patterns in Java, explaining each pattern along with its use cases and providing code examples.

1. Creational Patterns
a. Singleton Pattern
Purpose: The Singleton pattern ensures that a class has only one instance and provides a global point of access to that instance.

Use Case:
Database connections
Logger classes
Configuration classes
Example in Java:
java
Copy
public class Singleton {
    private static Singleton instance;

    // Private constructor prevents instantiation
    private Singleton() {}

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
Explanation:

getInstance() ensures that only one instance of the Singleton class is created. It checks if instance is null and, if so, creates the object.
This is useful when you want to control access to shared resources, like a configuration or logging system.
b. Factory Method Pattern
Purpose: The Factory Method pattern defines an interface for creating objects but allows subclasses to alter the type of objects that will be created.

Use Case:
Used when a class can’t anticipate the type of objects it must create.
When the creation process is complex and needs to be encapsulated.
Example in Java:
java
Copy
abstract class Vehicle {
    abstract void create();
}

class Car extends Vehicle {
    public void create() {
        System.out.println("Car is created.");
    }
}

class Bike extends Vehicle {
    public void create() {
        System.out.println("Bike is created.");
    }
}

abstract class VehicleFactory {
    public abstract Vehicle createVehicle();
}

class CarFactory extends VehicleFactory {
    public Vehicle createVehicle() {
        return new Car();
    }
}

class BikeFactory extends VehicleFactory {
    public Vehicle createVehicle() {
        return new Bike();
    }
}
Explanation:

Factory Method provides an abstract createVehicle() method for creating different types of vehicles.
The specific factories (CarFactory, BikeFactory) decide what type of object to instantiate.
2. Structural Patterns
a. Adapter Pattern
Purpose: The Adapter pattern allows incompatible interfaces to work together. It converts one interface into another expected by the client.

Use Case:
When you want to integrate new or legacy systems into an existing framework without modifying the existing code.
Converting one data format to another.
Example in Java:
java
Copy
// Old interface
interface OldSystem {
    void oldMethod();
}

class OldSystemImpl implements OldSystem {
    public void oldMethod() {
        System.out.println("Old method executed");
    }
}

// New interface
interface NewSystem {
    void newMethod();
}

// Adapter
class Adapter implements NewSystem {
    private OldSystem oldSystem;

    public Adapter(OldSystem oldSystem) {
        this.oldSystem = oldSystem;
    }

    @Override
    public void newMethod() {
        oldSystem.oldMethod();  // Adapter makes the old method compatible
    }
}
Explanation:

Adapter allows a new system to work with an old system by adapting its interface.
The adapter converts the oldMethod() from the OldSystem to a newMethod() in the NewSystem.
b. Decorator Pattern
Purpose: The Decorator pattern allows you to add new functionality to an object dynamically without altering its structure.

Use Case:
Enhancing or modifying the behavior of objects at runtime.
Used extensively in GUI frameworks and stream processing libraries.
Example in Java:
java
Copy
// Component interface
interface Coffee {
    double cost();
}

// Concrete component
class SimpleCoffee implements Coffee {
    public double cost() {
        return 5.0;
    }
}

// Decorators
class MilkDecorator implements Coffee {
    private Coffee coffee;

    public MilkDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    public double cost() {
        return coffee.cost() + 2.0;  // Add cost of milk
    }
}

class SugarDecorator implements Coffee {
    private Coffee coffee;

    public SugarDecorator(Coffee coffee) {
        this.coffee = coffee;
    }

    public double cost() {
        return coffee.cost() + 1.0;  // Add cost of sugar
    }
}
Explanation:

The Decorator Pattern allows additional behavior (like adding milk or sugar) to an object without modifying its base class.
Here, you can dynamically create a coffee object and add extra features by wrapping it with decorators (MilkDecorator, SugarDecorator).
3. Behavioral Patterns
a. Observer Pattern
Purpose: The Observer pattern defines a dependency between objects, so that when one object changes state, all its dependents are notified.

Use Case:
Event handling systems (e.g., user interface event listeners)
Stock market systems where subscribers need updates when stock prices change.
Example in Java:
java
Copy
import java.util.ArrayList;
import java.util.List;

// Subject
interface Subject {
    void addObserver(Observer observer);
    void removeObserver(Observer observer);
    void notifyObservers();
}

class Stock implements Subject {
    private List<Observer> observers = new ArrayList<>();
    private double price;

    public void setPrice(double price) {
        this.price = price;
        notifyObservers();
    }

    @Override
    public void addObserver(Observer observer) {
        observers.add(observer);
    }

    @Override
    public void removeObserver(Observer observer) {
        observers.remove(observer);
    }

    @Override
    public void notifyObservers() {
        for (Observer observer : observers) {
            observer.update(price);
        }
    }
}

// Observer
interface Observer {
    void update(double price);
}

class StockInvestor implements Observer {
    private String name;

    public StockInvestor(String name) {
        this.name = name;
    }

    @Override
    public void update(double price) {
        System.out.println(name + " has been notified. New Stock price: " + price);
    }
}
Explanation:

Subject is the Stock object, and Observers are the StockInvestor objects that want to be notified when the stock price changes.
When the price is updated in Stock, all registered observers are notified.
b. Strategy Pattern
Purpose: The Strategy pattern allows a method's behavior to be defined at runtime. It defines a family of algorithms, encapsulates each one, and makes them interchangeable.

Use Case:
Used when you want to select an algorithm dynamically based on user input or runtime conditions.
Example in Java:
java
Copy
interface PaymentStrategy {
    void pay(int amount);
}

class CreditCardPayment implements PaymentStrategy {
    public void pay(int amount) {
        System.out.println("Paid " + amount + " using Credit Card.");
    }
}

class PayPalPayment implements PaymentStrategy {
    public void pay(int amount) {
        System.out.println("Paid " + amount + " using PayPal.");
    }
}

class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public ShoppingCart(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void checkout(int amount) {
        paymentStrategy.pay(amount);  // Payment method is decided dynamically
    }
}
Explanation:

The Strategy Pattern allows selecting the payment method (CreditCardPayment or PayPalPayment) dynamically at runtime.
The payment method can be easily changed without modifying the code for the ShoppingCart.
Conclusion
The Gang of Four (GoF) Design Patterns are critical tools in object-oriented design and software engineering. They provide solutions to common design problems and help improve software maintainability, flexibility, and scalability. Here's a summary of each pattern's use case:

Creational Patterns (e.g., Singleton, Factory Method): Used when object creation needs to be abstracted or controlled.
Structural Patterns (e.g., Adapter, Decorator): Used for composing objects into larger structures or enhancing object behavior without changing their class.
Behavioral Patterns (e.g., Observer, Strategy): Used to manage object interactions and responsibilities.
By mastering these patterns, developers can design more modular, maintainable, and flexible systems.