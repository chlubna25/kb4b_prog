import random

def spin_roulette():
    number = random.randint(0, 36)
    if number == 0:
        color = "zelená"
    elif number in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]:
        color = "červená"
    else:
        color = "černá"
    return number, color

def place_bet(balance):
    print(f"Váš aktuální zůstatek: {balance} Kč")
    print("Možnosti sázení: 1) Číslo (0-36), 2) Barva (červená/černá)")
    choice = input("Vyberte typ sázky (1 nebo 2): ")

    try:
        bet_amount = int(input("Zadejte částku sázky (Kč): "))
        if bet_amount <= 0 or bet_amount > balance:
            print("Neplatná částka sázky nebo nedostatečný zůstatek!")
            return None, None, 0
    except ValueError:
        print("Zadejte platnou číselnou částku!")
        return None, None, 0

    if choice == "1":
        try:
            bet = int(input("Vsadit na číslo (0-36): "))
            if bet < 0 or bet > 36:
                print("Neplatné číslo!")
                return None, None, 0
            return bet, "number", bet_amount
        except ValueError:
            print("Zadejte platné číslo!")
            return None, None, 0
    elif choice == "2":
        bet = input("Vsadit na barvu (červená/černá): ").lower()
        if bet not in ["červená", "černá"]:
            print("Neplatná barva!")
            return None, None, 0
        return bet, "color", bet_amount
    else:
        print("Neplatná volba!")
        return None, None, 0

def evaluate_bet(bet, bet_type, bet_amount, number, color):
    """Vyhodnotí sázku, vrátí výsledek a aktualizovanou částku."""
    if bet is None:
        return "Sázka zrušena.", 0
    
    if bet_type == "number":
        if bet == number:
            win = bet_amount * 35  
            return f"Vyhráli jste! Padlo číslo {number}. Výhra: {win} Kč.", win
        else:
            return f"Prohráli jste. Padlo číslo {number}.", -bet_amount
    elif bet_type == "color":
        if bet == color:
            win = bet_amount  
            return f"Vyhráli jste! Padla barva {color}. Výhra: {win} Kč.", win
        else:
            return f"Prohráli jste. Padla barva {color}.", -bet_amount

def main():
    balance = 1000  
    print("Vítejte v ruletě! Začínáte s 1000 Kč.")
    
    while True:
        if balance <= 0:
            print("Nemáte dostatek peněz na další hru. Konec hry!")
            break

        bet, bet_type, bet_amount = place_bet(balance)
        if bet is None:
            continue
        
        number, color = spin_roulette()
        print(f"Výsledek: Číslo {number}, Barva: {color}")
        result, winnings = evaluate_bet(bet, bet_type, bet_amount, number, color)
        balance += winnings
        print(result)
        print(f"Nový zůstatek: {balance} Kč")
        
        play_again = input("Chcete hrát znovu? (ano/ne): ").lower()
        if play_again != "ano":
            break
    
    print(f"Děkujeme za hru! Konečný zůstatek: {balance} Kč")

if __name__ == "__main__":
    main()