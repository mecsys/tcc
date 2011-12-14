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
		font = pygame.font.SysFont('Arial', 48)
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
		RESULT = True
		START = True
		START2 = True
		QUIZ = True
		FINAL = False

		# Listas
		desafio = []
		fichas = []
		pre_result = []
		self.img_r = []
		self.img_g = []
		self.img_b = []
		self.img_y = []
	
		# Numeros vermelhos 
		self.img_r.append({'img':self.rescale("img/r-0.png"), 'cor':'red', 'num':0})
		self.img_r.append({'img':self.rescale("img/r-1.png"), 'cor':'red', 'num':1})
		self.img_r.append({'img':self.rescale("img/r-2.png"), 'cor':'red', 'num':2})
		self.img_r.append({'img':self.rescale("img/r-3.png"), 'cor':'red', 'num':3})
		self.img_r.append({'img':self.rescale("img/r-4.png"), 'cor':'red', 'num':4})
		self.img_r.append({'img':self.rescale("img/r-5.png"), 'cor':'red', 'num':5})
		self.img_r.append({'img':self.rescale("img/r-6.png"), 'cor':'red', 'num':6})
		self.img_r.append({'img':self.rescale("img/r-7.png"), 'cor':'red', 'num':7})
		self.img_r.append({'img':self.rescale("img/r-8.png"), 'cor':'red', 'num':8})
		self.img_r.append({'img':self.rescale("img/r-9.png"), 'cor':'red', 'num':9})

		# Numeros verdes
		self.img_g.append({'img':self.rescale("img/g-0.png"), 'cor':'green', 'num':0})
		self.img_g.append({'img':self.rescale("img/g-1.png"), 'cor':'green', 'num':1})
		self.img_g.append({'img':self.rescale("img/g-2.png"), 'cor':'green', 'num':2})
		self.img_g.append({'img':self.rescale("img/g-3.png"), 'cor':'green', 'num':3})
		self.img_g.append({'img':self.rescale("img/g-4.png"), 'cor':'green', 'num':4})
		self.img_g.append({'img':self.rescale("img/g-5.png"), 'cor':'green', 'num':5})
		self.img_g.append({'img':self.rescale("img/g-6.png"), 'cor':'green', 'num':6})
		self.img_g.append({'img':self.rescale("img/g-7.png"), 'cor':'green', 'num':7})
		self.img_g.append({'img':self.rescale("img/g-8.png"), 'cor':'green', 'num':8})
		self.img_g.append({'img':self.rescale("img/g-9.png"), 'cor':'green', 'num':9})


		# Numeros azuis
		self.img_b.append({'img':self.rescale("img/b-1.png"), 'cor':'blue', 'num':0})
		self.img_b.append({'img':self.rescale("img/b-2.png"), 'cor':'blue', 'num':1})
		self.img_b.append({'img':self.rescale("img/b-3.png"), 'cor':'blue', 'num':2})
		self.img_b.append({'img':self.rescale("img/b-4.png"), 'cor':'blue', 'num':3})
		self.img_b.append({'img':self.rescale("img/b-5.png"), 'cor':'blue', 'num':4})
		self.img_b.append({'img':self.rescale("img/b-6.png"), 'cor':'blue', 'num':5})
		self.img_b.append({'img':self.rescale("img/b-7.png"), 'cor':'blue', 'num':6})
		self.img_b.append({'img':self.rescale("img/b-8.png"), 'cor':'blue', 'num':7})
		self.img_b.append({'img':self.rescale("img/b-9.png"), 'cor':'blue', 'num':9})

		# Numeros amarelos
		self.img_y.append({'img':self.rescale("img/y-0.png"), 'cor':'yellow', 'num':0})
		self.img_y.append({'img':self.rescale("img/y-1.png"), 'cor':'yellow', 'num':1})
		self.img_y.append({'img':self.rescale("img/y-2.png"), 'cor':'yellow', 'num':2})
		self.img_y.append({'img':self.rescale("img/y-3.png"), 'cor':'yellow', 'num':3})
		self.img_y.append({'img':self.rescale("img/y-4.png"), 'cor':'yellow', 'num':4})
		self.img_y.append({'img':self.rescale("img/y-5.png"), 'cor':'yellow', 'num':5})
		self.img_y.append({'img':self.rescale("img/y-6.png"), 'cor':'yellow', 'num':6})
		self.img_y.append({'img':self.rescale("img/y-7.png"), 'cor':'yellow', 'num':7})
		self.img_y.append({'img':self.rescale("img/y-8.png"), 'cor':'yellow', 'num':8})
		self.img_y.append({'img':self.rescale("img/y-9.png"), 'cor':'yellow', 'num':9})

	def rescale(self, img):
		self.img = pygame.image.load(img)
		return pygame.transform.scale(self.img, (50, 50))

	def init_screen(self):
		#self.screen.blit(self.img_b[0], ((self.size[0] / 3) - 100, (self.size[1] / 3)))
		self.drawImg(self.img_r[0]['img'], ((self.size[0] / 3) - 100), (self.size[1] / 3))
		self.drawImg(self.img_g[1]['img'], ((self.size[0] / 3)), (self.size[1] / 3))
		self.drawImg(self.img_b[2]['img'], ((self.size[0] / 3) + 100), (self.size[1] / 3))

	def MainLoop(self):
		"""Este eh o loop principal do jogo"""
		"""Draw the blocks onto the background, since they only need to be drawn once"""
		self.screen.blit(self.background, self.backgroundRect)
		self.screen.blit(self.logo1, self.logopos)
		
		self.init_screen()
		pygame.display.flip()

		# run the game loop
		while True:
		# check for events
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
		
	def drawImg(self, img, x, y):
		self.img = img
		self.imgRect = self.img.get_rect()
		self.imgRect.topleft = (x, y)
		self.screen.blit(self.img, self.imgRect)
		return self.img, self.imgRect, 

	def drawText(text, font, surface, x, y,f,b):
		textobj = font.render(text, 1, f, b)
		textrect = textobj.get_rect()
		textrect.topleft = (x, y)
		return textobj, textrect, text

