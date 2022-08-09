from concurrent.futures import thread
from threading import Thread
from wsgiref.util import request_uri
from flask import Flask, render_template, request
import platform, socket,re,uuid,json,psutil,logging
from cpu_usage import *
import mysql.connector
import os
import dotenv
from dotenv import load_dotenv
load_dotenv()

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])
def home():
    y=sysinfo()
    return render_template('index.html',y=y)


@app.route('/about')
def about():
    return render_template ('about.html')

@app.route('/custom_scripts')

def custom_scripts():
    return render_template('custom_scripts.html')

@app.route('/hosted')
def selfhosted():
    
    mydb=mysql.connector.connect( host='localhost', user=os.environ.get("user"),password=os.environ.get("password"), database='bifrost')
    mycursor=mydb.cursor()
    sql='select link from config where id=1'
    mycursor.execute(sql)
    result=mycursor.fetchall()
    
        
    return render_template('selfhosted.html',result=result)

@app.route('/settings', methods=['POST','GET'])
def settings():

    if request.method=='POST':
        link=request.form.get('link')
        name=request.form.get('name-link')
        mydb=mysql.connector.connect( host='localhost', user=os.environ.get("user"),password=os.environ.get("password"), database='bifrost')
        mycursor=mydb.cursor()
        sql='insert into config (name, link) values (%s, %s)'
        val=(link, name)
        mycursor.execute(sql, val)
        mydb.commit()
    #maybe put this in try and catch block and add a response drom the db if the value is added or not.     
    return render_template('settings.html')


if __name__=='__main__':
    app.run(debug=True)