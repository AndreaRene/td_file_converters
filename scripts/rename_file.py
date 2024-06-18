import os
import re

# Define the base directory where the files were renamed
base_directory = '/your/file/path/here'  # Replace with your absolute path

def rename_files(base_dir):
    base_dir = os.path.abspath(base_dir)  # Ensure it's an absolute path
    print(f"Starting in base directory: {base_dir}")

    # Define the regex pattern for the naming convention
    naming_pattern = re.compile(r'^[a-z_]+_\d{2}\.\w+$')

    for root, dirs, files in os.walk(base_dir):
        for filename in files:
            old_file_path = os.path.join(root, filename)
            file_base, original_extension = os.path.splitext(filename)

            # Check if the current filename matches the naming convention
            if naming_pattern.match(filename):
                print(f"Skipping {filename} (already matches naming convention)")
                continue

            # Extract the numeric values from the filename with leading zeros
            match = re.findall(r'\d+', file_base)
            if match:
                number = match[0]  # Use the first numeric value found
            else:
                number = ''  # If no numeric value found, leave it empty

            # Construct the new filename prefix
            relative_path = os.path.relpath(root, base_dir)
            relative_path_parts = relative_path.split(os.sep)
            new_file_base = f"{'_'.join(relative_path_parts).lower()}"
            if number:
                new_file_base += f"_{number.zfill(2)}"
            else:
                new_file_base += "_00"

            new_file_path = os.path.join(root, new_file_base + original_extension)

            # Check if the new file path already exists and handle conflicts
            if os.path.exists(new_file_path):
                counter = 1
                while os.path.exists(os.path.join(root, f"{new_file_base}_{counter}{original_extension}")):
                    counter += 1
                new_file_path = os.path.join(root, f"{new_file_base}_{counter}{original_extension}")

            # Rename the file and log the operation
            print(f"Renaming {old_file_path} to {new_file_path}")
            os.rename(old_file_path, new_file_path)

if __name__ == "__main__":
    rename_files(base_directory)