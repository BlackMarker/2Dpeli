# -*- coding:cp1251 -*-

#hahmoille luokka

import pygame

class Ukko:
	def __init__(self):
		#statsit
		self.happi = 120 #2 min.
		self.elama = 20
		self.ammukset = 5
		self.maxAmmukset = 20
		self.armor = 0 #arvo joka miinustetaan vihun lämästä
		self.koko = [16,24] #ukon hit box

		#liikkuminen
		self.koords = [0,0]
		self.nopeus_x = 0
		self.nopeus_y = 0
		self.maxNopeus_x = 4
		self.maxNopeus_y = 6
		self.kiihtyvyys_x = 1 #Nopeus yksikköä framessa, juostessa
		self.kiihtyvyys_y = 0 #ukon kiihtyvyys ylöspäin (hypyn alussa saa arvon ja alkaa vähenemään hypyn aikana)
		self.haluttuSuunta = [0,0] #mihinkä suuntaan ollaan liikuttamassa ukkoa näppäimistöllä (x-akseli, y-akseli) on vain suunta arvo ei nopeus

		#animointi
		kuva1 = pygame.image.load("media/spritet/hahmo_1.png")
		self.kaikkiSpritet = [kuva1] #kaikki ukon mahdolliset animaatio kuvat
		self.animoitavat = [0] #spritet joita animoidaan tässä järjestyksessä vuoronperään
		self.animMenossa = 0

	
	def Liiku(self):
		#Nyt kömpelö liikkuminen testaamiseen, joka pitää parannella
		self.koords[0] += self.haluttuSuunta[0]
		self.koords[1] += self.haluttuSuunta[1]

	def Menossa(self, akseli, paljonko):
		self.haluttuSuunta[akseli] = paljonko

	def VaihdaAnimoitava(self):
		#Vaihtaa animointi numeron seuraavaan numeroon 
		if len(self.animoitavat) > self.animMenossa: #jos on vielä animoitavia spritejä animoitavat listassa
			self.animMenossa += 1
		if len(self.animoitavat) == self.animMenossa: #animoitavien spritejen pää saavutettu --> aloita alusta listan pyöritys
			self.animMenossa = 0
		if self.animMenossa > len(self.animoitavat): #Voi tulla tapaus kun hypätään suuremmasta animointikuva määrästä pienempää ja tässä korjataan se
			self.animMenossa = 0


	def Teleporttaa(self, koords):
		self.koords = koords
	
	def TeleporttaaSuhteellisesti(self, koords):
		self.koords[0] += koords[0]
		self.koords[1] += koords[1]
