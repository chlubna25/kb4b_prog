def delitele(cislo):
    if cislo <= 0:
        print("Zadejte kladné číslo")
        return
    
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            print(i)

delitele(12)