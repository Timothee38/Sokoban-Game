# -*- coding: utf-8 -*-
"""
Created on Fri Mar 13 14:24:09 2015

Module basé sur WConio et permettant de conserver des fonctionnalités de 
debuggage dans l'interpreteur Python de l'IDE
Utilise la variable sys.flags.interactive pour basuler entre des 
fonctions WConio et des fonctions de l'interpréteur Python.

@author: barasc
"""

import sys
import WConio

# Définition d'un sous-ensemble de couleur
BLACK = WConio.BLACK
BLUE = WConio.BLUE
GREEN = WConio.GREEN
CYAN = WConio.CYAN
RED = WConio.RED
MAGENTA = WConio.MAGENTA
BROWN = WConio.BROWN
LIGHTGRAY = WConio.LIGHTGRAY
YELLOW = WConio.YELLOW
WHITE = WConio.WHITE


# ******************************************
def clrscr() :
    """Efface la console Windows"""
    if sys.flags.interactive == 0 : # en WConio
        WConio.clrscr()
        
# ******************************************
def cputs( car ) :
    """Affiche une chaine de caractère"""
    if sys.flags.interactive == 1 : # en execfile
       print car
    else : # en WConio
        WConio.cputs( car )
        
# ******************************************
def getkey( ) :
    """Renvoie la touche ou la chaine de caractère saisie par l'utilisateur"""
    if sys.flags.interactive == 1 : # en execfile
       return raw_input()
    else : # en WConio
        return WConio.getkey( )
        
# ******************************************
def gotoxy(x, y) :
    """Positionne le curseur en console"""
    if sys.flags.interactive == 0 : # en WConio
        WConio.gotoxy(x, y)

# ******************************************
def settitle( chaine ) :
    """Modifie le titre de la console, ou l'affiche dans l'interpreteur"""
    if sys.flags.interactive == 0 :
        WConio.settitle(chaine)
    else :
        print "TITRE :", chaine
        
# ******************************************        
def textbackground( color ) : 
    """Modifie la couleur de fond de la console"""
    if sys.flags.interactive == 0 :
        WConio.textbackground( color )
        
# ******************************************
def textcolor( couleur ) :
    """Modifie la couleur du style de la console"""
    if sys.flags.interactive == 0 : # en WConio
        WConio.textcolor( couleur )





