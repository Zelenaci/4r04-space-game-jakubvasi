#!/usr/bin/env python3
# Soubor:  kameny.py
# Datum:   06.11.2018 10:01
# Autor:   Marek Nožka, nozka <@t> spseol <d.t> cz
# Licence: GNU/GPL
############################################################################
import pyglet
from pyglet.window import key
import random
from math import sin, cos, radians, pi

window = pyglet.window.Window(800, 600)
keys = key.KeyStateHandler()
window.push_handlers(keys)
batch = pyglet.graphics.Batch()   # pro optimalizované vyreslování objektů


class SpaceObject(object):

    def __init__(self, img_file,
                 x=None, y=None,
                 x_spd=None, y_spd=None
                 speed=None, rotation=None):

        # nečtu obrázek
        self.image = pyglet.image.load(img_file)
        # střed otáčení dám na střed obrázku
        self.image.anchor_x = self.image.width // 2
        self.image.anchor_y = self.image.height // 2
        # z obrázku vytvořím sprite
        self.sprite = pyglet.sprite.Sprite(self.image, batch=batch)

        # pokud není atribut zadán vytvořím ho náhodně
        self._x = x if x is not None else random.randint(0, window.width)
        self._y = y if y is not None else random.randint(0, window.height)
        # musím správně nastavit polohu sprite
        self.x = self._x
        self.y = self._y
        
        self.direction = direction if direction is not None else radians(random.randint(0, 360))
        self.speed = speed         if speed is not None else random.randint(30, 180)
        self.rotation = rotation   if rotation is not None else random.randint(-10, 10)
        
    def set_attr(self, direction, speed, rotation=0):
        self.direction = direction
        self.speed = speed
        self.rotation = rotation

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, new):
        self._x = self.sprite.x = new

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, new):
        self._y = self.sprite.y = new

    def tick(self, dt):
        #self.bounce()

        # do promenne dt se uloží doba od posledního tiknutí
        self.x += dt * self.speed * x_spd
        self.sprite.x = self.x
        self.y += dt * self.speed * y_spd
        self.sprite.y = self.y
        
class Meteor(SpaceObject):
    def __init__(self, img_file,
                 x=None, y=None,
                 direction=None, 
                 speed=None, rotation=None):
        super().__init__(img_file, x, y, direction)


def test():
    if keys[key.LEFT]:
        a.set_attr(90, -500)
        
    elif keys[key.RIGHT]:
        a.set_attr(90, 500)
        
    elif keys[key.UP]:
        a.set_attr(0, 500)
        
    elif keys[key.DOWN]:
        a.set_attr(0, -500)
        
    #elif keys[key.UP and symbol == key.LEFT:
        #a.set_attr(45, -500)


a = SpaceObject('SpaceShooterRedux/PNG/playerShip1_red.png', window.width//2, 40, 0, 0 )
pyglet.clock.schedule_interval(a.tick, 1/60)


@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_press(symbol, modifiers):
    #a.set_attr(90, -400)

@window.event
def on_key_release(symbol, modifiers):
    a.set_attr(0, 0)


pyglet.app.run()
