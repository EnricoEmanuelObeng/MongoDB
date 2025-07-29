# MongoDB

MongoDB is a document-oriented NoSQL database designed for storing and managing unstructured or 
semi-structured data using a flexible schema design.


![image1](/images/image1.jpg)


<br>

## Documents

A document in MongoDB is a record in a collection, similar to a relational databases table row. 
Documents are stored in BSON (Binary JSON) format.

##### Example:
```JSON
db.academy.insertMany([{"course":"Data Engineering", "length": 10},{"course":"Data Analysis", "length": 8}])

<{
  acknowledged: true,
  insertedIds: {
    '0': ObjectId('68877f866d4aeba134e94a61'),
    '1': ObjectId('68877f866d4aeba134e94a62')
  }
```


## Collections

A collection in MongoDB is like a table in relational databases. 
It is a grouping of MongoDB documents. Collections do not enforce schemas, meaning that 
documents within a collection can have different fields and data types.

##### Example:
```JSON
db.createCollection('academy')
```
<br>

## MongoDB Architecture

### Replica Set
MongoDB Replica Sets are essential for ensuring data redundancy, by maintaining identical 
datasets across multiple nodes. Replica Sets the ability to scale horizontally.

#### Advantages
- **Automatic Fail over:** In case the primary node becomes unavailable, 
a secondary node is automatically promoted to primary without manual intervention.
- **Data Redundancy:** All nodes in the replica set have identical copies of the data, 
ensuring that data is never lost.
- **Improved Read Performance:** Secondary nodes can serve as read operations, 
offloading the primary node and enhancing performance.
- **Disaster Recovery:** Replica Sets can be distributed across multiple data centers 
to ensure disaster recovery.

#### Disadvantages
- **Data consistency:** MongoDB’s use of replica sets can lead to situations where 
all users aren’t reading the same data at the same time.
- **Memory use:** MongoDB stores its most frequently used data and indexes in RAM, 
so its performance is highly dependent on having sufficient RAM. Resulting in more resources consumption.
- **Storage overhead:** The self-containing document paradigm used by MongoDB can lead 
to larger storage requirements
- **Cost:** In scenarios where high availability and horizontal scaling are required, 
the cost associated with running and maintaining a MongoDB cluster can be significant. 


![image2](/images/image2.jpg)


### Sharding
Sharding is a method for distributing large collection(dataset) and allocating it across 
multiple servers. It is designed to handle horizontal scaling by partitioning data into smaller,
more manageable pieces, which are then spread across multiple servers.

#### Workflow
1. The data is split into chunks and distributed across multiple shards. Each chunk contains a subset of documents, determined by the shard key.
2. Routing: The query router (mongos) directs requests to the correct shard based on the shard key.
3. Configuration: The config servers keep track of the metadata to manage how data is distributed across the shards.

#### Advantages
- Sharding adds more server to a data field automatically adjust data loads across various servers.
- The number of operations each shard manage got reduced.
- It also increases the write capacity by splitting the write load over multiple instances.
- It gives high availability due to the deployment of replica servers for shard and config.
- Total capacity will get increased by adding multiple shards.

#### Disadvantages
- **Uneven distribution:** across shard’s can lead to overused/underused shards.
- **Backup & Restore:** In case of loosing/corrupting Config Server(holds the chunk information)
might lead to corrupting the complete cluster.
- **Immutable Shard key:** Neither the shard-key can be changed nor the field values can be updated.


![image3](/images/image3.jpg)


## Use Cases

### Real-Time Analytics and Data Integration

MongoDB enables real-time data analysis, which is crucial for businesses that need to make 
quick decisions based on current data. It flexibility and strong query capabilities 
make it suitable for integrating and organising data from various sources in real-time. 

### Weather Channel

The Weather Channel used MongoDB to develop its smartphone application, serving over 40 million
active users with real-time meteorological data. MongoDB's scalable solution
and MapReduce functionalities enabled real-time analytics and forecasts.

### Content Management nad Customer Analytics

MongoDB is ideal for content management systems (CMS) due to its ability to handle 
unstructured and structured data. It is also used to aggregate and analyse customer data, 
helping companies with customer service.

### MetLife

MetLife uses MongoDB for its customer service solution.
"The Wall" a customer service application allow users to view of customer payments, 
policy statements, and other information.

## Validation
Schema validation can be implemented to ensure that documents conform to a specific structure,
preventing unintended schema changes or improper data types

