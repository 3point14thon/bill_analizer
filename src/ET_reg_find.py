import xml.etree.ElementTree as ET
import regex as re

def reg_findall(root, pattern):
    pattern = re.compile(pattern)
    matches = []
    for child in root:
        if pattern.match(child.tag):
            matches.append(child)
    return None if len(matches) == 0 else matches
