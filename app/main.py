
#
#Code referenced from https://github.com/noahspriggs/battlesnake-python/blob/master/app/main.py
from AStar import *
import bottle
import os
import random
import math
import copy
import sys

SNAKE = 1
FOOD = 3
SAFENODE = 5


@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='static/')


@bottle.post('/start')
def start():
    data = bottle.request.json
    game_id = data['game_id']
    board_width = data['width']
    board_height = data['height']

    head_url = '%s://%s/static/head.png' % (
        bottle.request.urlparts.scheme,
        bottle.request.urlparts.netloc
    )

    # TODO: Do things with data

    return {
        'color': '#00FF00',
        'taunt': '{} ({}x{})'.format(game_id, board_width, board_height),
        'head_url': head_url,
        'name': 'yes daddy'
    }


#prints grid
def printg(grid):
	for x in grid:
		print x

#initialize grid data
#map fill
def init(data, thisID):
	grid = [[0 for col in xrange(data['height'])] for row in xrange(data['width'])]
	print "************************"
	print thisID
	for s in data['snakes']:
		print "snake id's"
		print s['id']
		if s['id'] == thisID:
			print "FOUND OUR SNAKE"
			myS = s
			print s

		for coord in s['coords']:
			grid[coord[0]][coord[1]] = SNAKE

	
	for foods in data['food']:
		grid[foods[0]][foods[1]] = FOOD

	return grid, myS

def direction(start, dest):
	dx = start[0] - dest[0]
	dy = start[1] - dest[1]

	if dx == 1:
		return 'left'
	
	elif dx == -1:
		return 'right'

	elif dy == -1:
		return 'down'
	
	elif dy == 1:
		return 'up'
	


def getID(data):
	snake = init(data)
	id = data['you']
	return id

def distance(p, q):
	dx = abs(p[0] - q[0])
	dy = abs(p[1] - q[1])
	ans = dx + dy
	return ans

@bottle.post('/move')
def move():

	print "Hello world"
	data = bottle.request.json
	OURID = data['you']
	

	grid, mysnake = init(data)
	print "this is our snake ID"
	print OURID
	print "*********************"

	grid, mysnake = init(data, OURID)

	
	printg(grid)
	sys.stdout.flush()
	

	print "mysnake arr"
	print mysnake

	mysnakeHead = mysnake['coords'][0]
	mysnakeCoords = mysnake['coords']

	foodList = sorted(data['food'], key = lambda p: distance(p, mysnakeHead))
	
	path = None
	for food in foodList:
		print food
		sys.stdout.flush()
		path = a_star(mysnakeHead, food, grid, mysnakeCoords)	
		if path != None:
			print food
			sys.stdout.flush()
			break
		
				



	print "PATH"
	print path
	sys.stdout.flush()
	dir = direction(path[0], path[1])
	

	print dir
	sys.stdout.flush()


	return {
        'move': dir,
        'taunt': 'battlesnake-python!'
    }





def find_path(mysnakeHead):


# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
