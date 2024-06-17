import os
import json

def add_object_code_to_json_objects(root_dir):
    data_dir = os.path.join(root_dir, 'data', 'object_codes')
    total_updated = 0
    
    for root, dirs, files in os.walk(data_dir):
        for filename in files:
            if filename.endswith('.json'):
                file_path = os.path.join(root, filename)
                object_code = extract_object_code(filename)
                updated_count = update_json_objects(file_path, object_code)
                total_updated += updated_count
    
    print(f"Total 'objectCode' fields updated or added: {total_updated}")

def extract_object_code(filename):
    # Extract the value from the filename before 'Objects' in lowercase
    parts = filename.split('Objects', 1)
    if len(parts) > 1:
        object_code = parts[0].lower()
        return object_code
    return None

def update_json_objects(file_path, object_code):
    updated_count = 0
    
    with open(file_path, 'r+') as file:
        data = json.load(file)
        for item in data:
            if 'objectCode' not in item or item['objectCode'] != object_code:
                item['objectCode'] = object_code
                updated_count += 1
        
        file.seek(0)
        json.dump(data, file, indent=2)
        file.truncate()

    print(f"Object Codes added to {updated_count} objects in {file_path}")
    return updated_count

if __name__ == "__main__":
    # Get the current directory of the script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Navigate up to the root directory
    root_directory = os.path.abspath(os.path.join(script_dir, '..'))
    
    # Call the function to add 'objectCode' field to JSON objects
    add_object_code_to_json_objects(root_directory)
