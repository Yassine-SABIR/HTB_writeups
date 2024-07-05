# HTB A Nightmare On Math Street YS4B

import pwn

host = "94.237.48.147"
port = 36327

def equationChanger(equation):

    equation = "(" + equation.replace("*", ")*(") + ")"

    return equation

s = pwn.connect(host, port)

for index in range(500):

    data = s.recvuntil(b" = ?")

    equation = data.split(b"]: ")[1].split(b" = ")[0].decode("utf-8")

    equation = equationChanger(equation)

    result = bytes(str(eval(equation)), "utf-8")

    s.sendline(result)

    print(f"{index} : {equation} = {result}")


while True:
    data = s.recvline()
    print(data) # HTB{D0_1t_Your$3lf:)}

