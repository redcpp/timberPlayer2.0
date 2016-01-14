from PIL import ImageGrab as IG
from PIL import ImageOps as IO
import win32api, win32con
import os
import time

'''

All coordinates assume a screen resolution of 1920x1080, and Opera 
no Bookmarks Toolbar enabled, running in a Win8 PC.
URL = http://goo.gl/6v7nM6
x_pad = 462
y_pad = 68
Play area =  x_pad+1, y_pad+1, 901, 727

Colores:
Leñador = (186, 27, 0) or (164, 23, 0)
Arbol = (163, 150, 63)
Score = (255, 255, 255)
GameOver = (236, 183, 91) in (287, 227)

'''

class Coord:
	left = (31, 293)
	right = (407, 293)
	play = (225, 473)
	
	lTree = (105, 328)
	rTree = (335, 328)

	lMan = (145, 498)
	rMan = (295, 498)

	score = (227, 117)

def leftTree():
	im = screenGrab()
	color = im.getpixel(Coord.lTree)  
	if color == (163, 150, 63):
		return True
	return False

def rightTree():
	im = screenGrab()
	color = im.getpixel(Coord.rTree)  
	if color == (163, 150, 63):
		return True
	return False

def leftTimber(color = 0):
	if color[2] == 0:
		time.sleep(.04)
		tree = leftTree()
		if tree:
			print('Moving right')
			click(Coord.right)
			time.sleep(.019)
			click(Coord.right)
			time.sleep(.0149)
			im = screenGrab()
			color = im.getpixel(Coord.rMan) 
			rightTimber(color)
		else:
			click(Coord.left)
			leftTimber(color)
	elif color == (187, 187, 187):
		print('Bye! :D')
	else:
		print(color)

def rightTimber(color = 0): 
	if color[2] == 0:
		time.sleep(.04)
		tree = rightTree()
		if tree:
			print('Moving left')
			click(Coord.left)
			time.sleep(.019)
			click(Coord.left)
			time.sleep(.0149)
			im = screenGrab()
			color = im.getpixel(Coord.lMan)
			leftTimber(color)
		else:
			click(Coord.right)
			rightTimber(color)
	elif color == (187, 187, 187):
		print('Bye! :D')
	else:
		print(color)

def screenGrab():
	box = (x_pad + 1, y_pad + 1, x_pad + 439, y_pad + 659)
	im = IG.grab(box)
	im.save( os.getcwd() + '\\img\\Snap__' + str( int( time.time() ) ) + '.png', 'PNG' )
	return im

def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(.011)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	print('Clic!')

def mousePos(coord):
	win32api.SetCursorPos((x_pad + coord[0], y_pad + coord[1]))

def getCoords():
	x,y = win32api.GetCursorPos()
	x = x - x_pad
	y = y - y_pad
	print(x,y)

def click(xy):
	mousePos(xy)
	if xy == Coord.left:
		print('left', end=' ')
	elif xy == Coord.right:
		print('right', end=' ')
	else:
		print('play', end=' ')
	leftClick()
	time.sleep(.065)

def startGame():
	click(Coord.play)
	time.sleep(.1)
	im = screenGrab()
	color = im.getpixel(Coord.lMan)
	leftTimber(color)

def main():
	#startGame()
	pass

# GLOBALS
x_pad = 462
y_pad = 68
score = 0

if __name__ == '__main__':
	main()