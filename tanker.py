__author__ = 'Su Lei'

import pyglet

images_src = './/images'
pyglet.resource.path = ['./images']
pyglet.resource.reindex()



class A():
    def __init__(self):
        self.x = 1000


class Tanker(pyglet.sprite.Sprite):
    def __init__(self, *args, **kargs):
        super(Tanker, self).__init__(*args, **kargs)
        self.velocity_x = 20
        self.velocity_y = 20

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

