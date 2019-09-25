from cipher_aux import *
import sys

def euclid(r_1, r_2):
    if r_2 == 0:
        return r_1

    q = r_1 // r_2
    r = r_1 - (q*r_2)

    return euclid(r_2, r)

def extended_euclid(r1, r2, s1=1, s2=0, t1=0, t2=1):
    if r2 == 0:
        return r1, s1, t1

    q = r1 // r2
    r = r1 - (q*r2)
    s = s1-q*s2
    t = t1-q*t2

    return extended_euclid(r2, r, s2, s, t2, t)


def main():
    if len(sys.argv) == 4 and sys.argv[1] == "-x":
        gcd, x, y = extended_euclid(int(sys.argv[2]), int(sys.argv[3]))
        print("ax + by = gcd")
        print("x = %d  y = %d gcd = %d" % (x, y, gcd))
    elif len(sys.argv) == 3:
        gcd = euclid(int(sys.argv[1]), int(sys.argv[2]))
        print("gcd(a, b) = ", gcd)
    else:
        print("Usage:\neuclid.py [-x] a b")


if __name__ == "__main__":
    main()
