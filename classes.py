class Student:

	def __init__(self):
		self.courses = []

	@property
	def age(self):
		return self.age
		
	@age.setter
	def age(self, value):
		self.age = value

	@property
	def name(self):
		return self.name 
	
	@name.setter
	def name(self, value):
		self.name = value

	def register(self, course):
		self.courses.append(course)
		
	def total_costs(self):
		total_costs = 0
		for course in self.courses:
			total_costs += course.cost
		return total_costs

	def show_classes(self):
		for course in self.courses:
			print course.__class__

class Course:
	
	@property
	def cost(self):
		return self.cost # Int is not callable
		
	@property
	def date(self):
		return self.date
	
	def senior_discount(self, student):
		if student.age > 64:
			self.cost *= 0.8
			return True 
		return False
		
class LearnPython(Course):

	def __init__(self):
		self.cost = 45
		self.date = "09/25"
		
class LearnBaristo(Course):

	def __init__(self):
		self.cost = 75
		self.date = "10/24"
	
student = Student()
student.name = "Alexander"
student.age = 29

student.register(LearnPython())
student.register(LearnBaristo())

print "total costs", str(student.total_costs()) # 120

student.show_classes()

print "discount:", LearnPython().senior_discount(student)

