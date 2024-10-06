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
                text = child.text
                if text.isdigit():
                    parsed_dict[child.tag] = int(text)
                else:
                    try:
                        parsed_dict[child.tag] = float(text)
                    except ValueError:
                        parsed_dict[child.tag] = text
        return parsed_dict
    
    return parse_element(root)
