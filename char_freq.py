import re
import sys

BASE_A = 65

# Remove anything not an alpha character
# and capitalize
def clean_text(text):
    regex = re.compile('[^a-zA-Z]')
    return regex.sub('', text).upper()

# Return the frequency that each character
# occurs in the text string
def char_freq(text):
    char_count = [0]*26
    c_text = clean_text(text)
    for c in c_text:
        char_count[ord(c)-BASE_A] += 1
    total_count = len(c_text)
    return [x/total_count for x in char_count]

# Print the character frequencies nicely
def print_freq(freq):
    for i in range(0, len(freq)):
        print(chr(i+BASE_A), "%.3f" % freq[i])

# Prints freqencies of each character in given
# text file
def main():
    if len(sys.argv) != 2:
        print("python3 word_freq.py [text_file_path]")

    text_file = open(sys.argv[1], 'r')
    text = text_file.read()
    freq = char_freq(text)
    print_freq(freq)

if __name__ == "__main__":
    main()
