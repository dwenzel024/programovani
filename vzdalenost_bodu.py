import math

ax = float(input("ax: "))
ay = float(input("ay: "))
bx = float(input("bx: "))
by = float(input("by: "))

vzdalenost = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)
print("Vzdálenost mezi body A a B je:", vzdalenost)