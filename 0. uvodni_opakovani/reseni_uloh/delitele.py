def vypis_delitele(n):
    for i in range (1, n+1):
        if n % i == 0:
            print(i)

vypis_delitele(12)