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
        return Point(self._x + other.get_x(), self._y + other.get_y(), self._z + other.get_z())

    def __sub__(self, other):
        return Point(self._x - other.get_x(), self.get_y() - other.get_y(), self._z - other.get_z())

    def __mul__(self, other):
        return Point(self._x * other.get_x(), self._y * other.get_y(), self._z * other.get_z())

    def __div__(self, other):
       return Point(self._x / other.get_x(), self._y / other.get_y(), self._z / other.get_z())

    def __repr__(self):
        return "x = {}, y = {}, z = {}".format(self._x, self._y, self._z)

    def __neg__(self):
        return Point(self * Point(-1, -1, -1))

p1 = Point(1, 2, 3)
p2 = Point(1, 2, 3)

print(p1 * p2)
print(-p1)