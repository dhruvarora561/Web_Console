import psutil
import csv
from datetime import datetime

header=['Time','CPU']

def getCpuUsage():
    
    
    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    
    cpu=str(psutil.cpu_percent(1))

    data=[current_time,cpu]


    printToCsv(data)

def printToCsv(data):

    f=open('cpu_usage.csv','w')
    writer=csv.writer(f)
    writer.writerow(header)
    writer.writerow(data)
    print(data)


getCpuUsage()