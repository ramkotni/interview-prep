No, thank you, MongoDB, okay, so coming to the journal link is journaling is nothing, but it's a checkpoints to provide a consistent view of data on disk and allow the MongoDB to recover from the last checkpoints. However, if MongoDB exit unexpectedly in between the checkpoints, journaling is required to recover the information that occurred after the last checkpoint.
It's a journaling is a wide Tiger create on journal record for each client initiated write operation. The Journal records include any internal write operation and caused by the internal write for example, updating a document in a collection may result in the modification to the indexes. Why did Tiger create a single journal record that includes both update operation it is associated to the index modification?
17? 17.
In Java, 17 you are asking you
collection, a collection,
okay, garbage collection is basically used to remove the focusing on the performance of the efficient and the efficiency. The key changes in this is g1 garbage collector. So default garbage collector in Java 17, g1 it received the performance enhancement and improve the including reducing a memory usages by identifying the removing the duplicate strings, and improve the performance when dealing with the large object and parallel full GC speed up of GC process, which significantly improving the application performance.
And Z. Garbage Collector is mainly so it is a low let.
So functional interfaces are interface which consists of a single abstract method. Each goes only single, abstract method. There are four types of a functional interfaces are predicates, consumer, supplier and the function predicates is nothing, but it accepts the inputs and judge it whether it is a true or a false. Mainly, we are using of any filter functions and consumer. Consumer is nothing, but it is accepts the arguments, but it does not return any return type will not be there, but it. Suppliers will act. They will not accept anything, but it gives us something output.
Predicates are basically used for the filter operation. I
Hello, you.
Sorry, option classes are used in Java eight futures to to use, to to avoid the null pointer exceptions so method likes or else will provide a default values if the value is for absent, while if present, execute the code only if the value is present. The equals method checks the Equality between the optional objects you
You want the position of you
Okay, position of for well sinister. I
Yeah, sure, I'll be using even a control Girl system. I
connection with MJ can be I
so I don't have the idea deleted. Can I write In the Online compiler? So
Okay, fine. So here we are. I'm using a boat of Java, eight futures. Okay, first, we are going to consider about of any int string input is wrong and well, I am going to add it now I'm going to take this As a input Stream. I
just code logic after code Logic and Rasta Ninja Pali I
So fail first, and the Fail say for the two. Okay. So the there are two things are there that is fail fast is iterators used to loop across the collection object, if the collection structure change, fail fast iterator immediately through the concurrent modification exception when iterating over the collection that was undergoes the structural change
the fail safe iterator. Do not throw any exception you
uh, to handle the concurrent modification. How to Handle, right?
Okay, so to handle the concurrent modification exception in Java, we need to use the regular hash map,
sorting key value pair, but
that is a thread safe, allowing the multiple threads to read and write data concurrently without explicitly synchronization. So the so the internal mechanism, the internal segment, Segment mechanism, where each segment is at its own block, enabling the efficiently to the parallel accesses to the different parts of the map. Just be a mindful potential concurrency issues when performing of complex operation involving in multiple key values update
where you might need to use the methods like compute to ensure the authenticity You
Yes, I was done. Yes, yes, I was
sub. Submit.
What? Okay, so submit and the executors are both were used in the executor services. This moth methods used to submit the task for execution. There are, there are key differences between them. First is executor. This method is inherited from the executor interface and does not return a value. It simply execute a given runnable task. But submitter is a method it will return the future object which represent the result of submitted task. You can also use this object to check if the task is complete,
wait for completion or retrieve the result you
compatible future we are we are going to use you.
What is the best using
from monolithic to the microservices application the process, need to break down into the single application, into the smaller and independent services. This can be complex and the time consuming process, but need to be helped the cloud agility. So the first thing we should wanted to plan like evaluate the current monolithic application, include the performance dependencies and the structure we need to identify the modulars, identify the logic into the independent modules and group of modules decompose, breakdown into the application, into the smaller and more manageable components, refactor, refactor the code data to split the database into smaller service specific databases. Design communication, design and implement a communication between the micro services. We need to test the architecture thoroughly and
track progress, monitor the application performance during of the migration you
micro services.
I was used a port of saga. Design pattern,
C, Q, R, S design pattern
and resilience for J like circuit breaker mechanism,
which design pattern i
Okay. Circuit tracker design pattern is an A. It is used to for the fault tolerance in our application. For suppose a micro services was communicating with the B micro services. In some cases, B micro services is not responding back to the a micro services, if something is going on happens, so the fault tolerance will handle this situation. There are three segments in it, half closed, under the open. So closed is nothing. But when a service A B is communicating with the service B, so it is in the closed state, but A is not communicating with the B, then it is in the open state. So during this open state, half open will every recurrently, like every five milliseconds, it will check whether connection is happened between A to
B. So this is the way we can implement a circuit breaker mechanism you
Yes, I worked on load balancing.
Load balancing in microservice is a process to distribute the traffic across the multiple services in the micro services architecture. It helps us ensure that no single server is over violent, and the application can scale up the needed. So main, main purpose of using of load balances to traffic between the services, user as a service poll and need to be configured to distribute a traffic evently user, the specific rules we need to automatically updating the routing table and when the server is added or removed, and load
balancer can redirect the traffic from the failed instance to the healthiest one. One
the other benefits of the load balancing are ensure ensuring resilience, responsive and the scalability. It help us decoupling the client for the scalability for
other services and load balancer also help to
remove the fault tolerance.
There are two types of things. Are there, server side load balancing and client side load balancing. You
one by using of in a dependencies, Eureka registry services, we need to use it this dependency and we need to write the configuration in our
application dot property file so that it will register in our Eureka server. You
in the distributor microservices architecture, we use the event driven architecture like
we use about transaction management and rollback mechanism we are going to implement so
a two stage commit program you are asking,
two phase, yeah, two phase committer is in the he says it is a like it's a distributed algorithm where it ensure the autumn city across the multiple process in the transaction. It involves the preparing phase where the participants vote to commit or roll back and commit phase where the coordinator
dictates the final actions.
This guarantee that there is a data consistency will be there. You
we are you? Yeah, we are using, often, a JWT token for the authorization and
and the authentication, also, role
based authentication. We are implementation. I rotation
authorization, sorry, it is.
We are using otter rate of controller advisors, and globally we are going to write exception handlers. Ah,
ah, JPA,
sorry, I
the criteria like, I didn't understand, what is the question?
JP, IR, we are using which
caching mechanism we are implementing, like cache at the rate of cacheable we are going to use it.
Enable caching annotation we are using and we will read it. You.
Many to one, right? So?
Okay, so we will use the cascading to
be used to the propagate change to associated within the entities.
And you need explanation, like, whatever, how, how I should want to do so one to many mapping otter, rate of many to one annotation is the one entity that represent of many side of a relationship, so many to one annotation, like a like, if they take an example for the student entities that is associated with the department entities. We need to write at the rate of join column, the name of how we are going to join. Join column is nothing but a foreign
key in the student table that reference the primary key of the department table. So
yes, cscd pipelines are used with Jenkins. I
confirmation jobs in Jenkins are
a deployment like,
just a second later. So we will write a scripts like generally basic pipeline script we are going to write to automate the production deployment, like we use the groovy syntax to check out coding from the repository, building the application,
running the test, Test and deployment into the production server. The
Yes,
elastic bin stack is in a bin stack in AWS is nothing, but it's a server which help us, developer, deploy and manage web application in AWS cloud. It automate the many deployment details, including capacity provisions, load balancing, auto scaling,
application, health monitoring and resource provision.
It simplifies the deployment managing and provision resources you it
supports to need to scale on the several millions of users. Also, it integrated with Amazon
relational databases services also like rds, also you can integrate it. Yes,
yes, I have experience, yes,
yes, mostly functional. Components rarely use the class components,
use state,
use reference. Okay. So, okay, so, fine. The use state is the managing the stateful values that triggers re render when they when they change. But the use reference is nothing but store the mutable values that persist
across the renders without triggering re renders.
Custom
Okay, custom hooks in React, like generally, when is a reusable components, we can use it that can encapsulate the component logic, enhance the code reusability and reduce the redundancy that but it should be named as the use prefix,
but followed by the let use
capitalized word.
One example, you record just a second. Let me think about one example.
Yeah, let us consider like,
like, help us in retrieving the values from the local storage. Like, use local storage,
we can use a use local storage is an A hook which we are going to use it.
Like, can I explain the code?
Or like, how I should wanted to utilize that? Hello.
Whenever, if you using of any local storage hook rich, which recently was created, it retrieves the initial value from the local storage and used to provide a default it syncs the changes the local storage whenever the state is updated. Let us consider a counter component when, when I use the use local storage, the counter comma zero to to store the counter state, persistently clicking the buttons and updating the count and save it is in the local storage
so that We can use the custom hooks In our React. I
The reactor, dot memo, no. Use call back.
Okay, use memo and react away, both the tools which help us to improve the performance by avoiding unnecessary render, re rendering power process So react, dot memo is a higher order component that can prevent unnecessary re renders of entire component. It is a best for the functional component that depends on their props. Use memo a hook that can optimize the performance by caching the result of a function. It is better for
components with complex internal logic, we can use the use memo.
So react dot memo wraps the around the component to memorize the RE Render Output. It re renders only when the props passed to the child component changes. But in the case of use, memo store the result of a function and only the reallocates it when it dependence changes, it useful for expensive calculations
or operation that aren't needed for every rendering you
use.
Okay, so use reducer is another tool which is used to it help us to aggregate a multiple states of components in one place, particularly in scenario that it involves in the states changes of multiple nesting levels and originating from the multiple actions types and resources use. Render
will use the access to the data and action to define in the reactor reducer Hi,
in the state management in the reactor, We can use the third party libraries that is called Redux. We can use it. State Management is nothing, but you can handle the update data that affect how your components render. So we can use the there are three types of any management with the local state management. We can use the use state hook, sharing the states between the components. We can use the props and context API, context
API, share the data across the multiple component Without a prop drilling. You
Yes, I worked on the
states in Redux.
So are you okay? I
ah, resetting in the Redux
state involves into like there are several approaches we can do it.
Okay, can I connect just a second? Let me take one example, and I'll explain you.
So whenever you are wanted to modify the root reducer to handle the global reset actions, we can use this thing reset
Redux state within the global accents we can be used
so and resetting of any individual slice in the Redux tool kit. I
Sorry, can you repeat again? You
localization in the React, generally,
it is in a it involves into the
it's a part. It's a partially important for us whenever web application reactor doesn't provide a built in localization futures, but we can achieve the localization by using library techniques, and internationalization will be helpful to it. So I
18. N is a I 18 library which we are used.
Yes, we use for Java, we use a vote of Any JUnit for
for reactive, we use the gesture you
react
fever. Okay, react to fever. I was worked on it.
It's basically to to provide builder.
It's a powerful tool to building of a responsive and renderable user
interfaces in the React application.
It was a
It allows the react to split the RE render box into chunks and spread into over the multiple frames i
Hello, Hello, hello,
ah,
Go Wrong
question,
complex code only
coding correctly. Otter,
result, result,
my connection
to Okay, okay, okay,
okay, okay,
okay, fine,
okay. Fine. Okay. Right, right. Thank you.