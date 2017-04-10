
class Vector(object):
	
	def __init__(self, x, y):
		self._x = float(x)
		self._y = float(y)
	
	@property
	def x(self):
		return self._x

	@property
	def y(self):
		return self._y

	def __iter__(self):
		return (i for i in (self.x, self.y))

	def __abs__(self):
		return abs(self._x) + abs(self._y)

	def __repr__(self):
		class_name = type(self).__name__
		return "{}({!r}, {!r})".format(class_name, *self)

	def __str__(self):
		return str(tuple(self))

	def __bool__(self):
		return bool(abs(self))

	def __eq__(self, other):
		return tuple(self) == tuple(other)

	def __add__(self, other):
		cls = type(self)
		return cls(*(tuple(self) + tuple(other)

	def __radd__(self, other):
		return other + self

	def __sub__(self, other):
		cls = type(self)
		return cls(*(tuple(self) - tuple(other)))

	def __rsub__(self, other):
		return -other + self

	def __pos__(self):
		cls = type(self)
		return cls(self)

	def __neg__(self):
		cls = type(self)
		return cls(-i for i in self)

