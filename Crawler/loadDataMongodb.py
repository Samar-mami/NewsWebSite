"""#Connect to MongoDB"""
from pymongo import MongoClient
from Crawler.config import username,password,database,collection

# Connect to MongoDB client and database/collection
def connect_mongo_db_collection(username, password, database, collection):
    uri = "mongodb+srv://" + username + ":" + password + "@cluster0.38i5zz9.mongodb.net/?retryWrites=true&w=majority"
    try:
        client = MongoClient(uri)
        db = client[database]
        collection = db[collection]
        collection_stats = collection.stats
        # print(collection_stats)
        print("Connection to MongoDB collection successful :)\n")
    except Exception as e:
        print("Connection to MongoDB collection failed:", str(e))
    return collection


# Insert the dataframe tp mongodb
def store_data(df):
    if 'index' not in df.columns:
        df.reset_index(inplace=True)
    data_dict = df.to_dict("records")
    # connect to database
    collection = connect_mongo_db_collection(username, password, database, collection)
    # Insert collection
    collection.delete_many({})
    print("files deleted")
    try:
        # Delete existing documents from the collection
        collection.insert_many(data_dict)
        print("Data inserted/replaced successfully in MongoDB collection")
    except Exception as e:
        print("Error occurred:", str(e))
