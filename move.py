__author__ = 'Su Lei'

import pyglet, tanker, bullet, load

# a = tanker.A()
# print a.x

images_src = './/images'
pyglet.resource.path = ['./images']
pyglet.resource.reindex()
tank = pyglet.resource.image('tanker.png')
tank.anchor_x = tank.width / 2
tank.anchor_y = tank.height / 2
print tank.width
main_batch = pyglet.graphics.Batch()
tank = tanker.Tanker(img=tank, x=100, y=100, batch=main_batch)
# text = pyglet.text.Label('hello you', x=600, y=600, batch=main_batch)



window = pyglet.window.Window(1000, 800)
window.set_caption('Super Tanker')
window.push_handlers(tank)

@window.event
def on_draw():
    window.clear()
    main_batch.draw()


def update(dt):
    tank.update(dt)


pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()

