# 3. Please write a program to output a random number,
# which is divisible by 5 and 7, between 0 and 10 inclusive using random module and list comprehension.

import random

listOfComprehension = [((x % 5) % 7) for x in range(int(random.uniform(0, 10))) if x != 0]

print(listOfComprehension)
