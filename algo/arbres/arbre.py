class ArbreBinaire:
    def __init__(self, etiquette=None, gauche=None, droit=None):
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit

    def est_vide(self) -> bool:
        if self.etiquette is None:
            return True
        else:
            return False

    def est_feuille(self) -> bool:
        if self.est_vide():
            return False
        else:
            return self.gauche.est_vide() and self.droit.est_vide()

    def taille(self) -> int:
        """Retourne la taille de l'arbre, c'est à dire son nombre de noeuds"""
        if self.etiquette is None:
            return 0
        else:
            return 1 + self.gauche.taille() + self.droit.taille()

    def hauteur(self) -> int:
        """Retourne la hauteur de l'arbre"""
        if self.etiquette is None:
            return 0
        else:
            return 1 + max(self.gauche.hauteur(), self.droit.hauteur())

    def __str__(self):
        if self.est_vide():
            return "()"
        elif self.est_feuille():
            return f"('{self.etiquette}', (), ())"
        else:
            return f"('{self.etiquette}', {self.gauche.__str__()}, {self.droit.__str__()})"


# Définition de l'arbre :
#       1
#     /   \
#    2     3
#   / \     \
#  4   5     6

a = ArbreBinaire(etiquette=1)
a.gauche = ArbreBinaire(etiquette=2)
a.droit = ArbreBinaire(etiquette=3)
a.gauche.gauche = ArbreBinaire(etiquette=4, gauche=ArbreBinaire(), droit= ArbreBinaire())
a.gauche.droit = ArbreBinaire(5, ArbreBinaire(), ArbreBinaire())
a.droit.gauche = ArbreBinaire()
a.droit.droit = ArbreBinaire(6, ArbreBinaire(), ArbreBinaire())
# a.droit.droit.droit = ArbreBinaire(8, ArbreBinaire(), ArbreBinaire())
# a.droit.droit.droit.gauche = ArbreBinaire(7, ArbreBinaire(), ArbreBinaire())

print(a)
print(f'a.taille() => {a.taille()}')
print(f'a.hauteur() => {a.hauteur()}')
print(f'a.est_vide() => {a.est_vide()}')
print(f'a.est_feuille() => {a.est_feuille()}')
