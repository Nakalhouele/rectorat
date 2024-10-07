# from calculatrice.Addition import Addition
# from calculatrice.Soustraction import Soustraction

# TODO: encapsuler la calculatrice dans une classe calculatrice
# TODO: //ajouter une memoire pour remonter dans l'historique en utilisant une liste


class Addition():
    
    def __init__(self) -> None:
        pass
    
    def calcule(self, a, b):
        return a + b


class Soustraction():
    
    def __init__(self) -> None:
        pass
    
    def calcule(self, a, b):
        return a - b
    
class Multiplication():
    
    def __init__(self) -> None:
        pass
    
    def calcule(self, a, b):
        return a * b 


class Division():
    
    
    def __init__(self) -> None:
        pass
    
    def calcule(self, a, b) -> int:
        return a / b


class RacineCarre():
    
    def __init__(self) -> None:
        pass
    
    def calcule(self, nombre) -> int:
        return nombre ** 0.5


# MAIN
addition = Addition()
soustraction = Soustraction()
multiplication = Multiplication()
division = Division()
racine_carre = RacineCarre()

volonte = input("Que veux tu faire : ")
if volonte == "0":
    print("Vous souhaitez faire une Addition")
    a = int(input("Saisir le premier nombre : "))
    b = int(input("Saisir le deuxieme nombre : "))
    resultat = addition.calcule(a, b)
    print(resultat)
elif volonte == "1":
    print("Vous souhaitez faire une Soustraction")
    a = int(input("Saisir le premier nombre : "))
    b = int(input("Saisir le deuxieme nombre : "))
    resultat = soustraction.calcule(a, b)
    print(resultat)
elif volonte == "2":
    print("Vous souhaitez faire une Multiplication")
    a = int(input("Saisir le premier nombre : "))
    b = int(input("Saisir le deuxieme nombre : "))
    resultat = multiplication.calcule(a, b)
    print(resultat)
elif volonte == "3":
    print("Vous souhaitez faire une Division")
    a = int(input("Saisir le premier nombre : "))
    b = int(input("Saisir le deuxieme nombre : "))
    resultat = division.calcule(a, b)
    print(resultat)
elif volonte == "4":
    print("Vous souhaitez faire une Racine Carre")
    a = int(input("Saisir le nombre : "))
    resultat = racine_carre.calcule(a)
    print(resultat)