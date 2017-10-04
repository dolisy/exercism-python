class Direction(object):
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y
    self.coordinates = "(%s,%s)" % (self.x, self.y)

WEST = Direction(-1,0)
NORTH = Direction(0,1)
EAST = Direction(1,0)
SOUTH = Direction(0,-1)

def turn_right(direction_instance):
  if direction_instance == WEST:
    return NORTH
  elif direction_instance == NORTH:
    return EAST
  elif direction_instance == EAST:
    return SOUTH
  elif direction_instance == SOUTH:
    return WEST
  else:
    raise ValueError("direction is not valid")

def turn_left(direction_instance):
  return turn_right(turn_right(turn_right(direction_instance)))

class Robot(object):
  def __init__(self, bearing=NORTH, x=0, y=0):
    self.bearing = bearing
    self.x = x
    self.y = y
    self.coordinates = (self.x, self.y)

  def advance(self):
    self.x += self.bearing.x
    self.y += self.bearing.y
    self.coordinates = (self.x, self.y)

  def turn_right(self):
    self.bearing = turn_right(self.bearing)

  def turn_left(self):
    self.bearing = turn_left(self.bearing)

  def simulate(self, string):
    for letter in string:
      if letter == "L":
        self.turn_left()
      elif letter == "R":
        self.turn_right()
      elif letter == "A":
        self.advance()
      else:
        raise ValueError("direction is not valid")




