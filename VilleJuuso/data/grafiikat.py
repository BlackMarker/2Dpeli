# -*- coding:cp1251 -*-

#Grafiikkaluokka mikä saa pelin objectit listassa [pelaaja, vihut, jutut] sekä hoitaa kaiken piirtämisen näytölle. Ja vain piirtämisen 

import pygame
pygame.init() #Alustetaan pygame joka aloittaa pygame ajastimen ja mahdollistaa ruudun luonnin
import time

class Ruutu:
	def __init__(self):
		leveys = 1200
		korkeus = 800 #pixeliä
		self.naytto = pygame.display.set_mode((leveys, korkeus), 0)
		self.objectit = [] #Lista missä kaikki piirrettävät asiat
		self.huone = [] #Lista missä ladatun alueen tileset
		self.taustavari = (0,0,0)

	def PiirraKaikki(self, kello, exKello):
		#exkello on aika milloinka viimeksi vaihdettiin animoitavat kuvat ja kello paljonko aika on nytten (kulunutta sekuntia)
		self.naytto.fill(self.taustavari)
		self.PiirraHuone()
		exKello = self.PiirraObjectit(kello, exKello)
		pygame.display.update()
		viimeksiVaihdettu = 0 #milloinka viimeksi vaihdettiin animoitava kuva (jeasarikorjaus nyt)
		return viimeksiVaihdettu

	def PiirraHuone(self):
		#Kartan piirto taakse
		pass

	def PiirraObjectit(self, kello, exKello):
		#Kaikkien objectien piirto (eli kaikki mitkä hahmo luokassa)
		for objecti in self.objectit:
			self.naytto.blit(objecti.kaikkiSpritet[objecti.animoitavat[objecti.animMenossa]], (objecti.koords[0], objecti.koords[1]))
			#Piirrä näytölle(objectin spriteistä[animoitavistaSpriteistä[animaatio menossa nro]], (näytön koordinaatteihin))


	#Ruutu luokan propertyjen muutto (eli kartan ja objectien päivitys)
	def PaivitaObjectit(self, objectit):
		self.objectit = objectit

	def PaivitaHuone(self, huone):
		self.huone = huone

	def VaihdaTaustaVari(self, vari):
		self.taustavari = taustavari
