import re

def string_to_list(message):
    return list(message)

def list_to_string(message):
    return ''.join(message)

def clean_string(message):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', message).upper()

def clean_list(message):
    s = clean_string(list_to_string(message))
    return string_to_list(s)

def mod_char(a):
    return ((a - ord('A')) % 26) + ord('A')

VALID_ALPHA     = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
VALID_ALPHA_INV = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]