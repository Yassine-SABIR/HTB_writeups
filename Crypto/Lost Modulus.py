# HTB Lost Modulus yabir
from Crypto.Util.number import getPrime, long_to_bytes, inverse

e = 3
flag_hex = "05c61636499a82088bf4388203a93e67bf046f8c49f62857681ec9aaaa40b4772933e0abc83e938c84ff8e67e5ad85bd6eca167585b0cc03eb1333b1b1462d9d7c25f44e53bcb568f0f05219c0147f7dc3cbad45dec2f34f03bcadcbba866dd0c566035c8122d68255ada7d18954ad604965"

flag = int(flag_hex, 16)

"""
    e is too small, so probably : pow(plaintext, e, n) = plaintext**e
"""
# Dichotomic search

top = flag
bottom = 0
median = (top + bottom)//2

while median ** 3 != flag:

    if median ** 3 > flag:
        top = median
        median = (top + bottom)//2

    else:
        bottom = median
        median = (top + bottom)//2

hex_plainTxt = long_to_bytes(median).hex()

plainText = ""

for i in range(0, len(hex_plainTxt), 2):
    plainText += chr(int(hex_plainTxt[i:i+2], 16))

print(plainText) # HTB{n3v3r_us3_sm4ll_3xp0n3n7s_f0r_rs4}

