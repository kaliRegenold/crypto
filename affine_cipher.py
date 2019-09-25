from cipher_aux import *
from math import gcd
import sys
from char_freq import char_freq

def affine_encrypt(message_l, a, b, force=False):
    if not force:
        if a not in VALID_ALPHA:
            print("Invalid alpha value. Use force.")
            return []
    return [(a*m + b) % 26 for m in message_l]

def affine_decrypt(message_l, a, b):
    a_star = VALID_ALPHA_INV[VALID_ALPHA.index(a)]
    return [( a_star*m - a_star*b ) % 26 for m in message_l]

def affine_attack_exhaust(message_l):
    for a in VALID_ALPHA:
        for b in range(0,26):
            print("(%d, %d)  \t%s" % (a, b, list_to_string(affine_decrypt(message_l,a,b))))

def affine_attack_frequency(message_l):
    alpha = -1
    beta = -1
    freq = char_freq(message_l)
    freq_sorted = sorted(range(len(freq)), key=lambda k: freq[k], reverse=True)
    E_e = freq_sorted[0]
    T_e = freq_sorted[1]
    E_d = ord('E') - ord('A')
    T_d = ord('T') - ord('A')
    enc_diff = (E_e - T_e) % 26
    dec_diff = (E_d - T_d) % 26
    for a in VALID_ALPHA:
        if (a*dec_diff) % 26 == enc_diff:
            alpha = a
    if alpha == -1:
        print("Valid alpha not found. E_e: %d T_e: %d" % (E_e, T_e))
        return []

    beta = (E_e - (E_d * alpha)) % 26
    print(list_to_string(affine_decrypt(message_l, alpha, beta)))

def usage():
    print("Usage:")
    print("affine_cipher -[e/d/a] textfile.txt A B")
    print("\t-e\tEncrypt\t\t A and B values are required.")
    print("\t-d\tDecrypt\t\t A and B values are required.")
    print("\t-ae\tAttack Exhaust\t Omit A and B values.")
    print("\t-af\tAttack Frequency Omit A and B values.")
    print("\tA\tMultiplier\t Must be int.")
    print("\tB\tDisplacement\t Must be int.")

def main():
    if len(sys.argv) < 3:
        usage()
        return

    # Set command from commandline args
    command = sys.argv[1]

    # Set message from text file
    try:
        f = open(sys.argv[2], 'r')
    except IOError:
        print("Could not read file: %s" % sys.argv[2])
        return
    m_s = f.read()
    f.close()
    message_l = string_to_list(clean_string(m_s))

    # Handle encyption/decryption case
    if command == "-e" or command == "-d":
        if len(sys.argv) < 5:
            usage()
            return

        # Set alpha and beta values from commandline args
        alpha = int(sys.argv[3])
        beta = int(sys.argv[4])

        # Do encryption or decryption
        if command == "-e":
            enc_l = affine_encrypt(message_l, alpha, beta)
            print(list_to_string(enc_l))
        elif command == "-d":
            dec_l = affine_decrypt(message_l, alpha, beta)
            print(list_to_string(dec_l))

    elif command == "-ae":
        affine_attack_exhaust(message_l)
    elif command == "-af":
        affine_attack_frequency(message_l)
    else:
        usage()

if __name__ == "__main__":
    main()
