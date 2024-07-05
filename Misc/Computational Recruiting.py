# HTB Computational Recruiting YS4B

import pandas as pd
import pwn

file  = open("data.txt", "r")

data = file.read()

data_lines = data.split("\n")[4:-1]

filtered_data = [line.split(" ") for line in data_lines]

file2 = open("filtered_data.csv", "w")

file2.write("First Name;Last Name;Health;Agility;Charisma;Knowledge;Energy;Resourcefulness\n")

for line in filtered_data:

    first = True

    for data_ in line:
        if len(data_) > 0:
            if first:
                file2.write(data_)
                first = False
            
            else:
                file2.write(";" + data_)

    file2.write("\n")

file2.close()

health_weight = 0.2
agility_weight = 0.3
charisma_weight = 0.1
knowledge_weight = 0.05
energy_weight = 0.05
resourcefulness_weight = 0.3

df = pd.read_csv("filtered_data.csv", sep=";")

df["Health"] = round(6 * (df["Health"] * health_weight)) + 10
df["Agility"] = round(6 * (df["Agility"] * agility_weight)) + 10
df["Charisma"] = round(6 * (df["Charisma"] * charisma_weight)) + 10
df["Knowledge"] = round(6 * (df["Knowledge"] * knowledge_weight)) + 10
df["Energy"] = round(6 * (df["Energy"] * energy_weight)) + 10
df["Resourcefulness"] = round(6 * (df["Resourcefulness"] * resourcefulness_weight)) + 10

df["Overall_value"] = round(5 * (0.18 * df["Health"] + 0.20 * df["Agility"] + 0.21 * df["Charisma"] + 0.08 * df["Knowledge"] + 0.17 * df["Energy"] + 0.16 * df["Resourcefulness"]))

df = df.sort_values("Overall_value", ascending=False)

desired_df = df[:14]

list_condidates = ""

for index, condidate in desired_df.iterrows():
    list_condidates += condidate["First Name"] + " " + condidate["Last Name"] + " - " + str(int(condidate["Overall_value"])) + ", "

list_condidates = list_condidates[:-2]

host = "94.237.55.62"
port = 59967

s = pwn.connect(host, port)

data = s.recvuntil(b"\n>")

print(data)

s.sendline(bytes(list_condidates, "utf-8"))

while True:
    data = s.recv()
    print(data) # HTB{D0_1t_Your$3lf:)}