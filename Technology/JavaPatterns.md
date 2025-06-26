Features of OOP (Object-Oriented Programming)
Encapsulation:


Bundling data (fields) and methods (functions) that operate on the data into a single unit (class).
Example:
public class Person {
    private String name; // Encapsulated field
    
    public String getName() { // Getter
        return name;
    }
    
    public void setName(String name) { // Setter
        this.name = name;
    }
}
Inheritance:


Mechanism where one class (child) inherits properties and behaviors from another class (parent).
Example:
public class Animal {
    public void eat() {
        System.out.println("This animal eats food.");
    }
}

public class Dog extends Animal {
    public void bark() {
        System.out.println("The dog barks.");
    }
}
Polymorphism:


Ability to take many forms, typically achieved through method overloading and overriding.
Example:
// Method Overloading
public class Calculator {
    public int add(int a, int b) {
        return a + b;
    }

    public double add(double a, double b) {
        return a + b;
    }
}

// Method Overriding
public class Animal {
    public void sound() {
        System.out.println("Animal makes a sound");
    }
}

public class Cat extends Animal {
    @Override
    public void sound() {
        System.out.println("Cat meows");
    }
}
Abstraction:


Hiding implementation details and exposing only the essential features.
Example:
public abstract class Shape {
    abstract void draw(); // Abstract method
}

public class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a Circle");
    }
}
<hr></hr>
Common Java Design Patterns
Singleton Pattern:


Ensures a class has only one instance and provides a global point of access to it.
Example:
public class Singleton {
    private static Singleton instance;

    private Singleton() {} // Private constructor

    public static Singleton getInstance() {
        if (instance == null) {
            instance = new Singleton();
        }
        return instance;
    }
}
Factory Pattern:


Provides a way to create objects without specifying the exact class.
Example:
public interface Shape {
    void draw();
}

public class Circle implements Shape {
    public void draw() {
        System.out.println("Drawing Circle");
    }
}

public class ShapeFactory {
    public Shape getShape(String shapeType) {
        if (shapeType.equalsIgnoreCase("CIRCLE")) {
            return new Circle();
        }
        return null;
    }
}
Observer Pattern:


Defines a one-to-many dependency between objects so that when one object changes state, all dependents are notified.
Example:
import java.util.ArrayList;
import java.util.List;

public class Subject {
    private List<Observer> observers = new ArrayList<>();
    private int state;

    public void setState(int state) {
        this.state = state;
        notifyAllObservers();
    }

    public void attach(Observer observer) {
        observers.add(observer);
    }

    private void notifyAllObservers() {
        for (Observer observer : observers) {
            observer.update();
        }
    }
}

public abstract class Observer {
    protected Subject subject;
    public abstract void update();
}

public class ConcreteObserver extends Observer {
    public ConcreteObserver(Subject subject) {
        this.subject = subject;
        this.subject.attach(this);
    }

    @Override
    public void update() {
        System.out.println("State changed to: " + subject.state);
    }
}
Builder Pattern:


Constructs a complex object step by step.
Example:
public class Car {
    private String engine;
    private int wheels;

    public static class Builder {
        private String engine;
        private int wheels;

        public Builder setEngine(String engine) {
            this.engine = engine;
            return this;
        }

        public Builder setWheels(int wheels) {
            this.wheels = wheels;
            return this;
        }

        public Car build() {
            Car car = new Car();
            car.engine = this.engine;
            car.wheels = this.wheels;
            return car;
        }
    }
}
Decorator Pattern:
Adds new functionality to an object dynamically.
Example:
public interface Car {
    void assemble();
}

public class BasicCar implements Car {
    public void assemble() {
        System.out.println("Basic Car");
    }
}

public class CarDecorator implements Car {
    protected Car car;

    public CarDecorator(Car car) {
        this.car = car;
    }

    public void assemble() {
        this.car.assemble();
    }
}

public class SportsCar extends CarDecorator {
    public SportsCar(Car car) {
        super(car);
    }

    public void assemble() {
        super.assemble();
        System.out.println("Adding features of Sports Car");
    }
}
