#!/usr/bin/python3
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)

class Student:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
	def __str__(self):
		return 'Student: ' + str(self.firstname) + ' ' + str(self.lastname)

class Class:
	def __init__(self, title):
		self.title = title
		self.students = []

	def add_student(self,student):
		self.students.append((student,[]))

	def get_students(self):
		return map(lambda s: s[0], self.students)

	def add_score_for_student(self,student,score):
		student_index = self.get_students().index(student)
		self.students[student_index][1].append(score)

	def __str__(self):
		return_str = 'Class ' + self.title
		for student in self.students:
			return_str = return_str + '\n' + str(student[0]) + ' scores: ' + str(student[1])
		return return_str
	
		
def main():
	test_student_1 = Student("Jan","Kowalski")
	test_student_2 = Student("Iwona","Kowalska")

	python_class = Class("Python")

	python_class.add_student(test_student_1)
	python_class.add_student(test_student_2)

	python_class.add_score_for_student(test_student_1, 3.0)
	python_class.add_score_for_student(test_student_2, 3.5)

	print(str(python_class))
	print('main')


print('start')
main()



