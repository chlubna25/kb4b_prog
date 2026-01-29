# Neuronová síť predikující BMI kategorii
# Jedná se pouze o učební ukázku - pro BMi je jinak využití neuronky nevhodné

import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
cesta = r"C:\Users\st025498\Downloads\kb4b_jebus\3. strojove_uceni\data\high_elo_opening.csv"


# Funkce pro extrakci prefixu (první písmeno kódu)
def extract_prefix(code):
    return code[0]  # Vrátí první znak kódu (např. "E" z "ECO")

# Funkce pro unikátní kódování celého kódu
def unique_code_encoding(code, code_to_int):
    if code not in code_to_int:
        code_to_int[code] = len(code_to_int)  # Přiřadí unikátní číslo k novému kódu
    return code_to_int[code]

# Inicializace seznamů pro X a Y
X = []
Y = []

# Inicializace slovníku pro přiřazení unikátních čísel k celým kódům
code_to_int = {}

# Načítání dat z CSV souboru
with open("data/bmi.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        height = float(row["Height"])
        weight = float(row["Weight"])

        # Na vstupu mohou být jen číselné vstupy:
        if row["Gender"] == "Male":
            gender = 0
        else:
            gender = 1

        bmi_category = int(row["Index"])

        # Extrahujeme prefix a unikátní kód pro každý kód (např. "ECO", "B03")
        code = row["ECO"]  # Předpokládáme, že kódy jsou v sloupci "Code"
        prefix = extract_prefix(code)
        prefix_encoding = unique_code_encoding(prefix, code_to_int)
        unique_code_encoding_val = unique_code_encoding(code, code_to_int)

        # Přidáme vstupy X a výstupy Y
        X.append([gender, height, weight])
        Y.append([prefix_encoding, unique_code_encoding_val])  # Přidáme dvě hodnoty




# ---------- Rozdělení na trénování a testování ----------
rows = len(X)
split = round(0.8 * rows)

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.2,
        random_state=42)

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(8, 4),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=4
)

neural_network.fit(trening_X, trening_Y)

# ---------- Vyhodnocení ----------
results = neural_network.predict(test_X)

correct = 0
for i in range(len(results)):
    if test_Y[i] == results[i]:
        correct += 1
print("Přesnost:", correct / len(results))

# ---------- Confusion matrix ----------
# zobrazuje jaké odpovědi dává neuronka pro dané vstupy
ConfusionMatrixDisplay.from_predictions(
    test_Y, results)
plt.show()
