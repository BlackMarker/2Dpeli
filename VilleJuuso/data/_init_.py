# -*- coding:cp1251 -*-

#hahmoille luokka

class Hahmo:
	def __init__(self):
		self.happi = 120 #2 min.
		self.elama = 20
		self.kiihtyvyys_x = 1 #Nopeus yksikköä framessa, juostessa
		self.nopeus = 0
		self.maxNopeus = 4
		self.ammukset = 5
		self.maxAmmukset = 20
		self.koords = [0,0]
		self.koko = [16,24] #ukon hit box
		self.kiihtyvyys_y = 0 #ukon kiihtyvyys ylöspäin (hypyn alussa saa arvon ja alkaa vähenemään hypyn aikana)
		self.armor = 0 #arvo joka miinustetaan vihun lämästä

		self.kaikkiSpritet = ["","",""] #kaikki ukon mahdolliset animaatio kuvat
		self.animoitavatSpritet = [1,2] #spritet joita animoidaan tässä järjestyksessä vuoronperään
