import random
import unidecode

barvy = ["Červená", "Modrá", "Zelená", "Žlutá", "Fialová", "Oranžová", "Hnědá", "Růžová"]
barvy_normalizovane = [unidecode.unidecode(b).lower() for b in barvy]

pocet_barev = int(input("Kolik barev chceš hádat? (2-6): "))
tajny_kod = random.sample(barvy, pocet_barev)

def ziskej_tip():
    while True:
        tip = input(f"Zadej {pocet_barev} barev oddělených mezerou: ").split()
        normalizovany_tip = [unidecode.unidecode(barva).lower() for barva in tip]

        if len(normalizovany_tip) != pocet_barev:
            print("Špatný počet barev!")
            continue
        if len(set(normalizovany_tip)) != len(normalizovany_tip):
            print("Barvy se nesmí opakovat!")
            continue
        if not all(barva in barvy_normalizovane for barva in normalizovany_tip):
            print("Neplatné barvy! Použij: ", ", ".join(barvy))
            continue
        
        tip = [barvy[barvy_normalizovane.index(barva)] for barva in normalizovany_tip]
        return tip

def vyhodnot_tip(tip, tajny_kod):
    cerne = sum(1 for i in range(pocet_barev) if tip[i] == tajny_kod[i])
    bile = sum(1 for barva in tip if barva in tajny_kod) - cerne
    return cerne, bile

pokusy = 7

while pokusy > 0:
    hracuv_tip = ziskej_tip()
    cerne, bile = vyhodnot_tip(hracuv_tip, tajny_kod)
    print(f"ČERNÁ: {cerne}, BÍLÁ: {bile}")

    if cerne == pocet_barev:
        print("Vyhrál jsi! Všechny barvy jsou správně.")
        break
    
    pokusy -= 1
    print(f"Zbývá {pokusy} pokusů.")

if pokusy == 0:
    print("Prohrál jsi! Tajný kód byl:", ", ".join(tajny_kod))