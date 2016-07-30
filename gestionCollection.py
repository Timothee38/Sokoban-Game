#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothee
#
# Created:     24/04/2015
# Copyright:   (c) Timothee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- Coding: UTF-8 -*-
from os.path import *
from os import *
import io

SCORE_MAX=10000

def initialisationCollectionPourTest():
    """
    initialise un dictionnaire collection
    """
    collection = {'nom': "novoban", 'xsbs': ["novoban01.xsb", "novoban02.xsb", "novoban03.xsb",
    "novoban49.xsb", "novoban50.xsb"], 'encours': 1, 'debloque': 2, 'records': [40, 60, 70,
    10000, 10000] }

    return collection


def lectureListeRecords(nom,nbreNiveaux):
    """
    Renvoie la liste des records d'une collection
    """
    global SCORE_MAX
    listeRecords=[]
    fichier="grilles/sauvegarde/"+nom+".txt"
    isThereAFile=isfile(fichier)    #Le fichier existe?
    if isThereAFile:        #Si le fichier existe...
        readFich=io.open(fichier, 'r') #Alors on le lit...
        l = readFich.readline()     #Ligne par ligne
        while l != "":
            liste=l.split(":")      #A chaque ligne on découpe selon le caractère séparateur ":"
            listeRecords.append(liste[1][:-1]) #Il s'agit du record, auquel on a retiré le \n
            l = readFich.readline()
        readFich.close()
        for i in range(nbreNiveaux-len(listeRecords)):
            listeRecords.append(SCORE_MAX)
    else:                   #Sinon...
        for i in range(nbreNiveaux): #En fonction du nombre de niveaux...
            listeRecords.append(SCORE_MAX) #On définit le score a SCORE_MAX, une variable globale

    return listeRecords

def initialisationCollection(nom,collection):
    """
    initialise une collection
    """
    collection['nom']=nom   #Ajoute un nom
    collection['encours']=0 #Initialise encours
    collection['debloque']=0    #initialise debloque
    collection['xsbs']=listdir("grilles/"+nom)  #Seulement si nom est un string
    collection['records']=lectureListeRecords(nom,len(collection['xsbs']))  #initialise les records (score_max par défaut)

def sauvegardeListeRecords(sauv,collection):
    """
    Sauvegarde la liste des records par niveau de collection
    dans sauv
    """
    fichRecords=io.open(sauv,'w')  #Ouverture du fichier en mode écriture
    for i in range(len(collection['records'])):    #Parcours du nombre d'éléments de la liste
        ligne=str(collection['xsbs'][i])+":"+str(collection['records'][i])+"\n"
        fichRecords.write(unicode(ligne)) #écriture des records dans le fichier, par niveau, et en suivant le formatage.
    fichRecords.close()

def debloqueNiveau(collection):
    """
    Regarde si un niveau peut-être débloqué, et le débloque
    """
    potentielDebloque=collection['debloque']+1
    if (potentielDebloque<len(collection['xsbs'])):
        collection['debloque']=potentielDebloque
        return True

    return False







