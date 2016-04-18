#!/usr/bin/env python
# The above line is an environment directive; please ignore it

# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?
# abstraction
# polymorphism
# encapsulation

# Explain each concept.

# 1. What is a class?
# It's a generalized definition of a single concept. 

# 2. What is an instance attribute?
# It's an attribute specific to an instance of an object. 

# 3. What is a method?
# It's a function that's tied to a class.

# 4. What is an instance in object orientation?
# It's a specific, actual, individual object. 

# 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.
# A class attribute is one attribute shared for the whole class, whereas the instance attribute is
# specific to that instance. 


# Parts 2 through 5:
# Create your classes and class methods

# Directions: Make Python classes that could store the each of the following three pieces of data. Use the dictionaries below as examples to guide you in creating class definitions for the following objects. Define an __init__ method to allow callers of this class to provide initial values for each attribute.

# Student

# Students can have first and last names and addresses. Here are two example students. Write a 
# class that can store data like this:

# {'first_name': 'Jasmine',
#  'last_name': 'Debugger',
#  'address': '0101 Computer Street'}

# {'first_name': 'Jaqui',
#  'last_name': 'Console',
#  'address': '888 Binary Ave'}

class Student():

	def __init__(self, first_name, last_name, address):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address


# Question

# Questions are a question & a correct answer; here are two example questions. Write a class that could store data like this:

# {'question': 'What is the capital of Alberta?',
#  'correct_answer': 'Edmonton'}

# {'question': 'Who is the author of Python?',
#  'correct_answer': 'Guido Van Rossum'}

# Add a method to the Question class that prints the question to the console and prompts the user 
# for an answer. It should return True or False depending on whether the correct answer matches 
# the user's answer.

# For example

# $ python -i skills.py
# >>> question = Question(
# ...     'What is the method for adding an element to a set?',
# ...     '.add()')
# >>> question.ask_and_evaluate()
# What is the method for adding an element to a set? > .add()
# True

class Question():

	def __init__(self, question, answer):
		self.question = question
		self.correct_answer = answer

	def ask_and_evaluate(self):
		possible_answer = raw_input(self.question + " ")
		return (possible_answer == self.correct_answer)


# Exam

# Notice that an Exam should have an attribute called questions. Simply initialize the questions 
# attribute as an empty list in the body __init__ function. We'll deal with adding questions to 
# the exam later on in this assignment. Your __init__ function should take a name for the exam 
# as a parameter.

# A Note on Attributes
# Though we've mainly seen attributes that are strings or integers, remember: attributes can also 
# be lists, and many other data types. In the case of our questions attribute, we'll have a list 
# of Question objects.

# For example, here are two exams. Make a class that could store data like this:

# {'name':'Midterm',
#  'questions': [

#     {'question':'What is the capital of Alberta?',
#      'correct_answer': 'Edmonton'},

#     {'question': 'Who is the author of Python?',
#      'correct_answer': 'Guido Van Rossum' }

#   ]
# }

# {'name':'Final',
#  'questions': [

#     {'question':"Who is Ubermelon's competition?",
#      'correct_answer': 'Sqysh'},

#     {'question': "What is Balloonicorn's favorite color?",
#      'correct_answer': 'Sparkles'}

#   ]
# }

# Add a method to the Exam class which takes a question and a correct_answer as parameters, makes 
# a Question from those, and adds it to the exam's list of questions.

# For example

# $ python -i skills.py
# >>> exam = Exam('midterm')
# >>> exam.add_question(
# ...     'What is the method for adding an element to a set?',
# ...     '.add()')

# Add a method to the Exam class which administers all of the exam's questions, and returns the 
# user's score at the end.

# So, building on our code from problem 2, here's how the Exam class should work.

# $ python -i skills.py
# >>> exam = Exam('midterm')
# >>> exam.add_question(
# ...     'What is the method for adding an element to a set?',
# ...     '.add()')
# >>> exam.administer()
# What is the method for adding an element to a set? > .add()
# 1.0

# Hint
# Here's some pseudocode for the administer method.

# Inside the Exam.administer method, you'll need to first initialize a variable called score; 
# set it to zero.

# Next, loop through each of the questions in the exam.

# For each question, call the question's method from Problem #2 - ask_and_evaluate.

# If the return value of ask_and_evaluate is True, increment the score.

# After the last question has been administered, return the score.


class Exam():

	def __init__(self, name, questions = [] ):
		self.score = 0
		self.name = name
		self.questions = questions

	def add_question(self, question, correct_answer):

		self.questions.append(Question(question, correct_answer))


	def administer(self):

		for q in self.questions:
			if q.ask_and_evaluate():
				self.score += 1

		return self.score


# Write a function, take_test, that takes an exam and a student as parameters, administers the 
# exam, and assigns the score to the student instance as a new attribute called score.

def take_test(exam, student):
	student.score = exam.administer()
	print student.score


# Write a function, example, which does the following:
# Creates an exam
# Adds a few questions to the exam
# These should be part of the function; no need to prompt the user for questions.
# Creates a student
# Administers the test for that student

def example():
	exam = Exam('Exam PLE')
	exam.add_question('What is the method for adding an element to a set?','.add()')
	exam.add_question('What is the capital of Alberta?','Edmonton')
	exam.add_question('Who is the author of Python?','Guido Van Rossum')
	exam.add_question("Who is Ubermelon's competition?",'Sqysh')
	exam.add_question("What is Balloonicorn's favorite color?",'Sparkles')

	chriki_chekorir = Student('Chriki', 'Chekorir', 'A village in Kenya')

	take_test(exam, chriki_chekorir)


# A “quiz” is like an exam — it’s a set of questions that students are prompted to answer. However, 
# whereas exams are given a percentage score, quizzes are pass/fail: if you answered at least half 
# of the questions correct, you pass the quiz. When you call the administer method on a quiz, it 
# should only return True if you passed or False if you failed.
#
# Think about we could solve this requirement: we have an Exam class and we want to have a Quiz
# class that is similar.
#
# Write code to solve this problem. Incorporate as many of the “design” parts of the class lectures
# as you feel comfortable with.

# I ran out of time for this :-(
