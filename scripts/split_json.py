import os
import json
import shutil

def split_json_objects(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Loop through all files in the input directory
    for file_name in os.listdir(input_dir):
        if file_name.endswith('.json'):
            input_file_path = os.path.join(input_dir, file_name)
            
            # Read the JSON file
            with open(input_file_path, 'r') as f:
                data = json.load(f)
            
            # Create a subdirectory in the output directory named after the file name
            sub_dir_name = os.path.splitext(file_name)[0]
            sub_dir_path = os.path.join(output_dir, sub_dir_name)

            # Delete the subdirectory if it exists
            if os.path.exists(sub_dir_path):
                shutil.rmtree(sub_dir_path)

            # Create the subdirectory
            os.makedirs(sub_dir_path, exist_ok=True)
            
            # Loop through each object in the JSON data
            for obj in data:
                obj_id = obj.get('id')
                if not obj_id:
                    print(f"Object in file {file_name} does not have an 'id' field. Skipping.")
                    continue
                
                # Create a new file for each object
                output_file_path = os.path.join(sub_dir_path, f"{obj_id}.json")
                with open(output_file_path, 'w') as out_f:
                    json.dump(obj, out_f, indent=4)
            
            print(f"Processed file: {file_name}")

# Define input and output directories
input_directory = '../data/split_objects'
output_directory = '../output'

# Call the function to split JSON objects
split_json_objects(input_directory, output_directory)
