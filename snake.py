import pygame
import random
from pygame.locals import *
current=1
current2=1
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self) 
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location 
def getpos(current,ladders,Snakes,playerpos):
	dice=random.randint(1,6)
	print dice
	if dice+current>100:
		current=current
	else:
		current+=dice
	if current in ladders:
		current=ladders[current]
	if current in Snakes:
		current=Snakes[current]
	j=(current-1)%10
	i=current/10
	if i%2!=0:
		j=9-j
	return 64*j+10,580-64*i,current


pygame.init()
width, height = 640, 640
screen=pygame.display.set_mode((width, height))

key=False
key2=False
playerpos=[10,580]
player = pygame.image.load("player1.jpg")
player2=pygame.image.load("player2.png")
player2pos=[10,580] 
ladders={99:7,92:35,78:39,73:53,37:17,31:14,37:17}
Snakes={5:25,10:29,22:41,28:55,44:95,70:89,79:81}
while 1:
	screen.fill([255,255,255])
	BackGround = Background('snakeladder.jpg', [0,0])
	screen.blit(BackGround.image, BackGround.rect)
	screen.blit(player,playerpos)
	screen.blit(player2,player2pos)
	pygame.display.flip()	    
	for event in pygame.event.get():
		key=False
		key2=False
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
		if event.type==pygame.KEYDOWN and event.key==K_w:
			key=True
		if event.type==pygame.KEYDOWN and event.key==K_s:
			key2=True
		if key:
			playerpos[0],playerpos[1],current=getpos(current,ladders,Snakes,playerpos)
		if key2:
			player2pos[0],player2pos[1],current2=getpos(current2,ladders,Snakes,player2pos)

		if current==100:
			print "Player 1 win"
			exit(0)
		if current2==100:
			print "Player 2 win"
			exit(0)
		

			
		
        


