# Kali Regenold
# Fall 2019
# Cryptoraphy CSC-412
# Notes:
#   TODO: Add linear feedback shift register
#   You'll probably want to collapse this file

import auxiliary as aux
import cryptomath as cm
import affine
import vigenere
import lsfr
import test_suite

#####################################
# Helper Functions
#####################################
def get_user_input_choice():
    try:
        user_input = int(input("> "))
    except ValueError:
        user_input = -1
    return user_input

def get_user_input_message():
    print("Type out message to be processed or prepend -f to read from a file.")
    message_input = input("> ");
    if message_input[0:2] == "-f":
        message_l = aux.list_from_file(message_input[2:].strip())
        if message_l == []:
            return []
    else:
        message_l = aux.string_to_list(message_input)
    return aux.clean_list(message_l)


#####################################
# Classic Cryptosystems Funtions
#####################################
def user_affine_encrypt():
    message_l = get_user_input_message()
    try:
        a = int(input('a: '))
        b = int(input('b: '))
    except ValueError:
        return
    ciphertext = affine.affine_encrypt(message_l, a, b)
    print(aux.list_to_string(ciphertext))

def user_affine_decrypt():
    message_l = get_user_input_message()
    try:
        print("Use value a from encryption key, not the inverse")
        a = int(input('a: '))
        b = int(input('b: '))
    except ValueError:
        return
    plaintext = affine.affine_decrypt(message_l, a, b)
    print(aux.list_to_string(plaintext))

def user_affine_attack_exhuast():
    message_l = get_user_input_message()
    affine.affine_attack_exhaust(message_l)

def user_affine_attack_frequency():
    message_l = get_user_input_message()
    a, b = affine.affine_attack_frequency(message_l)
    print("a: %d b: %d" % (a, b))

def user_vigenere_encrypt():
    message_l = get_user_input_message()
    key_s = input("Key: ")
    key_l = aux.clean_list(aux.string_to_list(key_s))
    ciphertext = vigenere.vigenere_encrypt(message_l, key_l)
    print(aux.list_to_string(ciphertext))

def user_vigenere_decrypt():
    message_l = get_user_input_message()
    key_s = input("Key: ")
    key_l = aux.clean_list(aux.string_to_list(key_s))
    plaintext = vigenere.vigenere_decrypt(message_l, key_l)
    print(aux.string_to_list(plaintext))

def user_vigenere_attack():
    message_l = get_user_input_message()
    key_l = vigenere.vigenere_attack_frequency(message_l)
    print("Key: ", list_to_string(key_l))

def user_lsfr_attack():
    print("Provide file with key.")
    filename = input("> ");
    try:
        f = open(filename, 'r')
    except IOError:
        print("Could not read file: %s" % filename)
        return
    m_s = f.read().strip()
    f.close()
    v = [int(m) for m in m_s]
    coeffs = lsfr.lsfr_attack(v)
    print(coeffs)


def cryptosystems_help():
    print("---Affine")
    print()

#####################################
# Cryptomath Functions
#####################################
def user_frequency_counter():
    message_l = get_user_input_message()
    freq = cm.frequency_counter(message_l)
    for i in range(0,26):
        print("%s: %.4f" % (chr(i+ord('A')), freq[i]))

def user_gcd():
    try:
        a = int(input('a: '))
        b = int(input('b: '))
    except ValueError:
        return
    gcd = cm.euclid(a, b)
    print("gcd(a,b) = %d"% gcd)

def user_xgcd():
    try:
        a = int(input('a: '))
        b = int(input('b: '))
    except ValueError:
        return
    gcd, s, t = cm.extended_euclid(a, b)
    print("gcd(a,b) = %d"% gcd)
    print("s: %d" % s)
    print("t: %d" % t)

def user_mod_inverse():
    try:
        a = int(input('a: '))
        n = int(input('n: '))
    except ValueError:
        return
    a_inv = cm.mod_inverse(a, n)
    if a_inv == -1:
        print("No inverse found")
    else:
        print("a inverse: ", a_inv)

def user_is_prime():
    try:
        n = int(input('n: '))
    except ValueError:
        return
    is_prime_ish = cm.is_prime(n)
    if is_prime_ish:
        print("%d is PROBABLY prime" % n)
    else:
        print("%d is NOT prime" % n)

def user_is_primitive_root():
    try:
        a = int(input('a: '))
        n = int(input('n: '))
    except ValueError:
        return
    print(cm.is_primitive_root(a, n))


#####################################
# Menu Functions
#####################################
def classic_cryptosystems():
    user_input = -1
    while user_input != 0:
        print("===CLASSIC CRYPTOSYSTEMS===")
        print("---Affine")
        print("   1: Encrypt")
        print("   2: Decrypt")
        print("   3: Attack: Exhuast")
        print("   4: Attack: Frequency Analysis")
        print("---Vigenere")
        print("   5: Encrypt")
        print("   6: Decrypt")
        print("   7: Attack")
        print("---Other")
        print("   8: LSFR Attack")
        print("0: Return to Crypto Library Menu")
        user_input = get_user_input_choice()

        if user_input == 1:
            user_affine_encrypt()
        elif user_input == 2:
            user_affine_decrypt()
        elif user_input == 3:
            user_affine_attack_exhuast()
        elif user_input == 4:
            user_affine_attack_frequency()
        elif user_input == 5:
            user_vigenere_encrypt()
        elif user_input == 6:
            user_vigenere_decrypt()
        elif user_input == 7:
            user_vigenere_attack()
        elif user_input == 8:
            user_lsfr_attack()
        elif user_input == 0:
            return

def cryptomath():
    user_input = -1
    while user_input != 0:
        print("===CRYPTO MATH===")
        print("1: Frequency Counter")
        print("2: GCD")
        print("3: Extended GCD")
        print("4: Find mod inverse")
        print("5: isPrime")
        print("6: Random Prime")
        print("7: isPrimitiveRoot")
        print("0: Return to Crypto Library Menu")
        user_input = get_user_input_choice()

        if user_input == 1:
            user_frequency_counter()
        elif user_input == 2:
            user_gcd()
        elif user_input == 3:
            user_xgcd()
        elif user_input == 4:
            user_mod_inverse()
        elif user_input == 5:
            user_is_prime()
        elif user_input == 6:
            ...
        elif user_input == 7:
            user_is_primitive_root()
        elif user_input == 0:
            return

def crypto_library():
    user_input = -1
    while user_input != 0:
        print("===CRYPTO LIBRARY===")
        print("1: Classic Cryptosystems")
        print("2: Cryptomath and Utilities")
        print("3: DES")
        print("4: RSA")
        print("0: Return to Main Menu")
        user_input = get_user_input_choice()

        if user_input == 1:
            classic_cryptosystems()
        elif user_input == 2:
            cryptomath()
        elif user_input == 3:
            print("DES is only ran in test suite")
        elif user_input == 4:
            print("RSA not implemented")
        elif user_input == 0:
            return


def main():
    user_input = -1

    # Main menu
    while(user_input != 0):
        print("===MAIN MENU===")
        print("Welcome to Kali's CryptoLibrary")
        print("1: Enter Crypto Library")
        print("2: Enter Test Suite")
        print("0: Exit")
        user_input = get_user_input_choice()

        # Enter Crypto Library
        if user_input == 1:
            crypto_library()
        # Enter Test Suite
        elif user_input == 2:
            test_suite.test_all()
            user_input = -1

    print("Goodbye")


if __name__ == "__main__":
    main()
