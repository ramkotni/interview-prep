Understanding CompletableFuture in Java
In Java, CompletableFuture is a class introduced in Java 8 that provides a way to handle asynchronous programming in a more flexible, efficient, and non-blocking manner. It is part of the java.util.concurrent package and allows you to write asynchronous code without the complexities of callback-based approaches. It also helps in creating complex asynchronous workflows with better control over task completion, chaining, and exception handling.

Key Features of CompletableFuture:
Non-blocking: Allows performing tasks asynchronously without blocking the main thread.
Chaining: You can chain multiple tasks in sequence and even combine results from multiple asynchronous computations.
Exception Handling: Provides mechanisms to handle errors in asynchronous tasks.
Combining Results: You can combine multiple asynchronous results, such as using thenCombine, thenCompose, and allOf.
How CompletableFuture Works
A CompletableFuture can be created using the supplyAsync() or runAsync() methods, and it can be completed explicitly by calling the complete() method or implicitly when a task finishes. You can then attach actions to be performed when the task completes.

Basic Example:
Let’s start with a simple example where we asynchronously execute a task (such as fetching data from a database or performing a calculation) and then handle the result.

Example: Simple Asynchronous Task
java
Copy
import java.util.concurrent.CompletableFuture;

public class CompletableFutureExample {
    public static void main(String[] args) {
        // Start an asynchronous task using CompletableFuture
        CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
            try {
                // Simulating a long-running task (like fetching data)
                Thread.sleep(2000); // 2 seconds delay
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            return 42; // Simulate some result (e.g., fetched data)
        });

        // Continue with further operations once the task is complete
        future.thenAccept(result -> System.out.println("The result is: " + result));

        // Keep the main thread alive for a while to allow the asynchronous task to complete
        try {
            Thread.sleep(3000); // Let the async task finish
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}
Explanation:
supplyAsync(): Executes the task asynchronously in a separate thread.
thenAccept(): Once the task is complete, it processes the result (prints it to the console in this case).
The main thread waits (Thread.sleep(3000)) to allow the asynchronous task to complete before the program exits.
Chaining Tasks with thenApply()
You can chain tasks together using methods like thenApply() or thenCompose(). The result of one asynchronous task can be used as input for the next task.

Example: Chaining Tasks
java
Copy
import java.util.concurrent.CompletableFuture;

public class CompletableFutureChainingExample {
    public static void main(String[] args) {
        CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
            // Simulate an async task
            return 5;
        });

        // Chaining tasks: Multiply the result of the first task by 2
        CompletableFuture<Integer> result = future.thenApply(value -> {
            return value * 2;
        });

        // Another chained task: Add 10 to the result of the second task
        result.thenApply(value -> value + 10)
              .thenAccept(finalResult -> System.out.println("Final result: " + finalResult));
    }
}
Explanation:
thenApply(): This method is used to process the result of the previous task (multiplying it by 2 in this case).
Chaining: We chain multiple operations, each of which is applied to the result of the previous one.
Combining Results with thenCombine()
Sometimes, you may want to run multiple asynchronous tasks in parallel and combine their results when both tasks are complete.

Example: Combining Results from Two Asynchronous Tasks
java
Copy
import java.util.concurrent.CompletableFuture;

public class CompletableFutureCombineExample {
    public static void main(String[] args) {
        CompletableFuture<Integer> future1 = CompletableFuture.supplyAsync(() -> {
            // Simulate a task
            return 10;
        });

        CompletableFuture<Integer> future2 = CompletableFuture.supplyAsync(() -> {
            // Simulate another task
            return 20;
        });

        // Combine the results of both futures
        CompletableFuture<Integer> combinedFuture = future1.thenCombine(future2, (result1, result2) -> {
            return result1 + result2;
        });

        // Print the combined result
        combinedFuture.thenAccept(result -> System.out.println("Combined result: " + result));
    }
}
Explanation:
thenCombine(): This method is used to combine the results of two independent asynchronous tasks. The lambda function defines how the results should be combined.
In this example, the results of both future1 and future2 are added together.
Handling Exceptions with exceptionally() and handle()
CompletableFuture also provides ways to handle errors and exceptions in an asynchronous task.

Example: Handling Errors
java
Copy
import java.util.concurrent.CompletableFuture;

public class CompletableFutureExceptionHandlingExample {
    public static void main(String[] args) {
        CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
            if (true) {
                throw new RuntimeException("Something went wrong!");
            }
            return 42;
        });

        // Handle exception using exceptionally
        future.exceptionally(ex -> {
            System.out.println("Exception occurred: " + ex.getMessage());
            return -1; // Provide a default value in case of error
        }).thenAccept(result -> System.out.println("Result: " + result));
    }
}
Explanation:
exceptionally(): This method is used to handle exceptions that occur during the asynchronous task. It provides a fallback value in case of an error.
In this example, when the exception is thrown in the supplyAsync() task, the exceptionally() handler catches the error and returns -1.
Waiting for Completion with get() and join()
You can wait for the completion of an asynchronous task using the get() or join() methods. However, these methods block the calling thread, so they should only be used when necessary.

Example: Blocking to Get the Result
java
Copy
import java.util.concurrent.CompletableFuture;

public class CompletableFutureWaitExample {
    public static void main(String[] args) {
        CompletableFuture<Integer> future = CompletableFuture.supplyAsync(() -> {
            return 42;
        });

        try {
            // Block and wait for the result
            Integer result = future.get();
            System.out.println("Result: " + result);
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
Explanation:
get(): This method blocks the main thread until the result of the asynchronous task is available. It can throw checked exceptions like InterruptedException or ExecutionException.
join(): Similar to get(), but it throws an unchecked CompletionException if the task completes exceptionally.
Real-Time Use Case: Web Service Calls
Let’s consider a real-world scenario where CompletableFuture can be used for making parallel web service calls.

Example: Fetching User Data and Order Data Concurrently
java
Copy
import java.util.concurrent.CompletableFuture;

public class AsyncWebServiceCallExample {
    public static void main(String[] args) {
        CompletableFuture<String> userDataFuture = CompletableFuture.supplyAsync(() -> {
            // Simulate fetching user data from a remote API
            return "User: John Doe";
        });

        CompletableFuture<String> orderDataFuture = CompletableFuture.supplyAsync(() -> {
            // Simulate fetching order data from a remote API
            return "Order: #1234";
        });

        // Combine both results after both tasks are completed
        CompletableFuture<Void> combinedFuture = userDataFuture.thenCombine(orderDataFuture, (userData, orderData) -> {
            return userData + ", " + orderData;
        }).thenAccept(result -> {
            System.out.println("Combined result: " + result);  // Output: Combined result: User: John Doe, Order: #1234
        });

        // Wait for completion (optional in real use cases)
        combinedFuture.join();
    }
}
Explanation:
Here, we're simulating asynchronous web service calls for fetching user and order data.
The tasks are performed concurrently, and once both tasks complete, their results are combined and printed.
