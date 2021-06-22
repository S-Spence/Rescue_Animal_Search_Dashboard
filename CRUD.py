from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter():
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, user_name, password):
        """Initializing the MongoClient"""
        self.client = MongoClient('mongodb://%s:%s@localhost:44598/AAC'
                % (user_name, password))
        self.database = self.client['AAC']

    def create(self, data: dict) -> bool:
        """A method to create documents in MongoDB AAC database"""
        if data:
            # Check if the animal_id is unique (Separate variable from ObjectID)
            if "animal_id" in data.keys():
                check = list(self.database.animals.find(data))
                if check:
                    raise Exception("The animal ID is already in use.")

            # Insert a document into the database
            if self.database.animals.insert_one(data):
                return True
            else:
                return False
        else:
            raise Exception("Nothing to save. The data parameter is empty.")

    def read(self, data: dict) -> list:
        """A method to read documents in the MongoDB AAC database"""
        if data:
            result = list(self.database.animals.find(data,{"_id":False}))
            # Check if the query returned results
            if len(result) > 0:
                return result
            else:
                raise Exception("The document is not in the database.")
        else:
             raise Exception("Nothing to find. The data parameter is empty.")
                
    def read_all(self, data: dict) -> object:
        """A method to read all documents into the user dashboard and return a cursor"""
        result = self.database.animals.find(data, {"_id":False})
        return result
            
    def filtered_rescue_dogs(self, rescue_type: str) -> object:
        """A method to filter read results and return a cursor"""
        if rescue_type == "Water":
            water_query = {"animal_type":"Dog",
                           "breed":{"$in":["Labrador Retriever Mix","Chesapeake Bay Retriever","Newfoundland"]}, 
                           "sex_upon_outcome":"Intact Female",
                           "age_upon_outcome_in_weeks":{"$gte":26, "$lte":156}}
            result = self.database.animals.find(water_query, {"_id":False})
        elif rescue_type == "Mountain":
            mountain_query = {"animal_type":"Dog",
                              "breed":{"$in":["German Shephard","Alaskan Malamute","Old English Sheepdog",
                                       "Siberian Husky", "Rottweiler"]}, 
                              "sex_upon_outcome":"Intact Male",
                              "age_upon_outcome_in_weeks":{"$gte":26, "$lte":156}}
            result = self.database.animals.find(mountain_query, {"_id":False})
        elif rescue_type == "Disaster":
            disaster_query = {"animal_type":"Dog",
                              "breed":{"$in":["Doberman Pinscher", "German Shephard","Golden Retriever","Bloodhound",
                                       "Rottweiler"]}, 
                              "sex_upon_outcome":"Intact Male",
                              "age_upon_outcome_in_weeks":{"$gte":20, "$lte":300}}
            result = self.database.animals.find(disaster_query, {"_id":False})
        else:
            raise Exception("Please enter a valid rescue type: Water, Mountain, or Disaster")
        return result
           
    def update(self, search_data: dict, update_data: dict) -> object:
        """A method to update documents in MongoDB AAC database"""
        update_data = {"$set":update_data}
        # Confirm that search and update data were provided
        if search_data and update_data:
            check = list(self.database.animals.find(search_data))
            # Check if the search data is in the database
            if check:
                result = self.database.animals.update_many(search_data, update_data)
            else:
                raise Exception("There are no documents matching the search criteria.")
        else:
            raise Exception("You must provide data to search for and update.")
        return result

    def delete(self, data: dict) -> object:
        """A method to delete documents in the MongoDB AAC database"""
        if data:
            check = list(self.database.animals.find(data))
            # Check if the query returned results
            if check:
                result = self.database.animals.delete_many(data)
            else:
                raise Exception("The data is not in the database.")
        else:
            raise Exception("Nothing to delete. The data parameter is empty.")
        return result
