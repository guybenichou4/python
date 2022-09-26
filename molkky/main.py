def molkky():
    nbj = int(input("Quel est le nombre de joueur ? "))
    nbJoueursRestants = nbj
    scores = []  # liste des scores
    nomsJoueur = []  # liste des noms des joueurs
    nbZero = []  # sert à nous dire le nombre de zero d'un joueur
    scoreJoueur = 0
    termine = False
    for n in range(nbj):
        nomJoueur = f"Joueur {n+1}"
        nomsJoueur.append(nomJoueur)
        scores.append(0)
        nbZero.append(0)

    while not (50 in scores):
        for k in range(nbj):
            if (nbZero[k] == 3):
                continue
            numeroJoueur = k+1
            scoreJoueur = int(
                input(f"quel est le score du joueur {numeroJoueur} dans ce tour ? "))
            scores[k] += scoreJoueur
            if scores[k] == 50:
                print(f"le joueur {numeroJoueur} a gagné")
                break
            elif scores[k] > 50:
                scores[k] = 25
            elif scoreJoueur != 0:
                nbZero[k] = 0
            elif scoreJoueur == 0:
                nbZero[k] += 1
                if nbZero[k] == 3:
                    print(f"le joueur {numeroJoueur} a perdu")
                    scores[k] = "Elimine"
                    nbJoueursRestants = nbJoueursRestants - 1
                    if nbJoueursRestants == 1:
                        for l in range(nbj):
                            if not (nomsJoueur[l] == None):
                                print(f"le joueur {nomsJoueur[l]} a gagné")
                                termine = True
                                break
            for l in range(nbj):
                print(f"Score {nomsJoueur[l]} = {scores[l]}")
            if termine:
                break
        if termine:
            break
molkky()
