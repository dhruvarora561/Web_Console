import psutil
import csv
from datetime import datetime
import threading


def writeHeader():
    header=['Time','CPU']
    f=open('cpu_usage.csv','w')
    writer=csv.writer(f)
    writer.writerow(header)


def getTime():
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    getCpuUsage(current_time)


def getCpuUsage(current_time):
    cpu=str(psutil.cpu_percent(1))
    data=[current_time,cpu]
    printToCsv(data)

def printToCsv(data):

    f=open('cpu_usage.csv','a')
    writer=csv.writer(f)
    writer.writerow(data)



#writeHeader()



#while(True):
#    getTime()

