import random
import json
from elasticsearch import Elasticsearch
from elasticsearch_dsl import Search, Index, Document, Long, Keyword, Float
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

# the most common first names
firstNames = ["James", "Robert", "John", "Michael", "William",
              "David", "Richard", "Joseph", "Thomas", "Charles"]
# the most common last names
lastNames = ["Smith", "Johnson", "Williams", "Brown",
             "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Wilson"]
people = []
class Person(Document):
    firstName = Keyword()
    lastName = Keyword()
    height = Long ()
    weight = Float()
    BMI = Float()
    class Index:
        name = "aggregationtest"

Person.init()

for x in range(100):
    #based on average height
    height = random.randint(58, 80)
    #tracks obesity
    BMI = random.uniform(16, 41)
    #weight proportional to height calculated using the BMI formula
    weight = (BMI*height*height)/703
    person = Person(firstName= firstNames[random.randint(0, 9)], lastName= lastNames[random.randint(0, 9)], height= height, BMI= round(BMI, 2), weight= round(weight,2))
    #person.save()
    people.append(person)

client = Elasticsearch()

index = Index("aggregationtest")
s = index.search(using=client).query(
    "match", firstName="Richard")

s.aggs.bucket("names", "terms", field="lastName")

response = s.execute()

for hit in response:
    print(hit.meta.score, hit.firstName)

for name in response.aggregations.names.buckets:
    print(name.key, name.doc_count)

person = {"firstName": firstNames[random.randint(
    0, 9)], "lastName": lastNames[random.randint(0, 9)], "height": height, "BMI": round(BMI, 2), "weight": round(weight, 2)}
client.index(index="aggregrationtest", body=json.dumps(person))
index = Index("aggregationtest")
s = index.search(using=client)
response = s.execute()
for hit in response:
    print(hit.meta.score, hit.firstName)
