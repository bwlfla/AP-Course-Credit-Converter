import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import openpyxl

workbook=openpyxl.Workbook()
my_sheet=workbook.active
my_sheet.title= "UF"
filePath="C:\\Users\\Brian\\OneDrive\\Documents\\Computer Science\\MAT4930\\Final Project\\AP-Course-Credit-Converter\\"
nameOfFile="UF.xlsx"

url="https://catalog.ufl.edu/UGRD/academic-advising/exam-credit/#examstext"
page=requests.get(url)
soup=BeautifulSoup(page.content,'html.parser')

results=soup.find_all('table',summary='AP Exam')
print(results)

workbook.save(filePath+nameOfFile)
