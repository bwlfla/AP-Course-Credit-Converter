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
#performs an HTTP request to the given URL
page=requests.get(url)
#the contents of page are formatted by BeautifulSoup for easy usage/access
soup=BeautifulSoup(page.content,'html.parser')
#rows creates an array/arraylist of all the instances of the tag 'tr' with the field bgcolor='#ffffff'
rows=soup.find_all('tr',bgcolor='#ffffff')

counter=2
for row in rows:
	#creates an array/arraylist of all the instances of the tag 'td' that can be accessed by index
	division=row.findAll('td')

	apExamName=division[0].text.strip()
	credit3=division[1].text.strip()
	credit4=division[2].text.strip()
	#there is one element in the html of the fsu website that does not appear after the webscraping occurs
	try:
		credit5=division[3].text.strip()
	except IndexError:
		credit5="Same as 4"

	if("Same as" in credit4):
		credit4=credit3
	if("Same as" in credit5):
		credit5=credit4

	#place the strings in the right cells in excel
	my_sheet['A'+(str(counter))]=apExamName
	my_sheet['B'+(str(counter))]=credit3
	my_sheet['C'+(str(counter))]=credit4
	my_sheet['D'+(str(counter))]=credit5
	counter=counter+1

#saves the excel file at the filePath
workbook.save(filePath+nameOfFile)

'''Sources used:
https://www.analyticsvidhya.com/blog/2015/10/beginner-guide-web-scraping-beautiful-soup-python/
https://realpython.com/beautiful-soup-web-scraper-python/
'''