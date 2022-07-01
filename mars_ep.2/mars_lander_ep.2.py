import sys

surface_n = int(input())
surface = []
indexLand = 0
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]
    surface.append((land_x, land_y))
    if i > 0 and surface[i - 1][1] == land_y:
        indexLand = i - 1

targetX = (surface[indexLand][0] + surface[indexLand + 1][0]) / 2

while True:
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]

    altitude = y
    for i in range(surface_n):
        if x < surface[i][0] < targetX or x > surface[i][0] > targetX:
            altitude = min(y - surface[i][1], altitude)

    dist = abs(x - (surface[indexLand][0] + surface[indexLand + 1][0]) / 2)

    if x > surface[indexLand][0] and x < surface[indexLand + 1][0]:
        if y - surface[indexLand][1] < 500:
            rot = 0
        elif h_speed > 0:
            rot = 30 if h_speed > 30 else 15
        elif h_speed < 0:
            rot = -30 if h_speed < -30 else -15
        else:
            rot = 0
    elif x < surface[indexLand][0]:
        if surface[indexLand][0] - x > 1000:
            vit = 40
        else:
            vit = 18
        if h_speed < vit:
            rot = -30
        elif h_speed > vit + 3:
            rot = 30
        else:
            rot = 0
    else:
        if x - surface[indexLand + 1][0] > 1000:
            vit = -40
        else:
            vit = -18
        if h_speed > vit:
            rot = 30
        elif h_speed < vit - 3:
            rot = -30
        else:
            rot = 0

    if v_speed < -30:
        pow = 4
    elif y - surface[indexLand][1] < 1000:
        hmin = 300 if dist > 500 else 0
        if y - surface[indexLand][1] < hmin or v_speed < -5:
            pow = 4
        else:
            pow = 3
    elif rot != 0 and rot * rotate >= 0:
        pow = 4
    else:
        pow = 0

    if altitude < 200:
        rot, pow = 8 if rot > 0 else -8 if rot < 0 else 0, 4

    print(rot, pow)
