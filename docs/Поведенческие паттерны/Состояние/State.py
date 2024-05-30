class State:
	def __init__(self):
		self._traffic_light: 'TrafficLight' = None

	def next_state(self):
		pass

	def previous_state(self):
		pass

class TrafficLight:
	def __init__(self, st: State):
		self.set_state(st)

	def set_state(self, st: State):
		self.__state = st
		self.__state._traffic_light = self

	def next_state(self):
		self.__state.next_state()

	def previous_state(self):
		self.__state.previous_state()

class GreenState(State):
	def next_state(self):
		print('From green to yellow')
		self._traffic_light.set_state(YellowState())

	def previous_state(self):
		print('Now light is green')

class YellowState(State):
	def next_state(self):
		print('From yellow to red')
		self._traffic_light.set_state(RedState())

	def previous_state(self):
		print('From yellow to green')
		self._traffic_light.set_state(GreenState())

class RedState(State):
	def next_state(self):
		print('Now is to red')

	def previous_state(self):
		print('From red to yellow')
		self._traffic_light.set_state(YellowState())


if __name__ == "__main__":
	traffic_light = TrafficLight(YellowState())
	traffic_light.next_state()
	traffic_light.next_state()

	traffic_light.previous_state()
	traffic_light.previous_state()
	traffic_light.previous_state()
