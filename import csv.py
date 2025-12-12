import csv
import os
import random
import re
import sys
from collections import Counter

#!/usr/bin/env python3
"""
Utility script for tasks: file reading, quote generator, student selection,
CSV quiz, text analysis, and hangman. Expects data files in ./data directory.

Usage: run and follow menu prompts.
"""

DATA_DIR = "data"



def path_in_data(filename):
    return os.path.join(DATA_DIR, filename)


def read_lines(filename):
    p = path_in_data(filename)
    with open(p, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]


def task1_basic_load():
    fname = input("Filename (inside data/): ").strip()
    try:
        lines = read_lines(fname)
    except Exception as e:
        print("Error:", e)
        return
    for i, line in enumerate(lines, 1):
        print(f"{i:4}: {line}")
    text = "\n".join(lines)
    num_lines = len(lines)
    num_chars = len(text)
    # count words splitting on whitespace
    words = re.findall(r"\S+", text)
    num_words = len(words)
    print()
    print("Lines:", num_lines)
    print("Characters:", num_chars)
    print("Words:", num_words)


def task2_quote_of_the_day():
    emojis1 = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
    emojis2 = ["💥", "🔥", "❤️‍", "😎", "🤣"]
    try:
        quotes = read_lines("citaty.txt")
    except Exception as e:
        print("Error reading citaty.txt:", e)
        return
    if not quotes:
        print("No quotes found.")
        return
    random.shuffle(quotes)
    quote = random.choice(quotes).strip()
    n = random.randint(3, 5)
    e1 = "".join(random.choice(emojis1) for _ in range(n))
    e2 = random.choice(emojis2)
    print("Citát dne:")
    print(e1)
    print(quote)
    print("###", extract_author(quote), "###" if extract_author(quote) else "###")
    print(e2)


def extract_author(line):
    # If the quote file contains "quote - Author" or "quote — Author", try to extract.
    # Otherwise return empty string.
    for sep in (" - ", " — ", " -- "):
        if sep in line:
            parts = line.rsplit(sep, 1)
            return parts[1].strip()
    return ""


def task3_students_selection():
    fname = input("Students filename (inside data/, default studenti.txt): ").strip() or "studenti.txt"
    try:
        students = [s.strip() for s in read_lines(fname) if s.strip()]
    except Exception as e:
        print("Error:", e)
        return
    if not students:
        print("No students found.")
        return
    try:
        n = int(input("How many students to pick? ").strip())
    except Exception:
        print("Invalid number.")
        return
    if n <= 0:
        print("n must be positive.")
        return
    if n > len(students):
        print(f"Requested {n} > available {len(students)}. Will pick all students.")
        n = len(students)
    # unique selection without replacement
    picked = sorted(random.sample(students, n))
    for name in picked:
        print(name)


def task4_quiz_csv():
    fname = "otazky.csv"
    try:
        p = path_in_data(fname)
        with open(p, encoding="utf-8", newline="") as f:
            reader = list(csv.reader(f))
    except Exception as e:
        print("Error reading otazky.csv:", e)
        return
    rows = []
    for row in reader:
        # accept rows of length >=5: question, a, b, c, answer (A/B/C)
        if len(row) >= 5:
            rows.append(row[:5])
    if not rows:
        print("No quiz questions found.")
        return
    selected = random.sample(rows, min(3, len(rows)))
    correct = 0
    for q, a, b, c, ans in selected:
        print(q)
        print(" a)", a)
        print(" b)", b)
        print(" c)", c)
        user = input("Odpověď: ").strip().upper()
        if user == ans.strip().upper():
            print("Správně.")
            correct += 1
        else:
            print("Špatně. Správná odpověď:", ans.strip().upper())
        print()
    print("Správně celkem:", correct, "z", len(selected))


def load_full_text(filename):
    p = path_in_data(filename)
    with open(p, encoding="utf-8") as f:
        return f.read()


def task5_1984_analysis():
    fname = "1984.txt"
    try:
        text = load_full_text(fname)
    except Exception as e:
        print("Error reading 1984.txt:", e)
        return
    chars = len(text)
    # Count sentences by occurrences of ., ?, !
    sentences = len(re.findall(r"[\.!?](?:\s|$)", text))
    # count newspeak occurrences (word boundaries), case-insensitive
    newspeak_count = len(re.findall(r"\bnewspeak\b", text, flags=re.IGNORECASE))
    print("Characters:", chars)
    print("Sentences (approx.):", sentences)
    print("Occurrences of 'newspeak':", newspeak_count)
    # user word
    word = input("Zadej slovo pro spočítání výskytů (empty to skip): ").strip()
    if word:
        pattern = r"\b" + re.escape(word) + r"\b"
        count_word = len(re.findall(pattern, text, flags=re.IGNORECASE))
        print(f"Výskyt slova '{word}':", count_word)
    # most common word
    words = re.findall(r"\b[\w']+\b", text.lower())
    if words:
        cnt = Counter(words)
        most_common, freq = cnt.most_common(1)[0]
        print("Nejčastější slovo:", most_common, "(", freq, "krát )")
    else:
        print("No words found.")


def task6_hangman():
    fname = "slova.txt"
    try:
        words = [w.strip() for w in read_lines(fname) if w.strip()]
    except Exception as e:
        print("Error:", e)
        return
    if not words:
        print("No words available.")
        return
    word = random.choice(words).lower()
    lives = 7
    guessed = set()
    correct_letters = set(ch for ch in word if ch.isalpha())
    while lives > 0:
        display = "".join(ch if (not ch.isalpha()) or ch in guessed else "_" for ch in word)
        print("Word:", " ".join(display))
        print("Lives:", lives)
        if set(ch for ch in display if ch.isalpha()) == correct_letters:
            print("Vyhrál jste! Slovo bylo:", word)
            return
        guess = input("Hádání (písmeno nebo celé slovo): ").strip().lower()
        if not guess:
            continue
        if len(guess) == 1:
            if guess in guessed:
                print("Už bylo uhádnuto.")
            elif guess in correct_letters:
                guessed.add(guess)
                print("Správně.")
            else:
                lives -= 1
                print("Špatně.")
        else:
            if guess == word:
                print("Vyhrál jste! Slovo bylo:", word)
                return
            else:
                lives -= 1
                print("Špatně.")
    print("Prohrál jste. Slovo bylo:", word)


def main_menu():
    random.seed(42)  # reproducibility
    actions = {
        "1": ("Základní načtení souboru", task1_basic_load),
        "2": ("Citát dne", task2_quote_of_the_day),
        "3": ("Výběr studentů", task3_students_selection),
        "4": ("Kvíz z CSV", task4_quiz_csv),
        "5": ("Zpracování 1984.txt", task5_1984_analysis),
        "6": ("Šibenice", task6_hangman),
        "q": ("Konec", None),
    }
    while True:
        print("\nMenu:")
        for k, (desc, _) in actions.items():
            print(f" {k}) {desc}")
        choice = input("Vyber úlohu: ").strip()
        if choice == "q":
            break
        action = actions.get(choice)
        if not action:
            print("Neplatná volba.")
            continue
        _, func = action
        try:
            func()
        except Exception as e:
            print("Chyba během vykonávání:", e)


if __name__ == "__main__":
    if not os.path.isdir(DATA_DIR):
        print("Složka 'data' neexistuje. Vytvořte ji a vložte potřebné soubory.")
        sys.exit(1)
    main_menu()