import random

def citat_dne():
    random.seed()  # volitelně pro náhodnost

    emojis1 = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
    emojis2 = ["💥", "🔥", "❤️‍", "😎", "🤣"]

    with open("2. prace_se_soubory/data/citaty.txt", "r", encoding="utf-8") as f:
        citaty = [line.strip() for line in f if line.strip()]

    citat = random.choice(citaty)
    if " - " in citat:
        text, autor = citat.split(" - ", 1)
    else:
        text, autor = citat, "Neznámý"

    emojiset = "".join(random.choices(emojis1, k=random.randint(3, 5)))
    emojikon = random.choice(emojis2)

    print("Citát dne:")
    print(emojiset)
    print(text)
    print(f"### {autor} ###")
    print(emojikon)

citat_dne()