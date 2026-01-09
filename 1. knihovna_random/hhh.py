import random

def vypis_statistiky():
    a = random.randint(-10, 24)
    
    return a

teploty = []


a = vypis_statistiky()
teploty.append((a))
    

  

prumer = sum(teploty) / len(teploty)
print("Prumerna teplota:", round(prumer, 2), "C")

pod_mrazem = 0
for x in teploty:
        if x < 0:
            pod_mrazem = pod_mrazem + 1

print("Pocet mernei pod bodem mrazu:", pod_mrazem)

teploty = []
for i in range(24):
    t = random.randint(-10, 20)
    teploty.append(t)

vypis_statistiky()