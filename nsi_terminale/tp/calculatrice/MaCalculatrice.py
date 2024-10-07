# from calculatrice.Addition import Addition
# from calculatrice.Soustraction import Soustraction

# TODO: encapsuler la calculatrice dans une classe calculatrice
# TODO: //ajouter une memoire pour remonter dans l'historique en utilisant une liste


class Addition:

    def __init__(self) -> None:
        self.nom = "Addition"

    def calcule(self, memoire):
        a, b = self.recuperer_saisie()
        c = a + b
        memoire.append(f"{a} + {b} = {c}")
        return c

    def recuperer_saisie(self) -> tuple[int, int]:
        print(f"Vous souhaitez faire une {self.nom}")
        a = int(input("Saisir le premier nombre : "))
        b = int(input("Saisir le deuxieme nombre : "))
        return a, b


class Soustraction:

    def __init__(self) -> None:
        self.nom = "Soustraction"

    def calcule(self, memoire):
        a, b = self.recuperer_saisie()
        c = a - b
        memoire.append(f"{a} - {b} = {c}")
        return c

    def recuperer_saisie(self) -> tuple[int, int]:
        print(f"Vous souhaitez faire une {self.nom}")
        a = int(input("Saisir le premier nombre : "))
        b = int(input("Saisir le deuxieme nombre : "))
        return a, b


class Multiplication:

    def __init__(self) -> None:
        self.nom = "Multiplication"

    def calcule(self, memoire):
        a, b = self.recuperer_saisie()
        c = a * b
        memoire.append(f"{a} * {b} = {c}")
        return c

    def recuperer_saisie(self) -> tuple[int, int]:
        print(f"Vous souhaitez faire une {self.nom}")
        a = int(input("Saisir le premier nombre : "))
        b = int(input("Saisir le deuxieme nombre : "))
        return a, b


class Division:

    def __init__(self) -> None:
        self.nom = "Division"

    def calcule(self, memoire) -> int:
        a, b = self.recuperer_saisie()
        c = a / b
        memoire.append(f"{a} / {b} = {c}")
        return c

    def recuperer_saisie(self) -> tuple[int, int]:
        print(f"Vous souhaitez faire une {self.nom}")
        a = int(input("Saisir le premier nombre : "))
        b = int(input("Saisir le deuxieme nombre : "))
        return a, b


class RacineCarre:

    def __init__(self) -> None:
        self.nom = "RacineCarre"

    def calcule(self, memoire) -> int:
        nombre = self.recuperer_saisie()
        c = nombre**0.5
        memoire.append(f"racine carre {nombre} = {c}")
        return c

    def recuperer_saisie(self) -> int:
        print(f"Vous souhaitez faire une {self.nom}")
        a = int(input("Saisir le nombre : "))
        return a


class Calculatrice:
    memoire = []

    def __init__(self, nom: str) -> None:
        self.nom = nom
        self.on_off = True
        self.dictionnaire = {
            "0": (Addition().calcule),
            "1": (Soustraction().calcule),
            "2": (Multiplication().calcule),
            "3": (Division().calcule),
            "4": (RacineCarre().calcule),
            "-1": (self.eteindre),
        }
        print(f"Bienvenue sur {self.nom}")

    def eteindre(self, memoire):
        self.on_off = False
        print(f"Votre historique: {len(memoire)} opérations")
        memoire.reverse()
        for element in self.memoire:
            print(element)
        print(f"A bientôt sur {self.nom}")

    def enregistrer(self, operation: str) -> None:
        self.memoire.append(operation)

    def execute(self) -> None:
        while self.on_off:
            volonte = input("Que veux tu faire : ")

            action = self.dictionnaire.get(volonte)
            if action is not None:
                result = action(self.memoire)
                if result is not None:
                    print(result)


# MAIN

ma_calculatrice = Calculatrice("Martinique Instruments")
ma_calculatrice.execute()
