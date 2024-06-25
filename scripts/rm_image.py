import json
import os

# Define the directory path containing the JSON files
files_path = '../data/rm_img_file/'

# Iterate over all JSON files in the directory
for filename in os.listdir(files_path):
    if filename.endswith('.json'):
        file_path = os.path.join(files_path, filename)
        
        # Load the JSON file
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        # Check if data is a list or a single dictionary
        if isinstance(data, list):
            # Remove the 'imageFileName' field from each dictionary in the list
            for item in data:
                if 'imageFileName' in item:
                    del item['imageFileName']
        elif isinstance(data, dict):
            # Remove the 'imageFileName' field from the single dictionary
            if 'imageFileName' in data:
                del data['imageFileName']
        
        # Save the updated JSON back to the file
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)

print("All files updated successfully.")
