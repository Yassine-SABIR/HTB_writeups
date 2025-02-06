# HTB Android-in-the-Middle YS4B

import pwn
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib
from Crypto.Util.Padding import pad

host = "94.237.59.180"
port = 53358

p = 0x509efab16c5e2772fa00fc180766b6e62c09bdbd65637793c70b6094f6a7bb8189172685d2bddf87564fe2a6bc596ce28867fd7bbc300fd241b8e3348df6a0b076a0b438824517e0a87c38946fa69511f4201505fca11bc08f257e7a4bb009b4f16b34b3c15ec63c55a9dac306f4daa6f4e8b31ae700eba47766d0d907e2b9633a957f19398151111a879563cbe719ddb4a4078dd4ba42ebbf15203d75a4ed3dcd126cb86937222d2ee8bddc973df44435f3f9335f062b7b68c3da300e88bf1013847af1203402a3147b6f7ddab422d29d56fc7dcb8ad7297b04ccc52f7bc5fdd90bf9e36d01902e0e16aa4c387294c1605c6859b40dad12ae28fdfd3250a2e9
g = 2

s = pwn.connect(host, port)

M = 1

shared_secret = 1

sequence = b"Initialization Sequence - Code 0"

def encrypt(plaintext, shared_secret):
    key = hashlib.md5(long_to_bytes(shared_secret)).digest()
    cipher = AES.new(key, AES.MODE_ECB)
    encrypted = cipher.encrypt(plaintext)
    return encrypted

encrypt_sequence = encrypt(sequence, shared_secret)

data_to_be_sent = encrypt_sequence.hex()

s.recvuntil(b"Enter The Public Key of The Memory: ")
s.sendline("1".encode())

s.recvuntil(b"Enter The Encrypted Initialization Sequence: ")
s.sendline(data_to_be_sent.encode())

data = s.recvuntil(b"}")

flag = b"HTB{" + data.split(b"HTB{")[1]
print(f"flag = {flag}")# HTB{D0_1t_Your$3lf:)}



