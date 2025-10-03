import random 

strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
preference = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]


ucast = random.randint(50, 80)


vysledky = random.choices(strany, weights=preference, k=ucast)
print(vysledky)
print(f"Volilo {ucast} % lidí.")

print(random.random())  
print(random.randint(1, 10)) 
print(random.choice(strany))  
print(random.choices(strany, weights=preference, k=10)) 

random.shuffle(strany)  
print(strany)



