class Complex:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def __repr__(self):
        if self._y < 0:
            return f"{self._x}-{abs(self._y)}*i"
        return f"{self._x}+{self._y}*i"

    def _add__(self, other):
        real = self._x + other._x
        imag = self._y + other._y 
        return Complex(real, imag)
    
    def __sub__(self, other):
        real = self._x - other._x
        imag = self._y - other._y 
        return Complex(real, imag)

    def __mul__(self, other):
        real = self._x * other._x - self._y * other._y
        imag = self._x * other._y + other._x * self._y
        return Complex(real, imag)

    def __truediv__(self, other):
        real = self._x * other._x + self._y * other._y
        imag = self._y * other._x - self._x * other._y
        divider = float(other._x ** 2 + other._y ** 2)
        return Complex(real/divider, imag/divider)

c1 = Complex(1, -5)
c2 = Complex(5, 2)
print(c1)
print(c2)
res = c1 * c2
print(res)

c3 = Complex(1, 2)
c4 = Complex(2, -1)
res = c3 / c4
print(res)
