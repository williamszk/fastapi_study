# to enter mongodb
mongosh
show dbs

# to create or use a database we just write:
use sales

db.sales.insertOne({
    "id":1,
})

show dbs

# how to remove dbs?
use MisbehaviorDetection
use carData 
use cityData 
use companyData 
use flights 
use shop 
use hospital 
db.dropDatabase()