import xml.etree.ElementTree as ET

def mk_dict(bill_txt):
    '''
    Takes in bill text in xml format and produces a
    dictionary containing most meta and form data and
    pooled legislative body.

    Args:
        bill_txt(str): string of bill to be parsed in xml
        format
    Returns: Dictionary containing most of the  bills data
    '''
    root = ET.fromstring(bill_txt)
    bill = {}
    bill = get_lv1_data(root.find('metadata'), bill)
    bill = get_lv1_data(root.find('form'), bill)
    body = 'legis-body'
    bill[body] = get_legis_body(root.find(body))
    return bill

def get_lv1_data(root, xml_dict):
    '''
    returns a dictionary of data extracted from the children
    of the given branch but not the childrens "decendents".

    Args:
        branch(xml_element): Parent of elements data is to
        be extracted from.

        xml_dict(dict): Dictionary extracted data is loaded
        into.

    Returns: Dictionary of extracted data.
    '''
    for child in list(root):
        if child.text:
            xml_dict[child.tag] = child.text
    return xml_dict

def get_legis_body(root, kern=''):
    '''
    returns a string of all text fields in all downstream
    elements from the given branch concatinated into one
    string.

    Args:
        root(xml_element): root element used to find all
        downstream elements.

        leg(str): kernal string added to to form pooled text
        for all elements in given tree.

    Returns: String of pooled text from all text fields in
    given tree.
    '''
    for child in list(root):
        if child.text:
            kern = ' '.join([kern, child.text])
        kern = get_legis_body(child, kern)
    return kern
