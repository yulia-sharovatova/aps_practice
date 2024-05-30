class ProviderCommunication:
	def receive(self):
		print('Get production')

	def payment(self):
		print('Pay to the producer')

class Site:
	def placement(self):
		print('Place to the site')

	def delete(self):
		print('Delete from site')

class Database:
	def insert(self):
		print('Insert in DB')

	def delete(self):
		print('Delete from DB')

class MarketPlace:
	def __init__(self):
		self._provider = ProviderCommunication()
		self._site = Site()
		self._database = Database()

	def product_receipt(self):
		self._provider.receive()
		self._site.placement()
		self._database.insert()

	def product_release(self):
		self._provider.payment()
		self._site.delete()
		self._database.delete()


if __name__ == '__main__':
	market_place = MarketPlace()
	market_place.product_receipt()
	print()
	market_place.product_release()
