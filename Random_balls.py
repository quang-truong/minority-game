import random
from turtle import Turtle

# Ball move distance
#MOVE_DIST = 1
MOVE_DIST = random.randint(0,9)

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.color('blue')
    self.penup()
    self.x_move_dist = MOVE_DIST
    self.y_move_dist = MOVE_DIST
    self.reset()

  def move(self):
    # Move by some random steps ahead both vertically and horizontally 
    new_y = self.ycor() + self.y_move_dist
    new_x = self.xcor() + self.x_move_dist
    self.goto(x = new_y, y = new_y)

  def bounce(self, x_bounce, y_bounce):
    if x_bounce:
      # Reverse the horizontal direction 
      self.x_move_dist *= -1

    if y_bounce:
      # Reverse the vertical direction 
      self.y_move_dist *= -1
      
  def reset(self) -> None:
      return super().reset()