import random

def hod_dvema_kostkami():
    kocki_a = random.randint(1, 6)
    kocki_b = random.randint(1, 6)
    return kocki_a, kocki_b

hody = 0

hodecki = int(input("Zmackni 1 pro hod kostkami: "))

if hodecki == 1:
    hody += 1
    print("tvoje hodekci pocet: ", hody)

else:
    print("nesprane pismenko")