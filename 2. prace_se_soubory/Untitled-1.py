
import random


min_value = int(input("Zadejte minimální hodnotu: "))
max_value = int(input("Zadejte maximální hodnotu: "))
count = int(input("Kolik čísel chcete vygenerovat: "))


random_numbers = [random.randint(min_value, max_value) for _ in range(count)]


with open("random_numbers.txt", "w") as file:
   for number in random_numbers:
      file.write(str(number) + "\n")

print(f"Vygenerováno {count} náhodných čísel a uloženo do souboru 'random_numbers.txt'")
