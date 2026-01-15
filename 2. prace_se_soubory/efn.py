import random
import matplotlib.pyplot as plt
import pandas as pd

def hra():
    data = pd.read_csv(r"2. prace_se_soubory/PROJEKT_milionar/quiz_questions.csv")
    nahodna_otazka = data.sample(1)

    print(nahodna_otazka["question"].values[0])
        


def graf():
    pass

print("vitej cernochu v onoline nejlepism kasinu kde se stanes milionarem.")
print("vzber, jestli se chces prihlasit (P) a nebo vytvorit (V) ucet:")
epstein = input("Vyber P nebo V: ")

if epstein == "P":
    jmeno = input("Zadej sve uyivatelske jmeno: ")
    paspor = input("Zadej svoje heslicko: ")
    with open("heslicka.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()  # Načtení pole všech řádků souboru
        for line in lines:
            slovo = line.split()
            if slovo[0] == jmeno and slovo[1] == paspor:
                vyber = input("Vyber jestli si chces jit hrat (H) a nebo se mocinky moc chce jit podivat na graficky (G) ktere chces videt:")
                if vyber == "H":
                    hra()

                elif vyber == "G":
                    graf()

                else:
                    print("Asi vazne neumis psat nebo nevim cichna te spapa a nebuides stastnz.")
            else:
                print("spatne jmeno nebo heslo, zkus to znovu nebo si vytvor ucet.")
                    
    

elif epstein == "V":
    jmeno1 = input("yadej svoje vzsnene uzivatlekske menicko kter chces pouziva t a budes ho mot  nci rad: ")
    pasportz = input("zadfej sovje heslicko keter si vudes pamatovat a nezuapomenes na negho protoue uy nejde zmenit nikdz: ")
    with open("heslicka.txt", "a", encoding="utf-8") as file:
        file.write(jmeno1+" ")
        file.write(pasportz+" \n")

else:
    print("spatne si to napsal. za trest pujdes na cichnovu ve tri rano kde bude i hosko.")