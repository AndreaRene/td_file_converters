import json
import os

# Base URL for S3 bucket
BASE_URL = "https://tarotdeck-metadata.s3.us-east-2.amazonaws.com/"

def update_index_file(index_file_path, output_file_path, directory_prefix):
    with open(index_file_path, 'r') as file:
        index_data = json.load(file)

    for obj in index_data:
        obj_id = obj.get('id')
        if obj_id:
            # Construct the object file URL based on directory structure
            obj['objectFileUrl'] = f"{BASE_URL}{directory_prefix}/{obj_id}.json"

    with open(output_file_path, 'w') as file:
        json.dump(index_data, file, indent=4)

    print(f"Processed {index_file_path} successfully.")

# Path to the script directory (current working directory)
scripts_directory = os.path.dirname(os.path.abspath(__file__))

# Path to the root directory (one level up from the script directory)
root_directory = os.path.abspath(os.path.join(scripts_directory, '..'))

# Path to the data directory
data_directory = os.path.join(root_directory, 'data')

# Path to the directory containing index files
input_directory = os.path.join(data_directory, 'add_object_url')

# Path to the output directory
output_directory = os.path.join(root_directory, 'output')

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Ensure the input directory exists
if not os.path.exists(input_directory):
    print(f"Error: The directory {input_directory} does not exist.")
    exit(1)

# Loop through all files in the input directory
for filename in os.listdir(input_directory):
    # Check if the file is a JSON file and ends with '_index.json'
    if filename.endswith('_index.json'):
        print(f"Starting processing of {filename}...")
        # Extract prefix from filename (e.g., 'AVAT' from 'AVAT_index.json')
        directory_prefix = filename.split('_')[0] + "Objects"
        # Define input and output file paths
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename)
        # Update the index file with the dynamically determined directory
        update_index_file(input_file_path, output_file_path, directory_prefix)

print("All files processed successfully.")
