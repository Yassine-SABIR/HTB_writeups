# HTB Deterministic YS4B


file = open("deterministic.txt", "r")

content = file.read().split("\n")

data = {}

begin = "69420"
end = "999"

for line in content[2:]:

    l = line.split(" ")

    data[l[0]] = l[1:]

list_flag = []

state = data[begin]

while state[1] != end:
    list_flag.append(state[0])
    state = data[state[1]]

list_flag.append(state[0])

key = ord("}") ^ 20

flag = "".join([chr(int(l) ^ key) for l in list_flag])

print(flag)
"""
    You managed to pass through all the correct states of the automata and reach the final state. Many people tried to do this by hand and failed.. Only the real ones managed to reach the final state. You also found the secret key to decrypt the message. You are truly worthy!! You should be rewarded with this gift! The passphrase to unlock the door is: HTB{4ut0M4t4_4r3_FuUuN_4nD_N0t_D1fF1cUlt!!}
"""