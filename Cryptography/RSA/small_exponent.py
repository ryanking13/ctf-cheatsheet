from base64 import b64decode
from decimal import *

# modular inverse code adapted from: https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm#Python
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

# https://crypto.stackexchange.com/questions/6713/low-public-exponent-attack-for-rsa

e = 3
c1 = 0
n1 = 0
c2 = 0
n2 = 0
c3 = 0
n3 = 0


t1 = c1 * (n2 * n3) * modinv(n2 * n3, n1)
t2 = c2 * (n3 * n1) * modinv(n3 * n1, n2)
t3 = c3 * (n1 * n2) * modinv(n1 * n2, n3)

c = (t1 + t2 + t3) % (n1 * n2 * n3)

getcontext().prec = 1000
msg = c ** (Decimal(1)/3)
msg = int(msg)

msghex = hex(msg)[2:]
msgstr = []
for i in range(0, len(msghex), 2):
    ch = msghex[i:i+2]
    ch = chr(int(ch, 16))
    msgstr.append(ch)

print(''.join(msgstr))
