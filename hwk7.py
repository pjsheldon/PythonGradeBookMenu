'''--------By: PJ Sheldon---------
	--------Date: 8/20/20---------
	hwk7.py programming assignment 5
	SEC-290 Wilmington University'''

class Grades:                                                        # constructor 
	
	def __init__(self, score):

		self.score = score

		finalExamScore = 0
		quizScores = []
		assignmentScores = []

	def quizScore(self, score):
		self.quizScores.append(score)

	def assignmentScore(self, score):
		self.assignmentScores.append(score)

	def finalScore(self, score): 
		self.finalExamScore = score

	def currentAverage(self):
		if len(Grades.assignmentScores) > 0:
			assignmentScoreAverage = sum(Grades.assignmentScores)\
										// len(Grades.assignmentScores)
		else:
			assignmentScoreAverage = 0

		if len(Grades.quizScores) > 0:
			quizScoreAverage = sum(Grades.quizScores)\
								// len(Grades.quizScores) 
		else:
			quizScoreAverage = 0

		currentGrade = (0.4 * Grades.finalExamScore)\
						+ (0.3 * quizScoreAverage)\
						+ (0.3 * assignmentScoreAverage)
		return currentGrade


menu = ('''
0: Exit
1: Enter assignment grade
2: Enter quiz grade
3: Enter final exam grade
4: Display current grade
''')



done = False 
while not done:
	
	print("==========")                                            # program title
	print("Grade Book")
	print("==========")
	print(menu)
	selection = input("please make a selection between 0 and 4: ") # input for menu
	print()                                                        # spacing 
	gradeBook = Grades()

	if selection == '0':
		done = True                                                # variable is oppistie of while loop statement making the while loop false and claosing it
		print('Good bye!')
		print('Thanks for Playing!')                               # Exit messaging.

	elif selection == '1':                                          # selection 1 
		print()
		print("Assignments Grade")                                  # Title 
		print()
		
		while True:                                                 # validation while loop
			
			try:
				assignmentGrade = float(input('Please enter a grade for the assignment: ')) # float question
				grades.assignmentScore(assignmentGrade)          # class / method
				break
			
			except:
				print()
				print('Please check your input and try again.')      # Validation for assignment grade
				print()
				continue

	elif selection == '2':                                          #  slection 2 
		print()
		print("Quiz Grade")                                         # Quiz Grade
		print()
		
		while True:                                                 # validation while loop
			
			try:
				quizGrade = float(input('Please enter a grade for the quiz: ')) # quiz grade quesion
				Grades.quizScore(quizGrade)                        # class / method 
				break
			
			except:
				print('Please check your input and try again.')    # validation 
				continue

	elif selection == '3':                                          # selection 3 
		print()
		print("Final Exam Score")                                   # final exam score
		print()
		
		while True:                                                 # while loop validation
			
			try:
				finalGrade = float(input('Please enter a grade for the final exam: ')) # final grade question 
				Grades.finalScore(finalGrade)                     # class / method 
				break
			
			except:
				print('Please check your input and try again.')     # Validation
				continue

	elif selection == '4':                                          # Selection 4 
		print()
		print("Current Grade")                                      # current Grade display 
		print()
		
		average = gradeBook.currentAverage()                           # class / method
		print('Your current grade average is: ' + str(average))

	else:
		print("please select 0, 1, 2, 3, or 4")                     # if the wrong menu number is entered
		print()
		continue 
