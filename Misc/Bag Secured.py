#HTB Bag Secured YS4B

import pwn

host = "83.136.253.110"
port = 49619

clt = pwn.connect(host, port)

s = 100

values = [3, 9, 4, 1]
weights = [6, 7, 5, 2]
C = 14
N = 4

def knapSack(W, wt, val, n):
    #https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
    if n == 0 or W == 0:
        return 0

    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    else:
        return max(
            val[n-1] + knapSack(
                W-wt[n-1], wt, val, n-1),
            knapSack(W, wt, val, n-1))

for i in range(1, s+1):
    clt.recvuntil(b"/100\n")

    data = clt.recvuntil(b"\n")

    print(f"Test = {i}/100", end="\r", flush=True)

    N, C = data.decode("utf-8").split("\n")[0].split(" ")[:2]
    N, C = int(N), int(C)

    values = []
    weights = []

    for p in range(N):
        data = clt.recvuntil(b"\n")
        w_i, v_i = data.decode("utf-8").split("\n")[0].split(" ")[:2]
        w_i, v_i = int(w_i), int(v_i)
        values.append(v_i)
        weights.append(w_i)

    max_val = knapSack(C, weights, values, N)
    clt.sendline(bytes(str(max_val), "utf-8"))
data = clt.recvline()
print(data) # b'You filled your bag with amazing weapons, your adventure will be a piece of cake now. Here is your reward: HTB{D0_1t_Your$3lf:)}\n'