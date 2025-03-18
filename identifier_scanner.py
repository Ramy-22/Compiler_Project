import re
"""
 the identifier_pattern allows the start of the identifier with any letter (uppercase or lowercase)
 or an underscore followed by any number of of letters or numbers or underscores or any combination of all of them

"""
identifier_pattern = r'^[a-zA-Z_][a-zA-Z0-9_]*$'

# set of reserved keywords
reserved_keywords = {"if", "else", "while", "int", "float", "bool", "return", "and", "or", "not", "for", "break", "with", "class"} 

def is_valid_identifier(token): # validates a token and returns a boolean

    return bool(re.match(identifier_pattern, token) and token not in reserved_keywords)

def tokenize(input_string):
    # \b is a word boundry anchor. It matches the position between word character and non word character as punctuation chars
    # \w+ matches one or more word characters (letters A-Z or a-z, digits 0-9, underscores)
    tokens = re.findall(r'\b\w+\b', input_string) # findall() returns a list of tokens
    return tokens

def scan_identifiers(input_string): # scans the input string, and returns a list of valid identifiers
    tokens = tokenize(input_string) # tokenize the input string
    identifiers = [token for token in tokens if is_valid_identifier(token)] # make a list of tokens that are valid identifiers
    return identifiers