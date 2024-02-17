"Jeu de 2048 en ligne de commande."
import random # Import du module random pour gérer certaines actions aléatoires

grille_de_jeu = [[0,0,0,0] for i in range(4)] # Grille du jeu. Chaque valeur représente un nombre. Si cette valeur est de 0, alors la case correspondante est vide.

def remplir_grille():
    "Ajouter un nombre à la grille de jeu s'il y a des espaces libres"
    nombres_possibles = [2, 4] # Liste des nombres que l'on peut choisir de placer
    for ligne in range(len(grille_de_jeu)): # Pour chaque ligne de la grille de jeu 
        for colonne in range(len(grille_de_jeu[ligne])): # Pour chaque colonne d'une ligne
            if grille_de_jeu[ligne][colonne] == 0: # Si une case de la colonne est libre 
                position = random.randrange(len(nombres_possibles)) # On choisit une valeur au hasard sur toute la longueur de la liste des nombres possibles
                nombre_choisi = nombres_possibles[position] # Le nombre choisi est le résultat de la position par rapport à la longueur de la liste
                grille_de_jeu[ligne][colonne] = nombre_choisi # On remplit la case avec le nombre choisi



print(grille_de_jeu)
remplir_grille()
print(grille_de_jeu)
