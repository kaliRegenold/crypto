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
    return ((a - ord('a')) % 26) + ord('a')
