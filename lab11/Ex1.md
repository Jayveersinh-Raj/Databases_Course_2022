    from pymongo import MongoClient
    from pprint import pprint 

    client = MongoClient("mongodb://localhost")
    db = client['lab11']

    def query():
     cursor = db.Ex1.find({"cuisine": "Indian"}) 
     cursor2=db.Ex1.find({"cuisine": "Thai"})


    for record in cursor:
       pprint(record)

    for record in cursor2:
       pprint(record)


    def address():
        cursor = db.Ex1.find({"address": "1115 Rogers Avenue, 1122"}) 
 


    for record in cursor:
       pprint(record)



    #Insert
    def insert():
        cursor = db.Ex1.insert_one({"Address": "1480 2 Avenue, 10075, -73.9557413, 40.7720266", "Borough": "Manhattan", "Cuisine": "Italian", "Name": "Vella", "Id": 41704620,
        "Grades":"A, 11, 01 Oct, 2014" })



    #Delete
    def delete():
       cursor = db.Ex1.delete_one({"Borough":"Manhattan"})
       cursor2 = db.Ex1.delete_many({"cuisine": "Thai"})


    #Roger Avenue
    def rogerAvenue():
        count = 0
        array=[]
        cursor = db.Ex1.find({"address": "1115 Rogers Avenue, 1122"}) 
        for record in range(6):
            array = record["Grades"]
            for i in range(array.length):
                if array[i] == 'C':
                count=count+1
                    if(count>1):
                      cursor2 = db.Ex1.delete_one(range)
                      print("record deleted")

            if(count<2):
                cursor = db.Ex1.update_one({'$set':{"Grades":"C"}})

     #query()
     rogerAvenue()
