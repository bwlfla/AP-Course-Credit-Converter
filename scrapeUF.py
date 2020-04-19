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

counter=1
for row in rows:
	if(counter>2):
		apExamName=row.find('td',class_="column0").text.strip()
		credit3=row.find('td',class_="column1").text.strip()
		credit4=row.find('td',class_="column2").text.strip()
		credit5=row.find('td',class_="column3").text.strip()
		my_sheet['A'+(str(counter))]=apExamName
		my_sheet['B'+(str(counter))]=credit3
		my_sheet['C'+(str(counter))]=credit4
		my_sheet['D'+(str(counter))]=credit5
	counter=counter+1

workbook.save(filePath+nameOfFile)
