# -*- coding: utf-8 -*-

class SchoolMember(object): #for all school members
	def __init__(self,name,age):
		self.name=name
		self.age=age
		print('(Initialized SchoolMember:%s)' %self.name) #用%作格式化，区别format
	
	def tell(self): #tell me details
		print('Name:"{}" Age:"{}"'.format(self.name,self.age),end=" ") #end的作用是让子类打印在一行，不换行

class Teacher(SchoolMember):
	def __init__(self,name,age,salary):
		SchoolMember.__init__(self,name,age)
		self.salary=salary
		print('(Initialized Teacher:{})'.format(self.name))
	
	def tell(self):
		SchoolMember.tell(self)
		print('Salary:"{}"'.format(self.salary))

class Student(SchoolMember):
	def __init__(self,name,age,marks):
		SchoolMember.__init__(self,name,age)
		self.marks=marks
		print('(Initialized Student:{})'.format(self.name))
	
	def tell(self):
		SchoolMember.tell(self)
		print('Marks:"{:d}"'.format(self.marks))

t=Teacher('Mrs.Wenny',40,30000)
s=Student('Daniel',25,75)

print()
members=[t,s]
for member in members:
	member.tell()

