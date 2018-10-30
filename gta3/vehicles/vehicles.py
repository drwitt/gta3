class Vehicle:
    def __init__(self, numwheels, color, speed):
        self.numwheels = numwheels
        self.color = color
        self.speed = speed

    @property
    def speed(self):
        print('getting value ')
        return self._speed

    @speed.setter
    def speed(self, value):
        print('setting value ')
        if value > 150:
            raise ValueError("Speed Exeeds the maximum allowable value.")
        self._speed = value

    def __repr__(self):
        """Flexible string representation for any number of initialized variables."""
        return '{} at 0x{}({})'.format(
            self.__class__.__name__,
            id(self),
            ', '.join('{}={}'.format(k, v)
                      for k, v in sorted(self.__dict__.items())))