#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(file_csv):
    """
    Convert a CSV file to JSON format and write the serialized data to a file.
    
    Args:
        file_csv (str): The name of the CSV file to convert.
    
    Returns:
        bool: True if conversion is successful, False otherwise.
    """
    data = []
    try:
        # Open and read the CSV file
        with open(file_csv, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        # Serialize to JSON and write to file
        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        return True
    
    # Catch specific exceptions
    except FileNotFoundError:
        print(f"Error: The file '{file_csv}' does not exist.")
        return False
    except IOError as e:
        print(f"Error reading or writing file: {e}")
        return False
