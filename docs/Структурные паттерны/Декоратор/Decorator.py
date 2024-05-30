class IProcessor:
	def process(self):
		pass

class Transmitter(IProcessor):
	def __init__(self, data: str):
		self._data = data

	def process(self):
		print('Data {} transmitted by communication channel'.format(self._data))

class Shell(IProcessor):
	def __init__(self, pr: IProcessor):
		self._processor = pr
	
	def process(self):
		self._processor.process()

class HammingCoder(Shell):
	def __init__(self, pr: IProcessor):
		super().__init__(pr)

	def process(self):
		print('Using Hamming code->', end='')
		self._processor.process()

class Encryptor(Shell):
	def __init__(self, pr: IProcessor):
		super().__init__(pr)

	def process(self):
		print("Data encryption->", end='')
		self._processor.process()

if __name__== '__main__':
	transmitter: IProcessor = Transmitter('MESSAGE')
	transmitter.process()
	print()

	hamming_coder: Shell = HammingCoder(transmitter)
	hamming_coder.process()
	print()

	encryptor: Shell = Encryptor(hamming_coder)
	encryptor.process()
