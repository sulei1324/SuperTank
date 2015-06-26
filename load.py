__author__ = 'Su Lei'

import pyglet

pyglet.resource.path = ['./images']
pyglet.resource.reindex()

bullet = pyglet.resource.image('bullet.png')
bullet.anchor_x = bullet.width / 2
bullet.anchor_y = bullet.height / 2 - 3 - 25
