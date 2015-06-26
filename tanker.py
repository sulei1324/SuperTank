__author__ = 'Su Lei'

import pyglet, bullet, load, random, math

images_src = './/images'
pyglet.resource.path = ['./images']
pyglet.resource.reindex()


class A():
    def __init__(self):
        self.x = 1000


class Tanker(pyglet.sprite.Sprite):
    def __init__(self, *args, **kargs):
        super(Tanker, self).__init__(*args, **kargs)
        self.new_object = []
        self.velocity_x = 0
        self.velocity_y = 0
        self.dead = False
        self.control = False

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def on_key_press(self, symbol, modifiers):
        if self.control:
            return
        if symbol == pyglet.window.key.UP:
            self.rotation = 0
            self.velocity_y = 150
            self.control = True
        if symbol == pyglet.window.key.RIGHT:
            self.rotation = 90
            self.velocity_x = 150
            self.control = True
        if symbol == pyglet.window.key.DOWN:
            self.rotation = 180
            self.velocity_y = -150
            self.control = True
        if symbol == pyglet.window.key.LEFT:
            self.rotation = 270
            self.velocity_x = -150
            self.control = True
        if modifiers & pyglet.window.key.MOD_SHIFT:
            self.velocity_y *= 2
            self.velocity_x *= 2
            self.control = True
        if symbol == pyglet.window.key.SPACE:
            b = bullet.Bullet(img=load.bullet, batch=self.batch, x=self.x, y=self.y)
            b.rotation = self.rotation
            print b.rotation, math.sin(self.rotation), math.cos(self.rotation)
            b.visible = True
            self.new_object.append(b)


    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            self.velocity_y = 0
            self.control = False
        if symbol == pyglet.window.key.RIGHT:
            self.velocity_x = 0
            self.control = False
        if symbol == pyglet.window.key.DOWN:
            self.rotation = 180
            self.velocity_y = 0
            self.control = False
        if symbol == pyglet.window.key.LEFT:
            self.rotation = 270
            self.velocity_x = 0
            self.control = False

