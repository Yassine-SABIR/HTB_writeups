# HTB xorxorxor YS4B

encryptedFlag = '134af6e1297bc4a96f6a87fe046684e8047084ee046d84c5282dd7ef292dc9'

first_4_bytes_flag = [ord(char) for char in "HTB{"]

key = []

for i in range(len(first_4_bytes_flag)):
    key += [first_4_bytes_flag[i] ^ int(encryptedFlag[2*i: 2*(i+1)], 16)]

encryptedFlagList = []

for i in range(0, len(encryptedFlag), 2):
    encryptedFlagList += [int(encryptedFlag[i: i+2], 16)]

def decrypt(xored, key):
    data = ""
    for i in range(len(xored)):
        data += chr(xored[i] ^ key[i % len(key)])
    return data

print(decrypt(encryptedFlagList, key)) # HTB{rep34t3d_x0r_n0t_s0_s3cur3}

