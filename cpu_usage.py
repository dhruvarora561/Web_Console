import psutil,platform
import csv
from datetime import datetime
from threading import Thread


def sysinfo():
    return platform.node()

def osinfo():
    return platform.system()

def cpuinfo():
    return platform.processor()


def ramusage():
    return str(psutil.virtual_memory().percent)+"%"


def cpuusage():
    return str(psutil.cpu_percent(1))+"%"














































#def graphIt(data):
#    pass

#def writeHeader():
#    header=['Time','CPU']
#    f=open('cpu_usage.csv','w')
#    writer=csv.writer(f)
#    writer.writerow(header)


#def getTime():
#    now = datetime.now()
#    current_time = now.strftime("%H:%M:%S")
#    getCpuUsage(current_time)


#def getCpuUsage(current_time):
#    cpu=str(psutil.cpu_percent(1))
#    data=[current_time,cpu]
#    printToCsv(data)

#def printToCsv(data):
#    f=open('cpu_usage.csv','a')
#    writer=csv.writer(f)
#    writer.writerow(data)


#t1=Thread(args=getTime())
#t1.start()