import random

def hod_kostkou():
    return random.randint(1, 6)

hody = int(input("Kolikrát chceš hodit kostkou? "))
for _ in range(hody):
    print("Padlo číslo:", hod_kostkou())
