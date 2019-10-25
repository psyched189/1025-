# okay lets write a class

class Employee():

	def __init__(self,first,last,pay):
		self.first = first
		self.last  = last
		self.salary = pay
		self.instaID = first.lower() + '_' + last.lower()

	def fullname(self):
		return self.first + ' ' + self.last

	def age(self,birthyear):
		return 2019 - int(birthyear)

emp1 = Employee('Yash','Shinge','$500k/yr')
emp2 = Employee('Anushka','K','$50k/yr')

print(emp1.instaID)
print(emp2.fullname())
print('Age of {} is {}'.format(emp1.first,emp1.age(1996)))
