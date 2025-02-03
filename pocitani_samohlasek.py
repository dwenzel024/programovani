def pocet_samohlasek(text):
    samohlasky = "aeiouyáéíóúý"
    pocet = sum(1 for znak in text.lower() if znak in samohlasky)
    return pocet

vstup = input("Zadej text: ")
print("Počet samohlásek:", pocet_samohlasek(vstup))
