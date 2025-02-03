def je_prvocislo(n): 
    if n < 2:  
        return False  

    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:  
            return False  

    return True  

cislo = int(input("Zadej číslo: "))  

if je_prvocislo(cislo):  
    print(cislo, "je prvočíslo.")  
else:  
    print(cislo, "není prvočíslo.")  

