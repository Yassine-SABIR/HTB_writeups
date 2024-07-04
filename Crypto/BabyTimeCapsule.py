# HTB Baby Time Capsule YS4B
from pwn import *

s = remote('94.237.62.195', 30156)
time_capsules = []
pubkey_n = []
numberOfTimes = 3

for i in range(numberOfTimes):
    s.sendline(b'Y')
    data = s.recvline()
    data = str(data).split("\\n")[0]
    data = data.split('{"time_capsule": "')[1]
    time_capsules.append(int(data.split('", "pubkey": ["')[0], 16))
    data = data.split('", "pubkey": ["')[1]
    pubkey_n.append(int(data.split('"')[0], 16))
s.close()

result = 0
ProductNs = 1

for i in range(numberOfTimes):
    ProductNs *= pubkey_n[i]
    
    mi = 1

    for j in range(numberOfTimes):
        if j != i:
            mi *= pubkey_n[j]
    
    try:
        yi = pow(mi, -1, pubkey_n[i])
    except ValueError:
        pass
    result += time_capsules[i] * yi * mi

result = result % ProductNs
lower_boundary = 0
upper_boundary = result
e = 5


while lower_boundary < upper_boundary:
    mediane = (lower_boundary + upper_boundary) // 2

    if mediane**e < result:
        lower_boundary = mediane
    else:
        if mediane**e > result:
            upper_boundary = mediane
        else:
            break

mediane = hex(mediane)[2:]

flag = ""

for i in range(0, len(mediane), 2):
    flag += chr(int(mediane[i:i+2], 16))

print(flag) # HTB{D0_1t_Your$3lf:)}