#for i in range(7):
#    x, y, t = drawText('8', font, windowSurface, windowSurface.get_rect().centerx, 160, GREEN, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    x, y, t = drawText('9', font, windowSurface, 100, 160, YELLOW, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    x, y, t = drawText('1', font, windowSurface, 400, 160, BLUE, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    x, y, t = drawText('3', font, windowSurface, 30, 360, RED, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    x, y, t = drawText('5', font, windowSurface, 150, 360, BLUE, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    x, y, t = drawText('2', font, windowSurface, 320, 360, RED, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    x, y, t = drawText('7', font, windowSurface, 540, 360, GREEN, WHITE )
#    fichas.append({'text':x, 'textrect':y, 'num':t})

#    random.shuffle(fichas)
    

#	def init_screen():
#    x, y, t = drawText('7', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
#		self.screen.blit(img[0], (self.size[0] / 3) - 100, (self.size[1] / 3)) 
#    desafio.append({'num':t, 'textrect':y})
#    windowSurface.blit(x,y)
#    pygame.display.update()
#    sleep(1)

#    x, y, t  = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
#    desafio.append({'num':t, 'textrect':y})
#    windowSurface.blit(x,y)
#    pygame.display.update()
#    sleep(1)

#    x, y, t = drawText('2', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
#    desafio.append({'num':t, 'textrect':y})
#    windowSurface.blit(x,y)
#    pygame.display.update()
#    sleep(1)    

#    x, y, t = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
#    desafio.append({'num':t, 'textrect':y})
#    windowSurface.blit(x,y)
#    pygame.display.update()
#    sleep(1)    

#    x, y, t = drawText('5', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
#    desafio.append({'num':t, 'textrect':y})
#    windowSurface.blit(x,y)

#    x, y, t = drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
#    desafio.append({'num':t, 'textrect':y})
#    windowSurface.blit(x,y)
#    pygame.display.update()
#    sleep(1)

#def init_screen_2():

 #   windowSurface.fill(BLACK)

#    x, y, t = drawText('OK, Agora o resultado ;-) !!!', font, windowSurface, windowSurface.get_rect().centerx, 20, BLUE, WHITE )
 #   y.centerx = windowSurface.get_rect().centerx
 #   windowSurface.blit(x,y)

 #   x, y, t = drawText('7', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
 #   desafio.append({'num':t, 'textrect':y})
 #   windowSurface.blit(x,y)
    

 #   x, y, t  = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) - 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
 #   desafio.append({'num':t, 'textrect':y})
 #   windowSurface.blit(x,y)
   

#    x, y, t = drawText('2', font, windowSurface, (WINDOWWIDTH / 3), (WINDOWHEIGHT / 3),(255,0,0),(255,255,255))
 #   desafio.append({'num':t, 'textrect':y})
 #   windowSurface.blit(x,y)
    

 #   x, y, t = drawText('+', font, windowSurface, (WINDOWWIDTH / 3) + 50, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
 #   desafio.append({'num':t, 'textrect':y})
 #   windowSurface.blit(x,y)
      

 #   x, y, t = drawText('5', font, windowSurface, (WINDOWWIDTH / 3) + 100, (WINDOWHEIGHT / 3),(0,0,255),(255,255,255))
 #   desafio.append({'num':t, 'textrect':y})
 #   windowSurface.blit(x,y)

