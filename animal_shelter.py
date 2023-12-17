from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, user, passwd):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        user = 'aacuser'
        passwd = 'SNHU1234'
        host = 'nv-desktop-services.apporto.com'
        port = 30182
        database = 'AAC'
        collection = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (user,passwd,host,port))
        self.database = self.client['%s' % (database)]
        self.collection = self.database['%s' % (collection)]

# Complete this create method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
   
                self.database.animals.insert_one(data) # data should be dictionary
                return True
    
        else:
            raise Exception("Nothing to save, because data parameter is empty")#exception will display if the data was not created                                                                                #correctly
            return False
                 

    # Create method to implement the R in CRUD.
    def read(self,query):
     
        try: 
            result = self.database.animals.find(query) #assinging the result value
            return result #returning result for the read method
        
        except Exception as E:
            print (E) #this exception will rise if there is no data to return/read
            return []
        
    #Update method to implement the U in CRUD
    def update(self, query, data):
        try:
            result = self.database.animals.update_one(query,data)
            if result.modified_count > 0:
                return result #will return result if the data is greater than 0
                print ("Success!")
                print (result)
                return true
        except Exception as E:
                print (E) #this exception will raise if there is no data to delete
                return False
            
    #Delete method to implement the D in CRUD
    def delete(self, data):
            if data is not None: #if the data is present
                deleteResult = self.database.animals.delete_one(data)
                if result.deleted_count > 0: #if data to delete is more than one
                    return deleteResult #return result
                    return True
                else:
                    return False #if the data to delete is absent, return false
            else:
                raise Exception("no data to delete!!!!") #if no data is present to delete, this exception is thrown
                return false #method returns false

            
            
            
            
            