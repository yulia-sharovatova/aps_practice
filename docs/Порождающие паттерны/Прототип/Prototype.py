import copy

class Sheep:
	__name: str = ''
	__params: dict = {'Weight':20, 'Height':50}

	def __init__(self, donor: 'Sheep' = None):
		if donor is not None:
			self.__name = donor.get_name()
			self.__params = copy.deepcopy(donor.get_params())

	def set_name(self, name: str) :
		self.__name = name

	def get_name(self) :
		return self.__name

	def get_params(self) -> dict:
		return self.__params

	def set_weight(self, new_weight: int):
		self.__params['Weight'] = new_weight
	
	def clone(self):
		return Sheep(self)

#Example of use
if __name__ == '__main__':
	sheep_donor = Sheep()
	sheep_donor.set_name('Dolly')

	sheep_clone = sheep_donor.clone()
	print('Donor:', sheep_donor.get_name(), sheep_donor.get_params())
	print('Clone:', sheep_clone.get_name(), sheep_clone.get_params())

	sheep_clone.set_name('New Dolly');
	sheep_clone.set_weight(44);
	print('After modification_________');

	print('Donor:', sheep_donor.get_name(), sheep_donor.get_params())
	print('Clone:', sheep_clone.get_name(), sheep_clone.get_params())
