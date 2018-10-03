import os
import subprocess
import openpyxl
from os import path
from openpyxl import Workbook
def racadm():
	filepath="/root/racadm.xlsx"
	wb=Workbook()
	sheet=wb.active()
	if path.exists('/opt/dell/srvadmin/sbin/racadm') == False:
		print ("racadm binary doesnt exists")
	with open('/root/racadm') as f:
		content=f.readlines()
		for line in content:
			sut=subprocess.Popen(line, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			sut1=sut.communicate()
			data=[(line,str(sut1))]
			for row in data:
				sheet.append(row)
			if sut.wait()!=0:
				print line,sut1
			else:
				print "Success", line
	wb.save(filepath)
def omreport():
	filepath="/root/omreport.xlsx"
	wb=Workbook()
	sheet=wb.active
	if path.exists('/opt/dell/srvadmin/sbin/omreport') == False:
		print ("omreport command doesnt exists")
	with open('/root/omreport') as f:
		content=f.readlines()
		for line in content:
			sut=subprocess.Popen(line, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
			sut1=sut.communicate()
			data=[(line,str(sut1))]
			for row in data:
				sheet.append(row)
			if sut.wait()!=0:
				print line,sut1
			else:
				print "Success", line
	wb.save(filepath)
print "Enter the module to be tested , modules available are racadm and omreport \n"
print "Example :- omreport"
inp=raw_input('')
if inp=='omreport':
    omreport()
elif inp=='racadm':
	racadm()
else:
	print "Enter a valid option"
