import xml.etree.ElementTree as ET

def mk_dict(bill_txt):
    root = ET.fromstring(bill_txt)
    bill = {}
    bill = get_lv1_data(root.find('metadata'), bill)
    bill = get_lv1_data(root.find('form'), bill)
    body = 'legis-body'
    bill[body] = get_legis_body(root.find(body))
    return bill

def get_lv1_data(branch, xml_dict):
    for child in list(branch):
        if child.text:
            xml_dict[child.tag] = child.text
    return xml_dict

def get_legis_body(branch, leg=''):
    for child in list(branch):
        if child.text:
            leg = ' '.join([leg, child.text])
        leg = get_legis_body(child, leg)
    return leg
