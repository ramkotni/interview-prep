


Krishsoft Solutions
Today at 10:26 am

Copy Summary
SummaryTranscript
Keywords
Speakers
Angular is a TypeScript based, free and open source, single page web application framework. It is developed by the Google and the community of individuals and cooperation. Angular is a completely rewrite of from the same team, but built in the AngularJS. You
okay, Fine, you.
Okay,
Sure,
Angular, 15 version. Lastly, which we used, so we focus More on the 15 only.
Okay, I
they Project or
realizing? Project I
department,
Java, stuff, So I
i have good knowledge on Angular and Angular 715, version I was using In my project. Now I The
the Inventory
details,
I Guess. I I worked on the Amazon robotics ERP system we are using of Angular 16 well interacting with REST APIs, with RxJS, I optimized the page loading time by implementing a lazy loading and catchy techniques we use the Angular material for the UI components and ng RX for the state management application. One challenge was handling of large dataset efficiently, which I solved by using of pagination and the virtual scrolling you
this is the Amazon robotic application, like it will collect all the information From the warehouse, and it will integrated with our ERP system.
Details of the robots.
RAM explained, explain your job, what you did in the ERP. You
is okay, that sounds interesting.
So this website, again, Java, Spring Boot, micro services,
service application, and we have the three databases we are connecting to maintain login credentials. We use the DynamoDB and the large product warehouse data that will be stored in the MongoDB. And some of the services we use, about of Oracle database for the vendor connectivity services we use Oracle Database do
see Oracle, they both are the one relational another is a non relational delay databases. See, non relational databases is nothing but a where it's a JSON format, it will store like a large and the large quantity of any data which we cannot store in the relational format. So we store that into MongoDB like as we know that the warehouse, we have different types of products and different types of set of data, where we are maintaining of any trillions of data, this will be maintained in the MongoDB only. So in the vendor format, we are onboarding of any vendors and the sellers who are the registered for our Amazon applications, both even delivery partners also, so that it is a largest amount of not small, large amount of data, so that we will connect with the Oracle databases. Do
Is it running in the production environment as of now? Initially we are I also contributed some of the APIs to connectivity for the production environment,
it is continuously, it is continuously changing that application because the recent technology we are implementing so that we are continuously changing of our application. Yes,
Team 250, people in that working if to open, my team is about of 12 people. You
a code reviews, code reviews, I will do it and even have us even, I will do the sometimes of coding also, and I need to maintain all the code code reviews, previews and PR requesters. We need to maintain and story points are signings and
developmenting of an
we are using of any Eks server that is called elastic humanity services and ECS services, which we are using because it's a Amazon product. So we completely use AWS services only and CDN for the content delivery network. And the route 53 is in a DLs server, which we are implemented. And we store all the images related information in s3 bucket, all the files. And we use the notifications for SNS And SQS services. I in
terms of
so whenever we discussing like, we debugging the complex production issues, just like monitoring application performance, handling of any deployments and understanding the error logs similarity with the production specific configuration, we get optimize the techniques and ability to collaborate with the teams and resolve the production indicates effectively. So one such previously, I identify the I troubleshoot by using identifying the root cause of the issues in the production environment, including network errors, data inconsistence and unexpected behavior in complex Angular application, utilize the browser developer tools and debugging the techniques to pinpoint the problems within the application logic and the UI analysis the errors log and stack tracks To diagnose issues effectively, and we performance optimization. Also, we implement a strategies to implement the application load times and the responsive
we use a third party only, Amazon Cognito. We use the Amazon Amazon Cognito we used, which we integrated with our Angular application. So whenever you log in, so that it will connect it to the Amazon Cognito. From the Cognito only, it is Maintaining of our authentication and authorization. So
think production
issues. That certificate
issue We started
with so now, recent, critical, one of The critical issues which we are faces delay in the order processing in ERP system, which causes a backlog in the warehouse automation. The problem was when a large number of concurrent APIs over blind the system, leading of slow responses and even timeouts. The main root cause analysis I was done is it's a high databases bottleneck with high frequency queries to retrieve a real time inventory updates, where the slowing down the system insufficient API calls. Some of the API calls are not optimist, causing redundant request freezing of in a UI, also due to the asynchronizes call, its improper handling of asynchronizes operations. So we use the solutions for that. We immediately index the query optimization and reduce the execution time. And we created API rate limit and catching, introducing of radius catches and reduce the redundant API causes and improve the response of data time, implementing of RxJS and Lady loosing in Angular, used debounce time and the switch map to optimize the API request to prevent UI lag and asynchronizes job process. Use the rabbit MQ to handle The larger transaction queries effectively do
the out of memory errors in the production environment you are asking right
production environment,
the out of the server of the application running it, it's exhausted in available memory, unable to allocate it to the further space to create a new objects or data. This will resulting in the crash of Mal malfunctioning operation. So usually due to the high load and insufficient to keep memory within the application.
First, I need to identify the root cause analysis of excess memory usages the implementation solution like it, increaseable available memory on the server. We optimize our application code and use the memory efficient and memory use the closes closely and potentially adjusting the application memory, allocating the settings, depends upon the programming language and frameworks which we used it.
So we use the profiling tools to adjust our JVM settings by increasing of heap size flags like XM X and XMS. Optimize your code to reduce the memory consumption and potential investigating memory leakages, Heap dumps and generated when errors occurs if the necessary required scaling of your application large server with the more RAM So we will keep Yeah,
okay, so enjoy. What are the building so the so it offered to the profound benefits in the scalability and maintainability, the statics, the main building blocks of ng are excess state accent reducers, effects and in the selectors,
so the
which provides a background functionality not directly related to The views, such as the fetching of inner data, such services to be integrated in the components depends and make your code modular, reusable and effective, So that are the building blocks of our Angular you
Oh, can I explain a boat of any each individual building block?
Both I can tell 5050, because I invited into the initial phase with the back end, and I have no knowledge in The front end. Also you
Okay, so pagination, so we implemented in a so first we need to specify the scrolling window property, if you are not using the whole window, and we use the overflow scroll property to emulate the scrollable dev So, and we use the scroll component classes to need to have an item and the property of the class not able to wearable. So I
I need to explain intact and complete project. Time explain. I need to, you need to explain about complete project while we are using a working on Amazon robotics, CRP, one of the critical Yeah. I citizen, while we are working on Amazon robotics ERP, one of the critical challenge I was faced is handling of a large set effectively in Angular front end. Since ERP system process massive, the
Yes, yes,
yes, we use
so basically
in RX JX, merge map and switch maps are the both operators that map values or to the observable, and the merge them into in a single observable. So the merge went when we need to use when you wanted to merge the multiple observable into in a single stream, you need to use the Merge map. When you wanted to switch to the latest observable, then you need to use the switch map. Merge. Map is good for a list of items in the shopping cart, while switch map is commonly used with the Http get calls You
switch to him,
done, yes,
like, so like front of we have about of seven zones. Seven zones we have deployed our application. So each zone will be connected to the internet gateways. From the internet connector will connected to the load balancer. This load balancer will maintain the availability all these zones. So the income request will be first will be from the route 53 route 53 will be connected to internet gateways. Internet gateways will be connected to the load balancers. This load balancer will be connected to the public subnets where we have our React and Angular applications. And nginx reverse proxy server will be connected from the front end to the back end. Application from the back end, it is connected to the Gateway servers, where, in the gateway servers, we implemented ASG like Auto Scaling group. So these auto scaling groups will be connected to private subnets where we implemented all our ECS services for our all the micro services application. All these micro services is connected to the relational RDS and elastic cache and the dynamod.
for our application you
Yes, yes.
Auto, scaled automatically so it is connected to the networking load balancing so that networking load balance itself, it will give the correct action. I
Uh, yes, it is IoT application like IoT application only will collect the data and MQ, TT like data only, data so and that will send it to the ERP system. From there we are going to analysis from the which vendor, which the data, we analysis the products
that will be connected to the delivery partners,
seven zones.
No, it's not a product. Seven availability zones means there are. It's very big project.
Large number of our
applications are involved. I
availability zones like our server, we Keep it in The seven zones so
so the transaction flow for our application is like, like we are using of a event driven architecture only, like we are implemented of the micro services by using of saga design pattern, which we implemented. Not much aware about of that, but we have an application level. I was this a very large project. I worked, worked on this very particular areas only you
okay to configure for our auto scaling first, we need to have an easy to console, and we will select the Auto Scaling group. We'll select the creating Auto Scaling group, and in it we need to launch the template VPC. Will choose the VPC networks, and we need to create a subnets. Choose a subnet from each availability zone that you want to include, and the instant type choosing of that. Instant types we need to configure for advanced configurating. We need to provide a attaching of load balancing and health checks by turning of the elastic load balancing health checks and health check grace period now we will enter how long to wait before the checking and instances health status, and we'll create an A ASG, right? You. It.
Thank you. Thank
Can you come again with the question? Please? You
sorry I'm not able to hear you do
so like
so in error handling in our Angular application, we basically we use the catch and catch errors. So basically we implemented catching the errors for our observable. We create rejected promises and creating of an error compression when using of Switch, map, merge map, contact mat and exhaust map to
major question, 15 and both 15 and 16, we are upgrading now to 18.
Yes,
yes, I'm familiar with the signals. I
it's future which help us to manage the State and the data flow of our applications.
You okay, by using
of we are using Amazon Cognito only, right? So security, authorized person only we can able to access it. We implemented the JWT token, so it is a role based authentication which we are implemented. So authorized person only can able to access that end point. So we configurated with the help of spring security, where we use the security filter chains and in the request matches, we are restricting the endpoints who have the access of the right person you
it, yes.
Yes, it is so monitor, yes,
for CAC pipe you are
talking. About of sentry application? No, I don't have an idea, but I have a card. I
just specifically about of what we are doing is generally the implementing of optimizing of our Angular application. Recently we are implementing so we are performing of any like, we optimizing of images and on push change, detect, detections and any related issue of the loading, because the application is already developed. And then we are whenever a new, new, like new data will be populated that in the UI it is populating properly. Or what are the data? What are the products that need to be provided on priorities we need to be aligned. So for that purpose, we definitely will check the using of an angular also, I so
we use reducing often a male bundle size and making downloading often A praise phrasing fasters for our Angular application. Yes, yes, we Yes. One of the prototype application we are developing. We are developing You.
You know They
want locations, location.
Okay, yes, we Yes, we use Apache town, inbuilt so
sorry I didn't get your question. Please.
Apache, Tomcat, server,
by default, deleted set. I want to auto configurators externally. You need to exclude the Tomcat server, and we need to Add the palm dot XML file that particular server so
Okay, yeah, I can tell you something like A best practices, which I was faced in my so first thing is accept and respond with the JSON. Use the nouns instead of verbs in the end point, path names, the collection with the plural names, only nesting the resources for hierarchical objects, handle the error rates gracefully, and the written standard error codes allow the filter, sorting and the pagination, maintain the good security practices, catch the data To improve the performance and versioning of our APIs in on the
day of July
And mostly on the Non scale, MongoDB,
okay, yeah, we are not Using hibernate. We are using spin data, JPA, I Okay, do
you Yeah, in transaction management, we used in the springboard application at the rate of transactional annotation used to manage the transactions in Spring Boot application to configure its spring transaction. This annotation will help us in the class level or the method level. The transaction is a sequence of the actions performed by the application that together pipelined to perform a single operation, for example, like you are booking a flight ticket. Also a transaction where the end user can enter his information and make the payment to book the ticket. So that is the transaction which we did. We so basically, if the user has entered the information of the user information, get stored in the user info table. Now to book the tickets to make online payment due to the some reason system failures, the payment has been canceled, so the ticket will not book for him. But the problem is that the information gets stored on the user info table on the large scale of more than a 1000s of these things happens within a single day, so it is not a good practice to store in a single action for the transaction. So to overcome this problem, spring provides a transaction management which used to annotation to handle these issues in that scenario, spring stores the user information in temporary memory that can checks for the payment information. If the payment is successful, then It will be complete,
like We use the propagations. I
a rollback mechanism, how
so we have separately dev teams for it. Mostly whenever I get structure with some of the application, I use the indexing and I will have the writing of queries also, whenever we are writing off a native queries for our application, then there is a some activities that you need to perform in the databases. Also, I will check that the weather data is properly inserted or retrieving of the processing during my development of our native queries. Now we are converting native queries to the Spring Boot JPS streamers, so we avoid writing of queries, and we are using of JPS streamers only. So it's a clean code which using of Java eight futures and implementing of very proper manner. So retrieving of inner data, okay,
meeting next time June is you're
asking about of next or nest.
Okay, next. JS is nothing but a it's an A like it's an open sources web development framework created for the very cell. It's a react based web application with the server side rendering and static rendering. So
rendering purpose we use the next js. It's a popular react framework with extend of React capabilities which provide powerful tools for servers and rendering, static site generation and full stack development we can be done with help of next js, it widely used for SEO friendly, high performance web application Easily you
by using of observables and the promises
In Angular a synchronizes operation.
So in case of any promises we handle, I
in Angular or in spring bottom. I Okay,
so if you wanted to implement a Spring Boot API that can accept both the input parameters and the file upload, so we need to like for that, I used about of any web flux because it handled the asynchronization operation like
Spring Boot starter Web flux.
So while you in the post mapping, we will give the static file upload a directory we need to be provided. And in the post requesters, we need to give the request to params, like, what are the parameters that you should want to pass that is called the file, and the rest of all the entities we will consider as an one data. So now first, we ensure the directory is existed or not, and then we will save that file. We need to provide the file. So if the responsible entity is okay, then the file is uploaded successfully for the particular user, or if there is an error, any error, then the error is any uploading the file, it will be retrieved.
Yes, yes, Yes.
File, Uploading directories. I
so that is depends upon the logic, how you are going to write it. Yes, you can handle the both to the post, to the file uploaded and the same request in single call and separate based on our requirement. We can do the both approaches. We can do it so you can send the both the input parameter of the file, multi part and the form data request. You can send it or otherwise, you can also send it to the multiple guide, like you get it first, you can store the user information. And then you can separately applied the link also, that is also fine. Generally we see in these applications, into the Our application, like whenever you are Uploading, I
if you are implementing multi part file uploaded and that you wanted to scan the upload file for the various files from virus, malware and other checks. It is a best performance using of a synchronization avoiding blocking the main request thread. So you can achieve that. Asynchronizes file scanning in the Spring Boot we have it. So first we need to upload the file to the store in the temporarily respond immediately to the user so that it does not wait the scanning process. Run the asynchronizes background task to scan the file. Once the scanning is complete, let update the status file. Status safe or infected, we need to be throws. We need to use enable asynchronizes In the main class itself. So for that and we will implement order the file upload API key in the async scannings. We need to implement it.
We in Java, we have the compatible future so that, with help of async annotation, we can stimulate the time consuming virus scanning process. Okay, so
what is the text tags that you are using?
Any source You
Thank you. Thank
it question,
experience on killing delivery, I
Okay,
----
inerview will be on Angular 1. what is the latest version used. 2 how will you connect API from Angular. 3. Methods of Angular 4. explain angular work experience 5. how do you construct or protect code in angular 6. algortihms or principles used in angular 7. compare angular react and vue.js

