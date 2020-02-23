class Animal(object):
	def __init__(self):
		return
	
	def sound(self):
		print("animal sound")

class Dog(Animal):
	def __init__(self):
		return
	
	def sound(self):
		print("dog sound")

class Human(Animal):
	def __init__(self, name):
		self.name = name
	
	def sound(self):
		print(f"human sound: I am {self.name}")

class Student(Human):
	def __init__(self, name, school):
		super(Student, self).__init__(name)
		self.school = school
	
	def sound(self):
		print(f"student sound: I am {self.name} at {self.school}")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

human = Human("xz")
human.sound()

student = Student("xz", "cornell")
student.sound()



