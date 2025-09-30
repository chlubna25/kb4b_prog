import random
import os
import time

def clear_terminal():
    # Check the operating system and execute the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')



def hod_minci(def_balance):
    balance = def_balance
    multiplier = 2
    while balance > 0:
        clear_terminal()
        print("Balance: ", balance)
        sazka = int(input("Zadejte sazku: "))
        padne = int(input("Padne (0/1): "))
        if sazka <= balance:
            padlo = random.randint(0, 1)
            print("Padla: ", padlo)
            if padlo == padne:
                vyhra = sazka*multiplier
                print("Vyhral jsi: ", vyhra, "CZK")
                balance += vyhra
            else:
                print("Prohral jsi: ", sazka, "CZK")
                balance -= sazka
        else:
            print("Zadal jsi neplatnou hodnotu sazky")

        if input("Hrat znovu? [a/n]: ") == "n":
            print("Odchazis s ", balance, "CZK")
            break

def blackjack(def_balance):
    balance = def_balance
    multiplier = 2
    multiplier_bj = 2.5
    karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    vysledek_hrac = 0
    vysledek_dealer = 0

    while balance > 0:
        clear_terminal()
        print("Balance: ", balance)
        print("------")
        sazka = int(input("Zadejte sazku: "))
        if sazka <= balance:
            karty_hrac = []
            karty_dealer = []
            for i in range(2):
                n = random.choice(karty)
                karty_hrac.append(n)
                m = random.choice(karty)
                karty_dealer.append(m)
            print("Vaše karty: ", karty_hrac)
            print(f"Karty dealera: {karty_dealer[0]}, *")
            print("------")

            while True:
                if input("Liznout [a/n]: ") == "a":
                    print()
                    n = random.choice(karty)
                    karty_hrac.append(n)
                    print(f"Líznul jsi: {n}!")
                    print()
                    print(f"Vase karty: {karta} "for karta in karty_hrac)
                    print(f"Karty dealera: [{karta}]"for karta in karty_hrac)
                else:
                    break
            

#Hrac karty
            dupe_karty_hrac = karty_hrac.copy()
            while dupe_karty_hrac:
                for i in range(len(dupe_karty_hrac)):
                    if dupe_karty_hrac[i] == 'J':
                        vysledek_hrac += 10
                    elif dupe_karty_hrac[i] == 'Q':
                        vysledek_hrac += 10
                    elif dupe_karty_hrac[i] == 'K':
                        vysledek_hrac += 10

                for i in range(len(dupe_karty_hrac)):
                    if dupe_karty_hrac[i] == 'A' and vysledek_hrac <= 10:
                        vysledek_hrac += 11
                    elif dupe_karty_hrac[i] == 'A' and vysledek_hrac > 10:
                        vysledek_hrac += 1
                    elif isinstance(dupe_karty_hrac[i], int):
                        vysledek_hrac += dupe_karty_hrac[i]
                #print("Dbg: vysledek_dealer: ", vysledek_hrac)
                dupe_karty_hrac.clear()
            #print("Dbg vysledek_hrac: ", vysledek_hrac)

#Dealer karty + dobirani
            dupe_karty_dealer = karty_dealer.copy()

            while vysledek_dealer < 17:
                print("Dbg: dealer karty: ", karty_dealer)
                for i in range(len(dupe_karty_dealer)):
                    if dupe_karty_dealer[i] == 'J':
                        vysledek_dealer += 10
                    elif dupe_karty_dealer[i] == 'Q':
                        vysledek_dealer += 10
                    elif dupe_karty_dealer[i] == 'K':
                        vysledek_dealer += 10

                for i in range(len(dupe_karty_dealer)):
                    if dupe_karty_dealer[i] == 'A' and vysledek_dealer <= 10:
                        vysledek_dealer += 11
                    elif dupe_karty_dealer[i] == 'A' and vysledek_dealer > 10:
                        vysledek_dealer += 1
                    elif isinstance(dupe_karty_dealer[i], int):
                        vysledek_dealer += dupe_karty_dealer[i]
                #print("Dbg: vysledek_dealer: ", vysledek_dealer)
                dupe_karty_dealer.clear()

                if vysledek_dealer < 17:
                    print()
                    n = random.choice(karty)
                    karty_dealer.append(n)
                    print(f"Dealer líznul: {n}!")
                    print()
                    print("Vase karty: ", karty_hrac)
                    print(f"Karty dealera: ".join({karty_dealer}))
                    dupe_karty_dealer.append(n)


#Vysledek
            if vysledek_hrac > vysledek_dealer and vysledek_hrac < 21 or vysledek_dealer > 21 and vysledek_hrac < 21:
                balance += sazka*multiplier
                print("Vyhral jsi: ", sazka*multiplier)
                time.sleep(3)
            elif vysledek_hrac > vysledek_dealer and vysledek_hrac == 21:
                balance += sazka*multiplier_bj
                print("Vyhral jsi: ", sazka*multiplier_bj)
                time.sleep(3)
            elif vysledek_hrac < vysledek_dealer or vysledek_hrac > 21:
                balance -= sazka
                print("Prohral jsi: ", sazka)
                time.sleep(3)
            elif vysledek_dealer == vysledek_hrac:
                print("Remiza! Sazka byla navracena")
                time.sleep(3)

blackjack(100)