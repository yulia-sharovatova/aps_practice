#Phone class - simple string for example
class Phone:
	def __init__(self):
		self.data: str = ''

	def about_phone(self) -> str:
		return self.data

	def append_data(self, string: str):
		self.data += string

#Developer class interface and two concrete builders
class IDeveloper:
	def create_display(self):
		pass
	def create_box(self):
		pass
	def system_install(self):
		pass
	def get_phone(self) -> Phone:
		pass

class AndriodDeveloper(IDeveloper):
	def __init__(self):
		self.__phone = Phone()

	def create_display(self):
		self.__phone.append_data('Create Samsung display; ')

	def create_box(self):
		self.__phone.append_data('Create Samsung box; ')

	def system_install(self):
		self.__phone.append_data('Install OS Andriod; ')

	def get_phone(self) -> Phone:
		return self.__phone

class IPhoneDeveloper(IDeveloper):
	def __init__(self):
		self.__phone = Phone()

	def create_display(self):
		self.__phone.append_data('Create Apple display; ')

	def create_box(self):
		self.__phone.append_data('Create IPhone box; ')

	def system_install(self):
		self.__phone.append_data('Install MAC OS; ')

	def get_phone(self) -> Phone:
		return self.__phone

#Director class to control build variants for Developer
class Director:
	def __init__(self, developer: IDeveloper):
		self.__developer = developer

	def set_developer (self, developer:IDeveloper):
		self.__developer = developer

	def mount_only_phone(self) -> Phone:
		self.__developer.create_box()
		self.__developer.create_display()
		return self.__developer.get_phone()

	def mount_full_phone(self) -> Phone:
		self.__developer.create_box()
		self.__developer.create_display()
		self.__developer.system_install()
		return self.__developer.get_phone()

#Example of use
if __name__ == '__main__':

	andriod_developer = AndriodDeveloper()
	iphone_developer = IPhoneDeveloper()

	director = Director(andriod_developer)

	samsung = director.mount_full_phone()
	print(samsung.about_phone())

	director.set_developer(iphone_developer)
	iphone = director.mount_only_phone()
	print(iphone.about_phone())
