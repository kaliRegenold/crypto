import auxiliary as aux
import affine
import vigenere
import lsfr
import des
import cryptomath as cm

test_message_s = "themethodusedforthepreparationandreadingofcodemessagesis"+ \
           "simpleintheextremeandatthesametimeimpossibleoftranslatio"+ \
           "nunlessthekeyisknowntheeasewithwhichthekeymaybechangedis"+ \
           "anotherpointinfavoroftheadoptionofthiscodebythosedesirin"+ \
           "gtotransmitimportantmessageswithouttheslightestdangeroft"+ \
           "heirmessagesbeingreadbypoliticalorbusinessrivalsetc"
test_message_l = aux.string_to_list(test_message_s)

def des_test():
    print("===DES TEST===")
    r = 0b011100100110
    k = 0b011001010
    enc = des.DES_encrypt(r, k, 1)
    dec = des.DES_decrypt(enc, k, 1)
    if dec != r:
        print("FAILED: Encrypt-Decrypt Test")
    else:
        print("PASSED: Encrypt-Decrypt Test")


def is_primitive_root_test():
    print("===isPrimitiveRoot Test===")
    if not cm.is_primitive_root(3, 7):
        print("FAILED: 3 is primitive root mod 7")
    else:
        print("PASSED: 3 is primitive root mod 7")

def is_prime_test():
    print("===isPrime Test===")
    if cm.is_prime(38):
        print("FAILED: 38 is not prime")
    else:
        print("PASSED: 38 is not prime")
    if not cm.is_prime(37):
        print("FAILED: 37 is prime")
    else:
        print("PASSED: 37 is prime")

def find_mod_inverse_test():
    print("===Mod Inverse Test===")
    inv = cm.mod_inverse(11, 17)
    if inv != 14:
        print("FAILED: Standard Test")
    else:
        print("PASSED: Standard Test")

def extended_gcd_test():
    print("===Extended GCD Test===")
    gcd, s, t = cm.extended_euclid(12, 71)
    if gcd != 1 and s != 6 and t != -1:
        print("FAILED: Standard Test")
    else:
        print("PASSED: Standard Test")

def gcd_test():
    print("===GCD TEST===")
    gcd_36_60 = cm.euclid(36, 60)
    if gcd_36_60 != 12:
        print("FAILED: Non 1 GCD Test")
    else:
        print("PASSED: Non 1 GCD Test")

    gcd_12_71 = cm.euclid(12, 71)
    if gcd_12_71 != 1:
        print("FAILED: 1 GCD Test")
    else:
        print("PASSED: 1 GCD Test")

def lsfr_test():
    print("===LSFR TEST===")
    message_s = "101001101100010010000111000001011111"+ \
                "100101010001100111101110101101001101"+ \
                "100010010000111000"
    v = [int(m) for m in message_s]
    coeffs = lsfr.lsfr_attack(v)
    if coeffs != [0, 1, 1, 0, 1, 1]:
        print("FAILED: Matrix Attack Test")
    else:
        print("PASSED: Matrix Attack Test")

def vigenere_test():
    print("===VIGENERE TEST===")
    key_l = aux.string_to_list("CODES")
    encrypted_l = vigenere.vigenere_encrypt(test_message_l, key_l)
    decrypted_l = vigenere.vigenere_decrypt(encrypted_l, key_l)
    if decrypted_l != test_message_l:
        print("FAILED: Encrypt-Decrypt Test")
    else:
        print("PASSED: Encrypt-Decrypt Test")
    key_p = vigenere.vigenere_attack_frequency(encrypted_l)
    if key_p != key_l:
        print("FAILED: Attack Frequency Test")
    else:
        print("PASSED: Attack Frequency Test")

def affine_test():
    print("===AFFINE TEST===")
    alpha = 5
    beta = 11
    encrypted_l = affine.affine_encrypt(test_message_l, alpha, beta)
    decrypted_l = affine.affine_decrypt(encrypted_l, alpha, beta)
    if decrypted_l != test_message_l:
        print("FAILED: Encrypt-Decrypt Test")
    else:
        print("PASSED: Encrypt-Decrypt Test")
    alpha_p, beta_p = affine.affine_attack_frequency(encrypted_l)
    if alpha_p != alpha and beta_p != beta:
        print("FAILED: Attack Frequency Test")
    else:
        print("PASSED: Attack Frequency Test")

def test_all():
    print("Test string:")
    print(test_message_s)
    affine_test()
    vigenere_test()
    lsfr_test()
    gcd_test()
    extended_gcd_test()
    find_mod_inverse_test()
    is_prime_test()
    is_primitive_root_test()
    des_test()

if __name__ == "__main__":
    test_all()
