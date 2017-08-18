from pymongo import MongoClient
from datetime import datetime

class MongoDbManager:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)

    def connect(self, mongoUri):
        self.client = MongoClient(mongoUri)

    def getDatabase(self, database):
        db = self.client[database]
        return db

    def getCollection(self, database, collection):
        db = self.getDatabase(database)
        return db[collection]

    def addPost(self, post):
        collection = self.getCollection('test', 'posts')

        post_id = collection.insert_one(post).inserted_id

        post['id'] = str(post_id)

        return post

    def getAllPosts(self):
        collection = self.getCollection('test', 'posts')

        return collection.find()


if __name__ == "__main__":
    mdm = MongoDbManager()

    db = mdm.getDatabase('db')

    collection = mdm.getCollection('db', 'test')
    
    # print(db)
    print(collection)

    # add post
    post = {
        "author": "Garrett Wong",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.utcnow()
    }
    post = mdm.addPost(post)
    print(post)

    # get posts
    postsCursor = mdm.getAllPosts()
    posts = list(postsCursor)
    print(len(posts))