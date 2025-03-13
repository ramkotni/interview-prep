Service Discovery Pattern:

Service Discovery allows microservices to find and communicate with each other dynamically. It involves a service registry where services register themselves and look up other services.

A microservices-based application deployed in a cloud environment where instances of services start and stop frequently. Service discovery ensures that services can locate each other without manual configuration, enabling automatic scaling and resilience.

What’s the Problem/Challenge?
Imagine you are writing microservices. Your company has adopted the microservices architecture you have Address Service, Employee Service, Course Service, Student Service, etc, etc. You have many spring boot applications and all the spring boot application has been deployed into many different servers and you might have thousands of applications. Right now all these applications let’s say Course Service wants to connect to the Address Service, Student Service wants to connect to the Course Service, and wants to get some course-related data then how will these servers communicate with each other? We will simply make a REST call and all these servers will communicate with each other using the REST API. But the real challenging part is when a server wants to connect to another server then before this server connects to this server it needs to know the IP address, and it needs to know the port number where this particular application is running in the server. 

This is not going to be a simple job to manage the thing where you have thousands and thousands of applications. How you will manage the server IP? How you’ll maintain their port number? Because every server, when you want some data from another server, it needs to connect to them, and in order to connect to them it needs to know the IP and the server address of that and it will be a really critical job to handle all the IP and the server ports where you have thousands of servers where you have split your one application into thousands of different modules and deployed into different servers. Don’t you think managing the IP and the server URL will be critical? In the case of a Monolithic Application, there we have only one server so we used to remember the server IP and the port but now your monolithic has been split into thousands of applications how’ll be handling that? And for that Spring Cloud is providing us with Service Discovery and Service Registry to handle this problem.

What’s Service Discovery in Microservices?
Suppose we have Service-A & Service-B and we have our Load Balancer placed inside a different server. Now let’s introduce our Discovery Service. Now what this discovery service will do now whenever Service-A and Service-B want to communicate with each other then whenever we are starting our Microservices we’ll be registering them with Discovery Service. And this discovery service right now will know what is the IP and port number of Service-A and what is the IP and port number of Service-B. All detailed information will be there with Discovery Service. Similarly, if we have many different instances of Service-B, all this Service-B which is running in different servers will be registering their information with Discovery Service. So it is one central location where we’ll be managing our host and the port number information inside this particular server. This is basically called registration because all the services whenever they are starting off they are registering themselves with the discovery service and now the discovery service is maintaining all their information inside a particular map or a list or a database. We called it a Service Registry.

So, Service Registry is a crucial part of service identification. It’s a database containing the network locations of service instances. A Service Registry must be highly available and up-to-date. Here, inside Service Registry we have 4 different instances of Service-B and they are running in some port number and some IP address. Similarly, for Service-A we have one different instance.

Now Service-A wants to connect to Service-B. Now the load balancer once get the request, it is gonna do a query with the discovery service that, hey, can you tell me what instances are there for Service-B? Now the load balancer finds out that there are this many instances available where Service-B has been deployed. Now Load Balancer is going to dispatch to one of the servers by looking into Service Registry. It can take all four instances of Service-B and whoever has less load then to balance the load, it can send the request to there.

Types of Service Discovery
There are two types of Service Discovery

Client-Side Service Discovery
Server-Side Service Discovery
In this article, we are going to explain Server-Side Service Discovery.

Server Side Service Discovery in Microservices
So, the example we have taken above we call it as Server-Side Discovery. The entire concept is called a Server-Side Discovery. Why so? Let’s understand it step by step.

Step 1: The client (Service-A) makes a request to a server that is it may be a Router, Load Balancer, or Middleman. In this case, it’s a Load Balancer.
Step 2: The server (Load Balancer) does a query with a Discovery Service.
Step 3: The Discovery Service responded back with available numbers of instances of Service-B that the Load Balancer can call.
Step 4: Then the Load Balancer server picks up one of the Service-B instances and makes a call.
Step 5: Here the Service-A(Client) doesn’t talk to the Discovery Service directly. It calls another server (Load Balancer) which helps to discover Service-B URL info.
And this complete pattern we called Server Side Discovery.

