from concurrent.futures import thread
from threading import Thread
from wsgiref.util import request_uri
from flask import Flask, render_template, request
import platform, socket,re,uuid,json,psutil,logging
from cpu_usage import *
#import mysql.connector
import os
#import dotenv
#from dotenv import load_dotenv
#load_dotenv()
import json

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    y=sysinfo()
    z=osinfo()
    cpu=cpuinfo()
    ram=ramusage()
    usage=cpuusage()
    return render_template('index.html',y=y,z=z,cpu=cpu,ram=ram,usage=usage)
    
    

@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/custom_scripts')

def custom_scripts():
    if request.method=='POST':
        pass
    return render_template('custom_scripts.html')

@app.route('/hosted')
def selfhosted():
    
#     mydb=mysql.connector.connect( host='localhost', user=os.environ.get("user"),password=os.environ.get("password"), database='bifrost')
#     mycursor=mydb.cursor()
#     sql='select link from config'
#     mycursor.execute(sql)
#     result=mycursor.fetchall()
    
        
    return render_template('selfhosted.html')

@app.route('/settings', methods=['POST','GET'])
def settings():
    dictionary={
        
    }
    if request.method=='POST':
        link=request.form.get('link')
        name=request.form.get('name-link')
        
        dictionary["name"]=name
        dictionary["link"]=link
        with open('links.json','a') as file:
            
            x=json.dumps(dictionary,indent=4)
            
            file.write(x)
            

    return render_template('settings.html')





if __name__=='__main__':
    app.run(debug=True)