class IWorker():
	def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
		pass

	def execute(self, command: str) -> str:
		pass

class AbsWorker(IWorker):
	def __init__(self):
		self.__next_worker:IWorker = None

	def set_next_worker(self, worker: 'IWorker') -> 'IWorker':
		self.__next_worker = worker
		return worker

	def execute(self, command: str) -> str:
		if self.__next_worker is not None:
			return self.__next_worker.execute(command)
		return ''

class Designer(AbsWorker):
	def execute(self, command: str) -> str:
		if command == 'project house':
			return 'Designer make: ' + command
		else:
			return super().execute(command)

class Builder(AbsWorker):
	def execute(self, command: str) -> str:
		if command == 'build wall':
			return 'Builder make: ' + command
		else:
			return super().execute(command)

class Finish(AbsWorker):
	def execute(self, command: str) -> str:
		if command == 'paint the walls':
			return 'Finish make: ' + command
		else:
			return super().execute(command)

def give_command(worker: IWorker, command: str):
	string: str = worker.execute(command)
	if string == '':
		print(command + '- there is no performer')
	else:
		print(string)

if __name__ == '__main__':
	designer = Designer()
	builder = Builder()
	finish = Finish()

	designer.set_next_worker(builder).set_next_worker(finish)

	give_command(designer, 'project house')
	give_command(designer, 'build wall')
	give_command(designer, 'paint the walls')

	give_command(designer, 'make wires')
