import os
import json

def create_index_files(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all directories in the input directory
    for directory_name in os.listdir(input_dir):
        dir_path = os.path.join(input_dir, directory_name)
        if os.path.isdir(dir_path):
            index_file_name = f"{directory_name[:4]}_index.json"
            index_file_path = os.path.join(output_dir, index_file_name)
            index_data = []

            # Loop through all JSON files in the current directory
            for file_name in os.listdir(dir_path):
                if file_name.endswith('.json'):
                    file_path = os.path.join(dir_path, file_name)
                    
                    # Read the JSON file
                    with open(file_path, 'r') as f:
                        data = json.load(f)
                    
                    # Extract the necessary fields
                    index_entry = {
                        'id': data.get('id')
                    }
                    for key, value in data.items():
                        if 'name' in key.lower() or 'url' in key.lower():
                            index_entry[key] = value
                    
                    index_data.append(index_entry)
            
            # Write the index data to the output file, replacing it if it exists
            with open(index_file_path, 'w') as out_f:
                json.dump(index_data, out_f, indent=4)
            
            print(f"Created index file: {index_file_name}")

# Define input and output directories
input_directory = '../data/create_index'
output_directory = '../output'

# Call the function to create index files
create_index_files(input_directory, output_directory)
