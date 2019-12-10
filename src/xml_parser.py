from collections import defaultdict
import xml.etree.ElementTree as ET

def mk_dict(bill_txt):
    root = ET.fromstring(bill_txt)
    bill = defaultdict(list)
    bill = get_lv1_data(root.find('metadata'), bill)
    bill = get_lv1_data(root.find('form'), bill)
    body = 'legis_body'
    bill[body] = get_legis_body(root.find(body))
    return bill

def get_lv1_data(branch, xml_dict):
    for datum in list(branch):
        if datum.text:
            bill_dict[datum.tag] = datum.text
    return xml_dict

def get_legis_body(branch, leg=''):
    for child in branch:
        if child.text:
            leg = ' '.join([leg, child.text])
        leg = par_child(child, leg)
    return leg
