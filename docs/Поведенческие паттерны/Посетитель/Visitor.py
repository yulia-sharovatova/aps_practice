from typing import List

class IVisitor():
	def visit(self, place: 'IPlace'):
		pass

class IPlace():
	def accept(self, visitor: IVisitor):
		pass

class Zoo(IPlace):
	def accept(self, visitor: IVisitor):
		visitor.visit(self)

class Cinema(IPlace):
	def accept(self, visitor: IVisitor):
		visitor.visit(self)

class Circus(IPlace):
	def accept(self, visitor: IVisitor):
		visitor.visit(self)

class Person(IVisitor):
	def __init__(self): 
		self.value = ''

	def visit(self, place: IPlace):
		if isinstance(place, Zoo):
			self.value += 'Zoo '
		elif isinstance(place, Cinema):
			self.value += 'Movie '
		elif isinstance(place, Circus):
			self.value += 'Circus '

if __name__ == "__main__":
	places: List[IPlace] = [Zoo(), Cinema(), Circus()]

	visitor = Person()

	for place in places:
		place.accept(visitor)

	print(visitor.value)

