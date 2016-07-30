#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      craigt
#
# Created:     27/04/2015
# Copyright:   (c) craigt 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- Coding: UTF-8 -*-
import pickle
import os

def sauvegardePartie(sauv,xsb,niveau):
    """
    Procède a la sauvegarde de la partie en cours
    """
    fichier=open(sauv, 'wb') #Ouvre le fichier en mode write de manière a pouvoir écrire dedans.
    pickle.dump(xsb, fichier) #On envoie les informations xsb dans le fichier en utilisant dump
    pickle.dump(niveau, fichier) #Ainsi que les infos de niveau
    fichier.close() #Et on ferme le fichier.

def restaurationPartie(sauv, niveau):
    """
    Procède a la restauration d'une partie
    depuis la dernière sauvegarde.
    """
    testFichierSauvExiste=os.path.isfile(sauv)
    if testFichierSauvExiste:
        fichierSauv=open(sauv, 'rb') #Ouverture du fichier en mode read, on a seulement besoin de lire des infos
        pickle.load(fichierSauv) #On load uniquement le nom (ligne par ligne, comme ci dessus avec l'autre fonction)
        niveauLoad=pickle.load(fichierSauv) #On load ce qui concerne niveau, et on le remplace.
        for cle in niveau.keys():
            niveau[cle] = niveauLoad[cle]
        fichierSauv.close() #On referme le fichier
        return True #Fait
    else:   return False #Le fichier de sauvegarde est inxesistant.
