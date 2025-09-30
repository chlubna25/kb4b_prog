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