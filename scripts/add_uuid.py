import json
import os
import uuid

def add_unique_ids_to_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    ids_added = 0

    for item in data:
        if 'id' not in item:
            item['id'] = str(uuid.uuid4())
            ids_added += 1

    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

    print(f"Unique IDs added to {ids_added} objects in {file_path}")

def process_directory(directory_path):
    uuid_dir = os.path.join(directory_path, 'uuids')  # New directory path
    
    for filename in os.listdir(uuid_dir):
        file_path = os.path.join(uuid_dir, filename)
        if filename.endswith('.json'):
            add_unique_ids_to_file(file_path)

if __name__ == "__main__":
    # Get the directory path of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Set the data directory path
    data_dir = os.path.join(script_dir, '..', 'data')
    
    # Process the new data/uuid directory
    process_directory(data_dir)
