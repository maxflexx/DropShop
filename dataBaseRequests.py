from pymongo import MongoClient
import constants
import app
def insertNewUser(username, who, id):
    conn = None
    try:
        conn = MongoClient(constants.dataBaseUri)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
        return

    db = conn.dropshop
    collection = None
    userToInsert = None
    if(who=='provider'):
        collection = db.providers
    else:
        collection = db.sellers
    userToInsert = {
        "username": username,
        "who": who,
        "chatID": id
    }
    try:
        record = collection.insert_one(userToInsert)
    except:
        print('Error on inserting')

def echoToProviders(photo, caption):
    conn = None
    try:
        conn = MongoClient(constants.dataBaseUri)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
        return
    db = conn.dropshop
    collection = db.providers
    for post in collection.find({}):
        app.bot.send_photo(post['chatID'],photo,caption)


def whoIsUser(id):
    conn = None
    try:
        conn = MongoClient(constants.dataBaseUri)
        print("Connected successfully!!!")
    except:
        print("Could not connect to MongoDB")
        return
    db = conn.dropshop
    collection = db.providers
    for post in collection.find({"chatID":id}):
        print("provider")
        return "provider"
    collection = db.sellers
    for post in collection.find({"chatID": id}):
        print("seller")
        return "seller"
    return None


