import random

Inside = 0
i = 0
n = int(input("Give the number of points: "))

while i <= n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        Inside += 1
    i += 1

pi = 4 * Inside / n

print(f"Pii is approximately: {pi}")