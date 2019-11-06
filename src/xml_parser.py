from collections import defaultdict
import xml.etree.ElementTree as et

def mk_dict(file_name):
    tree = et.parse(file_name)
    root = tree.getroot()
    bill = defaultdict(list)
    get_node_info(root, bill)
    return bill

def get_node_info(branch, xml_dict):
    xml_dict[branch.tag].append(branch.text)
    if branch.getchildren():
        for child in branch:
            get_node_info(child, xml_dict)

