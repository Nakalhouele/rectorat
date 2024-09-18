# https://py-rates.fr/
# fgDQ4uA

#############################################################
import random


def avancer() -> None:
    print("Avancer")


def droite() -> None:
    print("Droite")


def gauche() -> None:
    print("Gauche")


def ouvrir() -> None:
    print("Ouvrir")


def sauter() -> None:
    print("Sauter")


def coup() -> None:
    print("Coup")


def sauter_hauteur(valeur: int) -> None:
    print(f"Sauter_hauteur({valeur})")


def lire_nombre() -> str:
    print("Lire_nombre")
    return random.randint(1, 5)


def lire_chaine() -> str:
    print("Lire_chaine")
    return random.choice(["gau", "droi"])


def sauter_haut() -> None:
    print("Sauter_haut")


def mesurer_hauteur() -> int:
    print("Mesurer_hauteur")
    return random.randint(0, 2)


def tirer(valeur: int):
    print(f"Tirer({valeur})")


def tourner():
    print("Tourner")


def detecter_obstacle() -> bool:
    print("Detecter_obstacle")
    return random.choice([True, False])


#############################################################


def niveau_1():
    avancer()
    droite()
    avancer()
    gauche()
    avancer()
    droite()
    for _ in range(16):
        avancer()
    ouvrir()

def niveau_1_2() -> None:
    for x in range(4):
        if x % 2 == 0:
            gauche()
        else:
            droite()
        avancer()
    for _ in range(16):
        avancer()
    ouvrir()



def niveau_2():
    for _ in range(6):
        sauter()
        avancer()
    avancer()
    gauche()
    avancer()
    avancer()
    for _ in range(9):
        coup()
        avancer()
    avancer()
    ouvrir()


def niveau_3():
    sauter_hauteur(4)
    avancer()
    sauter_hauteur(3)
    avancer()
    for _ in range(4):
        avancer()
        message = lire_nombre()
        avancer()
        sauter_hauteur(message)
        avancer()
    ouvrir()


def niveau_4():
    for _ in range(5):
        avancer()
        message = lire_chaine()
        if message == "gau":
            gauche()
        elif message == "droi":
            droite()
        avancer()
    avancer()
    ouvrir()


def niveau_5():
    avancer()
    sauter_haut()
    h = mesurer_hauteur()
    i = 0
    while h >= 0:
        if h == 0:
            if i == 12:
                break
            avancer()
            i = i + 1
        if h == 1:
            sauter()
        elif h == 2:
            sauter_haut()
        h = mesurer_hauteur()
    ouvrir()


def niveau_6():
    for _ in range(6):
        sauter_hauteur(_)
        avancer()
    ouvrir()


def niveau_7():
    for _ in range(2, 9):
        tirer(_)
        tourner()
    tirer(3)


def niveau_8():
    avancer()
    obstacle = detecter_obstacle()
    while obstacle == True:
        coup()
        obstacle = detecter_obstacle()
    for _ in range(3):
        avancer()
    droite()
    obstacle = detecter_obstacle()
    while obstacle == False:
        avancer()
        obstacle = detecter_obstacle()
    while obstacle == True:
        coup()
        avancer()
        obstacle = detecter_obstacle()
    ouvrir()


# niveau_1()
# niveau_2()
# niveau_3()
# niveau_4()
# niveau_5()
# niveau_6()
# niveau_7()
# niveau_8()
