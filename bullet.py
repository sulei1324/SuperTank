__author__ = 'Su Lei'

import pyglet, random, math

class Bullet(pyglet.sprite.Sprite):
    def __init__(self, *args, **kargs):
        super(Bullet, self).__init__(*args, **kargs)
        self.velocity_x = 100
        self.velocity_y = 100
        self.new_object = []
        pyglet.clock.schedule_once(self.die, 5)
        self.dead = False

    def update(self, dt):
        self.x += self.velocity_x * dt * math.sin(math.radians(self.rotation))
        self.y += self.velocity_y * dt * math.cos(math.radians(self.rotation))

    def die(self, dt):
        self.delete()
        self.dead = True