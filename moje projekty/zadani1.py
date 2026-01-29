def schody(vyska, znak):
 
    if vyska <= 0:
        print("Výška musí být kladné číslo.")
        return
    
    for i in range(1, vyska + 1):
        print(znak * i)


vyska = int(input("Zadejte výšku: "))
znak = input("Zadejte znak: ")
schody(vyska, znak)