class IMediator():
	def notify(self, emp: 'Employee', msg: str):
		pass

class Employee():
	def __init__(self, mediator: IMediator):
		self._mediator = mediator

	def set_mediator(self, med: IMediator):
		self._mediator = med

class Designer(Employee):
	def __init__(self, med: IMediator = None):
		super().__init__(med)
		self.__is_working = False

	def execute_work(self):
		print('<- Designer working')
		self._mediator.notify(self, 'Designer make project...')

	def set_work(self, state: bool):
		self.__is_working = state
		if state:
			print('<- Designer is free')
		else:
			print('<- Designer is busy')

class Director(Employee):
	def __init__(self, med: IMediator = None):
		super().__init__(med)
		self.__text: str = None

	def give_command(self, txt: str):
		self.__text = txt
		if txt == '':
			print('-> Director know that Designer already working')
		else:
			print('-> Director give command: ' + txt)
		self._mediator.notify(self, txt)

class Controller(IMediator):
	def __init__(self, designer: Designer, director: Director):
		self.__designer = designer
		self.__director = director
		designer.set_mediator(self)
		director.set_mediator(self)

	def notify(self, emp: 'Employee', msg: str):
		if isinstance(emp, Director):
			if msg == '':
				self.__designer.set_work(False)
			else:
				self.__designer.set_work(True)
		
		if isinstance(emp, Designer):
			if msg == 'Designer make project...':
				self.__director.give_command('')

if __name__ == "__main__":
	designer = Designer()
	director = Director()
	mediator = Controller(designer, director)

	director.give_command('Make project')
	designer.execute_work()
