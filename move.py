__author__ = 'Su Lei'

import pyglet, tanker

# a = tanker.A()
# print a.x

images_src = './/images'
pyglet.resource.path = ['./images']
pyglet.resource.reindex()
tank = pyglet.resource.image('tanker.png')
print tank.width
tank = tanker.Tanker(img=tank, x=100, y=100)
text = pyglet.text.Label('hello you', x=600, y=600)


window = pyglet.window.Window(1000, 800)
window.set_caption('Super Tanker')

@window.event
def on_draw():
    window.clear()
    text.draw()


@window.event
def on_key_press(symbol, modifiers):
    if symbol == pyglet.window.key.UP:
        pass


# def update(dt):
#     tank.update(dt)

# pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()

