import csv

from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay

# ---------- Načtení CSV a úprava dat ----------
X = []  # = vstupy
Y = []  # = výstupy

with open("3. strojove_uceni/data/data.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        sqft_living = float(row["sqft_living"])
        floors = float(row["floors"])
        # Na vstupu mohou být jen číselné vstupy:
        if row["price"] > "1000000":
            price = 1
        else:
            price = 0

        category = int(row["condition"])

        X.append([price, sqft_living, floors])
        Y.append(category)


# ---------- Rozdělení na trénování a testování ----------
# ZMĚNA: split pomocí funkce
#   funcke má tu výhodu, že dataset zároveň promíchá

trening_X, test_X, trening_Y, test_Y  = train_test_split(
        X, Y,
        test_size=0.4,
        random_state=45)

# ---------- Neuronová síť ----------
neural_network = MLPClassifier(
    hidden_layer_sizes=(2, 8, 7, 2),
    activation="relu",
    max_iter=2000,
    verbose=True,
    random_state=67
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