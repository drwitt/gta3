

class Bus(Vehicle):
    """Class Bus inherits from Vehicle."""
    def __init__(self, mpg, numwheels, color, speed):
        self.mpg = mpg
        super().__init__(numwheels, color, speed)