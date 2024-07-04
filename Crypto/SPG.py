# HTB SPG YS4B

from hashlib import sha256
import string, random
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64decode

ALPHABET = string.ascii_letters + string.digits + '~!@#$%^&*'

password = "t*!zGnf#LKO~drVQc@n%oFFZyvhvGZq8zbfXKvE1#*R%uh*$M6c$zrxWedrAENFJB7xz0ps4zh94EwZOnVT9&h"

encrypted_flag = b64decode("GKLlVVw9uz/QzqKiBPAvdLA+QyRqyctsPJ/tx8Ac2hIUl8/kJaEvHthHUuwFDRCs")

def extract_MASTER_KEY(generated_password):

    delimiter = len(ALPHABET) // 2

    byte = ""
    
    master_key = ""

    for character in generated_password:

        index_character = ALPHABET.index(character)

        if index_character < delimiter:
            bit = 1
        else:
            bit = 0

        byte = str(bit) + byte

        if len(byte) == 8:

            byte_int = int(byte, 2)

            master_key = master_key + chr(byte_int)

            byte = ""

    if len(byte) != 0:
        byte_int = int(byte, 2)

        master_key = master_key + chr(byte_int)

    return bytearray(master_key, "utf-8")

MASTER_KEY = extract_MASTER_KEY(password)

encryption_key = sha256(MASTER_KEY).digest()
cipher = AES.new(encryption_key, AES.MODE_ECB)
flag = unpad(cipher.decrypt(encrypted_flag), 16)

print(flag)# HTB{D0_1t_Your$3lf:)}
