Immutable Class in Java
An immutable class ensures that an object’s state is consistent and cannot be changed after it is created. This helps in making your code more thread-safe and easier to reason about, especially when objects are shared across multiple threads.

How to Create an Immutable Class:
Declare the class as final to prevent subclassing.
Declare all fields as private and final to ensure they are only initialized once.
Don't provide setter methods that modify the fields.
If the class contains mutable objects, make sure to return copies of those objects instead of the original references to avoid modifying the state from outside.
Example of an Immutable Class:
java
Copy
public final class Person {
    private final String name;
    private final int age;

    // Constructor initializes fields
    public Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter methods (no setters)
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // No setter methods provided

    // If you had a mutable field, you could return a copy of it:
    // public List<String> getAddresses() {
    //     return new ArrayList<>(addresses);  // return a copy to prevent external modification
    // }
}
Use Cases for Immutable Classes:
Thread Safety: Immutable objects are naturally thread-safe since their state cannot be changed once they are created, making them useful in concurrent programming.
Consistency: Since immutable objects cannot change, they provide consistency in systems where objects are passed around and shared.
Caching: Immutable objects can be used for caching because their state is guaranteed not to change.
Security: Since immutable objects can't be altered, they are used in situations where data integrity is important (e.g., security tokens, hash codes, etc.).
Mutable Class in Java
A mutable class allows its fields to be modified after the object is created. This is achieved by providing setter methods or modifying the fields directly.

How to Create a Mutable Class:
Declare the class as public or package-private (no need for final).
Provide setter methods that allow fields to be modified.
You can modify the state of the object freely through the provided setters.
Example of a Mutable Class:
java
Copy
public class Employee {
    private String name;
    private int age;

    // Constructor to initialize fields
    public Employee(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Getter methods
    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }

    // Setter methods to change field values
    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }
}
Use Cases for Mutable Classes:
Flexibility: Mutable objects allow changes to the state after creation, which can be useful in applications where the state of an object needs to evolve over time.
Dynamic State: In applications where objects need to be updated frequently, such as in simulations or games, mutable objects are commonly used.
User Interaction: Mutable classes are commonly used in UI applications, where the user can change the data displayed (e.g., form fields that change over time).
Key Differences Between Immutable and Mutable Classes
Characteristic	Immutable Class	Mutable Class
State after creation	Cannot be changed	Can be modified after creation
Thread Safety	Naturally thread-safe	Not thread-safe by default
Getter/Setter methods	Only getter methods, no setters	Getter and setter methods
Use cases	Thread safety, consistency, caching	Dynamic state, flexibility
Design approach	Strong encapsulation, final fields	Allows changes via setters
Example Use Case of Immutable Class:
Let’s say you are building a banking application that handles financial transactions. You would want to represent Currency as an immutable class to prevent modifications after it has been initialized. This ensures that once a Currency object is created, it cannot be altered by any process in the system.

java
Copy
public final class Currency {
    private final String currencyCode;
    private final double amount;

    public Currency(String currencyCode, double amount) {
        this.currencyCode = currencyCode;
        this.amount = amount;
    }

    public String getCurrencyCode() {
        return currencyCode;
    }

    public double getAmount() {
        return amount;
    }
}
In this case, the Currency class is immutable, which ensures that the amount or currencyCode cannot be altered once the object is created, providing data integrity for the financial calculations.

Example Use Case of Mutable Class:
Now, let’s consider a shopping cart in an e-commerce application, where items can be added, updated, or removed over time. A mutable class would be appropriate here, as the state of the shopping cart changes dynamically.

java
Copy
public class ShoppingCart {
    private List<String> items;

    public ShoppingCart() {
        this.items = new ArrayList<>();
    }

    // Add an item to the cart
    public void addItem(String item) {
        items.add(item);
    }

    // Remove an item from the cart
    public void removeItem(String item) {
        items.remove(item);
    }

    // Get list of items
    public List<String> getItems() {
        return items;
    }
}
In this case, the ShoppingCart class is mutable, as items can be added or removed at any time.

Conclusion
Immutable Classes are useful when you need to ensure that the object's state remains consistent and cannot be changed. This is ideal for ensuring thread safety, preventing unintended side effects, and ensuring data integrity.
Mutable Classes are useful when you need to update the state of an object throughout its lifecycle, such as when interacting with databases or UI elements.
By understanding the differences and appropriate use cases for immutable and mutable classes, you can design your Java applications in a way that is both efficient and reliable.



Immutable Classes in Java
String:

Class Type: Immutable

Explanation: String is one of the most commonly used immutable classes in Java. Once a String object is created, its value cannot be changed. Any operation that seems to modify the string (like concatenation or replacing) actually creates a new String object instead of modifying the original one.

Example:

java
Copy
String s1 = "Hello";
String s2 = s1.concat(" World");  // This creates a new String object
System.out.println(s1);  // Output: Hello
System.out.println(s2);  // Output: Hello World
Wrapper Classes (Integer, Double, Character, Boolean, etc.):

