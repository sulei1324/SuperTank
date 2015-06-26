__author__ = 'Su Lei'

import pyglet
from pyglet import window

test_window = window.Window()
print window.key.MOD_SHIFT

@test_window.event
def on_draw():
    pass

@test_window.event
def on_key_press(symbol, modifiers):
    if symbol == window.key.A and not modifiers:
        t = pyglet.text.Label('a')
        t.draw()

    if symbol == window.key.A and modifiers & window.key.MOD_SHIFT:
        t = pyglet.text.Label('A')
        t.draw()

pyglet.app.run()