import random
import os
import time

#AI funkce na vyčištění terminálu
def clear_terminal():
    # Check the operating system and execute the appropriate command
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')


#def_balance = default balance, nema to byt funkce!!!
def blackjack(def_balance):
    balance = def_balance
    multiplier = 1
    multiplier_bj = 1.5
    karty = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
    
    while balance > 0:
        clear_terminal()
        print("Zůstatek: ", balance)
        print("------")
        
        sazka = int(input("Zadejte sázku: "))
        if sazka <= balance and sazka > 0:
            karty_hrac = []
            karty_dealer = []
            for _ in range(2):
                karty_hrac.append(random.choice(karty))
                karty_dealer.append(random.choice(karty))
            
#AI pro zprehledneni vypisu
            print("\nVaše karty: ", ', '.join(str(karta) for karta in karty_hrac), 
                  f"(Hodnota: {calculate_score(karty_hrac)})")
            print(f"Karty dealera: {karty_dealer[0]}, *")
            print("------")

            while True:
                akce = input("Hit, Stand or Double Down [h/s/d]: ").lower()
                if akce == "h":
                    clear_terminal()
                    print()
                    n = random.choice(karty)
                    karty_hrac.append(n)
                    print(f"Líznul jsi: {n}!")
                    print()
                    print("Vaše karty: ", ', '.join(str(karta) for karta in karty_hrac), 
                          f"(Hodnota: {calculate_score(karty_hrac)})")
                    print(f"Karty dealera: {karty_dealer[0]}, *")
                    print("------")
                    
                    if calculate_score(karty_hrac) > 21:
                        print("Prohral jsi: Překročil jsi 21!")
                        balance -= sazka
                        time.sleep(3)
                        break
                elif akce == "d":
                    if balance < sazka * 2:
                        print("Nemáš dostatek zůstatku pro Double Down!")
                        time.sleep(2)
                        clear_terminal()
                        print()
                        print("Vaše karty: ", ', '.join(str(karta) for karta in karty_hrac), 
                              f"(Hodnota: {calculate_score(karty_hrac)})")
                        print(f"Karty dealera: {karty_dealer[0]}, *")
                        print("------")
                        if calculate_score(karty_hrac) > 21:
                            print("Prohral jsi: Překročil jsi 21!")
                            balance -= sazka
                            time.sleep(3)
                            break
                        continue
                    clear_terminal()
                    sazka, karty_hrac = double_down(sazka, karty_hrac)
                    print()
                    print("Vaše karty: ", ', '.join(str(karta) for karta in karty_hrac), 
                          f"(Hodnota: {calculate_score(karty_hrac)})")
                    print(f"Karty dealera: {karty_dealer[0]}, *")
                    print("------")
                    break
                else:
                    break
            
            #Dealer lize
            while calculate_score(karty_dealer) < 17:
                time.sleep(2)
                n = random.choice(karty)
                karty_dealer.append(n)
                print(f"Dealer líznul: {n}!")
                print()
                print("Vaše karty: ", ', '.join(str(karta) for karta in karty_hrac), 
                      f"(Hodnota: {calculate_score(karty_hrac)})")
                print(f"Karty dealera: {', '.join(str(karta) for karta in karty_dealer)} (Hodnota: {calculate_score(karty_dealer)})")
                print("------")
                time.sleep(1)

            #Vysledek
            print(f"Vaše karty: {', '.join(str(karta) for karta in karty_hrac)} (Hodnota: {calculate_score(karty_hrac)})")
            print(f"Karty dealera: {', '.join(str(karta) for karta in karty_dealer)} (Hodnota: {calculate_score(karty_dealer)})")
            print("------")

            if calculate_score(karty_hrac) > calculate_score(karty_dealer) and calculate_score(karty_hrac) < 21 or calculate_score(karty_hrac) < 21 and calculate_score(karty_dealer) > 21:
                balance += sazka * multiplier
                print("Vyhral jsi: ", sazka * multiplier)
            elif calculate_score(karty_hrac) == 21:
                balance += sazka * multiplier_bj
                print("Vyhral jsi: ", sazka * multiplier_bj)
            elif calculate_score(karty_hrac) < calculate_score(karty_dealer) or calculate_score(karty_hrac) > 21:
                balance -= sazka
                print("Prohral jsi: ", sazka)
            elif calculate_score(karty_dealer) == calculate_score(karty_hrac):
                print("Remiza! Sazka byla navracena")
            time.sleep(3)

def calculate_score(karty):
    score = 0
    for karta in karty:
        if karta in ['J', 'Q', 'K']:
            score += 10
        elif karta == 'A':
            score += 11 if score <= 10 else 1
        else:
            score += karta
    return score

def double_down(sazka, karty_hrac):
    sazka *= 2
    n = random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"])
    karty_hrac.append(n)
    print(f"Líznul jsi: {n}!")
    return sazka, karty_hrac

        

blackjack(100)
