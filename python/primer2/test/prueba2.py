import random
def numero():
    horasA = 0
    minutosA = 0
    for i in range(6):
        horasA  = random.randint(-24, 24)
        minutosA = random.randint(-60, 60)