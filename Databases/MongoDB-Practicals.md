
1. login to atlas db ..mongodb.com
2. set up is done, create cluster ..
3. pip install pymongo

4. import pymongo
client = pymongo.MongoClient("mongodb+srv://ramkotni:ramkotni@cluster0.n8f5k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
print(client)

> client
>
> MongoClient(host=['cluster0-shard-00-02.n8f5k.mongodb.net:27017', 'cluster0-shard-00-00.n8f5k.mongodb.net:27017', 'cluster0-shard-00-01.n8f5k.mongodb.net:27017'], document_class=dict, tz_aware=False, connect=True, retrywrites=True, w='majority', appname='Cluster0', authsource='admin', replicaset='atlas-ue2nru-shard-0', tls=True)

5. Mongdb is document based DB
6. create a database instead table we create collection .. and also create documents

7. create db ..
8. client = pymongo.MongoClient("mongodb+srv://ramkotni:ramkotni@cluster0.n8f5k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
9. db = client['ramkotnidb']
10. colli_create = db['my_record']
11. data = {
    "name" : "ramkotni",
    "surname" : "kotni",
    "class" : "data science",
    "timing" : "flexi"
}
12.colli_create.insert_one(data)
13.you can see db, collection and record also called as document


data1 = {
    "email_id": "ramkotni123@gmail.com",
    "phonenumber" : 4535345345
    
}
colli_create.insert_one(data1)
--> to print all the records
for i in colli_create.find()
  print(i)

--> to find one record
colli_create.findOne()

-->
colli_create.find({"company":'ineuron'})

--> id >= 4
for i in colli_create.find({'_id' : {'$gte' : '4'}})
 print(i)

--> update 

colli_create.update_many({'companyname':'ineuron'},{'$set':{'companyname':'pwskills'}})

drop
colli_create.drop()








  
