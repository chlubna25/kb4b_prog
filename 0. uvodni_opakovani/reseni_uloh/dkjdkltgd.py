import random

penize = 100
print("Tvuj pocet penez: ", penize)
sazka = int(input("Zadej vysi sazky: "))

while sazka > penize:
    print("Tolik penez nemuzes vsadit.")
    break

volba = int(input("Chces sazet na pannu (0), nebo orla (1)? "))

strana = random.randint(0, 1)

if volba == strana:
    vyhra = sazka * 2
    penize += vyhra 
    print("Vyhral jsi, tvoje penize: ", penize)

else:
    penize -= sazka
    print("Prohral jsi, tvoje penize: ", penize)