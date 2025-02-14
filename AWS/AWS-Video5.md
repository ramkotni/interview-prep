Recap

Domanin Name Service

How the DNS working

Route 53

Register a domain

Hosted Zone

Record Type

Demos

Register a domain

Map S3 bucket to sub domain
Map Ec2 to sub domain

===================
Todays topic

Route 53

Public Hosted Zones
private Hosted Zones

Route 53 Health Checks

Routing Policies

Demos

  Health Checks
  Private hosted zones
  Failover routing policy
  Extending the hosted zones to other hosted zone.

Hosted Zones

A Route 53 hosted zone is DNS DB for a domain
ex rakeshtaninki.com

Globally Resilient ..

Hosted zones are automatically after the domain registration with Route 53

can be created separately for non Route 53 domain

public hosted zone

DNS Database hostedby Route 53 Public Name Servers

public or private hosted zone, private subnet or public subnet

like youtube.com

Accessible form public internet and VPC

Hosted on 4 Name servers (NS records)

private hosted zones

DNS data hosted by Route 53 private name server

Associated with VPC

Accessible from VPC only

Demo - Route 53 hosted zones

Utilize same domain in different account
using public hosted zone
private hosted zones

we will see the demo connecting 2 EC2 instances..

VPC lo DNS names resolve avvali ..
click on created hosted zones ..

connect EC2 instance with IP address

primary and secondary server

ping is not available .. check security groups ..

ICMP ports,,

ping secondary.demo.com ..

private hosted zones ..
second EC2 instance ..domain ..

Route 53 ping webserver .. 80 ..it will go unhealth ..
create health checks ..

Route53 health checks:
domain ki primary map ayi vuntundhi ... when unhealthy
dns lo it will change primary to secondary ...

Health checks are located globally
if you have any firewall - all the locations need to be whielisted
not only for aws resources but also for non aws resources
health checkers check at every 30 seconds default(10 seconds extra cost)

TCP / HTTP / HTTPS

Healthy / UnHealthy

Failover Routing Policy:


webserver 1 and webserver 2

use this route when primary 

active active .. passive ..

primary to secondar how it changes .. 

EC2 - creeat record and map one ip and if already record there
you cant create one more record ..

simple router, fail over routing policy, ip address or hostname
you can check in browser ..
failover threshold ..will take only 1 .. all the ips should
be whielisted. if you want notification .. enable seconds
you will get notification whethere staus is healthy or unhealthy

inbound rules .. edit inbound rules ..http ..fail
secondary ip will be mapped ..it will take maximum of 60 seconds

dns check ..propagation is happening ..dns propagation
will take time

Weighted Routing Policy:

Weight distirbution is possible for the records
for load balance we need to use load balacer


Latency / Geolocation / Geo Proximity Routing policy

Records works by latency / geo location and the Proximity

Based on user proximity Route 53 will analyze based on that
it will return the records ..


some times if the countries are in border like
pak / india / china ...

we get the records from pak / india / china ...


Failover Routing is very important, 

in exam point of view .. Multi ..
different policy ...

Vido 37:
========

VPC
 Flow logs
 private endpoints
   Gateway
   interface
Peering
Demos


VPC Flow logs:

 VPC
   private subnet
   public subnet

   Web server --> App server ...

   customers are accessing public network ...80 ports
   22 port, 53 port 

we did not enable logs .. security related projects VPC logs
we will have info related ports and the request come to the network

port no 80 and 443

ssh port ... 

some hacker will use other ports ..

Flow logs ... AWS will collect all the logs, we will analyze
the logs .. SIEM tools ..
Guard duty ... in the logs .. it will also record source
ip address ... from North Korea .. hackers ..

Threat Feed .. source ip .. malwares .. black list ips
around 70k and 1lakh ... AWS will provide Guard duty

VPC --> Subnets --> endpoints

s3 Bucket 

Cloud watch logs

Kinesis Data Firehouse ..

Flow log record ..

Capture metadata (not conetents)

source ip, what is the port what is the size
of input data ...

it will only print metadata ...

attached to a VPC All ENIs in that VPC
subnet All ENIs in that subnet
ENIs directly

Flow logs are not real time
log destinations $3 or cloud watch logs

Athena for querying the data ..

<version>
<accountid>
<interfaceid>
<srcaddr>
<srcport>
<dstport>
<protocl>
<packets>
<bytes>
<start>
<end>


yum install httpd -if
service http start

start apache server 

312 port we are getting reject


instance ip adress ..

ip address look up

VPC Private Endpoints (Interface)

 - Provide private access to all AWS Public services
 - Added to specific subnet - an ENI - not HA.
 - For HA .. add one endpoint to one subnet, per AZ used in the VPC.
 - Network access controlled via security groups
 - End point policies - restrict what can be done with endpoint
 - only TCP and IPV4
 - Endpoint provides a new service endpoint DNS
 - Eg: vpce-123-xyz.s3.app-south-1.vpce.amazonaws.com
 - Endpoint Regional DNS
 - Endpoint Zonal DNS


ENI - Elastic Network Interface ...

