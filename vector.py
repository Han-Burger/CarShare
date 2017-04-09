
class Vector(Object):
	
	def __init__(self, x, y):
		self._x = x
		self._y = y
	
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
		return "{}({}, {})".format(class_name, *self)
