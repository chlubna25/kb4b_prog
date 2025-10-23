import random

strany = ["ANO", "SPOLU", "SPD", "STAN", "Pirati", "Motoriste", "Stacilo", "Jine"]
preference = [27.3, 22.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2]

ucast = random.randint(50, 80)

pocet_volicu = 8275000

pocet_hlasujicich = pocet_volicu * (ucast / 100)

print("pocet hlasujicih:", pocet_hlasujicich)
print("ucast u voleb:", ucast, "%")

