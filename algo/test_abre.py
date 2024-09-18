class ArbreBinaire():
    
    def __init__(self, etiquette = None, gauche = None, droit = None):
        """Constructeur"""
        self.etiquette = etiquette
        self.gauche = gauche
        self.droit = droit
        
        print(f"(etiquette, gauche, droit) => {(etiquette, gauche, droit)}")
    
    def est_vide(self) -> bool:
        if self.etiquette is None:
            return True
        else:
            return False
    
    def taille(self) -> int:
        """Retourne la taille de l'arbre, c'est à dire son nombre de noeuds"""
        if self.etiquette is None:
            return 0
        else:
            tailleGauche = 0 if self.gauche is None else self.gauche.taille()
            tailleDroit = 0 if self.droit is None else self.droit.taille()
            return 1 + tailleGauche + tailleDroit
        

# Main

arbreBinaire = ArbreBinaire(etiquette = 1)
arbreBinaire.gauche = ArbreBinaire(etiquette=2)
arbreBinaire.droit = ArbreBinaire(etiquette=3)
arbreBinaire.gauche.gauche = ArbreBinaire(etiquette=4)
arbreBinaire.gauche.droit = ArbreBinaire(etiquette=5)

print(f'Taille={arbreBinaire.taille()}')