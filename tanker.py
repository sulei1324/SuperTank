__author__ = 'Su Lei'

import pyglet, bullet, load

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

    def update(self, dt):
        self.x += self.velocity_x * dt
        self.y += self.velocity_y * dt

    def on_key_press(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            print 'gggggg'
            self.rotation = 0
            self.velocity_y = 50
        if symbol == pyglet.window.key.RIGHT:
            self.rotation = 90
            self.velocity_x = 50
        if symbol == pyglet.window.key.DOWN:
            self.rotation = 180
            self.velocity_y = -50
        if symbol == pyglet.window.key.LEFT:
            self.rotation = 270
            self.velocity_x = -50
        if symbol == pyglet.window.key.SPACE:
            b = bullet.Bullet(img=load.bullet, batch=self.batch)
            b.x = 200
            b.y = 200
            b.visible = True
            print 'hhh'



    def on_key_release(self, symbol, modifiers):
        if symbol == pyglet.window.key.UP:
            self.velocity_y = 0
        if symbol == pyglet.window.key.RIGHT:
            self.velocity_x = 0
        if symbol == pyglet.window.key.DOWN:
            self.rotation = 180
            self.velocity_y = 0
        if symbol == pyglet.window.key.LEFT:
            self.rotation = 270
            self.velocity_x = 0

