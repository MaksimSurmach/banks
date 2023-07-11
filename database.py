from datetime import datetime, timezone, timedelta
import pymongo
import os


class Database:
    def __get_env(self):
        self.__DB_USER = os.getenv('DB_USER')
        self.__DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.__DB_URL = os.getenv('DB_URL')

    def __init__(self):
        self.__get_env()
        self.db_name = os.getenv('db_name')
        self.collection_name = os.getenv('collection_name')

        # Send a ping to confirm a successful connection
        try:
            self.client = pymongo.MongoClient(
                f"mongodb+srv://{self.__DB_USER}:{self.__DB_PASSWORD}@{self.__DB_URL}/?retryWrites=true&w=majority")
            self.db = self.client[self.db_name]
            self.collection = self.db[self.collection_name]
            # self.client.admin.command('ping')
            # print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def close(self):
        self.client.close()

    def get_random_joke(self):
        joke = self.collection.aggregate([{"$sample": {"size": 1}}])
        for i in joke:
            return i
