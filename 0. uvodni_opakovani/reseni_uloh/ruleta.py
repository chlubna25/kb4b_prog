import random

def ruleta():
    # začátek hry
    vklad = int(input("Vlož peníze do banku: "))
    print("Minimální sázka: 10 USD")

    while vklad >= 10:
        print("\nTvůj bank: ", vklad)
        sazka = int(input("Zadej sázku: "))

        if sazka < 10:
            print("Nesplňuješ minimální sázku (10 USD).")
            continue
        if sazka > vklad:
            print("Nemáš tolik peněz v banku.")
            continue

        # typ sázení
        volba = input("Chceš sázet na 'cervena', 'cerna' nebo číslo (0-36)? ").lower()

        # roztočení rulety
        cislo = random.randint(0, 36)
        barva = "cervena" if cislo % 2 == 0 and cislo != 0 else "cerna"

        print(f"\nPadlo číslo {cislo} ({barva}).")

        # vyhodnocení
        if volba.isdigit():  # hráč vsadil číslo
            if int(volba) == cislo:
                vyhra = sazka * 35
                print("Gratuluji! Uhodl jsi číslo a vyhráváš:", vyhra)
                vklad += vyhra
            else:
                print("Nevyšlo to, prohráváš:", sazka)
                vklad -= sazka
        elif volba in ["cervena", "cerna"]:
            if volba == barva:
                vyhra = sazka
                print("Gratuluji! Uhodl jsi barvu a vyhráváš:", vyhra)
                vklad += vyhra
            else:
                print("Nevyšlo to, prohráváš:", sazka)
                vklad -= sazka
        else:
            print("Neplatná volba. Prohráváš sázku:", sazka)
            vklad -= sazka

        # kontrola konce hry
        if vklad < 10:
            print("\nMáš méně než minimální sázku. Hra končí.")
            break

        pokracovat = input("\nChceš hrát dál? (ano/ne): ").lower()
        if pokracovat != "ano":
            break

    print("\nKonec hry. Zůstatek v banku:", vklad)

# spuštění hry
ruleta()