#    x, y, t = drawText('=', font, windowSurface, (WINDOWWIDTH / 3) + 150, (WINDOWHEIGHT / 3),(0,255,0),(0,0,0))
  #  desafio.append({'num':t, 'textrect':y})
 #   windowSurface.blit(x,y)
    

    #Solucao
 #   x, y, t = drawText('15', font, windowSurface, 150 , 350, BLUE, WHITE)
 #   desafio.append({'num':t, 'textrect':y})
 #   pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
 #   windowSurface.blit(x,y)
    
    

 #   x, y, t = drawText('14', font, windowSurface, 250, 350, YELLOW, WHITE)
 #   desafio.append({'num':t, 'textrect':y})
 #   pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
 #   windowSurface.blit(x,y)
    

#    x, y, t = drawText('11', font, windowSurface, 350, 350, RED, WHITE)
#    desafio.append({'num':t, 'textrect':y})
 #   pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
 #   windowSurface.blit(x,y)
    
#def test_fichas():

 #   aux = int(14)

#    test = int(pre_result[0])
 #   test += int(pre_result[1])
 #   test += int(pre_result[2])
    
 #   if aux == test:
 #       return
 #   else:
 #       windowSurface.fill(RED)
 #       x, y, t = drawText('LAMENTO, VOCE NAO ACERTOU 8-( !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, WHITE, BLUE )
#        y.centerx = windowSurface.get_rect().centerx
 #       y.centery = windowSurface.get_rect().centery
#        pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
 #       windowSurface.blit(x,y)
 #       pygame.display.update()
 #       sleep(10)
  #      sys.exit(0)
           


#def final():
#    global FINAL
#    FINAL = True
#    init_screen_2()
#
#def test_click(x, y):
    
#    if FINAL:
 #       for cont in desafio:
 #           if cont['textrect'].collidepoint(x,y):
 #               aux = int(cont['num'])

  #              test = int(pre_result[0])
  #              test += int(pre_result[1])
  #              test += int(pre_result[2])

  #              if aux == test:
  #                  windowSurface.fill(WHITE)
  #                  x, y, t = drawText('PARABENS VOCE GANHOU ;-) !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, BLUE, RED )
  #                  y.centerx = windowSurface.get_rect().centerx
  #                  y.centery = windowSurface.get_rect().centery
  #                  pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
   #                 windowSurface.blit(x,y)
  #                  pygame.display.update()
   #                 sleep(10)
   #                 sys.exit(0)
                    
   #             else:
  #                  windowSurface.fill(RED)
  #                  x, y, t = drawText('LAMENTO, VOCE NAO GANHOU 8-( !!!', font, windowSurface, windowSurface.get_rect().centerx, 160, WHITE, BLUE )
  #                  y.centerx = windowSurface.get_rect().centerx
  #                  y.centery = windowSurface.get_rect().centery
  #                  pygame.draw.rect(windowSurface, WHITE, (y.left - 10, y.top - 10, y.width + 20, y.height + 20))
  #                  windowSurface.blit(x,y)
   #                 pygame.display.update()
  #                  sleep(10)
  #                  sys.exit(0)

 #   for cont in fichas:       
 #       if cont['textrect'].collidepoint(x,y):
 #           pre_result.append(cont['num'])
 #           if len(pre_result) == 3:
  #              test_fichas()
  #              global QUIZ
   #             QUIZ = False
   #             final()
  #          break
            
#def quiz():
      
 #   for x in fichas:       
 #       pygame.draw.rect(windowSurface, WHITE, (x['textrect'].left - 10, x['textrect'].top - 10, x['textrect'].width + 20, x['textrect'].height + 20))
 #       windowSurface.blit(x['text'], x['textrect'])
   


# run the game loop
#	while True:
		# check for events
#			for event in pygame.event.get():
#				if event.type == QUIT:
#					pygame.quit()
#					sys.exit()
					
#			if event.type == MOUSEBUTTONUP:
#				print("Mouse call!")
				#test_click(event.pos[0], event.pos[1])

# #           
    
    # draw the black background onto the surface
 #   windowSurface.fill(BLACK)

    # draw the player onto the surface
 #   if START:
 #       init_screen()
#        START = False
    
 #   if QUIZ:
  #      quiz()        

 #   if FINAL:
   #     final()
   
    # draw the window onto the screen
 #   pygame.display.update()
#    mainClock.tick(40)


if __name__ == "__main__":
    MainWindow = MathLegal()
    MainWindow.MainLoop()
