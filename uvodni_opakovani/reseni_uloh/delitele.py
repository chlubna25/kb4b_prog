def vypis_delitele(n):
    #vstup: cele kladne cislo

    for i in range(1, n+1):
        if n % i == 0:
            print(i)

vypis_delitele(12)

def vykresleni_schodu(n, znak):
    #vstup: cele kladne cislo + znak

    for i in range(n+1):
        print(znak*i)

vykresleni_schodu(5, "h")

