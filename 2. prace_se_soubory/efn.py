import csv
import random
import matplotlib.pyplot as plt

def hra():
    otazky_easy = []
    otazky_medium = []
    otazky_hard = []

    otazky = "2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv"

    with open(otazky, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for radek in reader:
            if radek["difficulty"] == "easy":
                otazky_easy.append(radek)
            elif radek["difficulty"] == "medium":
                otazky_medium.append(radek)
            elif radek["difficulty"] == "hard":
                otazky_hard.append(radek)

    vybrane_otazky = (
        random.sample(otazky_easy, 5) +
        random.sample(otazky_medium, 5) +
        random.sample(otazky_hard, 5)
    )

    print("\n hra zacina ted \n")

    cislo = 1
    for otazka in vybrane_otazky:
        print(f"otazecka {cislo}: {otazka['question']}")
        odpoved = input("T / F: ").strip().upper()


        if odpoved == "T":
            odpoved_bool = "TRUE"
        elif odpoved == "F":
            odpoved_bool = "FALSE"
        else:
            print("zadej pouze T nebo F! pokud zadas neco jineho tak to pro tebe nedopadne dobre")
            return


        spravna = otazka["correct_answer"].strip().upper()

        if odpoved_bool != spravna:
            print("\n spatna odpoved. smula, hra je na konecku.")
            return

        print(" spravna odpoved\n")


    print(" gratuluju. vyhral jsi zlateho bludistaka a dobry pocit k tomu")

def graf():
    easy = 0
    medium = 0
    hard = 0

    otazecky = "2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv"
    with open(otazecky, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for radek in reader:
            if radek["difficulty"] == "easy":
                easy += 1
            elif radek["difficulty"] == "medium":
                medium += 1
            elif radek["difficulty"] == "hard":
                hard += 1


    labels = ["easy", "medium", "hard"]
    hodnoty = [easy, medium, hard]


    plt.figure()
    plt.pie(hodnoty, labels=labels, autopct="%1.1f%%")
    plt.title("podil obtiznosti otazecek v kvizecku")

    plt.show()


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
                    
    

elif epstein == "V":
    jmeno1 = input("yadej svoje vzsnene uzivatlekske menicko kter chces pouziva t a budes ho mot  nci rad: ")
    pasportz = input("zadfej sovje heslicko keter si vudes pamatovat a nezuapomenes na negho protoue uy nejde zmenit nikdz: ")
    with open("heslicka.txt", "a", encoding="utf-8") as file:
        file.write(jmeno1+" ")
        file.write(pasportz+" \n")

else:
    print("spatne si to napsal. za trest pujdes na cichnovu ve tri rano kde bude i hosko.")