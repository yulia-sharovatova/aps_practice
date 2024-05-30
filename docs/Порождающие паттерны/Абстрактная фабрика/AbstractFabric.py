#Create interface and concrete classes for Engine
class IEngine:
	def release_engine(self):
		pass

class JapaneseEngine(IEngine):
	def release_engine(self):
		print('Japan Engine')

class RussianEngine(IEngine):
	def release_engine(self):
		print('Russian Engine')

#Create interface and concrete classes for Cars
class ICar:
	def release_car(self, engine:IEngine):
		pass

class JapaneseCar(ICar):
	def release_car(self, engine:IEngine):
		print('Create Japan Car, ', end='')
		engine.release_engine()

class RussianCar(ICar):
	def release_car(self, engine:IEngine):
		print('Create Russian Car, ', end='')
		engine.release_engine()

#Create interface and concrete classes for Factories
class IFactory():
	def create_engine(self) -> IEngine:
		pass

	def create_car(self) -> ICar:
		pass

class JapaneseFactory(IFactory):

	def create_engine(self) -> IEngine:
		return JapaneseEngine()

	def create_car(self) -> ICar:
		return JapaneseCar()


class RussianFactory(IFactory):

	def create_engine(self) -> IEngine:
		return RussianEngine()

	def create_car(self) -> ICar:
		return RussianCar()

#Example of use
if __name__ == '__main__':
	#Factory = RussianFactory()
	Factory = JapaneseFactory()

	Engine = Factory.create_engine()
	Car = Factory.create_car()
	Car.release_car(Engine)
