
# importing the necessary tools
from flask import Flask, render_template, request,redirect, url_for, session
# to let flask interact easily while performing file and folder processes irrespective of operating system
import os
import sys
# load the model using joblib
import joblib
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

@app.route('/diabetes',methods=['GET','POST'])
def diabetes():
    if request.method == "POST":
        try:
            Pregnancies = float(request.form["Pregnancies"])
            Glucose = float(request.form["Glucose"])
            Bloodpressure = float(request.form["Bloodpressure"])
            SkinThickness = float(request.form["SkinThickness"])
            Insulin = float(request.form["Insulin"])
            BMIn = float(request.form["BMI"])
            DiabetesPedigreeFunction = float(request.form["DiabetesPedigreeFunction"])
            Age = float(request.form["Age"])
            filename = "diabetes.sav"
            loaded_model = joblib.load(filename)
            dia_pred = loaded_model.predict([[Pregnancies,Glucose,Bloodpressure,SkinThickness,Insulin,BMIn,DiabetesPedigreeFunction,Age]])
            dia_pred = round(100*dia_pred[0])
            if(dia_pred == 0):
                res = "Congratulations! you are safe from Diabetes"
            else:
                res = "Sorry :( you have encountered with Diabetes"
            return render_template('diabetes.html',prediction=res)

        except Exception as e:
            print(e)
            return "Something went wrong !! Please check the entered values once"
    else:
        return render_template('diabetes.html')

@app.route('/pneumonia',methods=['GET','POST'])
def pneumonia():
    return render_template('pneumonia.html')

@app.route('/thyroid',methods=['GET','POST'])
def thyroid():
    return render_template('thyroid.html')

@app.route('/heart',methods=['GET','POST'])
def heart():
    return render_template('heart.html')

if __name__=="__main__":
    app.run(port=5000,debug=True)
