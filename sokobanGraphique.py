#-------------------------------------------------------------------------------
# Name:        sokobanGraphique
# Purpose:
#
# Author:      Timothee
#
# Created:     09/05/2015
# Copyright:   (c) Timothee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- coding: UTF -8 -*-
from Tkinter import *
from gestionAffichages import *
from gestionNiveau import *
from gestionPartie import *
from gestionCollection import *

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

def newNiveau():
    global varBoolGlobale
    varBoolGlobale=True

    partie(1)

def recommence():
    global numeroNiveau, varBoolGlobale
    varBoolGlobale=True
    partie(numeroNiveau)

def niveauSuivant():
    global numeroNiveau
    global collection

    if debloqueNiveau(collection):
        numeroNiveau+=1
        partie(numeroNiveau)

def niveauPrecedent():
    global numeroNiveau
    global collection

    if numeroNiveau>1:
        numeroNiveau-=1
        partie(numeroNiveau)

def sauvegarde():
    global sauv, niveau, numeroNiveauSave

    xsb=fileXSB(numeroNiveau)
    sauvegardePartie(sauv, xsb, niveau)
    numeroNiveauSave=numeroNiveau

def restore():
    global sauv, niveau, varBoolGlobale

    if restaurationPartie(sauv, niveau):
        varBoolGlobale=False
        partie(numeroNiveauSave)




def deplacement(event):
    """
    Gère les déplacements
    """
    global niveau
    global numeroNiveau
    global varBoolGlobale

    touche = event.keysym
    if touche in ['Up', 'Down','Left','Right']:
        if deplacementPerso(niveau,touche.lower()):
            incrementScore(niveau)
            affichageDessinGraphique(dessin, niveau, collection)
    elif touche=='BackSpace':
        if annuleDernierDeplacement(niveau):
            niveau['score']-=1
            affichageDessinGraphique(dessin, niveau, collection)
    niveau=testCaisseToutesRanges(niveau)
    if niveau['estFini']:
        numeroNiveau+=1
        affichageDessinGraphique(dessin, niveau, collection)
        varBoolGlobale=True
        partie(numeroNiveau)

def partie(numeroNiveau):
    """
    Initialise la grille
    """
    global niveau, varBoolGlobale
    if varBoolGlobale:
        niveau=chargementDonneesNiveau(niveau, fileXSB(numeroNiveau))
    elif not(varBoolGlobale):
        numeroNiveau=numeroNiveauSave

    initialisationCollection("novoban", collection)
    affichageDessinGraphique(dessin, niveau, collection)




def affichageDessinGraphique(dessin, niveau, collection):
    """
    Affiche le sokoban en version graphique
    """
    #rectangleCible = dessin.create_rectangle(0,0,30,30,fill="violet")
    #trianglePerso = dessin.create_polygon((0, 30, 15, 0, 30, 30), fill="red")
    #cercleCaisseNonRangée = dessin.create_oval(0,0,95,95,width=0,fill='blue')
    #cercleCaisseRangées = canvas.create_oval(0,0,95,95,width=0,fill='green')
    dessin.delete("all")

    maxx=0
    maxy=0
    for (x,y) in niveau['murs']:
        if x>maxx:
            maxx=x
        if y>maxy:
            maxy=y

    distanceX=(400-((maxx/2.0)*30.0))/30.0
    distanceY=(250-(((maxy)/2.0)*30.0))/30.0

    score=niveau['score']


    dessin.create_text(60,20,text="Novoban: niveau %d\nScore: %d"%(numeroNiveau,score))

    for (x,y) in niveau['cibles']:
        dessin.create_rectangle((distanceX+x)*30,(y+distanceY)*30,((distanceX+x)+1)*30,((y+distanceY)+1)*30, width=0, fill="violet")

    for cle in niveau.keys():   #Parcours du dictionnaire niveau selon les clés
        if cle=='murs':
            for (x,y) in niveau[cle]:
                dessin.create_rectangle((distanceX+x)*30,(y+distanceY)*30,((distanceX+x)+1)*30,((y+distanceY)+1)*30,fill="black")
        if cle=='caisses':
            for (x,y) in niveau[cle]:
                if (x,y) not in niveau['cibles']:
                    dessin.create_oval((distanceX+x)*30,(y+distanceY)*30,((distanceX+x)+1)*30,((y+distanceY)+1)*30,fill="green")
                else:
                    dessin.create_oval((distanceX+x)*30,(y+distanceY)*30,((distanceX+x)+1)*30,((y+distanceY)+1)*30,fill="red")
        if cle=='perso':
            (x,y)=niveau['perso']
            dessin.create_polygon((distanceX+x)*30,((y+distanceY)*30)+30,((distanceX+x)*30)+30/2.0, (y+distanceY)*30,((distanceX+x)+1)*30,((y+distanceY)+1)*30, fill='blue')



#main
fenetre=Tk()
fenetre.title("Sokoban Craig & Gras")
niveau=initialisationNiveauPourTest()
collection=initialisationCollectionPourTest()
numeroNiveau=1
numeroNiveauSave=1
sauv="grilles/sauvegarde/novoban.bin"
varBoolGlobale=True

dessin = Canvas(fenetre, bg="white", height=500, width=800)
dessin.pack(side=LEFT)


dessin.focus_set() #Capture active
dessin.bind('<Key>', deplacement)  #gestion évenement

choixCollection=Label(fenetre, text="Choix de la collection", width="30").pack(side=TOP)

gestionDesNiveaux=Label(fenetre, text="Gestion du(es) niveau(x)", width="30").pack(side=TOP)
boutonRecommencer=Button(fenetre, text="Recommencer", width="30", command=recommence).pack(side=TOP, padx=10, pady=5)
boutonPrecedent=Button(fenetre, text="Niveau Precedent", width="30", command=niveauPrecedent).pack(side=TOP, padx=10, pady=5)
boutonSuivant=Button(fenetre, text="Niveau Suivant", width="30", command=niveauSuivant).pack(side=TOP, padx=10, pady=5)

gestionDesParties=Label(fenetre, text="Gestion de la (des) partie(s)", width="30").pack(side=TOP)

boutonSave=Button(fenetre, text="Sauvegarder", width="30", command=sauvegarde).pack(side=TOP, padx=10, pady=5)
boutonReload=Button(fenetre, text="Recharger", width="30", command=restore).pack(side=TOP, padx=10, pady=5)
boutonNew=Button(fenetre, text="Nouvelle Partie", width="30", command=newNiveau).pack(side=TOP, padx=10, pady=5)

##dispNiveau=Label(fenetre, ).pack(side=LEFT)
##dispScore=Label(fenetre, text="Score: %d"%niveau['score']).pack(side=LEFT)

fenetre.mainloop() #Evenement actifs