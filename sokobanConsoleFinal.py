#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothee
#
# Created:     10/05/2015
# Copyright:   (c) Timothee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: UTF -8 -*-
from gestionAffichages import *
from gestionCollection import *
from gestionNiveau import *
from gestionPartie import *
from Console import *
import time

def fileXSB(numNiveau):
    """
    Renvoie le nom/chemin du fichier.xsb
    du niveau numNiveau
    """
    if numNiveau<10:
        xsb="grilles/novoban/novoban0"+str(numNiveau)+".xsb"
    elif numNiveau>=10:
        xsb="grilles/novoban/novoban"+str(numNiveau)+".xsb"
    return xsb

def main_menu():
    """
    Retourne l'entrée
    """
    global niveau
    global sauv
    global numNiveauSave
    global toucheGlobale

    Console.clrscr()
    Console.textbackground(Console.BLACK)
    Console.textcolor(Console.WHITE)

    toucheDebut=choixParametresJeu()
    if toucheDebut=="q":
        exit(5)
    while toucheDebut!="q":
        if toucheDebut=="n":
            niveau=chargementDonneesNiveau(niveau, fileXSB(1))
            toucheGlobale="n"
            jeu(1)


        elif toucheDebut=="e":
            toucheGlobale="e"
            if restaurationPartie(sauv, niveau):
                jeu(numNiveauSave)



def jeu(numNiveau):
    """
    Démarre un jeu en fonction du niveau n°numNiveau fourni en paramètre.
    """
    global numNiveauSave
    global niveau
    global collection
    global sauv
    global sauvRecord
    global toucheGlobale

    Console.clrscr()
    Console.textbackground(Console.BLACK)
    Console.textcolor(Console.WHITE)

    xsb=fileXSB(numNiveau) # fichier du niveau
    if toucheGlobale=="n":
        niveau=chargementDonneesNiveau(niveau, xsb)
    initialisationCollection("novoban", collection)
    affichageGrilleConsole(niveau)

    touche=""
    while touche!="a":
        Console.textbackground(Console.BLACK)   #Affichage du background de la console en noir (par défaut)
        Console.gotoxy(0,12)                    #On descends l'affichage des choix en dessous de la grille
        Console.textcolor(Console.WHITE)        #Affichage du texte de la console en blanc (par défaut)
        print "Score Record: %d"%int(collection['records'][(int(xsb[-5]))-1]) #Recuperation du score record pour la grille courante
        print "Score: %d"%niveau['score']
        touche=choixActionJeu()                 #Saisie de la touche entrée par l'utilisateur
        if touche=="f":
            numNiveau+=1
            toucheGlobale="n"
            jeu(numNiveau)
        elif touche=="b":
            if numNiveau>1:
                numNiveau-=1
                jeu(numNiveau)
        elif touche=="s":
            sauvegardePartie(sauv, xsb, niveau)
            numNiveauSave=numNiveau
            main_menu()
        elif touche=="r":
            jeu(numNiveau)
        elif touche=='\010':
            if annuleDernierDeplacement(niveau):
                niveau['score']-=1
        elif touche in ['up', 'down', 'right', 'left']:
            if deplacementPerso(niveau, touche):
                incrementScore(niveau)

        niveau=testCaisseToutesRanges(niveau)

        Console.textcolor(Console.WHITE)
        Console.textbackground(Console.BLACK)

        affichageGrilleConsole(niveau)

        if niveau['estFini']:
            Console.gotoxy(0,12)
            if numNiveau<10:
                if collection['records'][(int(xsb[-5]))-1]>niveau['score']:
                    collection['records'][(int(xsb[-5]))-1]=niveau['score']
            elif numNiveau>10:
                if collection['records'][(int(xsb[-6:-4]))-1]>niveau['score']:
                    collection['records'][(int(xsb[-6:-4]))-1]=niveau['score']
            print u"Félicitations!"
            sauvegardeListeRecords(sauvRecord,collection)
            time.sleep(3)   #Pause de 3 secondes avant la suite.
            if debloqueNiveau(collection):
                jeu(numNiveau+1)

    if touche=="a":
        niveau['caisses']=niveau['cibles']
        Console.clrscr()
        Console.textbackground(Console.BLACK)
        Console.textcolor(Console.WHITE)
        affichageGrilleConsole(niveau)
        Console.gotoxy(0,12)
        print "Voici la solution"
        time.sleep(3)   #Pause de 3 secondes avant la suite.
        main_menu()


#main
toucheGlobale=""
numNiveauSave=1
sauv="grilles/sauvegarde/novoban.bin"
sauvRecord="grilles/sauvegarde/novoban.txt"
niveau=initialisationNiveauPourTest()
collection=initialisationCollectionPourTest()
main_menu()

