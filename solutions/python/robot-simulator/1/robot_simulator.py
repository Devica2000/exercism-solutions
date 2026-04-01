# Globals for the directions
# Change the values as you see fit

NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

class Robot:
    
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, instructions):
        for cmd in instructions:
            if cmd == 'R':
                self.direction = (self.direction + 1) % 4
            elif cmd == 'L':
                self.direction = (self.direction - 1) % 4
            elif cmd == 'A':
                if self.direction == 0:
                    self.y_pos += 1
                elif self.direction == 2:
                    self.y_pos -= 1
                elif self.direction == 1:
                    self.x_pos += 1
                elif self.direction == 3:
                    self.x_pos -= 1

    @property
    def coordinates(self):
        return (self.x_pos, self.y_pos)
        

        
