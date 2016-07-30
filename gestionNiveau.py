#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Timothee & Jérémy
#
# Created:     26/03/2015
# Copyright:   (c) Timothee 2015
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
# -*- Coding: UTF-8 -*-
def initialisationNiveauPourTest():
    """
   Initialise une grille de base de la forme:
   ####
   #  ###
   #  $@#
   # *. #
   ##   #
    #####
   le tout sous la forme d'un dictionnaire
   donnant les positions de chacune des entités du
   puzzle sur la grille.
   """
    niveau = {'murs': [(0, 0), (1, 0), (2, 0), (3, 0), (0, 1), (3, 1), (4, 1), (5, 1), (0, 2), (5, 2),
    (0, 3), (5, 3), (0, 4), (1, 4), (5, 4), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)], 'cibles': [(2, 3), (3, 3)],
    'caisses': [(3, 2), (2, 3)], 'perso': (4, 2), 'score': 0, 'estFini': False,'historique':[]}
    return niveau




def indiceCaisseDansNiveau(niveau, position):
    """
   Regarde s'il existe une caisse à la position
   position dans le dictionnaire niveau et renvoie
   l'indice de cette position, sinon renvoie -1

   position est un tuple
   niveau un dictionnaire
   """
    for i in range(len(niveau['caisses'])):     #Parcours de la liste des caisses (les tuples)
        if position==niveau['caisses'][i]:
            return i
    return -1



def deplacementCaisse(niveau,indice,direction):
    """
   déplace la caisse dans la direction indiquée si elle ne rencontre pas un mur
   ou une autre caisse revoie false si la caisse n'est pas déplacée et true si aucun
   obstacle rencontré.

   niveau est un dictionnaire,
   indice un entier,
   direction une chaine de caractères.
   """
    (x,y)=niveau['caisses'][indice]                 #donne les coordonné de la caisse en paramètre sous la forme x,y
    if(direction=='up'):        #déplace la caisse vers le haut si different de condition
        (x,y)=(x,y-1)
    elif(direction=='right'):   #déplace la caisse vers la droite si different de condition
        (x,y)=(x+1,y)
    elif(direction=='left'):    #déplace la caisse vers la gauche si different de condition
        (x,y)=(x-1,y)
    elif(direction=='down'):    #déplace la caisse vers le bas si different de condition
        (x,y)=(x,y+1)

    condition=((x,y) in niveau['murs']) or ((x,y) in niveau['caisses']) #condition vérifie si il y a un mur ou une caisse(true) sinon false
    if condition:
        return False

    niveau['caisses'][indice]=(x,y)
    return True




def deplacementPerso(niveau,direction):
    """
  Deplace le personnage dans la direction indiquée
  selon la touche du clavier actionnée
  sur la grille

  niveau est un dictionnaire
  et direction une chaine de caractères.
  """

    # niveau est un dictionnaire, direction une chaine de caractères de la forme 'string' #
    #Les "return" arrêtent la fonction

    x=niveau['perso'][0]    #Definition en x de la position du personnage
    y=niveau['perso'][1]    #Definition en y de la position du personnage

    posPerso=niveau['perso']

    if direction=='up':         #Si la direction est "haut"...
        newPosPerso=(x, y-1)    #Changement de la position du personnage sur la grille niveau
    elif direction=='down':
        newPosPerso=(x,y+1)
    elif direction=='left':
        newPosPerso=(x-1,y)
    elif direction=='right':
        newPosPerso=(x+1,y)

    if (newPosPerso not in niveau['murs']) and (newPosPerso not in niveau['caisses']): #S'il n'y a pas d'obstacle (caisse ou mur)
        niveau['historique'].append((posPerso,))
        niveau['perso']=newPosPerso
        return True
    if newPosPerso in niveau['caisses']:  #S'il y a une caisse...
        indice=indiceCaisseDansNiveau(niveau, newPosPerso)
        caisseDeplacable=deplacementCaisse(niveau, indice, direction)
        if caisseDeplacable:    #Si cette caisse est déplaçable...
            niveau['perso']=newPosPerso
            niveau['historique'].append((posPerso, indice, newPosPerso))
            return True
    else:
        return False



def incrementScore(niveau):
    """
   Augment le score a chaque coup en ajoutant +1

   niveau est une dictionnaire.
   """
    niveau['score']+=1
    return niveau

def testCaisseToutesRanges(niveau):
    """
   Vérifie si il y a des caisse sur l'emplacement des cible si tel est le cas la clé estFini prend la valeur true
   pour finir le niveau.

   niveau est un dictionnaire.
   """

    #A CHAQUE DEPLACEMENT, RELANCER CETTE FONCTION

    total=0 #Nombre de caisses sur des cibles
    listeCaisses=niveau['caisses']
    listeCibles=niveau['cibles']
    for caisse in listeCaisses: #Parcours de toutes les caisses
        if caisse in listeCibles: #Si une des caisses est sur une cible:
            total+=1

    if total==len(listeCaisses): #Si le total des caisses sur des cibles correspond au nombre total de caisses:
        niveau['estFini']=True   #estFini devient True

    return niveau


def chargementDonneesNiveau(niveau, fichier):
    """
   réinitialise le dictionnaire niveau et le re-remplit
   à l'aide de "fichier"
   """
    fd = open(fichier, 'r')
    listeLignes=fd.readlines()
    listeMurs=[]
    listeCibles=[]
    listeCaisses=[]
    for i in range(len(listeLignes)):
        if listeLignes[i][0]=="T":
            break
        for j in range(len(listeLignes[i])):
            if listeLignes[i][j]=="#":
                listeMurs.append((j,i))
            elif listeLignes[i][j]=="$":
                listeCaisses.append((j,i))
            elif listeLignes[i][j]==".":
                listeCibles.append((j,i))
            elif listeLignes[i][j]=="@":
                niveau['perso']=(j,i)
            elif listeLignes[i][j]=="*":
                listeCibles.append((j,i))
                listeCaisses.append((j,i))
            elif listeLignes[i][j]=="+":
                listeCibles.append((j,i))
                niveau['perso']=(j,i)

    niveau['cibles']=listeCibles
    niveau['caisses']=listeCaisses
    niveau['murs']=listeMurs
    niveau['score']=0
    niveau['estFini']=False
    niveau['historique']=[]
    fd.close()
    return niveau

def annuleDernierDeplacement(niveau):
    """
    Annule le dernier déplacement du joueur en fonction
    de l'historique
    """
    if niveau['historique']!=[]:
        dernierePos=niveau['historique'][-1] #On récupère le dernier élément de la liste  correspondant a historique (tuple)
        if (len(dernierePos))>1:  #Si il y a aussi une caisse...
            indice=dernierePos[1]
            niveau['caisses'][indice]=dernierePos[-1] #On change la position de la caisse pour la repositionner.
        niveau['perso']=dernierePos[0]  #On déplace le perso a sa position précedente
        del niveau['historique'][-1]
        return True
    else:
        return False





