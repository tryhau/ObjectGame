#This code is a result of the tutorial @ https://pythonspot.com/snake-with-pygame/.
#It is meant as a project to become better at OOP.

#My main contribution to the code is a highscore counter and writer function that compares the current highscore
#with the all-time-highscore contained with player name and date in an excel spreadsheet, and overwrites it if
#the current score is greater.
#The player blocks and apple visuals have also been updated.

from pygame.locals import *
from random import randint
import pygame
import time
from HighscoreWrite import Highscore

class Apple:
    x = 0
    y = 0
    step = 44
 
    def __init__(self,x,y):
        self.x = x * self.step
        self.y = y * self.step
 
    def draw(self, surface, image):
        surface.blit(image,(self.x, self.y)) 
 
class Player:
    x = [0]
    y = [0]
    step = 44
    direction = 0
    length = 0
    updateCountMax = 2
    updateCount = 0
 
    def __init__(self, length,name):
        self.name = name
        self.length = length
        for i in range(0,2000):
            self.x.append(-100)
            self.y.append(-100)
 
       # initial positions, no collision.
        self.x[1] = 1*44
        self.x[2] = 2*44
 
    def update(self): 
        self.updateCount = self.updateCount + 1
        if self.updateCount > self.updateCountMax:
 
            # update previous positions
            for i in range(self.length-1,0,-1):
                self.x[i] = self.x[i-1]
                self.y[i] = self.y[i-1]
 
            # update position of head of snake
            if self.direction == 0:
                self.x[0] = self.x[0] + self.step
            if self.direction == 1:
                self.x[0] = self.x[0] - self.step
            if self.direction == 2:
                self.y[0] = self.y[0] - self.step
            if self.direction == 3:
                self.y[0] = self.y[0] + self.step
            self.updateCount = 0
 
    def moveRight(self):
        self.direction = 0
    def moveLeft(self):
        self.direction = 1
    def moveUp(self):
        self.direction = 2
    def moveDown(self):
        self.direction = 3 
 
    def draw(self, surface, image):
        for i in range(0,self.length):
            surface.blit(image,(self.x[i],self.y[i])) 
 
#Rules of the game
class Game:
    def isCollision(self,x1,y1,x2,y2,bsize):
        if x1 >= x2 and x1 <= x2 + bsize:
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False

    def boundaryCollision(self,x,y,windowWidth,windowHeight,bsize):
    	if -bsize < x < windowWidth-bsize and -bsize < y < windowHeight-bsize:
    		return False
    	return True

class App:
    windowWidth = 800
    windowHeight = 600
    player = 0
    apple = 0
    score = 0
	
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._apple_surf = None
        self.game = Game()
        self.player = Player(3,'Trym') 
        self.apple = Apple(5,5)        
 
    def on_init(self):
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Pygame Snek')
        self._running = True
        self._image_surf = pygame.image.load("snake.png").convert_alpha()
        self._apple_surf = pygame.image.load("apple.png").convert_alpha()
 
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
 
    def on_loop(self):
        self.player.update()

        # does snake eat apple?
        for i in range(0,self.player.length):
            if self.game.isCollision(self.apple.x,self.apple.y,self.player.x[i], self.player.y[i],44):
                self.apple.x = randint(2,9) * 44
                self.apple.y = randint(2,9) * 44
                self.player.length = self.player.length + 1
                self.score = self.score + 1 
 
        # does snake collide with itself?
        for i in range(2,self.player.length):
            if self.game.isCollision(self.player.x[0],self.player.y[0],self.player.x[i], self.player.y[i],40):
                print("You lose! Collision: ")
                print("Your score is:" + str(self.score))
                Highscore('Highscore.xlsx',self.score,self.player.name)
                exit(0)

        # does snake collide with boundaries?
        if self.game.boundaryCollision(self.player.x[0], self.player.y[0],self.windowWidth,self.windowHeight,44):
        	print("You lose! Collision: ")
        	print("Your score is:" + str(self.score))
        	Highscore('Highscore.xlsx',self.score, self.player.name)
        	exit(0)
        pass
 
    def on_render(self):
        pygame.init()
        font = pygame.font.Font(None, 30)
        self._display_surf.fill((0,0,0))
        self.player.draw(self._display_surf, self._image_surf)
        self.apple.draw(self._display_surf, self._apple_surf)
        
        self.playername = font.render("Player: " + str(self.player.name),True, (255,255,255))
        self.scoretext = font.render("Score: " + str(self.score),True, (255,255,255))
        
        self.playerRect = self.playername.get_rect()
        self.playerRect.topright = [795,35]
        
        self.scoreRect = self.scoretext.get_rect()
        self.scoreRect.topright = [795,5]
        self._display_surf.blit(self.playername,self.playerRect)
        self._display_surf.blit(self.scoretext,self.scoreRect)
        pygame.display.flip()
 
    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            pygame.event.pump()
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                self.player.moveRight()
 
            if (keys[K_LEFT]):
                self.player.moveLeft()
 
            if (keys[K_UP]):
                self.player.moveUp()
 
            if (keys[K_DOWN]):
                self.player.moveDown()
 
            if (keys[K_ESCAPE]):
                self._running = False

            self.on_loop()
            self.on_render()
            time.sleep (25/1000.0);
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()