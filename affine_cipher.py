from cipher_aux import *
from math import gcd

def affine_encrypt(message, a, b):
    return [chr(mod_char( a*ord(m)+b )) for m in message]

def affine_decrypt(message, a, b):
    a_star = VALID_ALPHA_INV[VALID_ALPHA.index(a)]
    return [chr(mod_char( a_star*ord(m) - a_star*b )) for m in message]

def affine_exhaust(message):
    for a in VALID_ALPHA:
        for b in range(0,26):
            print("(%d, %d)  \t%s" % (a, b, list_to_string(affine_decrypt(message,a,b))))

def main():
    m_list = string_to_list(clean_string("Hello, my name is Kali."))
    m_enc = affine_encrypt(m_list, 3, 8)
    print(list_to_string(m_enc))
    affine_exhaust(m_enc)
    # m_dec = affine_decrypt(m_enc, 3, 8)
    # print(list_to_string(m_dec))


if __name__ == "__main__":
    main()
