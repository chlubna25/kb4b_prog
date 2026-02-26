import random

n = random.randint(1, 10)

print("Pocet prikazu pro robota: ", n)

souradnice_X = 0
souradnice_Y = 0



for i in range(n):
    prikaz = random.choice(["W", "S", "A", "D"])

    if prikaz == "W":
        souradnice_Y += 1
    elif prikaz == "S":
        souradnice_Y -= 1
    elif prikaz == "A":
        souradnice_X -= 1
    elif prikaz == "D":
        souradnice_X += 1
    
print(f"Konecne souradnice robota jsou: ({souradnice_X}, {souradnice_Y})")