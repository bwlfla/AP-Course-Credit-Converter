#CHARLES COURSE, PRINT OUT FORM

import pandas as pd
#CANT INPUT SAME EXAM TWICE
#num to FSU equivalent
#num to UF equivalent
#ap menu
#make main functions and side functions
#object oriented??

#object of all??
#course equivalent object containing fsu and uf

class Course:
	def __init__(self, examNum, score):
		self.examNum = examNum
		self.score = score
		#self.examName = ""
		self.UFClass = ""
		self.UFCredit = 0
		self.FSUClass = ""
		self.FSUCredit = 0
		self.findUF()
		self.findFSU()
		#findexamname
	
	#def findClassName(self):
	
	#first name, then credits!
	
	def findUF(self):
		name = UFdf.iat[self.examNum,(self.score - 2)]
		
		if "(" in name: #if parenthesis, then number of credits is specified uniquely 
			x = name.split("(")
			self.UFClass = x[0]
			self.UFCredit = int((x[1])[0])
		else:
			self.UFClass = name
			if (self.score == 3):
				self.UFCredit = 3
			else:
				self.UFCredit = 6
	
	def findFSU(self):
		num = self.examNum
		FSUnum = 0
		
		#conversion to FSU order
		if (1 <= num <= 2):
			FSUnum = num + 42
		elif (3 <= num <= 6):
			FSUnum = num - 3
		elif (num == 7):
			FSUnum = 6
		elif (num == 8):
			FSUnum = 5
		elif (9 <= num <= 11):
			FSUnum = num - 2
		elif (num == 12):
			FSUnum = 11
		elif (num == 13):
			FSUnum = 42
		elif (14 <= num <= 18):
			FSUnum = num - 2
			
		print(FSUdf.iat[FSUnum,self.score - 2])
		
		#finding the scores
		
	

#possible library class, contains all courses and statistics like total number of credits at each school, display function??

def menu1():
	print("\nAP Exam Menu")
	print("------------")
	print("1. 2-D Art and Design")
	print("2. 3-D Art and Design")
	print("3. Art History")
	print("4. Biology")
	print("5. Calculus AB")
	print("6. Calculus BC")
	print("7. Capstone Research")
	print("8. Capstone Seminar")
	print("9. Chemistry")
	print("10. Chinese Language and Culture")
	print("11. Computer Science A")
	print("12. Computer Science Principles")
	print("13. Drawing")
	print("14. Economics: Macro")
	print("15. Economics: Micro")
	print("16. English Language and Composition")
	print("17. English Literature and Composition")
	print("18. Environmental Science")
	print("19. European History")
	print("20. French Language")
	print("21. German Language")
	print("22. Govt. and Politics: Comparative")
	print("23. Govt. and Politics: United States")
	print("24. Human Geography")
	print("25. Italian Language and Culture")
	print("26. Japanese Language and Culture")
	print("27. Latin")
	print("28. Music Theory")
	print("29. Physics 1")
	print("30. Physics 2")
	print("31. Physics B")
	print("32. Physics C: Electricity and Magnetism")
	print("33. Physics C: Mechanics")
	print("34. Psychology")
	print("35. Spanish Language")
	print("36. Spanish Literature")
	print("37. Statistics")
	print("38. United States History")
	print("39. World History: Modern")
	examNum = int(input("Please select an AP exam: "))

	print("\n")
	score = int(input("Please enter score (1-5) earned on exam: "))
	
	if (score == 1 or score == 2):
		print("Score too low, no credit earned.") 
	elif( score < 1 or score > 5):
		print("invalid score")
	else:
		c1 = Course(examNum, score)
		courses.append(c1)

courses = [];
exit = False

UFdf = pd.read_excel("UF.xlsx")
FSUdf = pd.read_excel("Computational MathFSU.xlsx")

print("\nWelcome to the AP credit Converter!")
print("This program converts AP scores into the course equivalents at the University of Florida and Florida State University.")

while(exit == False):
	
	print("\nCredit Converter Main Menu")
	print("1. Add Exam")
	print("2. View All Exams")
	print("3. Exit")
	menuOption = input("Please select an option: ")
	
	
	if (menuOption == "1"):
		menu1()
	elif(menuOption == "2"):
		for x in courses:
			print(x.score)
	elif (menuOption == "3"):
		print("Thank you for using Credit Converter. Goodbye!")
		exit = True
	else:
		print("invalid input")
	
	
	


# TRY CATCH FOR INVALID INPUTS
#display exam grades
#display cummulative exam scores







#menu selecting AP exam

#menu selecting AP exam grade

#exit and more exam grade options


#display running total