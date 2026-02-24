from pymongo import MongoClient
import gridfs
import os


class GridFSStorage:

    def __init__(self):
        self.fs = None
        self.get_connection()

    def get_connection(self):
        mongo_uri = os.getenv("MONGO_URI","mongodb://localhost:27017")
        client = MongoClient(mongo_uri)
        db = client["image_db"]
        self.fs = gridfs.GridFS(db)
   

    def gridfs_storage(self,file) -> bool:
        try:
            self.fs.put(file)
            return True
        except Exception as error:
            print("Failed to store file:", error)
            return False
            