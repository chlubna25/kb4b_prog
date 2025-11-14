import random

soubor = "2. prace_se_soubory/data/studenti.txt"

with open(soubor, "r", encoding="utf-8") as file:
    lines = file.readlines()
    for line in lines:
        slovo = line.strip()

for i in range(5):
    random_name = random.choice(lines).strip()
    print(f"Náhodně vybraní studenti: {random_name}")