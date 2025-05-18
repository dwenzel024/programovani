m = float(input("Zadej hmotnost v kg: "))
h = float(input("Zadej výšku v cm: "))
bmi = m / (h / 100) ** 2
print("Vaše BMI je:", round(bmi, 2))