from azure.storage.blob import BlobServiceClient
from dotenv import load_dotenv
import os

load_dotenv()

def get_data(type):
    client = BlobServiceClient.from_connection_string(os.environ.get('connect_str'))
    container_client = client.get_container_client(os.environ.get('container_name'))
    blob_name = os.environ.get(type)
    blob_client = container_client.get_blob_client(blob_name)
    
    if not os.path.isdir('json'):
        os.makedirs('json')
        
    with open(f'json/{type}.json', 'wb') as f:
        download_stream = blob_client.download_blob()
        f.write(download_stream.readall())