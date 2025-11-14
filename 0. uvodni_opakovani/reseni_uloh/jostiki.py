import random

def hod_dvema_kostkami():
    return random.randint(1, 6), random.randint(1, 6)

def spaten_dvojice():
    hody = []
    while True:
        a, b = hod_dvema_kostkami()
        hody.append((a, b))
        if a == b:
            break

    print("tvoje hodekci: ")
    for a, b in hody:
        print(f"{a}, {b}")
    posledni = hody[-1]
    print(f"dvojicka padla: {posledni[0]}, {posledni[1]}")
    print(f"tvoje hodecki pocet: {len(hody)}")

if __name__ == "__main__":
    spaten_dvojice()
