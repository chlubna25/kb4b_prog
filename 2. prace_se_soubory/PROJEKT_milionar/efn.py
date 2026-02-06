import matplotlib.pyplot as plt
import pandas as pd
import random
print("vitej cernochu v kasinu")
print("vyber, jestli se chces prihlasit (P) a nebo zaregistrovat (Z)")
epstein = input ("Vyber:")

if epstein == "P":
    jmeno = input("Zadej sve cerne jmeno:")
    passw = input("Zadej sve cerne heslo:")

    with open("heslicka.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()  
        for line in lines:
            slovo = line.split()
            
    
            if slovo [0] == jmeno and slovo [1] == passw:
                epstein2 = input ("Vyber jestli chces hrat (H) nebo graf (G)")

                if epstein2 == "H":
                    data = pd.read_csv(r"2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv")
                    nahodna_otazka = data.sample(1)

                    print(nahodna_otazka["question"].values[0])
                                    

                 

                elif epstein2 == "G":
                    


                    data = pd.read_csv(r"2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv")
                    difficulty_count = data["difficulty"].value_counts()

                    print("\nObtížnosti:")
                    for d, p in difficulty_count.items():
                        print(f"{d}: {p}")

                    import matplotlib.pyplot as plt
                    plt.figure()
                    plt.pie(difficulty_count.values, labels=difficulty_count.index, autopct="%1.1f%%")
                    plt.title("Poměr obtížností otázek")
                    plt.show()


                  


                  


   
    
            

elif epstein == "Z":
    jmeno1 = input("Zadej sve cerne jmeno:")
    passw1 = input("Zadej sve cerne heslo:")

    with open("heslicka.txt", "a", encoding="utf-8") as file:
        file.write(jmeno1+" ")
        file.write(passw1+" \n")


