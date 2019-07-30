class Point:
    def __init__(self, x=0, y=0, z=0):
        self._x = x
        self._y = y
        self._z = z

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y

    def get_z(self):
        return self._z

    def set_x(self, x):
        self._x = x
    
    def set_y(self, y):
        self._y = y

    def set_z(self, z):
        self._z = z

    def __add__(self, other):
        return (self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())

    def __sub__(self, other):
        return (self._x - other.get_x(), self.get_y() - other.get_y(), self._z - other.get_z())

    def __mul__(self, other):
        return (self._x * other.get_x(), self._y * other.get_y(), self._z * other.get_z())

    def __div__(self, other):
        return (self._x / other.get_x(), self._y / other.get_y(), self._z / other.get_z())

p1 = Point(1, 2, 3)
p2 = Point(1, 2, 3)

print(p1 * p2)