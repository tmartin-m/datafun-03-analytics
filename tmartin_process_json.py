"""
Process a JSON file to count houeses by furnishingstatus and save the result.

JSON file is in the format where houses is a list of dictionaries with keys "price", "area", "bedrooms", "bathrooms", "stories", "mainraod", "guestroom", "basement", "hotwaterheating", "airconditioning", "parking", "prefarea", and "furnishingstatus".

{
    "houses": [
        {
            "price": "13300000",
            "area": "7420",
            "bedrooms": "4",
            "bathrooms": "2",
            "stories": "3",
            "mainroad": "yes",
            "guestroom": "no",
            "basement": "no",
            "hotwaterheating": "no",
            "airconditioning": "yes",
            "parking": "2",
            "prefarea": "yes",
            "furnishingstatus": "furnished"
        },
        {
            "price": "12250000",
            "area": "8960",
            "bedrooms": "4",
            "bathrooms": "4",
            "stories": "4",
            "mainroad": "yes",
            "guestroom": "no",
            "basement": "no",
            "hotwaterheating": "no",
            "airconditioning": "yes",
            "parking": "3",
            "prefarea": "no",
            "furnishingstatus": "furnished"
        },
    "number": 2,
    "message": "success"
}

"""

#####################################
# Import Modules
#####################################

# Import from Python Standard Library
import json
import pathlib
import sys

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
from utils_logger import logger

#####################################
# Declare Global Variables
#####################################

FETCHED_DATA_DIR: str = "tmartin_data"
PROCESSED_DIR: str = "tmartin_processed"

#####################################
# Define Functions
#####################################

# TODO: Add or replace this with a function that reads and processes your JSON file

def count_houses_by_furnishingstatus(file_path: pathlib.Path) -> dict:
    """Count the number of houses for each furnishing status from a JSON file."""
    try:
        # Open the JSON file using the file_path passed in as an argument
        with file_path.open('r') as file:

            # Use the json module load() function 
            # to read data file into a Python dictionary
            houses_dictionary = json.load(file)  

            # initialize an empty dictionary to store the counts
            furnishing_counts_dictionary = {}

            # people is a list of dictionaries in the JSON file
            # We can get it using the get() method and pass in the key "people"
            houses_list: list = houses_dictionary.get("houses", [])

            # For each person in the list, get the craft and count them
            for houses_dictionary in houses_list:  

                # Get the craft from the person dictionary
                # If the key "craft" is not found, default to "Unknown"
                furnishingstatus = houses_dictionary.get("furnishingstatus", "furnished")

                # Update the craft counts dictionary for that craft
                # If the craft is not in the dictionary, initialize it to 0
                # Add 1 to the count for the current craft
                furnishing_counts_dictionary[furnishingstatus] = furnishing_counts_dictionary.get(furnishingstatus, 0) + 1

            # Return the dictionary with counts of astronauts by spacecraft    
            return furnishing_counts_dictionary
    except Exception as e:
        logger.error(f"Error reading or processing JSON file: {e}")
        return {} # return an empty dictionary in case of error

def process_json_file():
    """Read a JSON file, count astronauts by spacecraft, and save the result."""

    # TODO: Replace with path to your JSON data file
    input_file: pathlib.Path = pathlib.Path(FETCHED_DATA_DIR, "house_price_parquet.json")

    # TODO: Replace with path to your JSON processed file
    output_file: pathlib.Path = pathlib.Path(PROCESSED_DIR, "json_houses_by_furnishing.txt")
    
    # TODO: Call your new function to process YOUR JSON file
    # TODO: Create a new local variable to store the result of the function call
    furnshing_counts = count_houses_by_furnishingstatus(input_file)

    # Create the output directory if it doesn't exist
    output_file.parent.mkdir(parents=True, exist_ok=True)
    
    # Open the output file in write mode and write the results
    with output_file.open('w') as file:
        # TODO: Update the output to describe your results
        file.write("Houses by Furnishing Status:\n")
        for furnishingstatus, count in furnshing_counts.items():
            file.write(f"{furnishingstatus}: {count}\n")
    
    # Log the processing of the JSON file
    logger.info(f"Processed JSON file: {input_file}, Results saved to: {output_file}")

#####################################
# Main Execution
#####################################

if __name__ == "__main__":
    logger.info("Starting JSON processing...")
    process_json_file()
    logger.info("JSON processing complete.")