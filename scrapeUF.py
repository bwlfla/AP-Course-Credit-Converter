import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import openpyxl

workbook=openpyxl.Workbook()
my_sheet=workbook.active
my_sheet.title= "UF"
filePath="C:\\Users\\Brian\\OneDrive\\Documents\\Computer Science\\MAT4930\\Final Project\\AP-Course-Credit-Converter\\"
nameOfFile="UF.xlsx"

my_sheet['A1']="AP Exam Name"
my_sheet['B1']="Score of 3"
my_sheet['C1']="Score of 4"
my_sheet['D1']="Score of 5"

my_sheet['B2']="3 Credits/Exam unless otherwise noted"
my_sheet['C2']="6 Credits/Exam unless otherwise noted"
my_sheet['D2']="6 Credits/Exam unless otherwise noted"

url="https://catalog.ufl.edu/UGRD/academic-advising/exam-credit/#examstext"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

tableOfInfo=soup.find('table',summary='AP Exam')
rows=tableOfInfo.find_all('tr')



for row in rows:
#	apExamName=row.find()
	print(row)
	print("Happiness")

workbook.save(filePath+nameOfFile)