```JSON
{
  $jsonSchema: {
    bsonType: 'object',
    required: [
      'name',
      'course'
    ]
  }
}
```


## Embedding
 
Embedded documents in MongoDB are a powerful feature that allows you to nest documents 
within other documents. Essentially representing relationships between data.

```JSON
db.academy.insertOne({
  name: 'David',
  course: 'Data Engineering',
  trainer: {name: 'Luke', expertise: 'Data'}
})
```

## Useful lines

Update a document value
```JSON
db.action.updateOne(
   { name: "John Wick" },
   { $set: { year: 2014 } }
)
```

Deleted value
```JSON
db.action.deleteOne({name: "John Wick 3"})
```

Show general information
```JSON
db.characters.find({name:"Luke Skywalker"})
```

Show particular info
````JSON
db.characters.find({name:"Chewbacca"}, {name:1, eye_color: 1})
````

Don't show ID (get shown by default)
````JSON
db.characters.find({name:"Chewbacca"}, {_id:0, name:1, eye_color: 1})
````

Get a sub document info
````JSON
db.characters.find({name:"Ackbar"}, {_id:0, name:1, "species.name": 1}) 
````

**in** inside array
````JSON
db.characters.find(
  {
    eye_color:{
      $in:["yellow","orange"]
    }
  },
  {
    name: 1
  }
)
````

**and** filter
````JSON
db.characters.find(
  {
    $and: [{gender:"female"}, {eye_color:"blue"}]
  },
  {
    name: 1,
    eye_color: 1,
    gender:1
  }
)
````

**or** filter
````JSON
db.characters.find(
  {
    $or: [{gender:"male"}, {eye_color:"yellow"}]
  },
  {
    name: 1
  }
)
````

Change data types when there are errors or null values
````JSON
- db.characters.updateMany(
  {height: {$type: "string"}},
  [
    {
      $set: {
        height: { $convert: { input: "$height", to: "int", onError:null, onNull:null } }
      }
    }
  ]
)
```` 

Change data types and handle unknown values
````JSON
db.characters.updateMany(
  { height: { $type: "string" } },
  [
    {
      $set: {
        height: {
          $convert: {
            input: "$height",
            to: "int",
            onError: "unkown",   
            onNull: null        
          }
        }
      }
    }
  ]
)
````

Another way of changing data types
````JSON
db.characters.updateMany(
  {height: "unknown"},
  {$unset: {height: ""}}
)
db.characters.updateMany(
  {},
  [{$set: {height: {$toInt: "$height"}}}]
)
````

**eq** matching exact query
````JSON
db.characters.find({ hair_color: { $eq: "brown" } })
````

**gt** greater than
````JSON
db.inventory.find({ quantity: { $gt: 20 } }) 
````

**gte** greater or equal
````JSON
db.drones.find({ price: { $gte: 60000 } }).pretty()
````

**lt** less than
````JSON
db.characters.find( { height: { $lt: 100 } } )
````

**lte** less or equal than
````JSON
db.characters.find( { height: { $lte: 100 } } ) 
````

**ne** not equal to
````JSON
- db.characters.find({ height: { $ne: 200 } })
````

**nin** not equal to array
````JSON
- db.characters.find({ eye_color: { $nin: ['brown', 'blue'] } }, { _id: 0, name:1, eye_color:1 }) 
````

Change mass to double
````JSON
# Remove commas
- db.characters.update(
  {mass: "1,358"},
  {$set: {mass: "1358"}}
)

# Handle unknown
db.characters.update(
  {mass: "unknown"},
  {$unset: {mass: ""}},
  {multi: true}
)

# Cast into double
db.characters.update(
  {mass: {$exists: true}},
  [{$set: {mass: {$toDouble: "$mass"}}}],
  {multi: true}
)
````

Get all the fields
````JSON
db.characters.distinct('species.name')
````

Count
````JSON
db.characters.countDocuments({'species.name': 'Human'}) = 
````

Aggregate
````JSON 
db.characters.aggregate( [
  {$group: {_id:'$homeworld.name', max: {$max:'$height'}}}
]) = 

# Better version of aggregate
db.characters.aggregate([
  {
    $group: {
      _id: "$species.name",
      avg: {$avg: "$mass"},
      count: {$sum: 1}
    }
  }, {
    $match: {avg:{$ne:null}}
  },
  {$sort: {avg:1}}
]).toArray() = Find the average mass and count per species. Filter out null values and sort by average mass ascending.
````

