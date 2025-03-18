import re
"""
 the identifier_pattern allows the start of the identifier with any letter (uppercase or lowercase)
 or an underscore followed by any number of of letters or numbers or underscores or any combination of all of them

"""
identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

reserved_keywords = {"if", "else", "while", "int", "float", "bool", "return", "and", "or", "not", "for", "break", "with", "class"} # set of reserved keywords

def is_valid_identifier(token):

    return bool(re.match(identifier_pattern, token) and token not in reserved_keywords)

def tokenize(input_string):
    # \b is a word boundry anchor. It matches the position between word character and non word character (e.g. punctuation chars)
    # \w+ matches one or more word characters (letters A-Z or a-z, digits 0-9, underscores)
    tokens = re.findall(r'\b\w+\b', input_string) # findall() returns a list of tokens
    return tokens

def scan_identifiers(input_string):
    tokens = tokenize(input_string)
    identifiers = [token for token in tokens if is_valid_identifier(token)]
    return identifiers