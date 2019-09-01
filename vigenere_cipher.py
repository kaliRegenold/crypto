from cipher_aux import *
from char_freq import char_freq


def vigenere_encrypt(message, key):
    ret = [0]*len(message)
    key_count = 0
    for i in range(0, len(message)):
        ret[i] = chr(mod_char( ord(message[i]) + (ord(key[key_count])-ord('A')) ))
        key_count += 1
        if key_count == len(key):
            key_count = 0
    return ret

def vigenere_disp_freq(message, max_disp):
    disp_freq = [0]*max_disp
    for d in range(1, max_disp+1):
        for m in range(0, len(message)-d):
            if(message[m] == message[m+d]):
                disp_freq[d-1] += 1
    return sort_disp_freq(disp_freq)

def vigenere_get_key(message, disp):
    key = [0] * disp
    for k in range(0, len(key)):
        nth_index = message[k::disp]
        V = [nth_index.count(chr(i+ord('A'))) for i in range(0,26)]
        W = [round(v/len(nth_index),4) for v in V]
        WA = [round(dot_prod(W, get_A_i(i)),4) for i in range(0, 26)]
        key[k] = chr(WA.index(max(WA)) + ord('A'))
    return key

def dot_prod(a, b):
    return sum( [a[i]*b[i] for i in range(len(b))] )


def sort_disp_freq(disp_freq):
    df_list = list(zip( disp_freq, range(1, len(disp_freq)+1) ))
    return sorted(df_list, key = lambda x: x[0], reverse=True)

def print_disp_freq(disp_freq):
    for i,v in enumerate(disp_freq):
        print(i+1, v)

def main():
    m_string = "themethodusedforthepreparationandreadingofcodemessagesis"+ \
               "simpleintheextremeandatthesametimeimpossibleoftranslatio"+ \
               "nunlessthekeyisknowntheeasewithwhichthekeymaybechangedis"+ \
               "anotherpointinfavoroftheadoptionofthiscodebythosedesirin"+ \
               "gtotransmitimportantmessageswithouttheslightestdangeroft"+ \
               "heirmessagesbeingreadbypoliticalorbusinessrivalsetc"
    m_list = string_to_list(clean_string(m_string))
    k_list = string_to_list("CODES")
    m_enc = vigenere_encrypt(m_list, k_list)
    print(list_to_string(m_enc))
    disp_freq = vigenere_disp_freq(m_enc, 10)
    key = vigenere_get_key(m_enc, disp_freq[0][1])
    print(key)

if __name__ == "__main__":
    main()
