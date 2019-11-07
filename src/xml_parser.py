from collections import defaultdict
import xml.etree.ElementTree as ET

def mk_dict(bill_txt):
    root = ET.fromstring(bill_txt)
    bill = defaultdict(list)
    get_node_info(root, bill)
    return bill

def get_node_info(branch, xml_dict):
    if branch.text:
        xml_dict[branch.tag].append(branch.text)
    if branch.getchildren():
        for child in branch:
            get_node_info(child, xml_dict)

