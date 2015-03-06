import math

class Point (object):
  # constructor with default values
  def __init__ (self, x = 0, y = 0):
    self.x = x
    self.y = y

  # get distance to another Point object
  def dist (self, other):
    return math.hypot(self.x - other.x, self.y - other.y)

  # create a string representation of a Point (x, y)
  def __str__ (self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

  # test for equality between two points
  def __eq__ (self, other):
    tol = 1.0e-16
    return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))

class Line (object):
  # constructor assign default values if user defined points are the same
  def __init__ (self, p1_x = 0, p1_y = 0, p2_x = 1, p2_y = 1):
    tol = 1.0e-18
    if ((abs(p1_x - p2_x) < tol) and (abs(p1_y - p2_y) < tol)):
      self.p1 = Point (0, 0)
      self.p2 = Point (1, 1)
    else:
      self.p1 = Point (p1_x, p1_y)
      self.p2 = Point (p2_x, p2_y)
      
  # determine if line is parallel to x axis
  def is_parallel_x (self):
    tol = 1.0e-18
    return (abs(self.p1.y - self.p2.y) < tol)
  
  # determine if line is parallel to y axis
  def is_parallel_y (self):
    tol = 1.0e-18
    return (abs (self.p1.x - self.p2.x) < tol)
  
  # determine slope for the line
  # return float ('inf') if line is parallel to the y-axis
  def slope (self):
    if (self.is_parallel_y()):
      return float('inf')
    else:
      return (self.p1.y - self.p2.y) / (self.p1.x - self.p2.x)

  # determine the y-intercept of the line
  def y_intercept (self):
    return (self.p1.y - (self.slope() * self.p1.x))

  # determine the x-intercept of the line
  def x_intercept (self):
    return (-1.0 * self.y_intercept()) / (self.slope())

  # determine if two lines are parallel
  def is_parallel (self, other):
    tol = 1.0e-18
    return (abs(self.slope() - other.slope()) < tol)
  
  # determine if two lines are perpendicular to each other
  def is_perpendicular (self, other):
    tol = 1.0e-18
    return (abs(self.slope() + other.slope()) < tol)
  
  # determine if a point is on the line or on an extension of it
  def is_on_line (self, p):
    return (p.y == self.slope() * p.x + self.y_intercept())

  # determine the perpendicular distance of a point to the line
  def perp_dist (self, p):
    return (abs(-self.slope() * p.x + p.y - self.y_intercept()) / math.sqrt(1 + self.slope() ** 2))

  # determine the intersection point of two lines if not parallel
  def intersection_point (self, other):
    if (not Line.is_parallel (self, other)):
      x = (other.y_intercept() - self.y_intercept()) / (self.slope() - other.slope())
      y = self.slope() * x + self.y_intercept()
      return x, y

  # determine if two points are on the same side of the line
  # return False if one or both points are on the line
  def on_same_side (self, p1, p2):
    if ((p1.y < self.slope() * p1.x + self.y_intercept()) and (p2.y < self.slope() * p2.x + self.y_intercept())):
      return True
    elif ((p1.y > self.slope() * p1.x + self.y_intercept()) and (p2.y > self.slope() * p2.x + self.y_intercept())):
      return True
    else:
      return False

  # string representation of the line - one of three cases
  # y = c
  # x = c
  # y = m * x + b
  def __str__ (self):
    if (self.is_parallel_x ()):
      return 'y = ' + str(self.p1.y)
    elif (self.is_parallel_y ()):
      return 'x = ' + str(self.p2.y)
    else:
      return 'y = ' + str(self.slope()) + ' * x + (' + str(self.y_intercept()) + ')'

class Circle (object):
  # constructor with default values
  def __init__ (self, radius = 1, x = 0, y = 0):
    self.radius = radius
    self.x = x
    self.y = y

  # compute circumference
  def circumference (self):
    return 2 * self.radius * math.pi

  # compute area
  def area (self):
    return math.pow(self.radius, 2) * math.pi

  # determine if a point is inside the circle
  def is_inside_point (self, p):
    return math.hypot(self.x - p.x, self.y - p.y) < self.radius

  # determine if the other circle is strictly inside self
  def is_inside_circle (self, other):
    return (math.hypot(self.x - other.x, self.y - other.y) <= abs(self.radius - other.radius))
    
  # determine if the other circle intersects self
  def does_intersect_circle (self, other):
    return (math.hypot(self.x - other.x, self.y - other.y) <= (self.radius + other.radius))

  # string representation of a circle
  # Radius: radius, Center: (x, y)
  def __str__ (self):
    return "Radius: " + str(self.radius) + ", Center: (" + str(self.x) + ', ' + str(self.y) + ')'

