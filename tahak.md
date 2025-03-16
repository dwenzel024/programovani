# Python - Tahák

## 1. Proměnné
Proměnné slouží k ukládání hodnot:

```python
x = 10  # Celé číslo
jmeno = "David"  # Text
prumer = 2.5  # Desetinné číslo
pravda = True  # Logická hodnota (True/False)
```

## 2. Aritmetické operace
Aritmetické operace slouží k matematickým výpočtům:


```python
# Sčítání
5 + 3  # Výsledek: 8

# Odčítání
5 - 3  # Výsledek: 2

# Násobení
5 * 3  # Výsledek: 15

# Dělení
5 / 3  # Výsledek: 1.666...

# Celé dělení
5 // 3  # Výsledek: 1

# Zbytek po dělení
5 % 3  # Výsledek: 2

# Mocnina
5 ** 3  # Výsledek: 125
```
## 3. Podmínky a logické operace
Podmínky umožňují provádět různé akce podle zadaných podmínek:

```python
# Podmínky

vek = 18
if vek >= 18:
    print("Jsi dospělý.")
else:
    print("Nejsi dospělý.")


# Logické operace

# A současně
True and False  # Výsledek: False

# Nebo
True or False  # Výsledek: True

# Negace
not True  # Výsledek: False
```

## 4. Cykly
Cykly se používají pro opakované provádění kódu:

```python
for i in range(5):
    print(i)  # Vytiskne 0, 1, 2, 3, 4

x = 0
while x < 5:
    print(x)
    x += 1
```

## 5. Funkce
Funkce umožňují znovupoužití kódu:

```python
def secti(a, b):
    return a + b

vysledek = secti(3, 4)
print(vysledek)  # Vytiskne 7
```

## 6. Práce s texty
Texty (str) lze upravovat různými způsoby:

```python
text = "Ahoj, svete!"
print(text.upper())  # "AHOJ, SVETE!"
print(text.lower())  # "ahoj, svete!"
print(len(text))     # Délka textu
```

## 7. Výstupy
Funkce print() slouží k výpisu na obrazovku.

```python
print("Ahoj svete!")
```

## 8. Vstupy
Funkce input() slouží k získání uživatelského vstupu.

```python
jmeno = input("Jak se jmenujes? ")
print("Ahoj,", jmeno)
```