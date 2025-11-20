import random

min = int(input("Zadej minimální hodnotu intervalu: "))
max = int(input("Zadej maximální hodnotu intervalu: "))
amount = int(input("Zadej počet náhodných čísel k vygenerování: "))

random_numbers = [random.randint(min, max) for _ in range(amount)]

soubor = "2. prace_se_soubory/data/cisla.txt"

with open(soubor, "w", encoding="utf-8") as file:
    for number in random_numbers:
        file.write(f"{number}\n")
