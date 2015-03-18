"""
    KochSnowflake.py

    Simple fractal program which draws a Koch's Snowflake in terms of
    the order given.
"""

import turtle
import math

# Draw a line from (x1, y1) to (x2, y2)
def drawLine (ttl, x1, y1, x2, y2):
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

# Returns the midway between two points
def midpoint (p1, p2):
  p = [0, 0]
  p[0] = (p1[0] + p2[0]) // 2
  p[1] = (p1[1] + p2[1]) // 2
  return p

# Draw recursively a snowflake
def snow_flake (ttl, order, p1, p2):
  if (order == 0):
    drawLine (ttl, p1[0], p1[1], p2[0], p2[1])
  else:
    deltaX = p2[0] - p1[0]
    deltaY = p2[1] - p1[1]

    a_x = p1[0] + deltaX // 3
    a_y = p1[1] + deltaY // 3
    a = [a_x, a_y]

    b_x = p1[0] + deltaX * 2 // 3
    b_y = p1[1] + deltaY * 2 // 3
    b = [b_x, b_y]

    c_x = (p1[0] + p2[0]) // 2 - math.cos(math.radians(30)) * (p1[1] - p2[1]) // 3
    c_y = int((p1[1] + p2[1]) // 2 - math.cos(math.radians(30)) * (p2[0] - p1[0]) // 3)
    c = [c_x, c_y]

    # Recursively display the snow flake
    snow_flake (ttl, order - 1, p1, a)
    snow_flake (ttl, order - 1, a, c)
    snow_flake (ttl, order - 1, c, b)
    snow_flake (ttl, order - 1, b, p2)


def main():
  # Prompt the user to enter an order for the snow flake
  order = int (input ('Enter an order: '))

  turtle.setup (800, 800, 0, 0)
  turtle.title ('Koch Snow Flake')
  ttl = turtle.Turtle()
  ttl.pen(shown = False, speed = 0)

  p1 = [0, 350]
  p2 = [-300, -150]
  p3 = [300, -150]
  snow_flake (ttl, order, p1, p2)
  snow_flake (ttl, order, p2, p3)
  snow_flake (ttl, order, p3, p1)

  turtle.done()

main()
