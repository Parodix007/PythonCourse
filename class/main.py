class Person:

	def __init__(self, name, last_name, age):
		self.__name = name
		self.last_name = last_name
		self.age = age

	def get_name(self):
		print(f'{self.__name}')

	def set_name(self, new_name):
		self.__name = new_name

person1 = Person('john', 'doe', 40)

person1.get_name()

person1.set_name('kamil')

person1.get_name()
