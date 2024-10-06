#!/usr/bin/env python3

import csv
import json

def convert_csv_to_json(file_csv, file_json):
    data = []
    try:
        with open(file_csv) as csv:
            csvread = csv.DictReader(csv)
            for row in csvread:
                    data.append(row)
        with open(file_json, 'w') as json:
            json.dump(data, json, indent=4)
        return True
    except:
         return False