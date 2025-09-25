import random
import os

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
    hodnota_karet = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
    vysledek_hrac = 0
    vysledek_dealer = 0

    while balance > 0:
        clear_terminal
        print("Balance: ", balance)
        sazka = int(input("Zadejte sazku: "))
        if sazka <= balance:
            karty_hrac = []
            karty_dealer = []
            for i in 1:
                n = random.choice(karty)
                karty_hrac.append(n)
                m = random.choice(karty)
                karty_dealer.append(m)
            print("Vaše karty: ", karty_hrac)
            print("Karty dealera: ", karty_dealer[0], "*")

            while True:
                if input("Liznout [a/n]? ") == "a":
                    n = random.choice[karty]
                    karty_hrac.append(n)
                else:
                    break
            

#Hrac karty
            for karta in karty_hrac:
                if karta.isdigit():
                    vysledek_hrac += karta
                    karty_hrac.remove(karta)
                elif karta == "J" or karta == "Q" or karta == "K":
                    vysledek_hrac += 10
                    karty_hrac.remove(karta)
                elif karta == "A":
                    continue
            for eso in karty_hrac:
                if vysledek_hrac+11 <= 21:
                    vysledek_hrac += 11
                    karty_hrac.remove(eso)
                else:
                    vysledek_hrac += 1
                    karty_hrac.remove(eso)

#Dealer karty
            for karta in karty_dealer:
                if karta.isdigit():
                    vysledek_dealer += karta
                    karty_dealer.remove(karta)
                elif karta == "J" or karta == "Q" or karta == "K":
                    vysledek_dealer += 10
                    karty_dealer.remove(karta)
                elif karta == "A":
                    continue
            for eso in karty_dealer:
                if vysledek_dealer+11 <= 21:
                    vysledek_dealer += 11
                    karty_dealer.remove(eso)
                else:
                    vysledek_dealer += 1
                    karty_dealer.remove(eso)

#Vysledek
            if vysledek_hrac > vysledek_dealer and vysledek_hrac < 21:
                balance += sazka*multiplier
            elif vysledek_hrac > vysledek_dealer and vysledek_hrac == 21:
                balance += sazka*multiplier_bj