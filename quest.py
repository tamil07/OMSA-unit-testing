import os
import subprocess
import openpyxl
from os import path
from openpyxl import Workbook
filepath="/root/demo1.xlsx"
wb=Workbook()
sheet=wb.active
if path.exists('/opt/dell/srvadmin/sbin/omreport') == False:
    print ("omreport command doesnt exists")
with open('/root/cmd') as f:
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
