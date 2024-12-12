from random import random, seed

tot, hit = 0, 0
seed(34)
for i in range(100000):
    x = random() * 2 - 1
    y = random() * 2 - 1
    if x * x + y * y < 1:
        hit += 1
    tot += 1

print(hit / tot)