VPC End points - Demo

 - Gateway endpoints
 - Interface endpoints

 Will try to connect S3 from the above end points

 sudo -y

 ping google.com

 aws s3 ls


using endpoint, we can connect, if you do not have internet

aws s3 ls option ap-south endpoint url ..

VPC Peering

 - Hybrid networking ...if we connect from network to another network
 - vpc peering is not transitive
 - Direct encrypted network link between two VPCs
 - Works same/cross region and same/cross account
 - VPC peering doesn't support transitive peering.
 - Routing configuration needed, SGs and NACLs can filter.


 VPC Peering Demo

  - 3 VPCs
  - Peering b/w 3 VPCs
  - 1 EC2 in each VPC
  - Connect from one EC2 to another.

create peering connection ..
make changes in Route table

modify inbound and outbound rules.

for clean up activity

cloud formation .. slect vpc network delete
and peering demo .. delete ..

Video 40:
=========

Hybrid networking
 - S/w VPN  -- open VPN
 - Hardware VPN -S2S
 - Direct Connect
Demo
 - Transit Gateway(TGW)
 - Hardware VPN Demo - S2S

Today's topic

Event Driven Architecture
 - Queues
 Micros Service Architecture
 AWS Lambda
  - Demos
  - Cloud watch Eents & Event Bridge
  - Serverless Architectures.

  Event Driven Architecture:::

  activity completed only when event happens ..
  - server will create based on the request ..
  - compute environment create based on request.
  - no need to run 24/7
  ex: You Tube ...upload 4k video .. you tube is using
  tran coding ... youtube processing .. and it save 
  mdouele ..

  upload - processing - storage and manage

  if all modules are in single server then we call it Associated
  Monolithic.

  if any module fails ..it will stop working other modules also

  all fails if one component fails ..

  Scales together

  Bills together ..


  All 3 modules .. Tiered Architcuture ... upload .. processing
  store and manage ..

  for example if you upload 100 videos ...or 1000 videos
  it will have impact on upload and processing ..

  we will get the load balancer ... if it 100 one server
  more video, it will go to another module..

  1000 vies ... it will create 10 servers ..if its more
  more than 1k videos ..

  if you take Queue ...in the above case ..

  uplaod   ====Queue =====   

  4k video upload .. then send message to Queue ..

  Auto scaling Group ... Min 0, Desired 0, Max 100

  Queue message  lo vunna count ni batti servers create chestam.

  it depends on queue lentth ..

  IBM MQ and Rabbit MQ ..


  scale from 0 to n instances based on queue length

  Microservices Architecture:

   - for each service one server ...

   process module 1 upload 1 store mand mananger ..

   100 of small services ...

Each microservice execution has its own Core, RAM required
for the execution.


Event Driven Architecture::

 - No constant running or waiting for things
 - producers generates events when something happens
 - Clicks happens, errors, uploads , actions
 - Events are delivered to consumers
 - actions are taken & system return to waiting
 - serverless services are more capable of handling.


there are 2 components 1. Event Producer
2. Event consumer

Event produce ...

EC2 start or stop event ..click button ..event ..
sensor ..will send the data ..for every action is one event.

cloud watch events ..

Event Bridge ..

Mule soft ....

cloud watch or cloud trail .. if you pass it event bridge..
it will act as mediator ..

time based events .. pattern based events ..

- No constanct running or wiating for things
- if you look at lambda or fargate .. 
- EC2 will run server 24/7

AWS Lambda:

 - compute environment ..
 - lambda is servless ..when you request then only it will create
   server 
 - in lambda also .. they also use container ..
 - lambda .. is function as service
 - any automations are functions .. S3 lo upload ina filter
 process cheyali ..
 - event driven ..there also use function ..
 - http , response ela vasturndhi ..python, node, java ..
   container launch, env set up, runtime .. 
   - this is called cold start .. it will take some time
   to execute ..only need to wait for the first time.
   - 

- Function as a serivce Faas - short running & focused
- Lambda function - a piece of code lambda runs
- Funcitons use a runtime (ex python)
- fuctions are loaded and run in runtime environment
- the function has direct memory (indirect cpu) allocation
- you are billed for the duration that a function runs.

AWS lambda plasy key role in AWS ..

Deployment package

50 MB zipped
250 MB zippled ..

every lambda function you need to attach IAM Role ..

execution Role is very important ..

Memory min 120MB .. 10240 MB

you directly control the memory allocated for lambda functions whereas
vCPU allocated indirectly

custom runtimes alos possible ..

common runtimes, java python, node js

usage

servless application s3, api gateway lambda
file processing  (S3, S3 Events, Lambda)
Database triggers (Dynamo DB, Streams, lambda)
servless CRON (EventBridge/CW Events+ lambda)
Realtime stream data processing (Kinessi + lambda)

Evetns can be of 2 types

Time based
Event based
Event bridge is cloud watch events V2

A default event bus for the account.

Event bridge can have additional event buses.

Rules match incoming events .. or schedules

Rules route events to 1 or more targets ex lambda.

boto3 library ..python ..

Pattern based triggier : create a rule for that 

EC2 protect ..

















