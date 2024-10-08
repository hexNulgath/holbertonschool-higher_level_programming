#!/usr/bin/env python3

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    root = ET.Element('data')
    
    def add_elements(parent, dictionary):
        for key, value in dictionary.items():
            child = ET.SubElement(parent, key)
            if isinstance(value, dict):
                add_elements(child, value)
            else:
                child.text = str(value)
    
    add_elements(root, dictionary)
    
    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)

def deserialize_from_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    def parse_element(element):
        parsed_dict = {}
        for child in element:
            if len(child):
                parsed_dict[child.tag] = parse_element(child)
            else:
                parsed_dict[child.tag] = child.text.strip()
        return parsed_dict

    return parse_element(root)

data = {
    'name': 'Alice',
    'age': 30,
    'height': 5.5,
    'address': {
        'city': 'Wonderland',
        'zipcode': 12345
    }
}

serialize_to_xml(data, 'data.xml')

deserialized_data = deserialize_from_xml('data.xml')
print(deserialized_data)
