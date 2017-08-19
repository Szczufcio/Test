import random

a = random.sample(range(20), 12)
b = random.sample(range(20), 10)

print(set(x for x in a if x in b))


