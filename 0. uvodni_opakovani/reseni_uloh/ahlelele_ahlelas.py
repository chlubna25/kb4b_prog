cesta = "chatlog.txt"

with open(cesta, "w", encoding="utf-8") as file:
    file.close()

konec = "KONEC"
zprava = ""

print(f"chatlog opustis zadanim \'{konec}\'")

while zprava != konec:
        jmena = input("Zadej svoje jmeno: ")
        zprava = input("Zadej svoji zpravu: ")

        if zprava != konec:
            with open(cesta, "a", encoding="utf-8") as file:
                file.write(f"{jmena}: {zprava}\n")