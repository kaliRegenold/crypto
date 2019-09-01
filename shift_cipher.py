from cipher_aux import *
import random

def shift_encrypt(message, x):
    return [chr(mod_char( ord(m) + x )) for m in message]

def shift_decrypt(message, x):
    return [chr(mod_char( ord(m) + x )) for m in message]

def shift_exhaust(message):
    for i in range(0, 26):
        print("%d:\t%s" % (i, list_to_string(shift_decrypt(message, i))))

def main():
    m_string = "Hello, my name is Kali."
    m_clean = clean_string(m_string)
    m_list = string_to_list(m_clean)
    m_e = shift_encrypt(m_list, random.randint(0,25))
    print(list_to_string(m_e))
    shift_exhaust(m_e)
    # m_d = shift_decrypt(m_e, 1)
    # print(list_to_string(m_d))


if __name__ == "__main__":
    main()
