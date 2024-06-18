# File converters for TarotDeck

This repository houses file converters for the TarotDeck project.

## UUID Script

The UUID script is a tool for adding unique identifiers (UUIDs) to objects within JSON files. It ensures that each object has a unique identifier without modifying existing identifiers. The UUID script reads JSON files from a specified directory and adds UUIDs to objects that do not already have an "id" field. It leaves existing "id" fields unchanged.

### Usage

To use the UUID script, follow these steps:

1. Ensure Python 3 is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone the repository.
3. Add the JSON files (that need UUIDs added to objects) to the `uuids` directory.
4. Open a terminal or command prompt.
5. Navigate to the `scripts` directory in your project.
6. Run the script with the following command:

```bash
python3 add_uuid.py
```
### Example

Suppose we have a JSON file named `data.json` with the following contents:

```json
[{ "name": "Object 1" }, { "name": "Object 2", "id": "existing-id" }]
```

Running the UUID script will result in the following changes to `data.json`:

```json
[
  { "name": "Object 1", "id": "newly-generated-uuid" },
  { "name": "Object 2", "id": "existing-id" }
]
```

## Object Code Script

The Object Code script is a tool for adding object code identifiers to objects within JSON files. It ensures that each object has an object code. The Object Code script reads JSON files from a specified directory and adds the field to objects that do not already have an "objectCode" field. It reads objects that do have an "objectCode" field and ensures that the value is correct. If it is not, it will change the object code appropriately. The script assumes a naming convention of `filePrefixObjects.json`. It will take the file prefix and place it into an object code field, converting it to lowercase.

### Usage

To use the Object Code script, follow these steps:

1. Ensure Python 3 is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone the repository.
3. Add the JSON files (that need object codes added to objects) to the `object_codes` directory.
4. Open a terminal or command prompt.
5. Navigate to the `scripts` directory in your project.
6. Run the script with the following command:

```bash
python3 add_object_code.py
```

### Example

Suppose we have a JSON file named `dataObjects.json` with the following contents:

```json
[
  { "name": "Object 1" },
  { "name": "Object 2", "objectCode": "random-object-code" },
  { "name": "Object 3", "objectCode": "data" }
]
```

Running the Object Code script will result in the following changes to `dataObjects.json`:

```json
[
  { "name": "Object 1", "objectCode": "data" },
  { "name": "Object 2", "objectCode": "data" },
  { "name": "Object 3", "objectCode": "data" }
]
```

## Rename File Script

The Rename File script is a tool for renaming files in a specified directory according to a specific pattern. It ensures that filenames are changed based on their directory structure and numeric values within the filename, while preserving the original file extensions. If a filename already matches the desired pattern, it will be skipped.

### Usage

To use the Rename File script, follow these steps:

1. Ensure Python 3 is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Clone the repository.
3. Update the `base_directory` variable in the script to the path where your files are located. A `renaming` directory has been added for convenience if you want to organize the files you wish to rename into a specific directory before running the script.
4. Open a terminal or command prompt.
5. Navigate to the `scripts` directory in your project.
6. Run the script with the following command:

```bash
python3 rename_file.py
```

### Example

Suppose we have files in a directory structure as follows:

```
tarot_cards/
  ├── EOTS/
  │   ├── keys/
  │   │   ├── 01_Offering_of_the_Damned.png
  │   │   ├── 02_Another_File.png
  │   └── cups/
  │       ├── cups01.png
  │       ├── cups02.png
  └── cardbacks/
      ├── 01cardback.png
      ├── 02cardback.png
```

Running the Rename File script will result in the following changes:

```
tarot_cards/
  ├── EOTS/
  │   ├── keys/
  │   │   ├── eots_keys_01.png
  │   │   ├── eots_keys_02.png
  │   └── cups/
  │       ├── eots_cups_01.png
  │       ├── eots_cups_02.png
  └── cardbacks/
      ├── tarot_cards_cardbacks_01.png
      ├── tarot_cards_cardbacks_02.png
```


