import json

print("Bonjour et bienvenue dans se RPG")

nom = input("Entrer votre nom: ")


while True:
    print("\nOption:")
    print("\nCommencer = 1")
    print("\nQuitter = 2 \n")

    e = int(input("Entrer votre choix: "))

    if e == 1:
        print("\nBienvenue", nom)

        mana = 200
        vie = 20
        xp = 0
        
        # Début de la boucle de combat
        monstre_pv = 10
        vie = 20
        soin = 5
        while True:
            # Affichage des stats du joueur et du monstre
            print("\nPendant votre balade en foret, un monstre apparaît derrière vous et intrépide. Vous décidez de l'attaquer.")
            print("\nVous :")
            print("PV :", vie)
            print("Mana :", mana)
            print("\nMonstre :")
            print("PV :", monstre_pv)
            # Choix de l'attaque
            print("\nChoisissez votre attaque :")
            print("1. Magie (coût : 3 mana)")
            print("2. Soin (coût : 5 mana)")
            print("3. Bang (coût : 7 mana)")
            print("4. Nova (coût : 12 mana)")
            
            attaque = int(input("--> "))
            # Vérification que le joueur a assez de mana
            magie = 3
            soin = 10
            bang = 7
            nova = 12

            if attaque == 1 and mana < 3:
                print("Vous n'avez pas assez de mana !")
                continue
            elif attaque == 2 and mana < 5:
                print("Vous n'avez pas assez de mana !")
                continue
            elif attaque == 3 and mana < 7:
                print("Vous n'avez pas assez de mana !")
                continue
            elif attaque == 4 and mana < 12:
                print("Vous n'avez pas assez de mana !")            
                continue
            # Attaque du joueur
            if attaque == 1:
                print("Vous lancez une magie !")
                monstre_pv -= magie
                mana -= 3
            elif attaque == 2:
                print("Vous vous soignez !")
                vie += soin
                mana -= 5
            elif attaque == 3:
                print("Vous lancez un bang !")
                monstre_pv -= bang
                mana -= 7
            elif attaque == 4:
                print("Vous lancez une nova !")
                monstre_pv -= nova
                mana -= 12
            # Vérification si le monstre est mort
            if monstre_pv <= 0:
                print("Vous avez vaincu le monstre ! bravo")

                xp += 5
                print("vous gagnez 5XP vos attaques augmentent de 1")


            # Attaque du monstre
            print("Le monstre vous attaque !")
            vie -= 5

            # Vérification si le joueur est mort
            if vie <= 0:
                print("Vous êtes mort !")
                break

            # Fin de la boucle de combat

            # Début de la boucle de combat
            monstre_pv = 30
            xp = 5
            magie = 4 
            soin = 20
            bang = 9
            nova = 14
            vie = 20  # Il faut réinitialiser la vie du joueur avant de continuer
            print("\nSoudainement, un nouveau boss arrive vers vous et vous décidez de l'attaquer.")
            while True:
                # Affichage des stats du joueur et du monstre
                print("\nVous :")
                print("PV :", vie)
                print("Mana :", mana)
                print("XP :", xp)
                print("\nMonstre :")
                print("PV :", monstre_pv)
                # Choix de l'attaque
                print("\nChoisissez votre attaque :")
                print("1. Magie (coût : 4 mana)")
                print("2. Soin (coût : 20 mana)")
                print("3. Bang (coût : 9 mana)")
                print("4. Nova (coût : 14 mana)")

                attaque = int(input("--> "))
                # Vérification que le joueur a assez de mana
                if attaque == 1 and mana < 4:
                    print("Vous n'avez pas assez de mana !")
                    continue
                elif attaque == 2 and mana < 20:
                    print("Vous n'avez pas assez de mana !")
                    continue
                elif attaque == 3 and mana < 9:
                    print("Vous n'avez pas assez de mana !")
                    continue
                elif attaque == 4 and mana < 14:
                    print("Vous n'avez pas assez de mana !")
                    continue
                # Attaque du joueur
                if attaque == 1:
                    print("Vous lancez une magie !")
                    monstre_pv -= magie
                    mana -= 4
                elif attaque == 2:
                    print("Vous vous soignez !")
                    vie += soin
                    mana -= 20
                elif attaque == 3:
                    print("Vous lancez un bang !")
                    monstre_pv -= bang
                    mana -= 9
                elif attaque == 4:
                    print("Vous lancez une nova !")
                    monstre_pv -= nova
                    mana -= 14

                # Vérification si le monstre est mort
                if monstre_pv <= 0:
                    print("Vous avez vaincu le boss ! bravo")

                    xp += 10
                    print("vous gagnez 10XP vos attaques augmentent de 2")



                # Attaque du monstre
                print("Le monstre vous attaque !")
                vie -= 10

                # Vérification si le joueur est mort
                if vie <= 0:
                    print("Vous êtes mort !")
                    break

                # Fin de la boucle de combat


