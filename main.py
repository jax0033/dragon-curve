import pygame
import os

global width,height,scl
#set window position
os.environ["SDL_VIDEO_WINDOW_POS"] = "600,30"
scl = 1
width,height = 1000,1000
pygame.init()
screen = pygame.display.set_mode((width,height))

#drawing function
def line(x,y,dir,lr):
	#lr = left or right, dir = last direction
	if lr ==0:lr=-1
	dir+=lr
	if dir >4: dir=1
	if dir <1: dir=4
	if dir==1:
		#right
		pygame.draw.line(screen,(0,0,0),(x,y),(x+2*scl,y))
		return dir,x+2*scl,y
	if dir==2:
		#down
		pygame.draw.line(screen,(0,0,0),(x,y),(x,y+2*scl))
		return dir,x,y+2*scl
	if dir==3:
		#left
		pygame.draw.line(screen,(0,0,0),(x,y),(x-2*scl,y))
		return dir,x-2*scl,y
	if dir==4:
		#up
		pygame.draw.line(screen,(0,0,0),(x,y),(x,y-2*scl))
		return dir,x,y-2*scl

#iterates the fractal
def iterate(lst):
	ret_ = lst
	lst = lst[::-1]
	ret_.append(1)
	for n in lst:
		if n == 1:
			ret_.append(0)
		else:
			ret_.append(1)
	return ret_

def main():
	moves = []
	for n in range(17):
		moves = iterate(moves)
	dir = 1
	x,y = width//5.5,height//2.5
	clock = pygame.time.Clock()
	fps = 0
	screen.fill((255,255,255))

	for i in moves:
		dir,x,y = line(x,y,dir,i)
		pygame.display.update()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
		clock.tick(fps)

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()

		pygame.display.update()
		clock.tick(fps)

main()
