Virtualization Basics

EC2 Basics

Hands on - EC2 Linux

Hands on - EC2 Windows

SG
NACL - Network Access

Default VPC best practice
 - for production accounts delete the defualt VPC
 - do not use for the production workloads
 - 

1. Virutulization Basics


2. EC2 basics virutalization

ECC - Elastic compute cloud

3 tier architecute

front/end web tier
Back end app
Database

for all three layers what is the hardware capacity

4 core 16GB 4 core 16GB 4 core 16GB

what is the utilization in windows tasks manager
and linux using TOP command ...

we only use 20% utilized, remaining 80% is waste

80% is free

on premise .. it is used to be free, we are only using
20% .. cost is more .. cooling cost, maintianencase cost
operational cost ...

if you deploy backend and database on frontend server ..
if you put all three in single server ... now it will be used
100% ... previously it was 3 servers and now its one server

now cost is low ..
pubg heavy gaming applicaiton ... phone will hang if you open any other applicaiton ..its because of over consumption ..

web tier is using all the resource ..
it should use app tier resource ...
