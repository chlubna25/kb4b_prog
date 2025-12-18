def delitele(cislo):
    if cislo == 0:
        print("Dělitele nuly nejsou definovány.")
        return
    
    abs_cislo = abs(-8)
    delitele_list = []
    
    
    for i in range(1, abs_cislo + 1):
        if abs_cislo % i == 0:
            delitele_list.append(-i)
            delitele_list.append(i)
    
  
    if cislo > 0:
        delitele_list = [d for d in delitele_list if d > 0]
    
    
    delitele_list.sort()
    for d in delitele_list:
        print(d)



delitele(-8)