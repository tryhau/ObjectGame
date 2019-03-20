import pygame
from pygame.locals import *
import time

class GameObject:
	filename = "block.png"
	speed = (0,1)
	b_width = b_heigth = 20 
	width = 300
	def __init__(self):
		self.image = pygame.image.load(self.filename)
		self.pos = self.image.get_rect().move(self.width/2,0)
	def move(self):
		self.pos = self.pos.move(self.speed)

class I_block(GameObject):
	block = []
	for i in range(0,4):
		block.append(GameObject())
	block[1].pos[0] = block[0].pos[0] + block[0].b_width
	block[2].pos[0] = block[1].pos[0] + block[0].b_width
	block[3].pos[0] = block[2].pos[0] + block[0].b_width

pygame.init()
screenSize = width, height = 300, 800
black = 0,0,0

screen = pygame.display.set_mode(screenSize)
background = pygame.image.load("background.png")
screen.blit(background, (0, 0))

Player = GameObject()
screen.blit(Player.image,Player.pos)
pygame.display.flip()

i_block = I_block()
print(i_block.block)

def on_loop():

	pass

running = True
while running:
	pygame.event.pump()
	keys = pygame.key.get_pressed()
	if (keys[K_ESCAPE]):
		running = False
	if (keys[K_LEFT]):
		Player.speed = (-1,0)
		Player.move()
	if (keys[K_RIGHT]):
		Player.speed = (1,0)
		Player.move()
	if (keys[K_DOWN]):
		Player.speed = (0,2)
		Player.move()

	if Player.pos.left < 0:
		Player.pos.left = 0
	if Player.pos.bottom > height:
		Player.pos.bottom = height
		break
	if Player.pos.right > width:
		Player.pos.right = width 	
	screen.fill(black) 
	Player.pos = Player.pos.move(0, 1)
	screen.blit(Player.image, Player.pos)
	pygame.display.flip()
	time.sleep(5/1000)            