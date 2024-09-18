def euclidiene(n: int):
    diviseur: int = 2
    
    quotient = n // diviseur
    rest = n % diviseur
    print(f"{n} = {diviseur} * {quotient} + {rest}")

    if quotient == 0:
        return rest
    return euclidiene(quotient)

def euclidiene_2(n: int, memoire):
    diviseur: int = 2
    
    quotient = n // diviseur
    rest = n % diviseur
    print(f"{n} = {diviseur} * {quotient} + {rest}")
    if quotient == 0:
        memoire.append(rest)
        return rest
    memoire.append(rest)
    return euclidiene_2(quotient, memoire)


def binaire_decimale(n:int) -> int:
    var = str(n)
    longueur = len(var)
    resultat = 0
    for x in range(0, longueur):
        rang = longueur - (x + 1)
        print(f"valeur_rang={var[x]} rang={rang}: {var[x]} * {2 ** rang}")
        resultat += int(var[x]) * (2 ** rang)
    return resultat
    
    
    

# MAIN
nombre_a_convertir=195
# euclidiene(nombre_a_convertir)
memoire = []
# euclidiene_2(nombre_a_convertir, memoire)
# memoire.reverse()
# print(f"{nombre_a_convertir} = {''.join(str(x) for x in memoire)} en binaire")

binaire_a_convertir=11000011
print(f'binaire_decimale({binaire_a_convertir})={binaire_decimale(binaire_a_convertir)}')