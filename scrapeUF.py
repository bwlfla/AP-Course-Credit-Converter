import requests
from bs4 import BeautifulSoup
import openpyxl

workbook=openpyxl.Workbook()
my_sheet=workbook.active
my_sheet.title= "UF"
filePath="C:\\Users\\Brian\\OneDrive\\Documents\\Computer Science\\MAT4930\\Final Project\\AP-Course-Credit-Converter\\"
nameOfFile="UF.xlsx"

workbook.save(filePath+nameOfFile)
print("Hello World")
