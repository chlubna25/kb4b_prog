import random

def volby(choice):
    if choice == 1:
        strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
        return strany 
    elif choice == 2:
        preference = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]  # data ze STEM 28.9.
        return preference
    else:
        return print("Chyba v kodu! Kontaktujte Heryho")
    
def rachot():
    strany = volby(1)
    preference = volby(2)
    preference_new = preference.copy()
    for i in range(len(preference)):
        nahoda = round(random.uniform(-0.5, 0.5), 2)
        preference_new[i] = max(0, preference_new[i] + nahoda)
    total = sum(preference_new)
    original_total = sum(preference)
    preference_new = [p * original_total / total for p in preference_new]
    return preference_new

def ucast():
    populace = 10000000
    ucast_populace = round(random.uniform(0.50, 0.80), 5)
    ucastnici = ucast_populace*populace
    return ucastnici

def hlasovani():
    ucastnici = ucast()
    preference_new = rachot()
    strany = volby(1)
    hlasovani_strany = {
        'ANO': 0,
        'SPOLU': 0,
        'SPD': 0,
        'STAN': 0,
        'Piráti': 0,
        'Motoristé': 0,
        'Stačilo': 0,
        'Jiné': 0
    }
    for _ in range(int(ucastnici)):
        hlas = random.choices(strany, weights=preference_new, k=1)[0]
        hlasovani_strany[hlas] += 1
    return hlasovani_strany
def spocitani():
    hlasovani_strany = hlasovani()
    total_hlasu = sum(hlasovani_strany.values())
    procenta = {key: (value/total_hlasu)*100 for key, value in hlasovani_strany.items()}
    #for cycle by ai
    for strana, pocet_hlasu in hlasovani_strany.items():
        procento = procenta[strana]
        print(f"{strana}: {procento:.2f}% ({pocet_hlasu} hlasů)")

spocitani()