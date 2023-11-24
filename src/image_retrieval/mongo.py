from os import environ, getenv

from pymongo import MongoClient
from pymongo.collection import Collection

ENV_VAR_INTERNAL_MONGO_CONNECTION_URL = "INTERNAL_MONGO_CONNECTION_URL"
ENV_VAR_MONGO_TECHNICAL_USERNAME = "MONGO_TECHNICAL_USER_USERNAME"
ENV_VAR_MONGO_TECHNICAL_PASSWORD = "MONGO_TECHNICAL_USER_PASSWORD"
ENV_VAR_MONGO_HOST = "MONGO_HOST"
ENV_VAR_MONGO_PORT = "MONGO_PORT"
ENV_VAR_MONGO_DB = "MONGO_DB"
ENV_VAR_MONGO_COLLECTION = "MONGO_COLLECTION"
ENV_VAR_MONGO_AUTH_SOURCE = "MONGO_AUTH_SOURCE"
KEY_DEFAULT_COLLECTION_NAME = "content"
KEY_DEFAULT_DB_NAME = "mongo_local"
KEY_METADATA_CREATED = "metadata:created"
KEY_METADATA_UPDATED = "metadata:updated"
UNEXPOSED_KEYS = ["_id"]


def new_mongo_client(connection_url: str = None) -> MongoClient:
    if connection_url:
        print(f"new_mongo_client::connection_url: {connection_url}")
        return MongoClient(connection_url)
    if ENV_VAR_INTERNAL_MONGO_CONNECTION_URL in environ:
        print(
            f"new_mongo_client::{ENV_VAR_INTERNAL_MONGO_CONNECTION_URL}:"
            f"{environ.get(ENV_VAR_INTERNAL_MONGO_CONNECTION_URL)}"
        )
        return MongoClient(environ.get(ENV_VAR_INTERNAL_MONGO_CONNECTION_URL))
    username = getenv(ENV_VAR_MONGO_TECHNICAL_USERNAME, "admin")
    password = getenv(ENV_VAR_MONGO_TECHNICAL_PASSWORD, "admin")
    host = getenv(ENV_VAR_MONGO_HOST, "localhost")
    port = getenv(ENV_VAR_MONGO_PORT, "27017")
    auth_source = getenv(ENV_VAR_MONGO_AUTH_SOURCE, "admin")
    uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource={auth_source}"
    print(f"new_mongo_client::uri: {uri}")
    return MongoClient(uri)


def get_collection(client: MongoClient, collection_name: str) -> Collection:
    return client["mongo_local"][collection_name]
