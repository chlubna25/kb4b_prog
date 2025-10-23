import random

def hod_dvema_kostkami():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return a, b

hody = []
pocet_hodu = 0

while True:
    a, b = hod_dvema_kostkami()
    hody.append((a, b))
    pocet_hodu += 1
    if a == b:  
        break

print("Hody:")
for hod in hody:
    print(f"{hod[0]}, {hod[1]}")

print(f"Padla dvojice: {a}, {b}")
print(f"Počet hodů do dvojice: {pocet_hodu}")
