"""
    HilbertCurve.py

    Simple fractal program which draws a Hilbert's Curve in terms of
    the order given.
"""

import turtle

def upperU (ttl, order, length):
  if order > 0:
    leftU (ttl, order - 1, length)
    ttl.setheading (270)
    ttl.forward (length) 
    upperU (ttl, order - 1, length)
    ttl.setheading (0)
    ttl.forward (length)
    upperU (ttl, order - 1, length)
    ttl.setheading (90)
    ttl.forward (length)
    rightU (ttl, order - 1, length)

def leftU (ttl, order, length):
  if order > 0:
    upperU (ttl, order - 1, length)
    ttl.setheading (0)
    ttl.forward (length) 
    leftU (ttl, order - 1, length)
    ttl.setheading (270)
    ttl.forward (length)
    leftU (ttl, order - 1, length)
    ttl.setheading (180)
    ttl.forward (length)
    downU (ttl, order - 1, length)

def rightU (ttl, order, length):
  if order > 0:
    downU (ttl, order - 1, length)
    ttl.setheading (180)
    ttl.forward (length) 
    rightU (ttl, order - 1, length)
    ttl.setheading (90)
    ttl.forward (length)
    rightU (ttl, order - 1, length)
    ttl.setheading (0)
    ttl.forward (length)
    upperU (ttl, order - 1, length)

def downU (ttl, order, length):
  if order > 0:
    rightU (ttl, order - 1, length)
    ttl.setheading (90)
    ttl.forward (length) 
    downU (ttl, order - 1, length)
    ttl.setheading (180)
    ttl.forward (length)
    downU (ttl, order - 1, length)
    ttl.setheading (270)
    ttl.forward (length)
    leftU (ttl, order - 1, length)

# Put all the functions together to draw the Hilbert Curve
def draw_hilbert (ttl, order, size, length):
  for iter in range (order):
    length = length // 2

  x = (-1) * size // 2 + length // 2
  y = size // 2 - length // 2

  ttl.penup ()
  ttl.goto (x, y)
  ttl.pendown ()
  upperU (ttl, order, length)

def main():
  # Prompt the user to enter an order for the Hilbert Curve
  order = int (input ('Enter an order: '))

  turtle.setup (800, 800, 0, 0)
  turtle.title ('Hilbert Curve')
  ttl = turtle.Turtle()
  ttl.pen(shown = False, speed = 0)

  size = 600
  length = 600
  draw_hilbert (ttl, order, size, length)

  turtle.done()

main()
