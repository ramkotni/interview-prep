/******************************************************************************

                            Online Java Compiler.
                Code, Compile, Run and Debug java program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class Main
{
	public static void main(String[] args) {
	    int n=5;
        List<List<Integer>> result=new ArrayList<>();
        findcombination(n,new ArrayList<>(),result);
        result.forEach(combination->
              System.out.println(combination.stream().map(String::valueOf)
                                       .collect(Collectors.joining("+"))));
	}
	
	private static void findcombination(int n,List<Integer> tempList,List<List<Integer>> result){
	    if(n==0){
	        result.add(new ArrayList<>(tempList));
	        return;
	    }
	    for(int i=1;i<=n;i++){
	        if(! tempList.isEmpty() && i<tempList.get(tempList.size()-1)){
	            continue;
	        }
	        tempList.add(i);
	        findcombination(n-i,tempList,result);
	        tempList.remove(tempList.size()-1);
	    }
	}
}

============================


Bank of America.
American Express. I
Okay, I
this is Java full stack developer working in Amazon robotics. Mainly the contribution will be the front end, back end and the cloud based responsibilities, mainly focusing more on to the high performance, scalable and distributed systems coming to the back end application have worked us and maintained the high performance scalable back end services using Java, Spring Boot micro services and AWS and implementing a RESTful web services for seamless communication between the robotic systems and the Cloud based platforms, working on the multi threading environment, event driven architecture and real time data processing for optimization of databases, interactions with SQL and non SQL, where coming to the UI part, I build a response UI using React GS in monitor for some control robotic system integrated with back end APIs to ensure that seamless user experience, working with WebSockets, real time data visualization tools and coming to cloud computing part our deploy manager, scalable applications using AWS services, easy to lambda, s, 3d, DynamoDB, RTS, SNS and SQS were implemented by using of Jenkins, GitHub actions, CSD pipelines for AWS, I used to containerize and orchestration tools like Docker and Kubernetes For our applications, we also integrated with IoT integrations with protocols in Qt sub circuits, grcps to facilitate communication between robots and the back end services. Yeah,
Okay, I so as that, I
as architecture like I was mainly focusing more on trip to the like depends upon the project type. So based on the project type, we need to understand about of any exact business requirement. So based on the business requirement, we are going to do the further steps, like involvementing of any categorizing into teams, and from them there, we are going to analysis the what is the level of the architecture, by understanding about from them, what is how much millions, what's a traffic required, and what is the level of networking side, but of the coding side, and as well as the involvementing into the people budget, this all the things which comes under to the core architecting of any particular application as any software for the project. Perspective, I
as a software application dissolve it is involved divine into the structures of a system, including its components, modules and the interfaces. The first step is we need to understand the requirement. We need to make sure that understand the software needs and their constraints. Now we'll define the concepts. Now we need to consider how each component will be performed its specific task, and next dividing into layers. We will separate the applications into layers, each layer responsible for the specific set of functionalities. Next, we will create a prototype. We'll create a prototype for our design and visualize. We use the Visualize diagrams to visualize how the components will interact it. We consider the trade off some of the attributes each other, like content, contract each other. So there will be, always be any trade offs, documentation, document, architecture, designing and changes. So we can can understand the design choices maintaining of architects over a time. Coming to the software architecture design patterns we use, we have the two things, layered architecture and a client side client server patterns. In the layered architecture, separate task into the distinct layers, which make the system modular and easy to maintain while coming to the client server pattern works well with the centralized resources like emails and the bank and the banking systems.
So the main consideration is modularity, simplicity, clean architects and the DevOps architecture diagrams you
17 version we are using previously we use our 1118,
I I have about often a four years of experience for you.
See whenever we designing of a monolithic application to microservices application, the strangler pattern and Domain Driven designing are the two design patterns which we used migrate a monolithic application to the micro services architecture. Strangler pattern, a grand mic migration strategy that involved in building a new systems around the existent monolithic it allows to you incremental refactoring, continuous integration and deployment, so named after the fit that wraps around the tree, eventually eating it up. So useful when the monolithic affects the back box system like a third party software. So coming to the domain, driven designing, it involves in creational model and the business domain, using it to design micro services ensure that each micro services corresponding to the specific part of business domain and encouraged to create a micro services that align with the distinct domains within A application. So some challenges while we are migrating monolithic to microservices, architecture, complexity, data migration.
Yeah, I
Okay, so we are not going to disrupt of the existent services, so the same code, we will be refactoring that into to the micro services. As the micro services we are dividing of a monolithic application into the small chunks, means small, small services we are dividing and which is connected to their own databases, like recent our application is Amazon robotics. It was previously, it is in the monolithic application. Now we migrated that into a micro services application, where we use Eureka based micro services application. And some services are, we use synchronization, and some of the services are, we use asynchronizes communication. As we say, that is an Amazon robotics so frequently we are getting, often a data from the warehouse perspective. So these asynchronizes communication. We used Apache Kafka for communicating within our system robotic informations to our ERP system and with the communication between the services, we implemented about of in a figure where we use the load balancing and and to monitor this all the micro services, we use the Zipkin distributed raising system, but compared to the monolithic to the micro services, the complexity will be Very high. And to maintain this all the track. So
So, no,
no, we divided the applications into two zones, first in Zone One and the zone two. So the income traffic route 53 will implement it. This is a DNS server. From there, it is connected to the internet gateways. From the Internet Gateway, it will be connecting to the two distance servers. So from there it will be internet gate and networking, connecting, networking, application load balancing we are implementing and for our application to distribute our traffic. You
with internet gateways.
And so Internet Gateway will be connectivity. It will
internet load balancing. The load balancing will be connected to the NAT gates of the each services.
Gateways, yes,
our income traffic,
so, as we said, we are using often a into VPC connectivity. So Internet Gateway will be connected to the VPCs. So the VPCs having often a gateways. The these gateways will be connected to the NAT gateways. So NAT gateways will be distributed means servers, like depends upon the IP address it will be segregating into any two distinct services you
so in the Kubernetes part, we are not using as of no Kubernetes, we are using ECS services only that is called Full freshly managed by our AWS itself. Only pods are nothing but a to con to run the group of a one or more containers.
More containers together is known as called a force.
So coming to the container versus support, container is a lightweight unit of software that contains the code of an application, while pod is a group of container that can share resources. Both these are the fundamental components of Kubernetes only and managing the containerized applications. The purpose of the pod is to encapsulate the container for easy management and to share the storages, networking and a life cycle. But container will package the code and dependencies. Container will run the application process.
So to create of any
images to create the images,
we need to use the
it's a text based scripting container instruction. I
Okay, we are using of any Auto Scaling group, AGS in AWS. I
it will be the helpful so that to handle as of now, we are handling millions of user and it is implemented like content delivery network, so we need to implement a caching mechanism to store frequently, access to data and utilize the load balancer to distribute the traffic across the multiple servers and adopting a micro services architecture, obtaining of database queries, levering, leveraging the cloud services with Auto Scaling group capabilities, and using a Content Delivery Network, CDN for effectively static content delivery all will, designing will stateless application will enables the seamless distribution request across the servers, content delivery
networks for the servers to deliver the web content To the users based on their location.
So CDM,
okay, so
basically, the CDN is a geographical, distributed network of the servers that can store the couple store the copies of the web content across the multiple locations,
right which allows the user to access the contents from the server to closest to them.
It is result in the faster in loading time and improve the web performance by minimizing the latencies, like images, videos, JavaScript files, reduce the distance data travels and Improve the
Yeah,
Hello, madam will madable Internet is too slow. Number
laptop, laptop.
Okay, I want
the congregation.
Can I use the Java eight,
so combination in the senses, combination means it's some more multiplication or anything else, like how it is that I
only two digit like
two pairs, only like pair of the sum, only You wanted, I
Yeah, can I write a problem statement?
You for each loop to iterate our application, we use the for each loop,
the combinations for that purpose. We use that for it for each loop.
That is Java, eight, Future, so
collections will be collecting in the form of the list format or anything else. It will be joining all the things I
there is a main logic is done now we will going to rate off in a proper like find a combination. I find a combinations logic We need to write. I
uh to.
So one input right,
the first is the find the combination part. So second one is an A we first N is a remaining the sum we need to find out the achieve. The tempered list is current combination being built, so third one is a result.
Sorry, can you repeat again.
What is that view?
See the three arguments which first to first argument is n that will keep a track how much sum is left for each original N, we will decrement it. We will pick the number for the combinations. Next second one is a second one is a current combination being built. So this will store the number of forming of potential valid to the some combination, we will add a number to it recursively check if it is lead to the solution backtracking is if, if necessary For that backtracking purpose, we are using this thing you
let me complete my writing so that you will able to Understand and RAM chip pan di RAM. Let me complete my writing after that, I will explain to you.
I think
more Smart I
got it. I
No, I'm Clear.
No, actually, Thank you.
Hello,
Bucha.
Okay, Malachi, no one. I eat a gun on card them. I hear Aston on a day COVID Article output adjust to The i
three
but even if all it's allowed and I at
Lenny
certain, right.
Thank you. Thank you. Bye.
He was not On top of
given It is long day.
Given it is delivered.

