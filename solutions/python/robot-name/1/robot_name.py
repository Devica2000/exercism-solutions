import random

class Robot:
    all_names = set()

    def __init__(self):
        self.name = None
        self.reset()
    
    def generate_name(self):
        robot_name = ""
        letter_start = ord('A')
        letter_end = ord('Z')

        for _ in range(2):
            robot_name += chr(random.randint(letter_start, letter_end))
        robot_name += str(random.randint(100, 999))

        if robot_name not in Robot.all_names:
            Robot.all_names.add(robot_name)
        else:
            return self.generate_name()

        return robot_name
        
    def reset(self):
        self.name = self.generate_name()
