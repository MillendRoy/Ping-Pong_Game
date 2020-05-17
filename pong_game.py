# -*- coding: utf-8 -*-
"""
Created on Sat May 16 20:25:35 2020

@author: MILLEND
"""


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ReferenceListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint

class Paddle(Widget):
    score=NumericProperty(0)
    def ball_bounce(self,ball):
        if self.collide_widget(ball):
             ball.velocity_x *= -1
             

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
    ball= ObjectProperty(None)
    player1=ObjectProperty(None)
    player2=ObjectProperty(None)
    
    # change the ball velocity given inside vector, 4 denotes the x velocity
    def serve_ball(self):
        self.ball.velocity=Vector(10,0).rotate(randint(0,360))
    
    def update(self, dt):
        self.ball.move()
        
        # bounce off top and bottom
        if (self.ball.y < 0) or (self.ball.top > self.height):
            self.ball.velocity_y *= -1

        # bounce off left and score increment
        if (self.ball.x < 0):
            self.ball.velocity_x *= -1
            self.player1.score+=1
        # bounce off right and score increment    
        if (self.ball.right > self.width):
            self.ball.velocity_x *= -1
            self.player2.score+=1
        self.player1.ball_bounce(self.ball)
        self.player2.ball_bounce(self.ball)

    def on_touch_move(self, touch):
        if touch.x < self.width / 4:
            self.player1.center_y = touch.y
        if touch.x > self.width * 3/4:
            self.player2.center_y = touch.y  



class PongApp(App):
    def build(self):
        game=PongGame()
        game.serve_ball()
        
        # here in 1 sec 60 images will be shown and we need to call the update function regularly
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()