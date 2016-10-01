from pymongo import MongoClient
from config import DefaultConfig

client = MongoClient(DefaultConfig.MONGO_DB_URL)
db = client.genecard
