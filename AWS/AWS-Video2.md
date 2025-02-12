SAA - Solutions Architect Associate

Recap

Types of cloud computing

AWS History

Shared Responsibilty Model

Hands on AWS Account creation

Tour of AWS Account and services

Handson AWS Account Best practices

Hands on AWS Budgets set up

Free tier account - discussion


AWS Global Infrastructure

-- data centers el set up ayyayi .. regions, availabilty zone

Different ways to connect to AWS

IAM - Basics

IAM - Users

IAM - Roles

IAM Groups

IAM - Policies

Hands on IAM

1. AWS Global infrastructure


31 launched Regions each with multiple Avaialbility Zone

99 Avaiability Zones

4 more AWS Regions in Canada, Israel, New Zealand, Thailand


410 points of presence

India lo Mumbai, Hyderabad Nov 2022 is second region


NA, SA, EU , Asia Pacific, AF

ME - middle east ..

East, west, south ..

How to chose an AWS Region

compliance : data governance and legal requirements

proximity: customer reduce latency

private regions US Gove, China

Regions : logical grouping of Data centers

Every Region has 3 availabilty zones

and each availaibility zone has one to many data centers
AWS will not provide info related data centers..


website load ayi ....those latency issues..
if its near by location you can access fastly ..


Every service ... we need to select region ..


2. Different ways to Connect to AWS

console - website

CLI - cmd

SDK - software development kit ..

java, python, .net, php, Node, JS etc ..

python - boto3 library

3. IAM Service - Basics

Least privilege access ... principle ..
different scenario ..

IAM service ... I-Identiy  A-Access   M - Management

Identity

Manages the authenticaiton
username and password MFA
ex gmail, facebook

Access
Manages the authorizaiton
provides the permissions to use services


M - Management

4. IAM identities

IAM  -- users  identity for Humans / Applicaitons

Groups -- identify for collection of rleative users/departments

Roles -- identify AWS services or external or federated user

role attach ..EC2


5. IAM Access

user

groups  +++ policies - provides permission to identifies
allow or deny access to aws services

roles

Deny has highest priority ...

IAM Key points

IAM is a global service

it is hosted in N.Virgnia region

IAM is an AWS managed service

IAM is a highly available service


IAM is free of cost - no charges

IAM has direct / inderict integratiom

identity federation  - Microsoft AD Integrayion/
facebook / google/ Amazon

Allow / Deny within your account

Roles pi policies apply chestam 


AWS Managed policy

Customer managed policy ...




















