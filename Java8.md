Java 8 introduced several powerful features that transformed the language and provided more concise, efficient, and expressive ways of writing code. In an interview, you can expect questions on these features, so understanding them thoroughly is essential. Below are the most important Java 8 features with examples:

1. Lambda Expressions
Lambda expressions allow you to write more concise and functional-style code. They provide a way to implement methods of functional interfaces (interfaces with a single abstract method) in a more readable and compact manner.

Syntax:
java
Copy
(parameters) -> expression
Example:
java
Copy
// Before Java 8
List<String> list = Arrays.asList("Apple", "Banana", "Cherry");
for (String fruit : list) {
    System.out.println(fruit);
}

// Using Lambda Expression in Java 8
list.forEach(fruit -> System.out.println(fruit));
Lambda expressions are particularly useful with Java Collections and Streams.

2. Functional Interfaces
A functional interface is an interface with just one abstract method, and it may contain multiple default or static methods. Lambda expressions are used to provide the implementation of the single abstract method of these interfaces.

Example:
java
Copy
@FunctionalInterface
interface MyFunctionalInterface {
    void printMessage(String message);
}

public class LambdaExample {
    public static void main(String[] args) {
        // Using Lambda expression to implement the interface
        MyFunctionalInterface msg = (message) -> System.out.println(message);
        msg.printMessage("Hello from Lambda!");
    }
}
Common functional interfaces in Java 8 are:

Runnable, Callable, Comparator, Consumer, Supplier, Function, Predicate.
3. Stream API
The Stream API allows you to process sequences of elements (e.g., collections) in a functional style. It enables operations such as filtering, mapping, and reducing with just a few lines of code.

Example:
java
Copy
import java.util.*;
import java.util.stream.*;

public class StreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Using Stream to filter and perform operations
        List<Integer> evenNumbers = numbers.stream()
                                           .filter(n -> n % 2 == 0)
                                           .collect(Collectors.toList());

        System.out.println(evenNumbers);  // Output: [2, 4, 6, 8, 10]
    }
}
Operations in streams can be intermediate (like filter, map) or terminal (like collect, reduce).

4. Default Methods in Interfaces
Java 8 allows you to define default methods in interfaces. A default method has a body and provides a way to add functionality to interfaces without breaking existing implementations.

Example:
java
Copy
interface Animal {
    default void sound() {
        System.out.println("Animal makes a sound");
    }
}

class Dog implements Animal {
    // You can override the default method if necessary
    @Override
    public void sound() {
        System.out.println("Dog barks");
    }
}

public class DefaultMethodExample {
    public static void main(String[] args) {
        Dog dog = new Dog();
        dog.sound();  // Output: Dog barks
    }
}
Default methods allow backward compatibility in interfaces, enabling you to add new methods without affecting classes that implement the interface.

5. Method References
Method references are a shorthand notation of a lambda expression to call a method. It makes your code more readable by referring to methods using the :: operator.

Types of Method References:
Static Method Reference: ClassName::staticMethodName
Instance Method Reference: object::instanceMethod
Constructor Reference: ClassName::new
Example:
java
Copy
// Using a method reference for a static method
public class MethodReferenceExample {
    public static void printMessage(String message) {
        System.out.println(message);
    }

    public static void main(String[] args) {
        // Using Method Reference instead of Lambda
        List<String> messages = Arrays.asList("Hello", "World", "Java 8");
        messages.forEach(MethodReferenceExample::printMessage);
    }
}
Here, MethodReferenceExample::printMessage is a method reference that replaces the lambda expression.

6. Optional Class
The Optional class is a container object which may or may not contain a value. It's used to prevent NullPointerExceptions and is widely used with streams and in return types of methods to represent the absence of a value.

Example:
java
Copy
import java.util.Optional;

public class OptionalExample {
    public static void main(String[] args) {
        Optional<String> optionalString = Optional.ofNullable("Hello");
        optionalString.ifPresent(s -> System.out.println(s.length()));  // Output: 5

        Optional<String> emptyOptional = Optional.empty();
        System.out.println(emptyOptional.orElse("Default Value"));  // Output: Default Value
    }
}
With Optional, you can avoid null checks like if (object != null) and provide default values when an object is absent.

7. New Date and Time API
Java 8 introduced the new java.time package, which provides a more comprehensive and accurate approach to working with dates and times than the old java.util.Date and Calendar.

Example:
java
Copy
import java.time.*;
import java.time.format.DateTimeFormatter;

public class DateTimeExample {
    public static void main(String[] args) {
        // Getting the current date and time
        LocalDateTime now = LocalDateTime.now();
        System.out.println("Current Date and Time: " + now);

        // Parsing a date string
        DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd-MM-yyyy");
        LocalDate date = LocalDate.parse("24-01-2025", formatter);
        System.out.println("Parsed Date: " + date);
    }
}
The new Date and Time API is thread-safe and provides better support for formatting, parsing, and performing date arithmetic.

8. Nashorn JavaScript Engine
Java 8 introduced the Nashorn JavaScript engine, which allows you to execute JavaScript code within a Java application. You can use JavaScript code from within Java via the javax.script API.

Example:
java
Copy
import javax.script.*;

public class NashornExample {
    public static void main(String[] args) throws ScriptException {
        ScriptEngine engine = new ScriptEngineManager().getEngineByName("nashorn");
        engine.eval("var x = 10; var y = 20; print(x + y);");
    }
}
Nashorn allows you to interact with JavaScript directly, which can be useful for integrating Java applications with dynamic scripting languages.

9. Streams and Parallelism
Java 8 introduced parallel streams, which make it easy to process data in parallel by using multi-core processors. This can improve performance when processing large datasets.

Example:
java
Copy
import java.util.*;
import java.util.stream.*;

public class ParallelStreamExample {
    public static void main(String[] args) {
        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);

        // Using parallel stream to calculate sum
        int sum = numbers.parallelStream()
                          .mapToInt(Integer::intValue)
                          .sum();

        System.out.println("Sum: " + sum);  // Output: Sum: 55
    }
}
By calling .parallelStream(), you instruct Java to process the stream in parallel using multiple threads.

10. New Collector Methods
Java 8 introduced several new methods to the Collector interface, making it easier to perform aggregate operations like grouping, partitioning, and joining.

Example:
java
Copy
import java.util.*;
import java.util.stream.*;

public class CollectorExample {
    public static void main(String[] args) {
        List<String> words = Arrays.asList("apple", "banana", "cherry", "date");

        // Joining elements with a separator
        String result = words.stream()
                             .collect(Collectors.joining(", "));
        System.out.println(result);  // Output: apple, banana, cherry, date
    }
}
Conclusion:
Java 8 introduced significant changes to the language, especially with functional programming, streams, and new APIs for handling data and time. Mastering these features can not only improve your code’s efficiency and readability but also demonstrate your expertise during an interview.

Let me know if you want more details or practice examples on any of these features!