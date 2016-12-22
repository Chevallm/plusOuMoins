from random import randint
import sys
import os

def cleanConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# Affichage du début de jeu
print("╔═══════════════════════════╗")
print("║       Plus ou Moins ?     ║")
print("╚═══════════════════════════╝")
print()
print("Le but du jeu est de trouver le nombre entre 1 et 100 définit par l'ordinateur !")
print()

nombreDeVictoire = 0
nombreDeDefaite = 0

while True:
    nombreEssai = 0
    while nombreEssai == 0:
        # On demande la difficulté
        print("Quel niveau de difficulté ?")
        print("1: Facile (20 essais)")
        print("2: Moyen (15 essais)")
        print("3: Difficile (10 essais)")
        print("99: Sortir du programme")

        difficulte = int(input("Votre choix ? "))

        def getNombreEssaiFromDifficulte(difficulte):
            return {
                1: 20,
                2: 15,
                3: 10,
                99: 99
            }.get(difficulte, 0)

        nombreEssai = getNombreEssaiFromDifficulte(difficulte)
        if(nombreEssai == 99):
            sys.exit()
    # on génère le nombre aléatoire

    leNombreCible = randint(0,100)+1

    # on boucle pour le nombre d'essais
    for essai in range(1,nombreEssai+1):
        print("Essai n° " + str(essai))

        # demander la saisie
        leNombreEssai = int(input("Quel nombre essayer ?"))

        # si il a trouver le bon nombre
        if(leNombreCible == leNombreEssai):
            cleanConsole()
            print("Vous avez trouver le bon nombre ! Il s'agissait de " + str(leNombreCible))
            nombreDeVictoire+=1 # on lui ajoute une victoire
            print(str(nombreDeVictoire) + " victoires")
            print(str(nombreDeDefaite) + " défaites")
            break # on sort de la boucle

        # sinon
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            if(essai == nombreEssai): # si c'était le dernier essai
                nombreDeDefaite+=1
                print("Vous avez essayer trop de fois !")
                print("Vous avez perdu.")
                print(str(nombreDeVictoire) + " victoires")
                print(str(nombreDeDefaite) + " défaites")

            # on refait un tour dans la boucle
            if(leNombreEssai < leNombreCible):
                print("C'est plus !")
            if(leNombreEssai > leNombreCible):
                print("C'est moins !")
