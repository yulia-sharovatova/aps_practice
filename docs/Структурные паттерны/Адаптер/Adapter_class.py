
class IScale:
	def get_weight(self) -> float:
		pass
	def adjust(self):
		pass

class RussianScales(IScale):
	def __init__(self, cw: float):
		self.__current_weight = cw

	def get_weight(self) -> float:
		return self.__current_weight

	def adjust(self):
		print('Russian adjust')

class BritishScales:
	def __init__(self, cw: float):
		self.__current_weight = cw

	def get_weight(self) -> float:
		return self.__current_weight

	def adjust(self):
		print('British adjust', end = '')

#Adapter class
class AdapterForBritishScales(BritishScales, IScale):
	def __init__(self, cw: float):
		super().__init__(cw)
    
	def get_weight(self) -> float:
		return super().get_weight() * 0.453

	def adjust(self):
		super().adjust()
		print(' in adapter adjust')

if __name__ == '__main__':
	rScales = RussianScales(55.)
	bScales = AdapterForBritishScales(55.)

	print(rScales.get_weight())
	print(bScales.get_weight())

	rScales.adjust()
	bScales.adjust()
