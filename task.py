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

import json

def load_data(filename):
	return json.load(open(filename))

def set_student(diary, **kwargs):
	student = {}
	student["firstname"] = kwargs["firstname"]
	student["lastname"] = kwargs["lastname"]
	student["grade"] = kwargs["grade"]
	student["attendance"] = kwargs["attendance"]
	diary[kwargs["student_index"]] = student

def set_diary(data, **kwargs):
	data[kwargs["diary_index"]] = {}

def get_diary_avg(data,used_key):
	elements = [data[student_key][used_key] for student_key in data]
	if len(elements) == 0:
		return 0
	return sum(elements) / float(len(elements)) 

def get_total_avg(data, used_key):
	elements = [data[diary_key][student_key][used_key] for diary_key in data for student_key in data[diary_key]]
	if len(elements) == 0:
		return 0
	return sum(elements) / float(len(elements)) 

def save_data(data,filename):
    with open(filename, 'w') as outfile:
		json.dump(data, outfile)

if __name__ == "__main__":
	data = load_data('data.json')
	
	set_diary(data,diary_index='New Diary')
	set_student(data['New Diary'], firstname="Jan", lastname="Nowy", grade=4, attendance=2, student_index=1)
	
	print('Avg total grade: {0}'.format(get_total_avg(data,'grade')))
	print('Avg total attendance: {0}'.format(get_total_avg(data,'attendance')))

	for diary_key in data:
		print('Avg grade for {0}: {1}'.format(diary_key,get_diary_avg(data[diary_key],'grade')))
		print('Avg attendance for {0}: {1}'.format(diary_key,get_diary_avg(data[diary_key],'attendance')))

	save_data(data,'data2.json')