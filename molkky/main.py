def molkky():
    """Cette fonction sert à dire les scores d'un joueur de molkky en demandant le nombre et les noms des joueurs.
    Le programme nous dit à la fin qui a gagné et en combien de fois(tout en respectant le regles du molkky)"""
    nbj = int(input("Quel est le nombre de joueur ? "))#demande le nombre de joueurs
    nbJoueursRestants = nbj #met la variable nombre de joueurs restants à nombre de joueurs
    scores = []  # liste des scores
    nomsJoueur = []  # liste des noms des joueurs
    nbZero = []  # sert à nous dire le nombre de zero d'un joueur
    scoreJoueur = 0 
    termine = False
    scoref=0
    tablette=[]
    cbreussi=[]
    for n in range(nbj):
        nomJoueur = input(f"Comment s'apppelle le joueur {n+1} ? ")
        nomsJoueur.append(nomJoueur)
        scores.append(0)
        nbZero.append(0)
        tablette.append(0)
        cbreussi.append(0)
        
    while not (50 in scores):
        for k in range(nbj):
            if (nbZero[k] == 3):
                continue
                numeroJoueur = k+1
                scoref = int(input(f"combien de quille a fait tomber {nomsJoueur[k]}  dans ce tour ? "))
                cbreussi[k] += 1
                if scoref==1:
                    scoreJoueur = int(input("Quel est le score sur la quille ?"))
                elif scoref>1:
                    scoreJoueur = scoref
                else :
                    scoreJoueur=0   
                scores[k] += scoreJoueur
                if scores[k] == 50:
                    print(f"{nomsJoueur[k]} a gagné en {cbreussi[k]} fois")
                    break
                elif scores[k] > 50:
                    scores[k] = 25
                elif scoreJoueur != 0:
                    nbZero[k] = 0
                elif scoreJoueur == 0:
                    nbZero[k] += 1
                    if nbZero[k] == 3:
                        print(f"{nomsJoueur[k]} a perdu")
                        tablette[k] = None
                        scores[k] = "Elimine"
                        nbJoueursRestants = nbJoueursRestants - 1
                        if nbJoueursRestants == 1:
                            for l in range(nbj):
                                if not (tablette[l] == None):
                                    print(f"{nomsJoueur[l]} a gagné en {cbreussi[k]} fois")
                                    termine = True
                                    break
        for l in range(nbj):
            print(f"Score {nomsJoueur[l]} = {scores[l]}")
            if termine:
                    break
        if termine:
            break
    

molkky()
