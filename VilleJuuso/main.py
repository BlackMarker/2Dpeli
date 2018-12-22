# -*- coding:cp1252 -*-

#Juuson ja Villen Peli projekti 2018


#kirjastot
import pygame
import sys
import platform
import os

polku = os.path.dirname(os.path.abspath(__file__)) #Ohjelman suoritettava polku
kirjastopolku = polku + "/data/" #Oman kirjaston polun lisääminen pythoniin Linuxilla
#kirjastopolku = polku + "\data\" #Oman kirjaston polun lisääminen pythoniin windowsilla
print "polku on:" + kirjastopolku
sys.path.append(kirjastopolku) #sisällytetään omat kirjastot

import pelimoottori

print "Kaikki kirjastot loytyy!"

def main():
	print "main 1 toimii"
	PELI = pelimoottori.Peli()
	PELI.main()
	print "suljit pelin..."

main()


