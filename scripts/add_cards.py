import json
import os

# Define the directory path containing both deck and card files
files_path = '../data/card_arrays/'

# Initialize variables to store the deck data and card IDs
deck_data = None
deck_card_ids = {}

# Load the deck file and card files
for filename in os.listdir(files_path):
    if filename.startswith('DECK') and filename.endswith('.json'):
        # Load the deck file
        with open(os.path.join(files_path, filename), 'r') as file:
            deck_data = json.load(file)
    elif filename.endswith('.json') and not filename.startswith('DECK'):
        # Load card files
        with open(os.path.join(files_path, filename), 'r') as file:
            cards = json.load(file)
            for card in cards:  # Iterate through the list of card objects
                deck_id = card['objectCode']
                card_id = card['id']  # Use the 'id' field instead of 'cardId'
                
                if deck_id not in deck_card_ids:
                    deck_card_ids[deck_id] = []
                deck_card_ids[deck_id].append(card_id)

# Update the deck data with card IDs
for deck in deck_data:
    if deck['deckId'] in deck_card_ids:
        # Replace the cardIds with the new list
        deck['cardIds'] = deck_card_ids[deck['deckId']]
    else:
        # Ensure cardIds is reset if there are no cards for the deck
        deck['cardIds'] = []

# Save the updated deck file
deck_filename = [f for f in os.listdir(files_path) if f.startswith('DECK') and f.endswith('.json')][0]
with open(os.path.join(files_path, deck_filename), 'w') as file:
    json.dump(deck_data, file, indent=4)

print("Deck file updated with card IDs successfully.")
