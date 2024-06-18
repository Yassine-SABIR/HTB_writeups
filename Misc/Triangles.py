# HTB Triangles YS4B

import csv
import math
import random

arr = []
with open('grid.csv') as grid:
    for x in csv.reader(grid):
        arr.append(x)
        pass

dic_arr = {}

for i in range(100):
    for j in range(100):
        dic_arr[f"{i}::{j}"] = arr[i][j]

def getDistance(x,y,x2,y2):
    return math.sqrt(math.pow(x - x2,2) + math.pow(y - y2,2))

"""def cap(num):
    if num > 99:
        return 99
    if num < 0:
        return 0
    return num"""

def piDiscover(val):
    return [[int(i.split("::")[0]), int(i.split("::")[1])] for i in dic_arr.keys() if dic_arr[i] == val]

"""def createCoords(x,y):
    x1 = random.randint(-7,7)
    y1 = random.randint(-7,7)
    x2 = random.randint(-7,7)
    y2 = random.randint(-7,7)
    x3 = random.randint(-7,7)
    y3 = random.randint(-7,7)

    p1 = [cap(x1 + x), cap(y1 + y)]
    p2 = [cap(x2 + x), cap(y2 + y)]
    p3 = [cap(x3 + x), cap(y3 + y)]

    val1 = arr[p1[0]][p1[1]]
    val2 = arr[p2[0]][p2[1]]
    val3 = arr[p3[0]][p3[1]]

    distances = [(val1,getDistance(x,y,p1[0], p1[1])),(val2,getDistance(x,y,p2[0], p2[1])),(val3,getDistance(x,y,p3[0], p3[1])),(f"{val1}{val2}",getDistance(p1[0], p1[1],p2[0], p2[1])),(f"{val2}{val3}",getDistance(p2[0], p2[1],p3[0], p3[1])),(f"{val1}{val3}",getDistance(p1[0], p1[1],p3[0], p3[1]))]
    return distances"""

def getPis(distance_list):
    assert len(distance_list) == 6

    val1, val2, val3 = distance_list[0][0], distance_list[1][0], distance_list[2][0] 
    distp1p2, distp2p3, distp1p3 = distance_list[3][1], distance_list[4][1], distance_list[5][1] 

    possible_p1, possible_p2, possible_p3 = piDiscover(val1), piDiscover(val2), piDiscover(val3)

    for p1 in possible_p1:
        for p2 in possible_p2:

            if getDistance(p1[0], p1[1],p2[0], p2[1]) != distp1p2:
                continue

            for p3 in possible_p3:
                if getDistance(p1[0], p1[1],p3[0], p3[1]) != distp1p3 or getDistance(p2[0], p2[1],p3[0], p3[1]) != distp2p3:
                    continue

                return p1, p2, p3
            
def solve(a, b, c):
    #solve the system : ax² + bx + c = 0

    descriminant = b**2 - 4*a*c

    if descriminant >= 0:
        sqrt_delta = math.sqrt(descriminant)

        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)

        return x1, x2


def inverseCreateCoords(p1, p2, p3, d1, d2, d3):

    if p1[1] == p2[1]:
        if p1[1] != p3[1]:
            p2, p3 = p3, p2
            d2, d3 = d3, d2
        
        if p2[1] != p3[1]:
            p3, p1 = p1, p3
            d3, d1 = d1, d3

    alpha = (p2[0] - p1[0]) / (p1[1] - p2[1])
    beta = (d2**2 - d1**2 + p1[1]**2 + p1[0]**2 - p2[0]**2 - p2[1]**2) / (2*(p1[1] - p2[1])) 

    # y = alpha * x + beta

    a = 1 + alpha ** 2
    b = 2*(alpha*(beta - p3[1]) - p3[0])
    c = p3[0]**2 + (beta - p3[1])**2 - d3**2

    # ax² + bx + c = 0

    x1, x2 = round(solve(a, b, c)[0]), round(solve(a, b, c)[1])
    y1, y2 = round(alpha * x1 + beta), round(alpha * x2 + beta)

    if getDistance(x1,y1,p1[0], p1[1]) == d1 and getDistance(x1,y1,p2[0], p2[1]) == d2 and getDistance(x1,y1,p3[0], p3[1]) == d3:
        return x1, y1

    if getDistance(x2,y2,p1[0], p1[1]) == d1 and getDistance(x2,y2,p2[0], p2[1]) == d2 and getDistance(x2,y2,p3[0], p3[1]) == d3:
        return x2, y2


def getXY(distance_list):
    assert len(distance_list) == 6

    dist1, dist2, dist3 = distance_list[0][1], distance_list[1][1], distance_list[2][1]

    p1, p2, p3 = getPis(distance_list)

    x, y = inverseCreateCoords(p1, p2, p3, dist1, dist2, dist3)

    return x, y

distance_list = []
flag = ""

with open('out.csv') as grid:
    for x in csv.reader(grid):
        distance_list.append([x[0], float(x[1])])

        if len(distance_list) == 6:
            x, y = getXY(distance_list)
            flag += arr[x][y]
            distance_list = []
        pass

print(flag) # HTB{sQU@r3s_R_4_N3rD$}





