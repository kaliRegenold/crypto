import random as rand
import re

def frequency_counter(message_l):
    char_count = [0]*26
    for c in message_l:
        char_count[c] += 1
    total_count = len(message_l)
    return [x/total_count for x in char_count]

def euclid(r_1, r_2):
    if r_2 == 0:
        return r_1

    q = r_1 // r_2
    r = r_1 - (q*r_2)

    return euclid(r_2, r)

# Returns gcd, s, t
def extended_euclid(r1, r2, s1=1, s2=0, t1=0, t2=1):
    if r2 == 0:
        return r1, s1, t1

    q = r1 // r2
    r = r1 - (q*r2)
    s = s1-q*s2
    t = t1-q*t2

    return extended_euclid(r2, r, s2, s, t2, t)

def mod_inverse(a, n):
    gcd, s, t = extended_euclid(a, n)
    if gcd != 1:
        return -1
    return s % n

def is_prime(n):
    # Fermat's Primality Test
    a = rand.randint(1,n-1)
    return (a**(n-1) % n == 1)

def is_primitive_root(a, n):
    tracker = 0b0
    for i in range(1,n):
        tracker ^= 1 << (a**i % n)
    return tracker == (2**n)-2
