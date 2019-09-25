import re

VALID_ALPHA     = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]
VALID_ALPHA_INV = [1, 9, 21, 15, 3, 19, 7, 23, 11, 5, 17, 25]
A =  [.08167, .01492, .02782, .04253, .12702, .02228, .02015, \
      .06094, .06966, .00153, .00772, .04025, .02406, .06749, \
      .07507, .01929, .00095, .05987, .06327, .09056, .02758, \
      .00978, .02360, .00150, .01974, .00074]

def string_to_list(message_s):
    return [ord(c)-ord('A') for c in message_s.upper()]

def list_to_string(message_l):
    return ''.join([chr(c+ord('A')) for c in message_l])

def clean_string(message_s):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', message_s).upper()

def clean_list(message_l):
    message_s = clean_string(list_to_string(message_l))
    return string_to_list(message_s)

def mod_char(a):
    return a%26

def get_A_i(i):
    return A[-i:] + A[:-i]
