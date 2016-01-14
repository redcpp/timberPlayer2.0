from PIL import ImageGrab as IG
from PIL import ImageOps as IO
import win32api, win32con
import time

'''

All coordinates assume a screen resolution of 1920x1080, and Opera 
no Bookmarks Toolbar enabled, running in a Win8 PC.
URL = http://goo.gl/6v7nM6
x_pad = 462
y_pad = 68
Play area =  x_pad+1, y_pad+1, 901, 727
(145, 88, 62)

'''

class IterationLimit(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(IterationLimit, self).__init__(message)

        # Now for your custom code...
        self.errors = errors

class ColorNotFound(Exception):
    def __init__(self, message, errors):

        # Call the base class constructor with the parameters it needs
        super(ColorNotFound, self).__init__(message)

        # Now for your custom code...
        self.message = message
        self.errors = errors

class Coord:
	left = (75, 395)
	right = (360, 395)
	play = (219, 476)
	
	lTree = (103, 217)
	rTree = (333, 217)

	lMan = (145, 498)
	rMan = (295, 498)

	score = (227, 117)
	GameOver = (287, 227)

class Color:
	Tree = (163, 150, 63)
	NoTree = (156, 98, 70)
	Ad = (187, 187, 187)
	GameOver = (236, 183, 91)

def leftTree(im):
	color = im.getpixel(Coord.lTree)
	if color == Color.Tree:
		print('Careful')
		click(Coord.left)
		changeSide('right')
	elif color == Color.NoTree:
		click(Coord.left)
		leftTimber()
	else:
		raise ColorNotFound('leftTree', color)

def rightTree(im):
	color = im.getpixel(Coord.rTree)
	if color == Color.Tree:
		print('Careful')
		click(Coord.right)
		changeSide('left')
	elif color == Color.NoTree:
		click(Coord.right)
		rightTimber()
	else:
		print('Score = ' + str(n-1))
		raise ColorNotFound('rightTree', color)

def leftTimber():
	if n%150 == 0:
		raise IterationLimit('Left' , 'left')
	im = screenGrab()
	leftTree(im)

def rightTimber():
	if n%150 == 0:
		raise IterationLimit('Right' , 'right')
	im = screenGrab()
	rightTree(im)

def changeSide(string):
	if string == 'right':
		click(Coord.right)
		click(Coord.right)
		rightTimber()
	elif string == 'left':
		click(Coord.left)
		click(Coord.left)
		leftTimber()
	else:
		print('WTF!?')

def screenGrab():
	im = IG.grab(box)
	return im

def leftClick():
	global c
	c += 1
	time.sleep(.005)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
	time.sleep(.005)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
	print('Clic!')
	time.sleep(.03) #recommended 0.008

def mousePos(coord):
	win32api.SetCursorPos((x_pad + coord[0], y_pad + coord[1]))

def getCoords():
	x,y = win32api.GetCursorPos()
	x = x - x_pad
	y = y - y_pad
	print(x,y)

def click(xy):
	global n
	n += 1
	mousePos(xy)
	if xy == Coord.left:
		print('left', end=' ')
	elif xy == Coord.right:
		print('right', end=' ')
	else:
		print('play', end=' ')
	leftClick()

def startGame(string):
	global n

	if not n > 1:
		click(Coord.play)
		time.sleep(.1)

	try:
		if string == 'left':
			leftTimber()
		elif string == 'right':
			rightTimber()

	except IterationLimit as e:
		n += 1
		startGame(e.errors)

	except ColorNotFound as ce:
		print('-'*80)
		print('In ' + str(ce.message) + ', the bot found the rgb color: ' + str(ce.errors))
		print('Aprox. Score = ', int(c/2))

def main():
	startGame('left')

# GLOBALS
x_pad = 462
y_pad = 68
box = (x_pad + 1, y_pad + 1, x_pad + 439, y_pad + 659)
n = 0
c = 0
sg = 0

if __name__ == '__main__':
	main()