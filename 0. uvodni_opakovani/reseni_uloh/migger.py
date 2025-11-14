cesta = "2. prace_se_soubory\data\citaty.txt"

with open(cesta, 'r', encoding="utf-8") as soubor:
    text = soubor.read()
    for line in text.split():
        print(line)
        delka +=1

    print("Pocet radku v souboru je: ", delka)