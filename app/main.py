import bottle
import os
import random


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
        'name': 'battlesnake-python'
    }


@bottle.post('/move')
def move():
    data = bottle.request.json
    height = data[height]
    width = data[width]
    coords = snake.coords
    direction = 'left'

    print "height" + height
    print "width" + width
    print "snake coords" + coords

        snakehead = coordinates[0]
    
    print "curr coords: ", coordinates[0]
    #case snake hits left wall
    direction = 'east'

    snakehead = coords[0]
    if snakehead[0] == 0:
        if snakehead[1] == 0:
            return 'east'
        print "on turn ", turn, " we hit the left wall and go north"
        return 'north'
    #case snake hits right wall
    if snakehead[0] == width-1:
        if snakehead[1] == height-1:
            return 'west'
        print "on turn ", turn, " we hit the right wall and go south"
        return 'south'
    #case snake hits top
    if snakehead[1] == 0:
        if snakehead[0] == width-1:
            return 'south'
        print "on turn ", turn, " we hit the top and go east"
        return 'east'
    #case snake hits bottom
    if snakehead[1] == height-1:
        if snakehead[0] == 0:
            return 'north'
        print "on turn ", turn, " we hit the bottom and go west"
        return 'west' 
    # snake hits nothing
    
    print "on turn ", turn, " we continue in last direction"
    return {
        'move': 'down',
        'taunt': 'get lit up'
    }       

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()
if __name__ == '__main__':
    bottle.run(application, host=os.getenv('IP', '0.0.0.0'), port=os.getenv('PORT', '8080'))
