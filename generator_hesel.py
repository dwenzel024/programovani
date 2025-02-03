import random
import string

def generuj_heslo(delka):
    znaky = string.ascii_letters + string.digits + "!@#$%^&*"
    heslo = "".join(random.choice(znaky) for _ in range(delka))
    return heslo

delka = int(input("Zadej délku hesla: "))
print("Vygenerované heslo:", generuj_heslo(delka))
