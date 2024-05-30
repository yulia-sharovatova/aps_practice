#Interface Reader and classes
class IDataReader:
	def read(self):
		pass

class DataBaseReader(IDataReader):
	def read(self):
		print('Data from DB ', end='')

class FileReader(IDataReader):
	def read(self):
		print('Data from File ', end='')

class Sender:
	def __init__(self, data_reader:IDataReader):
		self.reader = data_reader

	def set_data_reader(self, data_reader:IDataReader):
		self.reader = data_reader

	def send(self):
		pass

class EmailSender(Sender):
	def __init__(self, data_reader:IDataReader):
		super().__init__(data_reader)

	def send(self):
		self.reader.read()
		print(' send by Email')

class TelegramSender(Sender):
	def __init__(self, data_reader:IDataReader):
		super().__init__(data_reader)

	def send(self):
		self.reader.read()
		print(' send by Telegram')

#Example of use
if __name__ == '__main__':
	sender = EmailSender(DataBaseReader())
	sender.send()

	sender.set_data_reader(FileReader())
	sender.send()

	sender = TelegramSender(DataBaseReader())
	sender.send()
