class Person:
    def __init__(self, clothes_color):
        self.clothes_color = clothes_color
        self.health = 100

    @property
    def health(self):
        print('getting value ')
        return self._health

    @health.setter
    def health(self, value):
        print('setting value ')
        if (value > 100) or (value < 0):
            raise ValueError("Health exceeds limits.")
        self._health = value

    def __repr__(self):
        """Flexible string representation for any number of initialized variables."""
        return '{} at 0x{}({})'.format(
            self.__class__.__name__,
            id(self),
            ', '.join('{}={}'.format(k, v)
                      for k, v in sorted(self.__dict__.items())))

class Man(Person):
    pass

class Woman(Person):
    pass