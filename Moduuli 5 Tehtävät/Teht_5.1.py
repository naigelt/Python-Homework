
from random import randint
cubes = int(input("Give the number of cubes: "))
sum = 0
for cubes in range(cubes):
    x = randint(1, 7)
    sum += x

print(f"Total sum is {sum}")


