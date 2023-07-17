import random

np = -1
while np< 0:
    np = int(input("How many players are playing?"))

names = []
player = 0
for i in range(0,np):
    player += 1
    names.append(input(f"Enter Player {player}'s name"))

print("The one who has to pay the bill is ", random.choice(names))