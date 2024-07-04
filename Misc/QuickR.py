# HTB QuickR YS4B

import pwn
import cv2
import numpy as np

dict = {b"\x1b[0m\x1b[41m" : 0, b"\x1b[0m\x1b[7m":255}

def data2img(data_list):
    global dict
    img = []

    for data in data_list:
        data_ = data.split(b"  ")
        row = []

        for pixel in data_:
            if pixel in dict.keys():
                row += [dict[pixel]]

        img += [row]

    return np.array(img, np.uint8)



host = "94.237.59.91"
port = 40825

s = pwn.connect(host, port)

all_data = []

data = s.recvline()
all_data.append(data)

while b"[+]" not in data:

    all_data.append(data)

    data = s.recvline()

img = data2img(all_data[14:-2])

data = s.recvuntil(b"string: ")

qcd = cv2.QRCodeDetector()

retval, decoded_info, points, straight_qrcode = qcd.detectAndDecodeMulti(img)
result = bytes(str(eval(decoded_info[0].split(" = ")[0].replace("x", "*"))), "utf-8")

s.sendline(result)

data = s.recv()

print(data) # b'\x1b[1m\x1b[92m[+] \x1b[0mCongratulations! Here is your flag: HTB{D0_1t_Your$3lf:)}'







