class Item:
	def __init__(self, name):
		self._item_name = name
		self._owner_name = None

	def set_owner(self, o):
		self._owner_name = o

	def add(self, sub_item):
		pass

	def remove(self, sub_item):
		pass

	def display(self):
		pass

class ClickableItem(Item):
	def __init__(self, name):
		super().__init__(name)

	def add(self, sub_item):
		raise Exception('Clickable element dose not have subitems')

	def remove(self, sub_item):
		raise Exception('Clickable element dose not have subitems')

	def display(self):
		print(self._owner_name + self._item_name)

class DropDownItem(Item):

	def __init__(self, name):
		super().__init__(name)
		self.__children = []

	def add(self, sub_item):
		sub_item.set_owner(self._item_name)
		self.__children.append(sub_item)

	def remove(self, sub_item):
		self.__children.remove(sub_item)

	def display(self):
		for item in self.__children:
			if self._owner_name is not None:
				print(self._owner_name, end='')
			item.display()


if __name__ == '__main__':
	file: Item = DropDownItem('File->')

	create: Item = DropDownItem('Create->')
	open_: Item = DropDownItem('Open->')
	exit_: Item = ClickableItem('Exit')
	file.add(create)
	file.add(open_)
	file.add(exit_)

	project: Item = ClickableItem('Project...')
	repository: Item = ClickableItem('Repository...')
	create.add(project)
	create.add(repository)

	solution: Item = ClickableItem('Solution...')
	folder: Item = ClickableItem('Folder...')

	open_.add(solution)
	open_.add(folder)

	file.display()
	print()

	file.remove(open_)
	file.display()
	print()
