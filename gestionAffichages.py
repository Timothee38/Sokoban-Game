#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothee
#
# Created:     26/03/2015
# Copyright:   (c) Timothee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- Coding: UTF-8 -*-
import Console
def affichageGrilleConsole(niveau):
    """
    Affiche la grille dans la console en utilisant
    un code couleur ainsi que le dictionnaire niveau contenant
    les variables.
    """

    # niveau est un dictionnaire #


    Console.clrscr()                            #Efface le contenu de la console.
    Console.textbackground(Console.LIGHTGRAY)   #Change le fond du texte en gris clair (esthetique)
    cles = niveau.keys()                        #Recuperation de toutes le clés du dictionnaire niveau

    #Création d'une liste de tuples contenant tous les tuples des positions de la grille
    listeTuples=[]
    listeClesListe=['murs', 'caisses', 'cibles']    #Liste des clés qui contiennent des listes de tuples
    for cle in cles:                                #Scan de la liste en fonction des clés
        if cle in listeClesListe:                   #Si la clé fait partie de la liste des clés définies ci-dessus...
            for element in niveau[cle]:             #Scan des elements de cette liste
                listeTuples.append(element)         #Ajout de l'element qui est un tuple à la liste des tuples de ce dictionnaire
        elif cle == 'perso':                        #Ajout du tuple du personnage
            listeTuples.append(niveau[cle])


    #Affichage de la grille (éléments existants)
    for cle in cles:   #Parcours du dictionnaire niveau selon les clés
        if cle=='murs':
            Console.textcolor(Console.RED)
            for i in niveau[cle]:           #Parcours des items de la liste correspondant à la clé murs
                Console.gotoxy(i[0],i[1])
                print "#"          #Affichage des murs a leur positions
        elif cle=='cibles':
            for i in niveau[cle]:           #Parcours des items de la liste correspondant à la clé cibles
                Console.gotoxy(i[0],i[1])
                print "."          #Affichage de la cible a la position du gotoxy
        elif cle=="caisses":
            for i in niveau[cle]:           #Parcours des items de la liste correspondant à la clé caisses
                Console.textcolor(Console.BROWN)
                Console.gotoxy(i[0],i[1])
                print "$"          #Affichage des caisses en position du gotoxy
        elif cle=="perso":
            Console.textcolor(Console.WHITE)
            Console.gotoxy(niveau[cle][0], niveau[cle][1])
            print "@"              #Affichage du perso a la position dans le gotoxy (sur la console, comme d'habitude)


    #Affichage d'espaces aux endroits où il n'y a rien.
    maxx=0
    maxy=0
    for i in range(len(listeTuples)): #Parcours de la liste des tuples du niveau
        if listeTuples[i][0]>maxx:  #Si l'ième element de la liste est plus grande que le max... (0 = coord x)
            maxx=listeTuples[i][0]  #Alors c'est le nouveau max
        if listeTuples[i][1]>maxy:  #La même chose que x pour y
            maxy=listeTuples[i][1]


    for x in range(maxx+1):         #Parcours des positions en x de la grille selon sa longueur maximale
        for y in range(maxy+1):     #Parcours des positions en y de la grille selon sa longueur maximale
            if (x,y) not in listeTuples:
                Console.gotoxy(x,y) #Placement a l'endroit du tuple "vide"
                print " "           #Remplacement du caractère vide avec un espace pour avoir un textbackground

    #Check si des positions sont les mêmes, gestion des caisses sur les cibles et perso sur cible
    for pos in niveau['cibles']:    #Scan des positions des cibles
        for position in niveau['caisses']:  #Scan des position des caisses
            if pos==position:               #Comparaison de la ième position de la caisse avec la ième position de la cible
                Console.gotoxy(pos[0], pos[1])
                Console.textcolor(Console.BLUE)
                print "*"                   #Si les deux sont égales, affichage de ce caractère à la position
        if niveau['perso']==pos:    #Récupération de la position du personnageque l'on compare au tuple de la pos de la cible
            Console.gotoxy(pos[0],pos[1])
            Console.textcolor(Console.GREEN)
            print "+"



def choixActionJeu():
    """
    Affiche dans la console les choix du joueurs
    """
    #Affichage du menu
    print "Choix d'une action parmi"
    print u"    - Déplacement du personnage : fleches [up], [down], [right], [left], [backspace]"
    print u"    - Arrêter la partie en [a]"
    print u"    - Retour en arrière en [backspace]"
    print u"    - Sauvegarder en [s]"
    print u"    - Recommencer le niveau en [r]"
    print u"    - Naviguer dans les niveau [f] pour niveau suivant et [b] niveau précédent"
    listeTouches = ['down','up','right','left', 'a','\010', 's' ,'r' ,'f', 'b']    #Dictionnaire des touches utilisateur
    print u"Appuyez sur une touche!"

    #Saisie de la touche
    touche=Console.getkey()     #Retourne dans touche le string de la touche entré par l'utilisateur
    while touche not in listeTouches:    #Check si l'user a entré une touche correcte
        print u"Appuyez sur une touche!"
        touche=Console.getkey()
    return touche



def choixParametresJeu():
    """
   Permet l'affichage d'un menu de départ
   """
    print "###############################################"
    print "##           SOKOBAN CONSOLE                 ##"
    print u"##       Par Timothée C. & Jérémy G.         ##"
    print "###############################################"
    print
    print u"Démarrer une nouvelle partie avec la touche [n]"
    print u"Recharger une partie existante avec la touche [e]"
    print u"Quitter le jeu avec la touche [q]"
    print u"Appuyez sur une touche pour executer une des actions listées ci-dessus"
    touche=Console.getkey()
    while touche not in(['n','e','q']):
        print u"Appuyez sur une touche pour executer une des actions listées ci-dessus"
        touche=Console.getkey()

    return touche
