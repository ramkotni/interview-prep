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

Q1: What is your role and contribution at Amazon Robotics?
A1: I work as a Java Full Stack Developer at Amazon Robotics. My contributions span front-end, back-end, and cloud-based responsibilities. I focus on building high-performance, scalable, and distributed systems, working with Java, Spring Boot, microservices, and AWS to implement RESTful web services for communication between robotic systems and cloud platforms. Additionally, I work on multi-threading, event-driven architecture, real-time data processing, and database optimizations. On the UI side, I build responsive UIs using ReactJS and integrate them with backend APIs for a seamless user experience.

Q2: Can you explain how you use cloud technologies in your projects?
A2: I deploy and manage scalable applications using AWS services such as EC2, Lambda, S3, DynamoDB, RDS, SNS, and SQS. I implement CI/CD pipelines with Jenkins and GitHub Actions. Additionally, I use containerization and orchestration tools like Docker and Kubernetes for application deployment. We also integrate IoT protocols like MQTT and gRPC for seamless communication between robots and backend services.

Q3: How do you approach software architecture and design?
A3: My approach starts with understanding the business requirements for the project. From there, we categorize teams and analyze the architecture’s needs, considering aspects like traffic, networking, and code-level performance. We then break down the system into layers for modularity, define components, and create prototypes to visualize interactions. We use design patterns like layered architecture and client-server patterns to ensure simplicity, maintainability, and scalability.

Q4: How do you handle the migration from monolithic applications to microservices?
A4: To migrate from monolithic applications to microservices, we use the Strangler Pattern and Domain-Driven Design (DDD). The Strangler Pattern allows incremental refactoring, while DDD ensures that each microservice aligns with a specific business domain. We divide the monolithic system into smaller, independently managed services, and integrate tools like Kafka for asynchronous communication. For monitoring, we use Zipkin for distributed tracing. The complexity increases during migration, but it improves scalability and maintainability in the long term.

Q5: Can you describe the network architecture for your applications?
A5: We use a two-zone architecture with Amazon Web Services (AWS). Incoming traffic is routed through Route 53 (DNS server) to Internet Gateways, which connect to the VPCs (Virtual Private Cloud). The VPCs then connect to NAT Gateways, which distribute traffic across the various services. This architecture enables efficient load balancing and communication between services in a scalable and secure environment.

Q6: How do you use Kubernetes and containerization in your projects?
A6: Although we don’t use Kubernetes directly, we manage containerized applications with AWS ECS (Elastic Container Service). ECS is fully managed by AWS and allows us to deploy and scale containerized applications without the complexity of managing Kubernetes clusters. We use Docker containers for packaging applications and managing dependencies.

Q7: What are the key benefits of using a Content Delivery Network (CDN)?
A7: A CDN is a geographically distributed network of servers that caches copies of web content across multiple locations. It improves web performance by reducing latency and speeding up load times for users by delivering content from the nearest server. It helps with faster image, video, and JavaScript delivery, resulting in improved user experience.

Q8: Can you explain the concept of Auto Scaling in AWS?
A8: AWS Auto Scaling automatically adjusts the number of EC2 instances based on the traffic load. This helps us manage millions of users efficiently by ensuring the system can scale up or down depending on demand. It helps maintain application performance while optimizing cost.

Q9: How do you implement caching mechanisms in your application?
A9: We implement caching mechanisms to store frequently accessed data, improving performance by reducing database load. We use AWS services and CDNs to cache data at edge locations. For instance, caching static content helps deliver it faster to users based on their geographic location, which results in a better user experience.

Q10: How do you handle database optimization in real-time data processing?
A10: I focus on optimizing database interactions by minimizing database queries and optimizing the way data is processed in real-time. We use event-driven architectures and asynchronous communication to ensure the system can scale effectively and handle large amounts of data from multiple sources like robotic systems and cloud platforms.

Q11: How do you use design patterns in your architecture?
A11: In my architecture, I use design patterns such as Layered Architecture and Client-Server Pattern. The Layered Architecture separates the system into distinct layers, making it modular and easier to maintain. The Client-Server pattern works well with centralized resources, like banking or email systems. Both patterns help maintain simplicity, modularity, and scalability in the design.

Q12: How do you approach backtracking in algorithms?
A12: In backtracking, I define the base case and recursively build potential solutions. For example, when finding combinations, I track the remaining sum and store the current combination being built. By using recursion, I can explore all possible combinations and backtrack when necessary to find the optimal solution.


