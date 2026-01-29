import matplotlib.pyplot as plt
import pandas as pd


data = pd.read_csv("quiz_questions.csv")
plt.bar(["Babka", "Dědeček"], [4, 2])

plt.title("Počty jablek v dětských říkankách")
plt.xlabel("Postava")
plt.ylabel("Jablka [ks]")

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.show()
