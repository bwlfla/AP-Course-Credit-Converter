import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import openpyxl

workbook=openpyxl.Workbook()
my_sheet=workbook.active
my_sheet.title= "FSU"
filePath="C:\\Users\\Brian\\OneDrive\\Documents\\Computer Science\\MAT4930\\Final Project\\AP-Course-Credit-Converter\\"
nameOfFile="FSU.xlsx"

my_sheet['A1']="AP Exam Name"
my_sheet['B1']="Score of 3"
my_sheet['C1']="Score of 4"
my_sheet['D1']="Score of 5"


url="https://admissions.fsu.edu/credit/AP/"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

#tableOfInfo=soup.find('tbody')
rows=soup.find_all('tr',bgcolor='#ffffff')
#print(rows)

counter=2
for row in rows:
	division=row.findAll('td')
	apExamName=division[0].text.strip()
	credit3=division[1].text.strip()
	credit4=division[2].text.strip()

	try:
		credit5=division[3].text.strip()
	except IndexError:
		credit5="Same as 4"

	if("Same as" in credit4):
		credit4=credit3
	if("Same as" in credit5):
		credit5=credit4


	my_sheet['A'+(str(counter))]=apExamName
	my_sheet['B'+(str(counter))]=credit3
	my_sheet['C'+(str(counter))]=credit4
	my_sheet['D'+(str(counter))]=credit5
	counter=counter+1

workbook.save(filePath+nameOfFile)

#might not do since fsu physics c and magnetism has a tag of ==$0 on the side that makes it disappear

#IndexError is thrown maybe do a trycatch