Advantages: In this approach, the Load Balancer does the job of load balancing. This is the major advantage of this approach. Undoubtedly, developing this level of abstraction makes the Service Consumer more lightweight, as it doesn’t have to deal with the lookup procedure. So there’s no need to implement the discovery logic individually for each language and framework that the Service Consumer uses.

Disadvantages: The disadvantage is we must set up and operate the Load Balancer unless it’s already given by the deployment environment.

Example:

NGNIX: Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy, and HTTP cache. Nginx is a free and open-source software.
AWS ELB: Elastic Load Balancer (ELB) is a service provided by Amazon in which the incoming traffic is efficiently and automatically distributed across a group of backend servers in a manner that increases speed and performance. It helps to improve the scalability of your application and secures your applications.

Client Side Service Discovery in Microservices
Imagine you have a Service-A and Service-B and a Discovery Service. Now whenever Service-A and Service-B start off they register themselves inside the discovery service. Let’s say there are a few more instances of Service-B. All the information has been registered with the Service Discovery and it basically maintains everything inside a registry. The registry basically has the instance list like how many Service-B are available and how many Service-A are available and what are their instance details. Everything is maintained in the registry. 

Now let’s say Service-A wants to connect to Service-B then Servic-A is asking directly to the Discovery Service and the Discovery Service is providing the URLs or the port number of all instances of Servic-B. So when Service-A wants to call the Service-B then the Service-B is going to reply to them back with all the instances which are available. In the below image, you can see all these four instances which are available inside the discovery service, the discovery service given back to Service-A. Now Service-A is going to call Service-B. Service-A has 4 different instances of Service-B and it will call the one which can take the load. Right now whenever Service-A will call Service-B it knows which of the server can take the load. So Service-A only will do the load balancing and will pick up one of the servers and it is going to dispatch a request. Now let’s say if there is another request that comes it will not give to the same server the service area will dispatch the request to another instance.

Whatever the request is going to hit from Service-A to Service-B then the load will be distributed between all these instances because right now Service-A knows that Service-B has been deployed in four different instances and Service-A will call Service-B and it will do the load balance. One thing you can see over here is there is no load balancer the client is asking Service Discovery to get the details of Service-B and again the client is doing the load balancing and calling the Service-B instance by itself. This is what we call a client-side discovery.

Advantages and Disadvantages:

Assigning responsibility for client-side load balancing is both a disadvantage and an advantage. It’s an advantage because it saves an extra hop that we would’ve had with a dedicated load balancer. It’s a disadvantage because the Service Consumer must implement the load balancing logic.

Example:

Netflix Eureka: Eureka is the Netflix Service Discovery Server and Client. The server can be configured and deployed to be highly available, with each server replicating the state of the registered services to the others.
Zookeeper: Zookeeper is a distributed, open-source coordination service for distributed applications. It exposes a simple set of primitives to implement higher-level services for synchronization, configuration maintenance, and group and naming.
Consul: Consul is a service networking solution to automate network configurations, discover services, and enable secure connectivity across any cloud or runtime.

Implementation:

<dependency> 
            <groupId>org.springframework.cloud</groupId> 
            <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId> 
        </dependency> 

package com.gfg.discoveryservice; 
  
import org.springframework.boot.SpringApplication; 
import org.springframework.boot.autoconfigure.SpringBootApplication; 
import org.springframework.cloud.netflix.eureka.server.EnableEurekaServer; 
  
@SpringBootApplication
@EnableEurekaServer
public class DiscoveryServiceApplication { 
  
    public static void main(String[] args) { 
        SpringApplication.run(DiscoveryServiceApplication.class, args); 
    } 
  
}

Why is this line eureka.client.fetchRegistry=false? 


By writing this we are saying discovery service that no need to fetch any registry from another discovery service. You are the only one here.


Why is this line eureka.client.register-with-eureka=false?


By writing this we are saying that there is no need to register yourself in your discover server registry. It knows the port number and IP and it knows how to connect with you. You are here to discover other microservices not yourself.

