import math
#import sounddevice
#import numpy
import pygame
import time
#import matplotlib.pyplot as plt
SIZE = (1000,1000)
BLACK = (0, 0 ,0)
WHITE =(255, 255, 255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0, 255)
GREY = (128,128, 128)
YELLOW = (255, 255, 0)
fs = 48000
#A4 = numpy.zeros(fs)
#for x in range(len(A4)):
#	volume = x / len(A4)
#	freq   = 440 * 2**(0/12)
#	A4[x]  = volume * math.sin(2*math.pi * freq*x/fs)
#pieces = [silence, A4, B4, noisilence]
#song = numpy.concatenate(pieces)
pygame.init()
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")
x=0
y=0
square = pygame.Rect( 1000/2 - 100/2, 1000/2 - 20/2 ,75, 75)
barrel = pygame.Rect( 1065/2 - 100/2, 950/2 - 20/2 ,10, 50)
missle = pygame.Rect( 1065/2 - 100/2, 1000/2 - 20/2 ,10, 10)
direction = 0
ydir = 0
missle_speed = 0
while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			direction  = 1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
			while True:
				missle_speed = -2
			
			#sounddevice.play(song, fs)
			#plt.plot(song)
			#plt.show()
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
			direction = -1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
			ydir = -1
		elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
			ydir = 1
		elif event.type == pygame.KEYUP and event.key == pygame.K_RIGHT:
			direction  = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_LEFT:
			direction = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_UP:
			ydir = 0
		elif event.type == pygame.KEYUP and event.key == pygame.K_DOWN:
			ydir = 0
	screen.fill(BLACK)
	pygame.draw.rect(screen, BLUE, missle)
	pygame.draw.rect(screen, RED, square)
	pygame.draw.rect(screen, RED, barrel)
	pygame.display.flip()
	square = square.move(direction, ydir)
	barrel = barrel.move(direction, ydir)
	missle = missle.move( 0, missle_speed)
	missle = missle.move(direction, ydir)
	
