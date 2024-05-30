class Reader():
	def parse(self, url: str):
		pass

class ResourceReader():
	def __init__(self, reader: Reader):
		self.__reader = reader

	def set_strategy(self, reader: Reader):
		self.__reader = reader

	def read(self, url: str):
		self.__reader.parse(url)

class NewsSiteReader(Reader):
	def parse(self, url: str):
		print('Read news site from:',url)

class SocialReader(Reader):
	def parse(self, url: str):
		print('Read news from sociaal network:',url)

class TelegramReader(Reader):
	def parse(self, url: str):
		print('Read news from telegram:',url)

if __name__ == "__main__":

	resource_reader = ResourceReader(NewsSiteReader())
	url = 'https://news.site'
	resource_reader.read(url)

	resource_reader.set_strategy(SocialReader())
	url = 'https://facebook.com'
	resource_reader.read(url)

	resource_reader.set_strategy(TelegramReader())
	url = '@news_channel'
	resource_reader.read(url)
