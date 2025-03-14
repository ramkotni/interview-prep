SOLID Principles Java
In Java, SOLID principles represent an object-oriented approach applied to software structure design. Conceptualized by Robert C. Martin, also known as Uncle Bob, these five principles have revolutionized the world of object-oriented programming and transformed the way software is written.

By adhering to SOLID principles, developers can ensure that their software is modular, easy to understand, debug, and refactor. In this section, we will discuss the SOLID principles in Java, complete with proper examples. These principles not only enhance code quality but also facilitate better maintenance and scalability, ultimately leading to more robust and efficient software systems.

The word SOLID acronym for:

Single Responsibility Principle (SRP)
Open-Closed Principle (OCP)
Liskov Substitution Principle (LSP)
Interface Segregation Principle (ISP)
Dependency Inversion Principle (DIP)

Single Responsibility Principle
The single responsibility principle states that every Java class must perform a single functionality. Implementation of multiple functionalities in a single class mashup the code and if any modification is required may affect the whole class. It precise the code and the code can be easily maintained. Let's understand the single responsibility principle through an example.

Suppose, Student is a class having three methods namely printDetails(), calculatePercentage(), and addStudent(). Hence, the Student class has three responsibilities to print the details of students, calculate percentages, and database. By using the single responsibility principle, we can separate these functionalities into three separate classes to fulfill the goal of the principle.

Student.java

