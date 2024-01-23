# Develop a simple dice rolling simulator. 
# Generate random numbers between 1 and 6 to simulate the roll of a six-sided die using the random module.

import random


def zar():
    return random.randint(1,6)

# zar=[1,2,3,4,5,6]
# x=random.choice(zar)
# x=random.randint(1,6) կարծում եմ սրանք էլ են տարբերակ
# x=random.choices(zar, k=1)

print(zar())


