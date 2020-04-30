import pandas as pd

class Course: # course class stores the ap exam and its course equivalency at UF and FSU
	def __init__(self, examNum, score):
		self.examNum = examNum # menu number of AP exam
		self.score = score # AP exam score
		self.examName = APdict[examNum] # name of AP exam
		self.UFClass = "" # name of equivalent class at UF
		self.UFCredit = 0 # number of credits earned at UF
		self.FSUClass = "" # name of equivalent class at FSU
		self.FSUCredit = 0 # name of equivalent class at FSU
		self.findUF() # finds class name and credits at UF
		self.findFSU() # finds class name and credits at FSU
	
	def findUF(self): # finds UF equivalency information
		name = UFdf.iat[self.examNum,(self.score - 2)] # retrieves course information from excel
		
		if "(" in name: #if parenthesis, then number of credits is specified uniquely (need to extract credit info from name)
			x = name.split("(")
			self.UFClass = x[0]
			self.UFCredit = int((x[1])[0])
			
		else: # no specific credit information, can follow general format
			self.UFClass = name
			if (self.score == 3):
				self.UFCredit = 3
			else:
				self.UFCredit = 6
	
	def findFSU(self):
	
		# need dictionary to convert between menu numbering and numbering in FSU excel spreadsheet
		FSUdict = {
			1: 43, 2: 44, 3: 0, 4: 1, 5: 2,
			6: 3, 7: 6, 8: 5, 9: 7, 10: 8, 11: 9,
			12: 11, 13: 42, 14: 12, 15: 13, 16: 14,
			17: 15, 18: 16, 19: 22, 20: 17, 21: 19,
			22: 20, 23: 21, 24: 25, 25: 26, 26: 27, 27: 29,
			28: 30, 29: 32, 30: 33, 31: 34, 32: 35,
			33: 36, 34: 37, 35: 39, 36: 40,37: 41,
			38: 23, 39: 24
		}
			
		name = FSUdf.iat[FSUdict[self.examNum], self.score - 2] # retrieves FSU info from spreadsheet
		x = name.split(")")
		x.pop()
		for i in x : # extracts name and number of credits
			self.FSUClass += i[:-2]
			self.FSUCredit = self.FSUCredit + int(i[-1:])
	

def menu1(): #menu where new exams are added
	
	print("\nAP Exam Menu") # menu displays all ap exams
	print("------------")
	for x in APdict:
		print(str(x) + ". " + APdict[x])

	examNum = int(input("Please select an AP exam: ")) # user selects desired ap exam

	print("\n")
	score = int(input("Please enter score (1-5) earned on exam: ")) # user enters exam score
	
	if (score == 1 or score == 2): # no credit is earned for scoring a 1 or a 2
		print("Score too low, no credit earned.") 
	elif( score < 1 or score > 5): # scores must be between 1 and 5
		print("invalid score")
	else: # if valid score, add to list of earned courses
		c1 = Course(examNum, score)
		courses.append(c1)
		print("AP " + courses[-1].examName + " is equivalent to " + courses[-1].UFClass + "(" + str(courses[-1].UFCredit) + " credits) at UF and " + courses[-1].FSUClass + "(" + str(courses[-1].FSUCredit) + " credits) at FSU")

# dictionary of all ap exam names
APdict = {
		1 : "2-D Art and Design",
		2: "3-D Art and Design",
		3: "Art History",
		4: "Biology",
		5: "Calculus AB",
		6: "Calculus BC",
		7: "Capstone Research",
		8: "Capstone Seminar",
		9: "Chemistry",
		10: "Chinese Language and Culture",
		11: "Computer Science A",
		12: "Computer Science Principles",
		13: "Drawing",
		14: "Economics: Macro",
		15: "Economics: Micro",
		16: "English Language and Composition",
		17: "English Literature and Composition",
		18: "Environmental Science",
		19: "European History",
		20: "French Language",
		21: "German Language",
		22: "Govt. and Politics: Comparative",
		23: "Govt. and Politics: United States",
		24: "Human Geography",
		25: "Italian Language and Culture",
		26: "Japanese Language and Culture",
		27: "Latin",
		28: "Music Theory",
		29: "Physics 1",
		30: "Physics 2",
		31: "Physics B",
		32: "Physics C: Electricity and Magnetism",
		33: "Physics C: Mechanics",
		34: "Psychology",
		35: "Spanish Language",
		36: "Spanish Literature",
		37: "Statistics",
		38: "United States History",
		39: "World History: Modern"
	}
	
courses = []; # initialize array of course objects
exit = False

#loading course equivalency information from excel spreadsheets into a pandas dataframe
UFdf = pd.read_excel("UF.xlsx")
FSUdf = pd.read_excel("FSU.xlsx")

print("\nWelcome to the AP credit Converter!")
print("This program converts AP scores into the course equivalents at the University of Florida and Florida State University.")

while(exit == False): # loops main command window until user decides to exit
	
	print("\nCredit Converter Main Menu")
	print("1. Add Exam")
	print("2. View All Exams")
	print("3. Exit")
	menuOption = input("Please select an option: ") # user selects menu option
	
	
	if (menuOption == "1"): # option 1 is add an ap exam
		menu1() # branches to menu that gathers ap information and adds new course object to list
		
	elif(menuOption == "2"): # displays all current equivalency information
		totUFCredits = 0
		totFSUCredits = 0
		for x in courses: #prints information for each ap equivalency
			print("AP " + x.examName + " is equivalent to " + x.UFClass + "(" + str(x.UFCredit) + " credits) at UF and " + x.FSUClass + "(" + str(x.FSUCredit) + " credits) at FSU")
			totUFCredits = totUFCredits + x.UFCredit
			totFSUCredits = totFSUCredits + x.FSUCredit
		print("\nTotal credits earned at UF: " + str(totUFCredits)) # displays total credits earned at UF from ap exams
		print("Total credits earned at FSU: " + str(totFSUCredits)) # displays total credits earned at FSU from ap exams
		
	elif (menuOption == "3"): # exits the program
		print("Thank you for using Credit Converter. Goodbye!")
		exit = True
		
	else:
		print("invalid input")