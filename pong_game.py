# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:25:35 2020

@author: MILLEND
"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.vector import Vector

class PongBall(Widget):
    # velocity(direction of movement) of the ball on x and y axis
    # numeric property helps in identifying the datatypes when used in other sources such as Java for android
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)

    # referencelist property used if we need to change both the variables
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    # final position= velocity(direction) + initial position
    def move(self):
        self.pos = Vector(*self.velocity) + self.pos

class PongGame(Widget):
    pass


class PongApp(App):
    def build(self):
        return PongGame()


if __name__ == '__main__':
    PongApp().run()