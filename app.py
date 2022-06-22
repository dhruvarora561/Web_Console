from flask import Flask, render_template, request
import platform
import os

app=Flask(__name__)
@app.route('/', methods=['POST','GET']) #creating the route for our application in order to avoid being immediatly 404'd
def index():
    if request.method=='POST':
        command=request.form['command']
        os.popen(command)
        return command
        
    else:
        return render_template("index.html")
    

if __name__=="__main__":
    app.run(debug=True)
