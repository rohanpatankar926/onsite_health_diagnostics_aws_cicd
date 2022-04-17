
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
    if request.method == "POST":
        try:
            Radius_Mean = float(request.form["radius_mean"])
            Area_Mean = float(request.form["area_mean"])
            Compactness_Mean = float(request.form["compactness_mean"])
            Concavity_Mean = float(request.form["concavity_mean"])
            Concave_Points_Mean = float(request.form["concave_points_mean"])
            Area_Worst = float(request.form["area_worst"])
            Compactness_Worst = float(request.form["compactness_worst"])
            Concavity_Worst = float(request.form["concavity_worst"])
            Area_Se = float(request.form["area_se"])
            Fractal_Dimension_Se = float(request.form["fractal_dimension_se"])
            Symmetry_Worst = float(request.form["symmetry_worst"])
            Fractal_Dimension_Worst = float(request.form["fractal_dimension_worst"])

            breast_file = "breast_model.sav"
            loaded_breast_model = joblib.load(breast_file)

            breast_pred = loaded_breast_model.predict([[Radius_Mean, Area_Mean, Compactness_Mean, Concavity_Mean,
            Concave_Points_Mean, Area_Worst, Compactness_Worst,Concavity_Worst, 
            Area_Se, Fractal_Dimension_Se, Symmetry_Worst, Fractal_Dimension_Worst]])
            breast_pred = round(100*breast_pred[0])
            print(breast_pred)
            if(breast_pred == 0):
                res = "Congratulations! you are safe from Breast Cancer"
            else:
                res = "Sorry :( you have encountered with Breast Cancer"
            return render_template('breastcancer.html',prediction=res)
           

        except Exception as e:
            print(e)
            return "Something went wrong !!"
    else:
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

@app.route('/heart',methods=['GET','POST'])
def heart():
    if request.method == 'POST':
        try:
            Age = float(request.form["age"])
            sex = (request.form["sex"])
            if(sex == "male"):
                sex = 1
            else:
                sex = 0
            #chest pain
            chestpain = (request.form["chestpain"])
            if(chestpain == "ATA"):
                chestpain = 1
            elif (chestpain == "NAP"):
                chestpain = 2
            elif (chestpain == "ASY"):
                chestpain = 0
            else:
                chestpain = 3
            # resting bp
            restingbp = float(request.form["restingbp"])
            cholestrol = float(request.form["cholestrol"])
            fastingbs = float(request.form["fastingbs"])
            restingecg = (request.form["restingecg"])
            if(restingecg == "Normal"):
                restingecg = 1
            elif (restingecg == "ST"):
                restingecg = 2
            else:
                restingecg = 0

            maxhr = float(request.form["maxhr"])
            exercise = (request.form["exercise"])
            if(exercise == "N"):
                exercise = 0
            else:
                exercise = 1

            oldpeak = float(request.form["oldpeak"])
            stslope = (request.form["stslope"])
            if(stslope == "up"):
                stslope = 2
            elif(stslope == "flat"):
                stslope = 1
            else:
                stslope = 0
            
            file_heart = "heart_model.sav"
            loaded_model = joblib.load(file_heart)
            heart_pred = loaded_model.predict([[Age, sex, chestpain, restingbp, cholestrol, fastingbs, restingecg, maxhr,
            exercise, oldpeak, stslope]])

            heart_pred = round(100*heart_pred[0])
            if(heart_pred == 0):
                res = "Congratulations! you are safe from Heart Disease"
            else:
                res = "Sorry :( you have encountered with Heart Failure"
            return render_template('heart.html',predict = res)

        except Exception as e:
            print(e)
            return "Something went wrong! Please check your values once and try again"
    else:

        return render_template('heart.html')

@app.route('/pneumonia',methods=['GET','POST'])
def pneumonia():
    return render_template('pneumonia.html')

@app.route('/thyroid',methods=['GET','POST'])


def thyroid():
    return render_template('thyroid.html')



if __name__=="__main__":
    app.run(port=5000,debug=True)
