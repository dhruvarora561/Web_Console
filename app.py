from concurrent.futures import thread
from threading import Thread
from flask import Flask, render_template, request
import platform, socket,re,uuid,json,psutil,logging
from cpu_usage import *


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
    return render_template('selfhosted.html')

@app.route('/settings', methods=['POST','GET'])
def settings():

    return render_template('settings.html')


if __name__=='__main__':
    app.run(debug=True)