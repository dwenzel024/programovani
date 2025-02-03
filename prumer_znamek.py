def prumer_znamek(znamky):
    soucet = sum(z * v for z, v in znamky if isinstance(z, int))
    vaha = sum(v for _, v in znamky)
    return round(soucet / vaha, 2)

znamky = [[5, 1], [3, 4], [1, 7], [2, 7], ['N', 2]]
print("Vážený průměr známek je:", prumer_znamek(znamky))
