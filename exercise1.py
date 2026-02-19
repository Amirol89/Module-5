import random

num_dice = int(input("how many dic to roll? "))
total= 0
for i in range(num_dice):
    roll = random.randint(1,6)
    total = total + roll
print("sum of the dict rolls: ", total)