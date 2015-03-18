"""
    Spiral.py

    Simple fractal program which draws a spiral in terms of steps,
    decay rate, and angle.
"""

import turtle

# Draw spiral recursively
def drawSpiral (ttl, step, decay, angle):
  if step > 0:
    ttl.forward (step)
    ttl.left (angle)
    step = step - decay
    drawSpiral (ttl, step, decay, angle)

def main():
  # Prompt the user to enter a step size, decay rate, and angle
  step = int (input ('Enter step size: '))
  decay = int (input ('Enter a decay rate: '))
  angle = int (input ('Enter an angle to turn: '))

  turtle.setup (800, 800, 0, 0)
  turtle.title ('Spiral')
  ttl = turtle.Turtle()
  ttl.pen(shown = False, speed = 0)

  ttl.penup()
  ttl.goto (-200, -200)
  ttl.pendown()
  drawSpiral (ttl, step, decay, angle)
  ttl.penup()

  turtle.done()

main()
