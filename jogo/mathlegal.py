#!/usr/bin/env python

import pygame, sys, random
from time import sleep
from pygame.locals import *

if not pygame.font: print 'Warning, fonts disabled'
if not pygame.mixer: print 'Warning, sound disabled'

# set up pygame
class MathLegal:
	"""A Classe principal Mathlegal - Esta classe manipula o principal
	inicializacao e criacao do jogo."""

	def __init__(self, width=640,height=480):
		"""Inicializa"""
		"""Inicializa PyGame"""
		pygame.init()
		self.mainClock = pygame.time.Clock()
		self.font = pygame.font.SysFont('Arial', 48)
		pygame.mouse.set_visible(True)
		"""Seta o tamanho do janela"""
		self.background = pygame.image.load("img/fundo.png")
		self.backgroundRect = self.background.get_rect()
		self.size = (width, height) = self.background.get_size()

		self.logo1 = pygame.image.load("img/logo1.png")
		self.logo1Rect = self.logo1.get_rect()
		self.logopos = self.logo1.get_rect(centerx=self.background.get_width() / 2)
		"""Cria a tela"""
		self.screen = pygame.display.set_mode((self.size), 0, 32)
		pygame.display.set_caption('Matematica Legal')
			

		# set up the player and food data structure
		self.RED = (255, 0, 0)
		self.GREEN = (0, 255, 0)
		self.BLUE = (0, 0, 255)
		self.WHITE = (0, 0, 0)
		self.RESULT = True
		self.START = True
		self.START2 = True
		self.QUIZ = True
		self.FINAL = False
		self.OP = ""
		self.LOAD = True

		# Listas
		self.desafio = []
		self.fichas = []
		self.pre_result = []
		self.img = []
		self.img_r = []
		self.img_g = []
		self.img_b = []
		self.img_y = []
	
		# Numeros vermelhos 
		self.img.append({'img':self.rescale("img/r-0.png"), 'cor':'red', 'num':0})
		self.img.append({'img':self.rescale("img/r-1.png"), 'cor':'red', 'num':1})
		self.img.append({'img':self.rescale("img/r-2.png"), 'cor':'red', 'num':2})
		self.img.append({'img':self.rescale("img/r-3.png"), 'cor':'red', 'num':3})
		self.img.append({'img':self.rescale("img/r-4.png"), 'cor':'red', 'num':4})
		self.img.append({'img':self.rescale("img/r-5.png"), 'cor':'red', 'num':5})
		self.img.append({'img':self.rescale("img/r-6.png"), 'cor':'red', 'num':6})
		self.img.append({'img':self.rescale("img/r-7.png"), 'cor':'red', 'num':7})
		self.img.append({'img':self.rescale("img/r-8.png"), 'cor':'red', 'num':8})
		self.img.append({'img':self.rescale("img/r-9.png"), 'cor':'red', 'num':9})

		# Numeros verdes
		self.img.append({'img':self.rescale("img/g-0.png"), 'cor':'green', 'num':0})
		self.img.append({'img':self.rescale("img/g-1.png"), 'cor':'green', 'num':1})
		self.img.append({'img':self.rescale("img/g-2.png"), 'cor':'green', 'num':2})
		self.img.append({'img':self.rescale("img/g-3.png"), 'cor':'green', 'num':3})
		self.img.append({'img':self.rescale("img/g-4.png"), 'cor':'green', 'num':4})
		self.img.append({'img':self.rescale("img/g-5.png"), 'cor':'green', 'num':5})
		self.img.append({'img':self.rescale("img/g-6.png"), 'cor':'green', 'num':6})
		self.img.append({'img':self.rescale("img/g-7.png"), 'cor':'green', 'num':7})
		self.img.append({'img':self.rescale("img/g-8.png"), 'cor':'green', 'num':8})
		self.img.append({'img':self.rescale("img/g-9.png"), 'cor':'green', 'num':9})


		# Numeros azuis
		self.img.append({'img':self.rescale("img/b-1.png"), 'cor':'blue', 'num':0})
		self.img.append({'img':self.rescale("img/b-2.png"), 'cor':'blue', 'num':1})
		self.img.append({'img':self.rescale("img/b-3.png"), 'cor':'blue', 'num':2})
		self.img.append({'img':self.rescale("img/b-4.png"), 'cor':'blue', 'num':3})
		self.img.append({'img':self.rescale("img/b-5.png"), 'cor':'blue', 'num':4})
		self.img.append({'img':self.rescale("img/b-6.png"), 'cor':'blue', 'num':5})
		self.img.append({'img':self.rescale("img/b-7.png"), 'cor':'blue', 'num':6})
		self.img.append({'img':self.rescale("img/b-8.png"), 'cor':'blue', 'num':7})
		self.img.append({'img':self.rescale("img/b-9.png"), 'cor':'blue', 'num':9})

		# Numeros amarelos
		self.img.append({'img':self.rescale("img/y-0.png"), 'cor':'yellow', 'num':0})
		self.img.append({'img':self.rescale("img/y-1.png"), 'cor':'yellow', 'num':1})
		self.img.append({'img':self.rescale("img/y-2.png"), 'cor':'yellow', 'num':2})
		self.img.append({'img':self.rescale("img/y-3.png"), 'cor':'yellow', 'num':3})
		self.img.append({'img':self.rescale("img/y-4.png"), 'cor':'yellow', 'num':4})
		self.img.append({'img':self.rescale("img/y-5.png"), 'cor':'yellow', 'num':5})
		self.img.append({'img':self.rescale("img/y-6.png"), 'cor':'yellow', 'num':6})
		self.img.append({'img':self.rescale("img/y-7.png"), 'cor':'yellow', 'num':7})
		self.img.append({'img':self.rescale("img/y-8.png"), 'cor':'yellow', 'num':8})
		self.img.append({'img':self.rescale("img/y-9.png"), 'cor':'yellow', 'num':9})

		for x in self.img:
			x.update({'rect':x['img'].get_rect()})


	def rescale(self, tmp):
		self.tmp = pygame.image.load(tmp)
		return pygame.transform.scale(self.tmp, (50, 50))

	def drawImg(self, sprite, x, y):
		self.sprite = sprite['img']
		self.spriteRect = self.sprite.get_rect()
		self.spriteRect.topleft = (x, y)
		self.screen.blit(self.sprite, self.spriteRect)

	def drawImg2(self, sprite):
		self.sprite = sprite['img']
		self.spriteRect = self.sprite.get_rect()
		self.spriteRect.topleft = sprite['pos']
		self.screen.blit(self.sprite, self.spriteRect)

	def drawOp(self, op, x, y):
		self.op = op
		self.op = self.font.render(self.op, 1, (0, 0, 0), (255,255,255))
		self.opRect = self.op.get_rect()
		self.opRect.topleft = (x, y)
		self.screen.blit(self.op, self.opRect)

	def drawText(text, font, surface, x, y,f,b):
		textobj = font.render(text, 1, f, b)
		textrect = textobj.get_rect()
		textrect.topleft = (x, y)
		return textobj, textrect, text

	def getNum(self):
		random.shuffle(self.img)
		self.tmp = self.img.pop()
		self.fichas.append(self.tmp)
		return self.tmp

	def getOp(self):
		self.tmp = ["+","-","*","/"]
		random.shuffle(self.tmp)
		random.shuffle(self.tmp)
		random.shuffle(self.tmp)
		self.OP = self.tmp.pop()
		return self.OP
	
	def refreshBackground(self):
		self.screen.blit(self.background, self.backgroundRect)
		self.screen.blit(self.logo1, self.logopos)


	def init_screen(self):
		self.refreshBackground()

		self.drawImg(self.getNum(), ((self.size[0] / 3) - 100), (self.size[1] / 3))
		pygame.display.update()
		sleep(1)

		self.drawOp(self.getOp(), ((self.size[0] / 3)), (self.size[1] / 3))
		pygame.display.update()
		sleep(1)

		self.drawImg(self.getNum(), ((self.size[0] / 3) + 100), (self.size[1] / 3))
		pygame.display.update()
		sleep(1)
	
	def loadFichas(self):
		lugar = []
		lugar = [
				(((self.size[0] / 3) - 140),(self.size[1] / 3)),
				(((self.size[0] / 3) - 60), (self.size[1] / 3)),
				(((self.size[0] / 3) + 30), (self.size[1] / 3)),
				(((self.size[0] / 3) + 160), (self.size[1] / 3)),
				(((self.size[0] / 3) - 110), (self.size[1] / 2)),
				(((self.size[0] / 3) + 90), (self.size[1] / 2)),
				(((self.size[0] / 3) + 90), (self.size[1] / 2)),
				(((self.size[0] / 3) + 200), (self.size[1] / 2)),
				]


		self.fichas[0].update({'pos':lugar.pop()})
		self.fichas[1].update({'pos':lugar.pop()})

		for x in self.fichas[:]:
			self.desafio.append(x)

		for x in range(1,7):
			self.desafio.append(self.img[x])
			self.desafio[x].update({'pos':lugar.pop()})

		print self.desafio

	def quiz(self):
		if self.LOAD:
			self.loadFichas()
			self.LOAD = False

		self.drawImg2(self.desafio[0])
		self.drawImg2(self.desafio[1])
		self.drawImg2(self.desafio[2])
		self.drawImg2(self.desafio[3])
		self.drawImg2(self.desafio[4])
		self.drawImg2(self.desafio[5])
		self.drawImg2(self.desafio[6])
		#self.drawImg2(self.desafio[7])

	def test_fichas(self):

		aux = int(14)

		test = int(self.pre_result[0])
		test += int(self.pre_result[1])
		test += int(self.pre_result[2])
    
		if aux == test:
			return
		else:
			self.screen.fill(self.RED)
			x, y, t = self.drawText('LAMENTO, VOCE NAO ACERTOU 8-( !!!', self.font, self.screen, self.screen.get_rect().centerx, 160, self.WHITE, self.BLUE )
			y.centerx = self.screen.get_rect().centerx
			y.centery = self.screen.get_rect().centery
			pygame.draw.rect(self.screen.WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
			self.screen.blit(x,y)
			pygame.display.update()
			sleep(10)
			sys.exit(0)
           

	def final(self):
		global FINAL
		FINAL = True
		init_screen_2()

	def test_click(self, x, y):
		if self.FINAL:
			for cont in self.desafio:
				if cont['textrect'].collidepoint(x,y):
					aux = int(cont['num'])

					test = int(pre_result[0])
					test += int(pre_result[1])
					test += int(pre_result[2])
	
					if aux == test:
						self.screen.fill(WHITE)
						x, y, t = drawText('PARABENS VOCE GANHOU ;-) !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, BLUE, RED )
						y.centerx = windowSurface.get_rect().centerx
						y.centery = windowSurface.get_rect().centery
						pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
						self.screen.blit(x,y)
						pygame.display.update()
						sleep(10)
						sys.exit(0)
                    
					else:
						self.screen.fill(RED)
						x, y, t = drawText('LAMENTO, VOCE NAO GANHOU 8-( !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, WHITE, BLUE )
						y.centerx = windowSurface.get_rect().centerx
						y.centery = windowSurface.get_rect().centery
						pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
						self.screen.blit(x,y)
						pygame.display.update()
						sleep(10)
						sys.exit(0)

		for cont in self.fichas:       
			print cont['rect']
			if cont['rect'].collidepoint(x,y):
				print "aqui"
				self.pre_result.append(cont['num'])
				if len(self.pre_result) == 3:
					self.test_fichas()
					self.QUIZ = False
					self.final()
				break
			else:
				print "nao"

            
   

	def MainLoop(self):
		"""Este eh o loop principal do jogo"""
		"""Draw the blocks onto the background, since they only need to be drawn once"""
		


# run the game loop
		while True:
			# check for events
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
					
				if event.type == MOUSEBUTTONUP:
					print("Mouse call! "+str(event.pos[0])+ " " +str(event.pos[1]))
					self.test_click(event.pos[0], event.pos[1])

    		# draw the black background onto the surface
			self.refreshBackground()
    

			# draw the player onto the surface
			if self.START:
				self.init_screen()
				self.START = False
    
			if self.QUIZ:
				self.quiz()        

			if self.FINAL:
				self.final()
   
			# draw the window onto the screen
			pygame.display.update()
			self.mainClock.tick(60)


if __name__ == "__main__":
    MainWindow = MathLegal()
    MainWindow.MainLoop()
