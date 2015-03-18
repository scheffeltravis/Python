"""
    SierpenskiTriangle.py

    Simple fractal program which draws a Sierpenki's Triangle in terms of
    the order given.
"""

import turtle

# Draw a line from point p1 to point p2
def drawLine (ttl, p1, p2):
  x1 = p1[0]
  y1 = p1[1]
  x2 = p2[0]
  y2 = p2[1]
  ttl.penup()
  ttl.goto (x1, y1)
  ttl.pendown()
  ttl.goto (x2, y2)
  ttl.penup()

def midpoint (p1, p2):
  p = [0, 0]
  p[0] = (p1[0] + p2[0]) // 2
  p[1] = (p1[1] + p2[1]) // 2
  return p

# Draws triangle recursively
def draw_triangle (ttl, order, p1, p2, p3):
  drawLine (ttl, p1, p2)
  drawLine (ttl, p2, p3)
  drawLine (ttl, p3, p1)

  if (order > 0):
    # Find mid points of each of the sides
    q1 = midpoint (p1, p2)
    q2 = midpoint (p2, p3)
    q3 = midpoint (p3, p1)

    draw_triangle (ttl, order - 1, p1, q1, q3)
    draw_triangle (ttl, order - 1, p2, q1, q2)
    draw_triangle (ttl, order - 1, p3, q2, q3)

def main():
  # Prompt the user to enter an order for the triangle
  order = int (input ('Enter an order: '))

  turtle.setup (800, 800, 0, 0)
  turtle.title ('Sierpinski Triangle')
  ttl = turtle.Turtle()
  ttl.pen(shown = False, speed = 0)
  
  p1 = [0, 350]
  p2 = [-300, -150]
  p3 = [300, -150]
  draw_triangle (ttl, order, p1, p2, p3)

  turtle.done()

main()
