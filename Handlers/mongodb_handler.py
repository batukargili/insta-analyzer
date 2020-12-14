from datetime import datetime

from Models.mongodb_connection import MongoConnection
from pymongo import MongoClient

from Utils.log import init_logger

logger = init_logger(__name__, testing_mode=False)

def get_mongodb_client():
    mongo_connection = MongoConnection()
    mongo_connection.settings = "Config/config.ini"
    mongo_connection.port = "MongoDb"
    mongo_connection.host = "MongoDb"

    client = MongoClient(mongo_connection.host, int(mongo_connection.port))
    return client


def create_connection():

    client = get_mongodb_client()
    if client:
        try:
            db = client["insta"]
            col = db["followers_following"]
            return col
        except MongoConnection:
            logger.error("Can't connect to MongoDb, please check your connection")
            return None


def insert_value(post):
    col = create_connection()
    col.insert_one(post)

