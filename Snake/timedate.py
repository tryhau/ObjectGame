import datetime
import pandas as pd
import numpy as np 
from pandas import ExcelFile
import xlsxwriter
from datetime import datetime


file = 'Highscore.xlsx'
workbook = xlsxwriter.Workbook(file)
worksheet = workbook.add_worksheet()
x1 = ExcelFile(file)
df = pd.read_excel('Highscore.xlsx', sheet_name = 'Sheet1')
date_format = workbook.add_format({'num_format': 'd mmmm yyyy'})

score = df['Score']
date = df['Date']
time = df['Time']

def dateTime():
	day = datetime.now().day
	month = datetime.now().month
	year = datetime.now().year
	hour = datetime.now().time().hour
	minute = datetime.now().time().minute
	second = datetime.now().time().second
	return day,month,year,hour,minute,second

day,month,year,hour,minute,second = dateTime()

date = np.array([day,month,year])

worksheet.write('A2','23')
print(date)