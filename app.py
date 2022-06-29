from concurrent.futures import thread
from threading import Thread
from flask import Flask, render_template, request
import platform, socket,re,uuid,json,psutil,logging

import csv

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def one_line_cmd():
    if request.method=='POST':
        ckd=int(request.form.get('index_cmd'))
        return ckd 

    
    try:
        info={}#sys info in a dictionary
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        y=json.dumps(info)
        
    except Exception as e:
        logging.exception(e)


    return render_template('index.html' ,y=y,cpu=cpu)





@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/custom_scripts')

def custom_scripts():
    return render_template('custom_scripts.html')
    
if __name__=='__main__':
    app.run(debug=True)