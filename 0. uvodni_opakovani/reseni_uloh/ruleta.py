import random

def ruleta():
    vklad = 1000
    print("Minimálni sazka: 10 USD")

    while vklad >= 10:
        print("\nTvůj bank: ", vklad)
        sazka = int(input("Zadej sazku: "))

        if sazka < 10:
            print("Nesplnujes minimalni sazku (10 USD).")
            continue
        if sazka > vklad:
            print("Nemáš tolik peněz v banku.")
            continue

        volba = input("chces sazet na 'cervena', 'cerna' nebo cislo (0-36)? ").lower()

        cislo = random.randint(0, 36)
        barva = "cervena" if cislo % 2 == 0 and cislo != 0 else "cerna"

        print(f"\nPadlo cislo {cislo} ({barva}).")

        if volba.isdigit():
            if int(volba) == cislo:
                vyhra = sazka * 35
                print("Uhodl jsi cislo, vyhravas:", vyhra)
                vklad += vyhra
            else:
                print("Nevyslo to, prohravas:", sazka)
                vklad -= sazka
        elif volba in ["cervena", "cerna"]:
            if volba == barva:
                vyhra = sazka
                print("Uhodl jsi barvicku a vyhravas:", vyhra)
                vklad += vyhra
            else:
                print("nevyslo to, prohravas:", sazka)
                vklad -= sazka
        else:
            print("spatna volba. prohravas:", sazka)
            vklad -= sazka

        if vklad < 10:
            print("\nmas min jak minimalni sazku. hra konci.")                                      
            break

        pokracovat = input("\nChces hrat dal? (ano/ne): ").lower()
        if pokracovat != "ano":
            break

    print("\nKonec hry. Zustatek v banku:", vklad)

ruleta()