Class Type: Immutable

Explanation: All wrapper classes in Java (like Integer, Double, Character, etc.) are immutable. Once a value is assigned to a wrapper object, it cannot be changed. Operations on these objects create new objects.

Example:

java
Copy
Integer num1 = 100;
Integer num2 = num1 + 50;  // Creates a new Integer object
System.out.println(num1);  // Output: 100
System.out.println(num2);  // Output: 150
LocalDate, LocalTime, LocalDateTime (Java 8 Date and Time API):

Class Type: Immutable

Explanation: The Java 8 java.time package provides immutable date and time classes. For instance, LocalDate and LocalTime represent a date and time, respectively, but their state cannot be changed once instantiated.

Example:

java
Copy
LocalDate date1 = LocalDate.of(2022, 5, 20);
LocalDate date2 = date1.plusDays(5);  // Creates a new object, date1 is not modified
System.out.println(date1);  // Output: 2022-05-20
System.out.println(date2);  // Output: 2022-05-25
StringBuilder (although the class itself is mutable, objects of StringBuilder are often treated as immutable in Java due to certain usage patterns):

Class Type: Immutable within a specific context but mutable overall. The content of a StringBuilder can be modified, but its reference is not often intended to be modified.
Explanation: A StringBuilder object allows us to modify its content using various methods like append, insert, and delete. However, the object itself does not change its reference.
Mutable Classes in Java
StringBuffer:

Class Type: Mutable

Explanation: StringBuffer is similar to StringBuilder, but it is synchronized (thread-safe). It is mutable, meaning that the contents of a StringBuffer object can be modified after it is created.

Example:

java
Copy
StringBuffer sb1 = new StringBuffer("Hello");
sb1.append(" World");  // Modifies the content of the same StringBuffer object
System.out.println(sb1);  // Output: Hello World
ArrayList:

Class Type: Mutable

Explanation: ArrayList is part of the java.util package and is mutable. You can add, remove, or modify elements within an ArrayList after it is created.

Example:

java
Copy
ArrayList<String> list = new ArrayList<>();
list.add("Apple");
list.add("Banana");
list.set(1, "Orange");  // Modify existing element
list.remove("Apple");  // Remove element
System.out.println(list);  // Output: [Orange]
LinkedList:

Class Type: Mutable

Explanation: LinkedList is another type of list that is mutable. Similar to ArrayList, it allows modification of its contents. It’s a doubly linked list, so you can easily insert or remove elements from both ends.

Example:

java
Copy
LinkedList<String> list = new LinkedList<>();
list.add("A");
list.add("B");
list.remove("A");
System.out.println(list);  // Output: [B]
HashMap:

Class Type: Mutable

Explanation: HashMap is part of the java.util package and is a mutable collection that stores key-value pairs. You can modify the contents of a HashMap by adding, removing, or changing the values associated with keys.

Example:

java
Copy
HashMap<String, String> map = new HashMap<>();
map.put("name", "John");
map.put("age", "30");
map.put("city", "New York");
map.remove("age");
System.out.println(map);  // Output: {name=John, city=New York}
Vector:

Class Type: Mutable

Explanation: Vector is similar to ArrayList, but it is synchronized and therefore thread-safe. You can modify its contents after it is created by adding, removing, or updating elements.

Example:

java
Copy
Vector<String> vector = new Vector<>();
vector.add("One");
vector.add("Two");
vector.set(1, "Three");  // Modify the element at index 1
System.out.println(vector);  // Output: [One, Three]
HashSet:

Class Type: Mutable

Explanation: HashSet is a mutable collection that stores unique elements. The contents of a HashSet can be modified by adding or removing elements.

Example:

java
Copy
HashSet<String> set = new HashSet<>();
set.add("Apple");
set.add("Banana");
set.remove("Apple");
System.out.println(set);  // Output: [Banana]
Key Differences between Immutable and Mutable Classes
Feature	Immutable Class	Mutable Class
Modification	Cannot be modified after creation	Can be modified after creation
Thread Safety	Naturally thread-safe	Not thread-safe by default
Examples	String, Integer, LocalDate, etc.	ArrayList, HashMap, StringBuffer, etc.
Performance	Slightly slower due to object creation for changes	Faster in scenarios where frequent modification is needed
Design	Used for data integrity, caching, and concurrency	Used for flexibility, dynamic state changes
Conclusion
Immutable Classes: Ideal for scenarios where the object should not be modified once it is created, ensuring data consistency and thread safety. Examples include String, Integer, LocalDate, etc.

Mutable Classes: Suitable when the object needs to be modified during its lifecycle. They are more flexible but require careful handling, especially in multi-threaded applications. Examples include ArrayList, HashMap, StringBuffer, etc.

By understanding when to use immutable or mutable classes, you can design your Java applications more efficiently based on the requirements of the specific use case.


