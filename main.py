from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty , ReferenceListProperty,ObjectProperty  
from kivy.vector import Vector
from kivy.clock import Clock
from random import randint,choice


class pongPaddle(Widget):
 score=NumericProperty(0)
 def bounceball(self,ball):
  if self.collide_widget(ball):
   if ball.velocity_x >= -25 and ball.velocity_x <= 25: 
    ball.velocity_x*=-1.1
    print(ball.velocity_y)
   else:
    ball.velocity_x*=-1
    ball.velocity_y=-4
    
   
class pongBall(Widget):
 velocity_x=NumericProperty(0)
 velocity_y=NumericProperty(0)
 velocity=ReferenceListProperty(velocity_x,velocity_y)
	
 def move(self):
  self.pos= Vector(*self.velocity)+self.pos
  
  
class pongGame(Widget):
 ball=ObjectProperty(None)
 player1=ObjectProperty(None)
 player2=ObjectProperty(None)
	
	
 def serve_ball(self):
  self.ball.velocity=Vector(6,0).rotate(randint(0,360))
  
 def update(self,dt):
  self.ball.move()
###bounce of top and bottom
  if self.ball.y <0:
   self.ball.velocity_y*=-1
  if self.ball.y >self.height-100:
   self.ball.velocity_y*=-1
###Incresing score

###bounce off left  
  if self.ball.x <0:
   self.ball.velocity_x*=-1
   self.player1.score+=1
###bounce off left   
  if self.ball.x>self.width-100:
   self.ball.velocity_x*=-1
   self.player2.score+=1
   
  self.player1.bounceball(self.ball)
  self.player2.bounceball(self.ball)
  
 def on_touch_move(self,touch):
   if touch.x< self.width *1/4:
     self.player1.center_y=touch.y
   if touch.x>self.width *3/4:
      self.player2.center_y=touch.y
      
     
class pongApp(App):
 def build(self):
  game=pongGame()
  game.serve_ball()
  Clock.schedule_interval(game.update,1.0/60.0)
  return game

pongApp().run()
