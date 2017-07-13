import math
import sounddevice
import numpy
import pygame
import time
import matplotlib.pyplot as plt
import random
SIZE   = (1000,1000)
BLACK  = (0, 0 ,0)
WHITE  = (255, 255, 255)
RED    = (255,0,0)
GREEN  = (0,255,0)
BLUE   = (0,0, 255)
GREY   = (128,128, 128)
YELLOW = (255, 255, 0)
fs     = 48000
A4 = numpy.zeros(int(fs/8))
for x in range(len(A4)):
	volume = x / len(A4)
	freq   = 440 * 2**(0/12)
	A4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
noise = numpy.zeros(int(fs/8))
for x in range(len(noise)):
	noise[x] = random.uniform(-1, 1)


pieces = [A4]
song = numpy.concatenate(pieces)
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")
x=0
y=0
square = pygame.Rect( 1000/2 - 100/2, 1000/2 - 20/2 ,75, 75)
barrel = pygame.Rect( 1065/2 - 100/2, 950/2 - 20/2 ,10, 50)
missle1 = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10)
missle2 = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10)
missle3 = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10) 
enemy1 = pygame.Rect( 1000/2 - 100/2, 50,75,75)
enemy2 = pygame.Rect( 500/2 - 100/2, 50,75,75)
enemy3 = pygame.Rect( 1500/2 - 100/2, 50,75,75)
direction = 0
ydir = 0
missle_speed1 = 0
missle_speed2 = 0
missle_speed3 = 0



#if enemy1.x <= missle1.x and missle1.x <= enemy1.x+enemy1.w:
#		if enemy1.y-missle1.h <= missle1.y and missle1.y <= enemy1.y+enemy1.h:
#			missle1.x  = enemy1.x - missle1.w
#			enemy1 = pygame.Rect( 1000000 - 100/2, 10000,75,75)
			
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			direction  = 1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_a:
			missle_speed1 = -2
			sounddevice.play(song, fs)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
			missle_speed2 = -2
			sounddevice.play(song, fs)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_d:
			missle_speed3 = -2
			sounddevice.play(song, fs)
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			direction = -1
		elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			direction  = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			direction = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_w:
			square = pygame.Rect(1000/2 - 100/2, 1000/2 - 20/2, 75,75)
			barrel = pygame.Rect( 1065/2 - 100/2, 950/2 - 20/2 ,10, 50)
			missle1 = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10)
			missle_speed1 = 0
			missle2 = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10)
			missle_speed2 = 0
			missle3 = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10) 
			missle_speed3 = 0
		
	screen.fill(BLACK)
	pygame.draw.rect(screen, BLUE, missle1)
	pygame.draw.rect(screen, BLUE, missle2)
	pygame.draw.rect(screen, BLUE, missle3)
	pygame.draw.rect(screen, RED, square)
	pygame.draw.rect(screen, RED, barrel)
	pygame.draw.rect(screen, GREEN ,enemy1)
	pygame.draw.rect(screen, GREEN ,enemy2)
	pygame.draw.rect(screen, GREEN ,enemy3)
	pygame.display.flip()
	square = square.move(direction, ydir)
	barrel = barrel.move(direction, ydir)
	missle1 = missle1.move( 0, missle_speed1)
	missle1 = missle1.move(direction, ydir)
	missle2 = missle2.move( 0, missle_speed2)
	missle2 = missle2.move(direction, ydir)
	missle3 = missle3.move( 0, missle_speed3)
	missle3 = missle3.move(direction, ydir)


		

#class missle(pygame.sprite.Sprite):
#	def __init__(self):
#	self.image = pygame.Surface((10, 10))
#	self.image.fill(BLUE)
#	self.rect = self.image.get_rect()
	

#class enemy(pygame.sprite.Sprite):
#	def __init__(self):
#	self.image = pygame.Surface((75, 75))
#	self.image.fill(GREEN)
#	self.rect = self.image.get_rect()








	
