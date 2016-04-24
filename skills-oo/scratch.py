

exam = Exam('Midterm')
exam.add_question('What is the method for adding an element to a set?', '.add()')
exam.add_question('What is the capital of Alberta?', 'Edmonton')
exam.add_question('Who is the author of Python?', 'Guido Van Rossum')
exam.add_question("Who is Ubermelon's competition?", 'Sqysh')
exam.add_question("What is Balloonicorn's favorite color?", 'Sparkles')
print exam.questions[0]


for q in exam.questions:
    print q.question
    print q.correct_answer
    print exam.score

exam.administer()

quiz = Quiz('Quiz 1')

quiz.add_question('What is the method for adding an element to a set?', '.add()')
quiz.add_question('What is the capital of Alberta?', 'Edmonton')
quiz.add_question('Who is the author of Python?', 'Guido Van Rossum')
quiz.add_question("Who is Ubermelon's competition?", 'Sqysh')
quiz.add_question("What is Balloonicorn's favorite color?", 'Sparkles')

quiz.administer()