ublic class Student  
{  
public void printDetails();  
{  
//functionality of the method  
}  
pubic void calculatePercentage();  
{  
//functionality of the method  
}  
public void addStudent();  
{  
//functionality of the method  
}  

The above code snippet violates the single responsibility principle. To achieve the goal of the principle, we should implement a separate class that performs a single functionality only.

Student.java
public class Student  
{  
public void addStudent();  
{  
//functionality of the method  
}  
}  

PrintStudentDetails.java
public class PrintStudentDetails  
{  
public void printDetails();  
{  
//functionality of the method  
}  
}  
Percentage.java
public class Percentage  
{  
public void calculatePercentage();  
{  
//functionality of the method  
}  
}  

Hence, we have achieved the goal of the single responsibility principle by separating the functionality into three separate classes.

Open-Closed Principle
The application or module entities the methods, functions, variables, etc. The open-closed principle states that according to new requirements the module should be open for extension but closed for modification. The extension allows us to implement new functionality to the module. Let's understand the principle through an example.

Suppose, VehicleInfo is a class and it has the method vehicleNumber() that returns the vehicle number.

VehicleInfo.java

public class VehicleInfo  
{  
public double vehicleNumber(Vehicle vcl)   
{  
if (vcl instanceof Car)   
{  
return vcl.getNumber();  
if (vcl instanceof Bike)   
{  
return vcl.getNumber();  
}  
}  

If we want to add another subclass named Truck, simply, we add one more if statement that violates the open-closed principle. The only way to add the subclass and achieve the goal of principle by overriding the vehicleNumber() method, as we have shown below.

VehicleInfo.java


ublic class VehicleInfo   
{  
public double vehicleNumber()   
{  
//functionality   
}  
}  
public class Car extends VehicleInfo   
{  
public double vehicleNumber()   
{  
return this.getValue();  
}  
public class Car extends Truck   
{  
public double vehicleNumber()   
{  
return this.getValue();  
}  

Similarly, we can add more vehicles by making another subclass extending from the vehicle class. the approach would not affect the existing application.

Liskov Substitution Principle
The Liskov Substitution Principle (LSP) was introduced by Barbara Liskov. It applies to inheritance in such a way that the derived classes must be completely substitutable for their base classes. In other words, if class A is a subtype of class B, then we should be able to replace B with A without interrupting the behavior of the program.

It extends the open-close principle and also focuses on the behavior of a superclass and its subtypes. We should design the classes to preserve the property unless we have a strong reason to do otherwise. Let's understand the principle through an example.

Student.java

public class Student   
{  
private double height;  
private double weight;  
public void setHeight(double h)   
{   
height = h;   
}  
public void setWeight(double w)   
{   
weight= w;   
}  
...  
}  
public class StudentBMI extends Student  
{  
public void setHeight(double h)   
{  
super.setHeight(h);  
super.setWeight(w);  
}  
public void setWeight(double h)   
{  
super.setHeight(h);  
super.setWeight(w);  
}  
}  
The above classes violated the Liskov substitution principle because the StudentBMI class has extra constraints i.e. height and weight that must be the same. Therefore, the Student class (base class) cannot be replaced by StudentBMI class (derived class).

Hence, substituting the class Student with StudentBMI class may result in unexpected behavior.

Interface Segregation Principle
The principle states that the larger interfaces split into smaller ones. Because the implementation classes use only the methods that are required. We should not force the client to use the methods that they do not want to use.

The goal of the interface segregation principle is similar to the single responsibility principle. Let's understand the principle through an example.

Suppose, we have created an interface named Conversion having three methods intToDouble(), intToChar(), and charToString().

public interface Conversion  
{  
public void intToDouble();  
public void intToChar();  
public void charToString();  
}  
The above interface has three methods. If we want to use only a method intToChar(), we have no choice to implement the single method. To overcome the problem, the principle allows us to split the interface into three separate ones.

public interface ConvertIntToDouble  
{  
public void intToDouble();  
}   
public interface ConvertIntToChar  
{  
public void intToChar();  
}  
public interface ConvertCharToString   
{  
public void charToString();  
}  
Now we can use only the method that is required. Suppose, we want to convert the integer to double and character to string then, we will use only the methods intToDouble() and charToString().

public class DataTypeConversion implements ConvertIntToDouble, ConvertCharToString   
{  
public void intToDouble()  
{  
//conversion logic  
}  
public void charToString()  
{  
//conversion logic  Dependency Inversion Principle
The principle states that we must use abstraction (abstract classes and interfaces) instead of concrete implementations. High-level modules should not depend on the low-level module but both should depend on the abstraction. Because the abstraction does not depend on detail but the detail depends on abstraction. It decouples the software. Let's understand the principle through an example.

public class WindowsMachine  
{  
//functionality   
}  
It is worth, if we have not keyboard and mouse to work on Windows. To solve this problem, we create a constructor of the class and add the instances of the keyboard and monitor. After adding the instances, the class looks like the following:

public class WindowsMachine  
{  
public final keyboard;  
public final monitor;  
public WindowsMachine()  
{  
monitor = new monitor();  //instance of monitor class  
keyboard = new keyboard(); //instance of keyboard class  
}  
}  
Now we can work on the Windows machine with the help of a keyboard and mouse. But we still face the problem. Because we have tightly coupled the three classes together by using the new keyword. It is hard o test the class windows machine.

To make the code loosely coupled, we decouple the WindowsMachine from the keyboard by using the Keyboard interface and this keyword.

Keyboard.java

public interface Keyboard   
{   
//functionality  
}  
WindowsMachine.java

public class WindowsMachine  
{  
private final Keyboard keyboard;  
private final Monitor monitor;  
public WindowsMachine(Keyboard keyboard, Monitor monitor)   
{  
this.keyboard = keyboard;  
this.monitor = monitor;  
}  
}  
In the above code, we have used the dependency injection to add the keyboard dependency in the WindowsMachine class. Therefore, we have decoupled the classes.

Why should we use SOLID principles?
It reduces the dependencies so that a block of code can be changed without affecting the other code blocks.
The principles intended to make design easier, understandable.
By using the principles, the system is maintainable, testable, scalable, and reusable.
It avoids the bad design of the software.
Next time when you design software, keeps these five principles in mind. By applying these principles, the code will be much more clear, testable, and expendable.

Adavantages of SOLID Principles in Java
1. Enhanced Maintainability

Easier Code Refactoring: Adhering to SOLID principles results in cleaner, more modular code. This makes refactoring easier and safer since changes in one part of the codebase are less likely to impact other parts. This is crucial for long-term maintenance as requirements evolve.
Reduced Code Smells: By following SOLID principles, developers can avoid common code smells like large classes, long methods, and tightly coupled components. This leads to cleaner, more understandable code, making it easier to identify and fix bugs.
2. Improved Testability

Isolated Unit Testing: SOLID principles promote the development of loosely coupled modules. This makes it easier to isolate and test individual components, leading to more effective and reliable unit tests.
Mocking Dependencies: With loosely coupled classes and clear interfaces, mocking dependencies becomes straightforward. This enhances the ability to test components in isolation without needing to set up complex environments.
3. Scalability and Flexibility

Easier Addition of New Features: Following SOLID principles facilitates the addition of new features without requiring extensive changes to the existing codebase. This flexibility is essential for adapting to new requirements and scaling the application.
Adaptability to Change: SOLID-compliant code is more adaptable to changes. When business requirements change, the code can be adjusted with minimal disruption, reducing the time and cost associated with modifications.
4. Enhanced Readability and Comprehension

Clearer Code Structure: By encouraging well-defined interfaces and responsibilities, SOLID principles contribute to a clearer and more intuitive code structure. This makes it easier for new developers to understand the codebase and contribute effectively.
Improved Documentation: With well-defined responsibilities and modular design, the documentation can be more focused and clear. This enhances the overall comprehensibility of the system for both current team members and future maintainers.
5. Increased Reusability

Reusable Components: SOLID principles encourage the creation of reusable components. These components can be easily reused across different parts of the application or even in different projects, leading to more efficient development practices.
Library Development: When components adhere to SOLID principles, they are often generic enough to be extracted into libraries or frameworks, promoting reuse across multiple projects and reducing development time.
6. Reduced Technical Debt

Proactive Code Quality Management: By adhering to SOLID principles from the outset, developers can reduce the accumulation of technical debt. This proactive approach to code quality ensures that the software remains maintainable and scalable over time.
Long-Term Code Health: Maintaining a codebase that follows SOLID principles contributes to its long-term health. This minimizes the need for extensive rework and allows developers to focus on adding value through new features and improvements.
7. Collaboration and Team Efficiency

Standardization of Practices: Applying SOLID principles helps standardize development practices across a team. This common understanding leads to more efficient collaboration and smoother integration of different parts of the system.
Enhanced Code Reviews: Code reviews become more efficient and effective when the code adheres to SOLID principles. Reviewers can more easily understand the code's structure and intent, leading to higher-quality feedback and faster review cycles.
8. Improved Performance

Optimized Components: Well-structured code adhering to SOLID principles can be more easily optimized. Since components have clear responsibilities and are loosely coupled, performance bottlenecks can be identified and addressed more effectively.
Better Resource Management: With clear separation of concerns, resource management (such as memory and database connections) can be handled more efficiently. This leads to improved performance and resource utilization across the application.
9. Future-Proofing

Preparedness for Technological Changes: Adhering to SOLID principles ensures that the codebase is better prepared for technological advancements. Whether it's adopting new frameworks, integrating with different systems, or scaling to meet increased demand, a SOLID codebase is more resilient and adaptable.
Smooth Transitions: When migrating to new platforms or refactoring large parts of the system, having a codebase that follows SOLID principles ensures smoother transitions. This minimizes disruption and reduces the risk associated with large-scale changes.
}  
}  