def main():
  # open file "geometry.txt" for reading
  infile = open("geometry.txt", 'r')
  lines = infile.readlines()

  # read the coordinates of the first Point P
  p_coords = lines[0].split()
  p = Point (float(p_coords[0]), float(p_coords[1]))

  # read the coordinates of the second Point Q
  q_coords = lines[1].split()
  q = Point (float(q_coords[0]), float(q_coords[1]))

  # print the coordinates of points P and Q
  print ("Coordinates of P:", p)
  print ("Coordinates of Q:", q)

  # print distance between P and Q
  print ("Distance between P and Q:", "{0:.3f}".format(Point.dist(p, q)))

  # print the slope of the line PQ
  pq = Line (float(p_coords[0]), float(p_coords[1]), float(q_coords[0]), float(q_coords[1]))
  print ("Slope of PQ:", Line.slope(pq))

  # print the y-intercept of the line PQ
  print ("Y-Intercept of PQ:", Line.y_intercept(pq))

  # print the x-intercept of the line PQ
  print ("X-Intercept of PQ:", Line.x_intercept(pq))

  # read the coordinates of the third Point A
  a_coords = lines[2].split()

  # read the coordinates of the fourth Point B
  b_coords = lines[3].split()

  # print the string representation of the line AB
  ab = Line (float(a_coords[0]), float(a_coords[1]), float(b_coords[0]), float(b_coords[1]))
  print ("Line AB:", ab)

  # print if the lines PQ and AB are parallel or not
  if (Line.is_parallel (pq, ab)):
    print ("PQ is parallel to AB")
  else:
    print ("PQ is not parallel to AB")

  # print if the lines PQ and AB (or extensions) are perpendicular or not
  if (Line.is_perpendicular (pq, ab)):
    print ("PQ is perpendicular to AB")
  else:
    print ("PQ is not perpendicular to AB")

  # print coordinates of the intersection point of PQ and AB if not parallel
  if (not Line.is_parallel (pq, ab)):
    print ("Intersection point of PQ and AB:", Line.intersection_point (pq, ab))
  
  # read the coordinates of the fifth Point G
  g_coords = lines[4].split()
  G = Point (float(g_coords[0]), float(g_coords[1]))

  # read the coordinates of the sixth Point H
  h_coords = lines[5].split()
  H = Point (float(h_coords[0]), float(h_coords[1]))

  # print if the the points G and H are on the same side of PQ
  if (Line.on_same_side (pq, G, H)):
    print ("G and H are on the same side of PQ")
  else:
    print ("G and H are not on the same side of PQ")
    
  # print if the the points G and H are on the same side of AB
  if (Line.on_same_side (ab, G, H)):
    print ("G and H are on the same side of AB")
  else:
    print ("G and H are not on the same side of AB")
    
  # read the radius of the circleA and the coordinates of its center
  circ_a = lines[6].split()
  circleA = Circle (float(circ_a[0]), float(circ_a[1]), float(circ_a[2]))

  # read the radius of the circleB and the coordinates of its center
  circ_b = lines[7].split()
  circleB = Circle (float(circ_b[0]), float(circ_b[1]), float(circ_b[2]))

  # print the string representation of circleA and circleB
  print ("CircleA:", circleA)
  print ("CircleB:", circleB)
  
  # determine if circleB is inside circleA
  if (Circle.is_inside_circle (circleA, circleB)):
    print ("CircleB is inside of CircleA")
  else:
    print ("CircleB is not inside CircleA")

  # determine if circleA intersects circleB
  if (Circle.does_intersect_circle (circleA, circleB)):
    print ("CircleA does intersect CircleB")
  else:
    print ("CircleA does not intersect CircleB")

  # close file "geometry.txt"
  infile.close()

main()
