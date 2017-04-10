from vector import Vector
from car import Car

class Route(object):

	def __init__(self, orig, dest):
		self._orig = Vector(orig)
		self._dest = Vector(dest)

	@property
	def orig(self):
		return self._orig

	@property
	def dest(self):
		return self._dest

	def __rper__(self):
		class_name = type(self).__name__
		return "{}({!r}, {!r})".format(class_name, self.orig, self.dest


class Trip(Route):
	
	def __init__(self, orig, dest):
		super().__init__(self, orig, dest)
		self._start = False
		self._end = False
		self._car = None
	@property
	def has_start(self):
		return self._start

	@property
	def has_end(self):
		return self._end

	@property
	def on_trip(self):
		return has_start and !had_end

	def start(car):
		self.car = car
		self._start = True

	def end():
		self.car = None
		self._end = True
		