# Angular Interview Q&A

| **Question** | **Answer** |
|--------------|------------|
| **1. What is the latest version of Angular used?** | As of February 2025, Angular 15 is the latest stable version. |
| **2. How will you connect an API from Angular?** | Angular connects to an API using the `HttpClientModule`. You inject `HttpClient` service into your component or service, and then use methods like `get()`, `post()`, `put()`, or `delete()` to communicate with the API. Example: ```this.httpClient.get('API_URL').subscribe(response => { console.log(response); });``` |
| **3. What are the methods in Angular?** | Common Angular methods include: <ul><li>`ngOnInit()` – Lifecycle hook that runs when a component is initialized.</li><li>`ngOnChanges()` – Called when an input property changes.</li><li>`ngDoCheck()` – Custom change detection.</li><li>`ngAfterViewInit()` – After component’s view initialization.</li><li>`ngOnDestroy()` – Cleanup before destroying the component.</li></ul> |
| **4. Explain Angular work experience** | Angular provides a comprehensive framework for developing single-page applications (SPAs). It supports modular development, two-way data binding, dependency injection, routing, and forms handling. Working with Angular involves creating components, services, modules, and leveraging RxJS for managing asynchronous operations. |
| **5. How do you construct or protect code in Angular?** | To protect code in Angular: <ul><li>Use **environment variables** to manage different settings for development, production, etc.</li><li>Minimize bundle size by using **tree-shaking** (removing unused code) and **AOT (Ahead of Time) compilation**.</li><li>Use **Lazy Loading** to load modules only when needed.</li><li>**Obfuscate** the code during production build using tools like Webpack.</li></ul> |
| **6. What algorithms or principles are used in Angular?** | Key algorithms and principles used in Angular: <ul><li>**Dependency Injection**: To manage services and dependencies in the application.</li><li>**Change Detection**: Efficient detection of changes in the application’s state.</li><li>**Observables (RxJS)**: For handling asynchronous operations and event-driven programming.</li><li>**Routing and Navigation**: For managing views and URL states within the app.</li></ul> |
| **7. Compare Angular, React, and Vue.js** | **Comparison of Angular, React, and Vue.js**: |
| | **Feature** | **Angular** | **React** | **Vue.js** |
| | **Type** | Full framework | Library | Framework |
| | **Development Approach** | Opinionated, full MVC | Unidirectional data flow | Flexible, similar to Angular but simpler |
| | **Learning Curve** | Steeper, due to complex concepts like Dependency Injection and TypeScript | Moderate, focused on components | Easier to pick up, simpler structure |
| | **Architecture** | Uses components, services, and directives | Focuses on components | Uses components |
| | **Data Binding** | Two-way binding (via NgModel) | One-way binding | Two-way binding |
| | **State Management** | Built-in (NgRx for complex state management) | Redux (optional but common) | Vuex for state management |
| | **Popularity** | Popular for enterprise applications | Popular for fast UIs (React is widely adopted) | Gaining popularity for its simplicity and flexibility |
| | **Community & Ecosystem** | Large, extensive ecosystem | Very large, huge ecosystem | Growing community |
| | **Performance** | Good, with AOT and tree-shaking | Excellent for rendering large UIs | Excellent, smaller bundle size compared to Angular and React |
