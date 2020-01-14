import regex as re


def reg_findall(root, pattern):
    '''
   Returns a list of the immediate children from the given root whos tag
   matches the given regex pattern.

    Args:
        root(xml_element): The xml_element to compose list of children from.
        pattern(str): The regex pattern to be matched.

    Returns:
        List of children whoes tag matches the given regex pattern.
    '''
    pattern = re.compile(pattern)
    matches = []
    for child in root:
        if pattern.match(child.tag):
            matches.append(child)
    return None if len(matches) == 0 else matches
