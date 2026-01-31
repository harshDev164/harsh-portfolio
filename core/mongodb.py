from pymongo import MongoClient
from django.conf import settings


def get_db():
    uri = settings.MONGO_URI

    # HARD FAIL if wrong (debug safety)
    if not uri or not uri.startswith("mongodb"):
        raise Exception(f"Invalid Mongo URI detected: {repr(uri)}")

    client = MongoClient(
        uri.strip(),   # 🔥 IMPORTANT
        serverSelectionTimeoutMS=3000,
        connectTimeoutMS=3000,
    )

    return client[settings.MONGO_DB_NAME]
