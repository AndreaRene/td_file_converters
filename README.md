# File converters for TarotDeck

This repository houses file converters for the TarotDeck project.

## UUID Script

The UUID script is a tool for adding unique identifiers (UUIDs) to objects within JSON files. It ensures that each object has a unique identifier without modifying existing identifiers. The UUID script reads JSON files from a specified directory and adds UUIDs to objects that do not already have an "id" field. It leaves existing "id" fields unchanged.

### Usage

To use the UUID script, follow these steps:

1. Ensure Python 3 is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. Place the `add_uuid.py` script in a directory named `scripts`.
3. Create a directory named `data` in the root of your project.
4. Place the JSON files that you want to process in the `data` directory.
5. Open a terminal or command prompt.
6. Navigate to the `scripts` directory in your project.
7. Run the script with the following command:

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
