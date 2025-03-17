import re

def is_valid_identifier(identifier):
    pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$' # the pattern allows the start of the identifier with any letter (uppercase or lowercase) or an underscore followed by any number of of letters or numbers or underscores or any mixture of all of them

    if re.match(pattern, identifier):
        return True
    return False