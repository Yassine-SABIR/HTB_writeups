# HTB Quantum-Safe YS4B
import numpy as np

pubkey = np.array([[47, -77, -85],[-49, 78, 50],[57, -78, 99]])
invPubkey = np.linalg.inv(pubkey)

flag_enc = open("enc.txt", "r").read().split("\n")

def Encrypt(a, b, c, r):
    global pubkey
    v = np.array([a, b, c])

    return v @ pubkey + r

def Decrypt(v, r):
    global invPubkey
    return round(((v - r)@invPubkey)[0])

""" 
We have to determine the vector r = [r0, r1, r2]].

pubkey = [mi,j]
[ord(c), a, b] * pubkey + [r0, r1, r2]
    =   [r0 + ord(c)*m0,0 + a*m1,0 + b*m2,0 | r1 + ord(c)*m0,1 + a*m1,1 + b*m2,1 |r2 + ord(c)*m0,2 + a*m1,2 + b*m2,2]

x1 = ord(H) = 72 --> (-981, 1395, -1668)
x2 = ord(T) = 84 --> (6934, -10059, 4270)
x3 = ord(B) = 66 --> (3871, -5475, 3976)

(a1, b1), (a2, b2), and (a3, b3) are random numbers generated when calculating the encrypted values of "H", "T", and "B" in the "HTB" part of the flag.

r0 - 49*a1 + 57*b1 = -981 - 47*x1   = -4365
r1 + 78*a1 - 78*b1 = 1395 + 77*x1   = 6939
r2 + 50*a1 + 99*b1 = -1668 + 85*x1  = 4452

r0 - 49*a2 + 57*b2 = 6934 - 47*x2   = 2986
r1 + 78*a2 - 78*b2 = -10059 + 77*x2 = -3591
r2 + 50*a2 + 99*b2 = 4270 + 85*x2   = 11410

r0 - 49*a3 + 57*b3 = 3871 - 47*x3   = 769
r1 + 78*a3 - 78*b3 = -5475 + 77*x3  = -393
r2 + 50*a3 + 99*b3 = 3976 + 85*x3   = 9586

A = np.array([
    [1, 0, 0, -49, 57, 0, 0, 0, 0],
    [0, 1, 0, 78, -78, 0, 0, 0, 0],
    [0, 0, 1, 50, 99, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, -49, 57, 0, 0],
    [0, 1, 0, 0, 0, 78, -78, 0, 0],
    [0, 0, 1, 0, 0, 50, 99, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, -49, 57],
    [0, 1, 0, 0, 0, 0, 0, 78, -78],
    [0, 0, 1, 0, 0, 0, 0, 50, 99]
])

T = np.array([
    [-4365],
    [6939],
    [4452],
    [2986],
    [-3591],
    [11410],
    [769],
    [-393],
    [9586]
])

A * transpose([r0, r1, r2, a1, b1, a2, b2, a3]) = T --> transpose([r0, r1, r2, a1, b1, a2, b2, a3]) = Pseudo_inverse(A)*T

"""

A = np.array([
    [1, 0, 0, -49, 57, 0, 0, 0, 0],
    [0, 1, 0, 78, -78, 0, 0, 0, 0],
    [0, 0, 1, 50, 99, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, -49, 57, 0, 0],
    [0, 1, 0, 0, 0, 78, -78, 0, 0],
    [0, 0, 1, 0, 0, 50, 99, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, -49, 57],
    [0, 1, 0, 0, 0, 0, 0, 78, -78],
    [0, 0, 1, 0, 0, 0, 0, 50, 99]
])

T = np.array([
    [-4365],
    [6939],
    [4452],
    [2986],
    [-3591],
    [11410],
    [769],
    [-393],
    [9586]
])

Z = np.linalg.pinv(A) @ T

r =np.array([Z[i][0] for i in range(3)])

Flag = ""

for v in flag_enc:
    vec = np.array([int(l) for l in v[1:-1].split(", ")])
    Flag += chr(Decrypt(vec, r))

print(Flag) # HTB{D0_1t_Your$3lf:)}
