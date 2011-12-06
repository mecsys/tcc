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
	mainClock = pygame.time.Clock()
	pygame.mouse.set_visible(True)
        """Seta o tamanho do janela"""
        self.width = width
        self.height = height
        """Cria a tela"""
        self.screen = pygame.display.set_mode((self.width, self.height), 0, 32)
	pygame.display.set_caption('Matematica Legal')
	

    def MainLoop(self):
        """Este eh o loop principal do jogo"""
	self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0,255,0))
	
	"""Draw the blocks onto the background, since they only need to be 
        drawn once"""
        self.screen.draw(self.background)
	
	pygame.display.flip()
	sleep(10)

	
#pygame.init()
#mainClock = pygame.time.Clock()
#pygame.mouse.set_visible(True)

# set up the window
#WINDOWWIDTH = 640
#WINDOWHEIGHT = 480
#windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
#pygame.display.set_caption('Matematica Legal')

# set up the colors
#BLACK = (0, 0, 0)
#GREEN = (0, 255, 0)
#WHITE = (255, 255, 255)
#BLUE = (0, 0, 255)
#RED = (255, 0, 0)
#YELLOW = (0, 255, 255)

#font = pygame.font.SysFont('Arial', 48)

# set up the player and food data structure
#RESULT = True
#START = True
#START2 = True
#QUIZ = True
#FINAL = False

#desafio = []
#fichas = []
#pre_result = []

#def drawText(text, font, surface, x, y,f,b):
#    textobj = font.render(text, 1, f, b)
#    textrect = textobj.get_rect()    
#    textrect.topleft = (x, y)
#    return textobj, textrect, text

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
    

#def init_screen():
#    x, y, t = drawText('7', font, windowSurface, (WINDOWWIDTH / 3) - 100, (WINDOWHEIGHT / 3),(0,255,0),(255,255,255))
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
#while True:
#    # check for events
 #   for event in pygame.event.get():
 #       if event.type == QUIT:
  #          pygame.quit()
  #          sys.exit()
        
  #      if event.type == MOUSEBUTTONUP:
 #           print("Mouse call!")
 #           test_click(event.pos[0], event.pos[1])            
 #           
    
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
