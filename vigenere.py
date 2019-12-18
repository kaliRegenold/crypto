import auxiliary as aux
import cryptomath as cm


def vigenere_encrypt(message_l, key_l):
    ret = [0] * len(message_l)
    key_i = 0
    for i in range(0, len(message_l)):
        ret[i] = message_l[i] + key_l[key_i] % 26
        key_i += 1
        if key_i == len(key_l):
            key_i = 0
    return ret


def vigenere_decrypt(message_l, key_l):
    ret = [0] * len(message_l)
    key_i = 0
    for i in range(0, len(message_l)):
        ret[i] = message_l[i] - key_l[key_i] % 26
        key_i += 1
        if key_i == len(key_l):
            key_i = 0
    return ret


def vigenere_attack_frequency(message_l, max_shift=10):
    key_length = vigenere_find_key_length(message_l, max_shift)
    key = vigenere_get_key(message_l, key_length)
    return key


def vigenere_find_key_length(message_l, max_shift):
    # First value of matched_count element is the shift value when comparing
    #   characters in the message
    # Second value is number of matched characters in shift comparison
    matched_count = [[0] * 2 for i in range(max_shift)]

    # Fill out matched_count
    for d in range(1, max_shift+1):
        matched_count[d-1][1] = d
        for m in range(0, len(message_l)-d):
            if message_l[m] == message_l[m+d]:
                matched_count[d-1][0] += 1

    # Sort the 2D array by the number of matched characters
    sorted_matched = sorted(matched_count, key = lambda x: x[0], reverse=True)
    # Return the shift value
    return sorted_matched[0][1]


def dot_prod(a, b):
    return sum( [a[i]*b[i] for i in range(len(b))] )


def vigenere_get_key(message_l, key_length):
    key = [0] * key_length
    for k in range(0, len(key)):
        # Get every nth character in message
        nth_index = message_l[k::key_length]
        # Get character count
        V = [nth_index.count(i) for i in range(0,26)]
        # Divide by length to get freqency
        W = [round(v/len(nth_index),4) for v in V]
        # Multiply nth_index frequency list by standard English frequency
        WA = [round(dot_prod(W, aux.get_A_i(i)),4) for i in range(0, 26)]
        # Character for this index of key is index of max value in WA
        key[k] = WA.index(max(WA))
    return key


def test_vigenere():
    m_string = "themethodusedforthepreparationandreadingofcodemessagesis"+ \
               "simpleintheextremeandatthesametimeimpossibleoftranslatio"+ \
               "nunlessthekeyisknowntheeasewithwhichthekeymaybechangedis"+ \
               "anotherpointinfavoroftheadoptionofthiscodebythosedesirin"+ \
               "gtotransmitimportantmessageswithouttheslightestdangeroft"+ \
               "heirmessagesbeingreadbypoliticalorbusinessrivalsetc"
    m_list = aux.string_to_list(aux.clean_string(m_string))
    k_list = aux.string_to_list("CODES")
    m_enc = vigenere_encrypt(m_list, k_list)
    key = vigenere_attack_frequency(m_enc, 10)
    print(aux.list_to_string(key))
    #if key != k_list

if __name__ == "__main__":
    test_vigenere()
