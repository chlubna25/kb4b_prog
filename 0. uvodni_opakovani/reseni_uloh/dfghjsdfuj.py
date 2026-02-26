import random

def generuj_priklad():
    cislo1 = random.randint(0, 10)
    op = random.choice(['+', '-', '*',])
    cislo2 = random.randint(0, 10)

    print(f"{cislo1} {op} {cislo2} = ")
    vstup = int(input())

    if op == '+':
        spravne = cislo1 + cislo2
    elif op == '-':
        spravne = cislo1 - cislo2
    else:
        spravne = cislo1 * cislo2

    return vstup == spravne

poctet_prikladu = 3
body = 0

for i in range(3):
    if generuj_priklad() == True:
        body += 1

print(f"Vyresil jsi {body}/{poctet_prikladu} spravne.")