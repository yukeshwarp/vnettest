# Cosmos DB utility functions for CRUD operations
import os
from azure.cosmos import CosmosClient, PartitionKey
from dotenv import load_dotenv
load_dotenv()

COSMOS_ENDPOINT = os.getenv('COSMOS_ENDPOINT', 'https://your-cosmos-account.documents.azure.com:443/')
COSMOS_KEY = os.getenv('COSMOS_KEY', 'your-cosmos-key')
DATABASE_NAME = os.getenv('COSMOS_DATABASE', 'sampledb')
CONTAINER_NAME = os.getenv('COSMOS_CONTAINER', 'items')

client = CosmosClient(COSMOS_ENDPOINT, COSMOS_KEY)
database = client.create_database_if_not_exists(id=DATABASE_NAME)
container = database.create_container_if_not_exists(
    id=CONTAINER_NAME,
    partition_key=PartitionKey(path="/id"),
    offer_throughput=400
)

def create_item(item: dict):
    return container.create_item(body=item)

def read_items():
    return list(container.read_all_items())

def update_item(item_id: str, new_data: dict):
    item = container.read_item(item=item_id, partition_key=item_id)
    item.update(new_data)
    return container.replace_item(item=item_id, body=item)

def delete_item(item_id: str):
    return container.delete_item(item=item_id, partition_key=item_id)
