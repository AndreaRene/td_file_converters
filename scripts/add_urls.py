import json
import os

# Define the base URL for the images
base_url = "https://your-bucket-name.s3.your-region.amazonaws.com/"

# Define the directory containing the JSON files
directory = os.path.join(os.path.dirname(__file__), '../data/urls/')

# Function to process each JSON file
def process_json_file(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Iterate through each card and construct the image URL
    for card in data:
        # Ensure the number is two digits
        number_str = f"{card['number']:02}"
        # Construct the image URL
        image_url = f"{base_url}{card['objectCode']}/{card['suit'].lower()}/{card['objectCode'].lower()}_{card['suit'].lower()}_{number_str}.jpg"
        # Add the URL to the card object
        card['imageUrl'] = image_url

    # Save the updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

# Loop through each file in the directory
for filename in os.listdir(directory):
    if filename.endswith('.json'):
        file_path = os.path.join(directory, filename)
        process_json_file(file_path)
        print(f"Processed {file_path}")

print("URLs added to all JSON objects successfully.")
