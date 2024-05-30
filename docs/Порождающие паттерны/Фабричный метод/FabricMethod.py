#Create interace of delivery transport and concrete classes
class ITransport:
	def deliver(self):
		pass

class Ship(ITransport):
	def deliver(self):
		print('Delivering by Ship')

class Truck(ITransport):
	def deliver(self):
		print('Delivering by Truck')

#Create interace of logistics and concrete classes
class ILogistics:
	def create(self):
		pass

class SeaLogistics(ILogistics):
	def create(self):
		return Ship()

class RoadLogistics(ILogistics):
	def create(self):
		return Truck()

#Example of use
if  __name__ == "__main__":
	#creator = SeaLogistics()
	creator = RoadLogistics()

	transport = creator.create()
	transport.deliver()
