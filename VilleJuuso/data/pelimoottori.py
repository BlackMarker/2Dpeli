# -*- coding:cp1251 -*-

#Pelimoottori, jossa pelin pää looppi ja jaettu logiikka

#kirjastot
import pygame

#omat kirjastot
import hahmot
import grafiikat

pygame.init()

class Peli:
	def __init__(self):
		self.pelipaalla = 1
		#Luodaan omat luokat pelimoottorin propertyksi, mistä niihin pääsee helposti käsiksi pelimoottoriluokan sisällä
		self.RUUTU = grafiikat.Ruutu()
		self.UKKO = hahmot.Ukko()
		#self.HUONE = kenttaluokka.huone(1)

	def main(self):
		exKelloA = 10
		while self.pelipaalla == 1:
			######################################### Näppäimistön kuuntelu ###################################
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.pelipaalla = 0

				if event.type == pygame.KEYDOWN:
					pohjassa = pygame.key.get_pressed()
					if pohjassa[pygame.K_w]:
						#Kerro ukkoluokalle haluttu liikkumisuunta
						#HOX HOX y akseli on käänteinen koska screen pixels alkaa yläreunasta arvolla 0 ja kasvaa alaspäin
						#UKKO.Menossa(kummalla akselilla halutaan mennä, mihin suuntaan)
						self.UKKO.Menossa(1, -3)
					if pohjassa[pygame.K_s]:
						#Kerro ukkoluokalle liikkumisuunta
						self.UKKO.Menossa(1, 3)
					if pohjassa[pygame.K_d]:
						#Kerro ukkoluokalle liikkumisuunta
						self.UKKO.Menossa(0, 3)
					if pohjassa[pygame.K_a]:
						#Kerro ukkoluokalle liikkumisuunta
						self.UKKO.Menossa(0, -3)

					#Ukon liikkumisen pysäytys kun nappi nousee pohjasta
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_w or event.key == pygame.K_s:
						self.UKKO.Menossa(1, 0)
					if event.key == pygame.K_a or event.key == pygame.K_d:
						self.UKKO.Menossa(0, 0)
			self.UKKO.Liiku()
			kello = pygame.time.get_ticks() #Kulunut aika pelin aloittamisesta
			fpsRajoitin = pygame.time.Clock()
			fpsRajoitin.tick(60)
			objectit = [self.UKKO]
			self.RUUTU.PaivitaObjectit(objectit) #anna grafiikkaluokalle loopin aikana muutetut objectit
			exKelloA = self.RUUTU.PiirraKaikki(kello, exKelloA) #Piirrä objectit ruudulle








			
