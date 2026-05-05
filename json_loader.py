'''
Cinthya Calderon-Hernandez
CSMC 111
JSON Loader
'''

#Used ChatGPT for this code
# json_loader.py

import json

# Ask user for file name (like your example)
filename = input("Enter the JSON file name: ")

try:
    # Try to open and load the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)

        # Required success message (must match assignment exactly)
        print("JSON loaded successfully.")

        # Optional: show content (similar to your example)
        print("Content:")
        print(data)

except FileNotFoundError:
    # Match assignment requirement exactly
    print("File not found!")

except json.JSONDecodeError:
    # Match assignment requirement exactly
    print("Invalid JSON format!")

except Exception as e:
    # Extra safety (your example includes this)
    print("An unexpected error occurred.")
    print(f"Details: {e}")