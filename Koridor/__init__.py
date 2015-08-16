# -*- coding: utf-8 -*-
"""This project consists of recreating the Koridor game in Python.
@author: Iooss
@license: MIT
"""

from game import *
from interface.graphicInterface import *
from action import *
import pyglet
from pyglet.window import key
from pyglet.window import mouse

# Create game and interface instance
game = Game()
interface = GraphicInterface(game)


def play(actionString):
    """
        Function to play an action
    """
    action = Action()
    action.stringToAction(actionString)
    game.play(action)


@interface.factory.window.event
def on_draw():
    """
        Event to clear & draw the window
    """
    interface.factory.draw()


@interface.factory.window.event
def on_key_press(symbol, modifiers):
    """
        Event to bind keys to actions
    """
    if symbol == key.Z or symbol == key.UP:
        play('go_forward')
    elif symbol == key.D or symbol == key.RIGHT:
        play('go_right')
    elif symbol == key.S or symbol == key.DOWN:
        play('go_backward')
    elif symbol == key.Q or symbol == key.LEFT:
        play('go_left')
    interface.refresh()


@interface.factory.window.event
def on_mouse_press(x, y, button, modifiers):
    """
        Event to bind mouse to actions
    """
    if button == mouse.LEFT:
        coord = interface.grid.getCaseByAbsolutCoordinates(x, y)
        if coord:
            play('place_wall ' + str(coord[0]) + ' ' + str(coord[1]) + ' 1')


# Run Forest, run !
pyglet.app.run()
