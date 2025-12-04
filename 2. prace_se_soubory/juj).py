import random
min_value = int(input("Zadej minimální hodnotu: "))
max_value = int(input("Zadej maximální hodnotu: "))
count = int(input("Kolik čísel chceš vygenerovat: "))




random_numbers = [random.randint(min_value, max_value) for _ in range(count)]

with open("random_numbers.txt", "w") as file:
    for number in random_numbers:
        file.write(str(number) + "\n")

print(f"Soubor 'random_numbers.txt' byl vytvořen s {count} náhodnými čísly.")