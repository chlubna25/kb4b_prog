import csv
from sklearn.neural_network import MLPClassifier

X = []
Y = []

cesticka = r"3. strojove_uceni/data/heart.csv"
with open(cesticka, "r", encoding="utf-8") as file:
    for radek in csv.DictReader(file):
        Y.append(int(radek["heart_disease"]))
        
        if radek["heart_disease"] == 1:
            heart_disease = 1
        else:
            heart_disease = 0

        age = int(radek["age"])
        sex = int(radek["sex"])
        chest_pain_type = int(radek["chest_pain_type"])
        resting_bp = int(radek["resting_bp"])
        cholesterol = int(radek["cholesterol"])
        fasting_blood_sugar = int(radek["fasting_blood_sugar"])
        resting_ecg = int(radek["resting_ecg"])
        max_heart_rate = int(radek["max_heart_rate"])
        exercise_angina = int(radek["exercise_angina"])

        X.append([heart_disease, age, sex, chest_pain_type, resting_bp, cholesterol, fasting_blood_sugar, resting_ecg, max_heart_rate, exercise_angina])