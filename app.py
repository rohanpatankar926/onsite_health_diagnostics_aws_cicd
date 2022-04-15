
# importing the necessary tools
from flask import Flask, render_template, request,redirect, url_for, session

# to let flask interact easily while performing file and folder processes irrespective of operating system
import os

webroot = 'src'
static_dir = os.path.join(webroot,'static')
template_dir = os.path.join(webroot,'templates')

app = Flask(__name__,static_folder=static_dir,template_folder=template_dir)

@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/disease',methods=['GET','POST'])
def disease():
    return render_template('disease.html')

@app.route('/breastcancer',methods=['GET','POST'])
def breastcancer():
    return render_template('breastcancer.html')

if __name__=="__main__":
    app.run(port=5000,debug=True)