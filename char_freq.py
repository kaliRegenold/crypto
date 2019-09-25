#!/bin/python3

import sys
from cipher_aux import *

# Return the frequency that each character
# occurs in the text string
def char_freq(message_l):
    char_count = [0]*26
    for c in message_l:
        char_count[c] += 1
    total_count = len(message_l)
    return [x/total_count for x in char_count]

# Print the character frequencies nicely
def print_freq(freq):
    for i in range(0, len(freq)):
        print(chr(i+ord('A')), "%.3f" % freq[i])

# Prints freqencies of each character in given
# text file
def main():
    if len(sys.argv) != 2:
        print("python3 char_freq.py [text_file_path]")

    text_file = open(sys.argv[1], 'r')
    text = text_file.read()
    message_l = string_to_list(clean_string(text))
    freq = char_freq(message_l)
    print_freq(freq)

if __name__ == "__main__":
    main()
