What is CompletableFuture?
A CompltableFuture is used for asynchronous programming. Asynchronous programming means writing non-blocking code. It runs a task on a separate thread than the main application thread and notifies the main thread about its progress, completion or failure.

In this way, the main thread does not block or wait for the completion of the task. Other tasks execute in parallel. Parallelism improves the performance of the program.

A CompletableFuture is a class in Java. It belongs to java.util.cocurrent package. It implements CompletionStage and Future interface.

CompletionStage
It performs an action and returns a value when another completion stage completes.
A model for a task that may trigger other tasks.
Hence, it is an element of a chain.

When more than one thread attempt to complete - complete exceptionally or cancel a CompletableFuture, only one of them succeeds.

Future vs. CompletableFuture
A CompletableFuture is an extension to Java's Future API which was introduced in Java 8.

A Future is used for asynchronous Programming. It provides two methods, isDone() and get(). The methods retrieve the result of the computation when it completes.

Limitations of the Future
A Future cannot be mutually complete.
We cannot perform further action on a Future's result without blocking.
Future has not any exception handling.
We cannot combine multiple futures.
Future has so many limitations, that's why we have CompletableFuture. CompletableFuture provides a broad set of methods for creating multiple Futures, chaining, and combining. It also has comprehensive exception handling support.

Creating a CompletableFuture
We can create a CompletableFuture only by using the following no-argument constructor.

CompletableFuture<String> CompletableFuture = new CompletableFuture<String>();  
Example
The most frequently used CompletableFuture methods are:

supplyAsync(): It complete its job asynchronously. The result of supplier is run by a task from ForkJoinPool.commonPool() as default. The supplyAsync() method returns CompletableFuture on which we can apply other methods.
thenApply(): The method accepts function as an arguments. It returns a new CompletableStage when this stage completes normally. The new stage use as the argument to the supplied function.
join(): the method returns the result value when complete. It also throws a CompletionException (unchecked exception) if completed exceptionally.
File Name: CompletableFutureExample1.java


import java.util.Arrays;  
import java.util.List;  
import java.util.concurrent.CompletableFuture;  
public class CompletableFutureExample1   
{  
public static void main(String[] args)   
{  
try  
{  
List<Integer> list = Arrays.asList(5,9,14);  
list.stream().map(num->CompletableFuture.supplyAsync(()->getNumber(num))).map(CompletableFuture->CompletableFuture.thenApply(n-  
>n*n)).map(t->t.join()).forEach(s->System.out.println(s));  
}  
catch (Exception e)  
{  
e.printStackTrace();  
}  
}  
private static int getNumber(int a)  
{  
return a*a;  
}


Async Methods of CompletableFuture
CompletableFuture provides a set of asynchronous methods that allow for non-blocking operations, enabling the execution of tasks in a separate thread without blocking the caller thread. These methods are essential for developing responsive applications, especially when dealing with I/O-bound tasks, complex computations, or any process whose duration is unpredictable. Here's a summary of some key async methods provided by CompletableFuture:

thenApplyAsync()
The thenApplyAsync() function processes a task's outcome asynchronously, yielding a new CompletableFuture containing the modified result. A distinct thread from the ForkJoinPool.commonPool() carries out this processing, ensuring the operation does not block the calling thread and enhances application responsiveness by leveraging asynchronous execution patterns.

Filename: CompletableFutureExample.java

import java.util.concurrent.CompletableFuture;  
import java.util.concurrent.ExecutionException;  
public class CompletableFutureExample {  
    public static void main(String[] args) throws ExecutionException, InterruptedException {  
        // Asynchronously retrieve a user's name  
        CompletableFuture<string> userNameFuture = CompletableFuture.supplyAsync(() -> {  
            // Simulate a long-running operation, such as fetching from a database  
            try {  
                Thread.sleep(1000); // Sleep for 1 second to simulate a delay  
            } catch (InterruptedException e) {  
                Thread.currentThread().interrupt();  
            }  
            return "John";  
        });  
        // Process the result of the previous CompletableFuture, append a greeting  
        CompletableFuture<string> greetingFuture = userNameFuture.thenApplyAsync(name -> {  
            // Append the greeting in a separate thread from the ForkJoinPool.commonPool()  
            return "Hello, " + name + "!";  
        });  
        // Wait for the completion of the CompletableFuture and print the result  
        System.out.println(greetingFuture.get()); // Outputs: Hello, John!  
    }  
}  
</string></string>  

thenAcceptAsync()
The `thenAcceptAsync()` function facilitates the asynchronous consumption of a task's output, where no value is returned. Execution occurs on an independent thread from the `ForkJoinPool.commonPool()`, ensuring that the main workflow remains uninterrupted by this process.

Filename: ThenAcceptAsyncExample.java

import java.util.concurrent.CompletableFuture;  
import java.util.concurrent.ExecutionException;  
public class ThenAcceptAsyncExample {  
    public static void main(String[] args) throws ExecutionException, InterruptedException {  
        // Asynchronously compute a user's score  
        CompletableFuture<integer> scoreFuture = CompletableFuture.supplyAsync(() -> {  
            try {  
                Thread.sleep(1000); // Simulate a delay, e.g., fetching from a database  
            } catch (InterruptedException e) {  
                Thread.currentThread().interrupt();  
            }  
            return 85; // Example score  
        });  
        // Asynchronously consume the result of the CompletableFuture  
        CompletableFuture<void> resultFuture = scoreFuture.thenAcceptAsync(score -> {  
            System.out.println("User Score: " + score); // Consume the result asynchronously  
        });  
        resultFuture.get(); // Wait for the completion of all asynchronous operations  
        // Additional logic here if needed...  
    }  
}  
</void></integer>  

runAsync()
The runAsync() function facilitates the execution of a task in an asynchronous manner, where no return value is expected. Execution is carried out on an independent thread within the ForkJoinPool.commonPool(), ensuring the task does not interrupt the main workflow.

Filename: RunAsyncExample.java

import java.util.concurrent.CompletableFuture;  
import java.util.concurrent.ExecutionException;  
public class RunAsyncExample {  
    public static void main(String[] args) throws ExecutionException, InterruptedException {  
        // Execute a Runnable task asynchronously  
        CompletableFuture<void> future = CompletableFuture.runAsync(() -> {  
            // Simulate a task, e.g., logging  
            System.out.println("This is an asynchronous task running in a separate thread.");  
            try {  
                Thread.sleep(1000); // Simulate some delay  
            } catch (InterruptedException e) {  
                Thread.currentThread().interrupt();  
            }  
        });  
        // Wait for the asynchronous operation to complete  
        future.get(); // This blocks until the task is completed  
        System.out.println("Asynchronous task completed.");  
    }  
}  
</void>  


}  
