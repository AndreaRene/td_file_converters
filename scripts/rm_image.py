import json
import os

# Define the input and output directory paths
input_dir = os.path.join(os.path.dirname(__file__), '../data/rm_img_file')
output_dir = os.path.join(os.path.dirname(__file__), '../output/rm_img_file')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Iterate over all JSON files in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        input_file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)
        
        # Load the JSON file
        with open(input_file_path, 'r') as file:
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
        
        # Save the updated JSON to the output file
        with open(output_file_path, 'w') as file:
            json.dump(data, file, indent=4)

print("All files updated successfully.")
