import requests
import time
import os

ELASTIC_URL = "http://elasticsearch:9200"
# Define the two index names
INDEX_NAMES = ["kpi_pdc_job", "network_data_15min"]

# Get credentials from environment variables
ELASTIC_USERNAME = os.getenv("ELASTIC_USERNAME", "elastic")
ELASTIC_PASSWORD = os.getenv("ELASTIC_PASSWORD", "elasticelastic123")

# Define mapping
mapping = {
    "mappings": {
        "properties": {
            "location": {"type": "geo_point"},
            "Date": {"type": "date"}
        }
    }
}

def wait_for_elasticsearch():
    while True:
        try:
            r = requests.get(
                ELASTIC_URL,
                auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD),
                timeout=10
            )
            if r.status_code == 200:
                print("Elasticsearch is up!")
                break
        except Exception as e:
            print(f"Connection error: {e}")
        print("Waiting for Elasticsearch...")
        time.sleep(5)

def create_index_if_not_exists(index_name):
    try:
        res = requests.head(
            f"{ELASTIC_URL}/{index_name}",
            auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
        )
        
        if res.status_code == 404:
            print(f"Index '{index_name}' does not exist. Creating...")
            r = requests.put(
                f"{ELASTIC_URL}/{index_name}",
                json=mapping,
                auth=(ELASTIC_USERNAME, ELASTIC_PASSWORD)
            )
            if r.status_code in [200, 201]:
                print(f"Index '{index_name}' created successfully!")
                print("Response:", r.json())
            else:
                print(f"Error creating index '{index_name}': {r.status_code} - {r.text}")
        elif res.status_code == 200:
            print(f"Index '{index_name}' already exists. Skipping creation.")
        else:
            print(f"Unexpected response when checking index '{index_name}': {res.status_code}")
            
    except Exception as e:
        print(f"Error in create_index_if_not_exists for '{index_name}': {e}")

if __name__ == "__main__":
    wait_for_elasticsearch()
    
    # Create both indexes
    for index_name in INDEX_NAMES:
        create_index_if_not_exists(index_name)