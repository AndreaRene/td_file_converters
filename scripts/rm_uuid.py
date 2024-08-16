import os
import json

# Define directories
input_dir = os.path.join(os.path.dirname(__file__), '../data/rm_uuid')
output_dir = os.path.join(os.path.dirname(__file__), '../output/rm_uuid')

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to process each JSON file
def process_file(file_path, output_file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Remove the 'id' field from each item in the list
    updated_data = [{k: v for k, v in item.items() if k != 'id'} for item in data]

    # Write the updated data to the output file
    with open(output_file_path, 'w') as file:
        json.dump(updated_data, file, indent=4)

# Loop through each file in the input directory
for filename in os.listdir(input_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(input_dir, filename)
        output_file_path = os.path.join(output_dir, filename)

        process_file(file_path, output_file_path)
        print(f"Processed {filename}")

print("All files processed successfully.")
