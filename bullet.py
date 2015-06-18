__author__ = 'Su Lei'

import pyglet

class Bullet(pyglet.sprite.Sprite):
    def __init__(self, *args, **kargs):
        super(Bullet, self).__init__(*args, **kargs)
        self.velocity_x = 60
        self.velocity_y = 60
