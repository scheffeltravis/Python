"""
    Tree.py

    Simple fractal program which draws a tree based on bifurcation in terms
    of 'branch' length.
"""

import turtle

# Draw a tree recursively
def drawTree (ttl, length):
  if length > 5:
    ttl.forward (length)
    ttl.right (20)
    drawTree (ttl, length - 15)
    ttl.left (40)
    drawTree (ttl, length - 15)
    ttl.right (20)
    ttl.backward (length)

def main():
  # Prompt the user to enter a branch length
  length = int (input ('Enter branch length: '))

  turtle.setup (800, 800, 0, 0)
  turtle.title ('Recursive Tree')
  ttl = turtle.Turtle()
  ttl.pen(shown = False, speed = 0)

  ttl.penup()
  ttl.goto (0, -100)
  ttl.pendown()
  ttl.left (90)
  ttl.pendown()
  drawTree (ttl, length)
  ttl.penup()

  turtle.done()

main()
