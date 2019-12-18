import auxiliary as aux
import cryptomath as cm
from math import gcd
import sys

def affine_encrypt(message_l, a, b, force=False):
    if not force:
        if a not in aux.VALID_ALPHA:
            print("Invalid alpha value.")
            return []
    return [(a*m + b) % 26 for m in message_l]

def affine_decrypt(message_l, a, b):
    a_star = aux.VALID_ALPHA_INV[aux.VALID_ALPHA.index(a)]
    return [(a_star*m - a_star*b) % 26 for m in message_l]

def affine_attack_exhaust(message_l):
    print("(a, b)  \tPLAINTEXT")
    print("==================")
    for a in aux.VALID_ALPHA:
        for b in range(0,26):
            print("(%d, %d)  \t%s" %
                (a, b, aux.list_to_string(affine_decrypt(message_l,a,b))))

def affine_attack_frequency(message_l):
    alpha = -1
    beta = -1

    # Get frequencies of every character
    freq = cm.frequency_counter(message_l)

    # Sort frequencies (and their letter) in descending order
    freq_sorted = sorted(range(len(freq)), key=lambda k: freq[k], reverse=True)

    E_e = freq_sorted[0]        # Encrypted 'e' (assuming)
    T_e = freq_sorted[1]        # Encrypted 't' (assuming)
    E_d = ord('E') - ord('A')   # Actual 'e'
    T_d = ord('T') - ord('A')   # Actual 't'

    enc_diff = (E_e - T_e) % 26
    dec_diff = (E_d - T_d) % 26

    for a in aux.VALID_ALPHA:
        if (a*dec_diff) % 26 == enc_diff:
            alpha = a
    if alpha == -1:
        print("Valid alpha not found. E_e: %d T_e: %d" % (E_e, T_e))
        return []

    beta = (E_e - (E_d * alpha)) % 26
    return(alpha, beta)
