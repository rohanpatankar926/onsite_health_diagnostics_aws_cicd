# Onsite Health Diagnostic (OHD)

<img src="https://github.com/Nix-code/Onsite-Health-Diagnostic-OHD/blob/main/docs/src/disease.png" width="1100" height="500" />


<p> Official Documentation of the project</p>

-  [Documentation](https://nix-code.github.io/Onsite-Health-Diagnostic-OHD/)

Developing a disease predicting web application using the concept of Machine Learning and Deep Learning to make the predictive model for various diseases such as ```Breast Cancer```,```Malaria```, ```Pneumonia```, ```Diabetes```, ```Brain tumour```, ```plant disease``` etc.
## Table Of Contents

-   [Tools](#Tools)
-   [Datasets](#Datasets)
-   [Directory](#Directory)
-   [Impact](#Impact)
-   [Clone](#Clone)
-   [Developers](#Developers)
-   [Licence](#Licence)

## Tools : 
- ```Python```, ```Numpy```, ```Pandas```, ```Matplotlib```, ```Seaborn```, ```Scikit-learn```, ```Tensorlow & Keras```, ```Html```, ```Css```, ```JavaScript``` and ```openCV```

## Datasets
 - Pneumonia            :              [Dataset](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia)
 - Brain tumour         :              [Dataset](https://www.kaggle.com/ahmedhamada0/brain-tumor-detection)
 - Diabetes             :              [Dataset](https://github.com/Nix-code/Disease-Prediction-and-Deployment/blob/main/src/model/Diabetes/diabetes.csv)
 - Heart disease        :              [Dataset](https://github.com/Nix-code/Disease-Prediction-and-Deployment/blob/main/src/model/Heart%20disease/heart.csv)
 - Breast Cancer        :              [Dataset](https://github.com/Nix-code/Disease-Prediction-and-Deployment/blob/main/src/model/Breast%20Cancer/data.csv)
 - Malaria-Detection    :              - [Dataset](https://lhncbc.nlm.nih.gov/LHC-publications/pubs/MalariaDatasets.html#:~:text=Abstract%3A,the%20Malaria%20Screener%20research%20activity.&text=The%20dataset%20contains%20a%20total,of%20parasitized%20and%20uninfected%20cells.)


## Directory basic overview
```
├── docs
|    
├── src
|    |── static
|    |      |── css
|    |      |    
|    |      |── img
|    |      |       
|    |      |── js  
|    |
|    |── model 
|    |      |── Breast Cancer
|    |      |── Diabetes
|    |      |── Heart Disease
|    |      |── Pneumonia
|    |      |── Brain Tumor
|    |      |── Malaria Detection
|    |      |── Thyroid prediction
|    |
|    |── Templates
│        
|
├── app.py
├── README.md
└── requirements.txt
```
## Impact
<p> Impact in the real world</p>

We are developing this project which involves the prediction of many diseases based on the user input which consists of facts or ```Radiography images```.  And also we will be providing all the required information about the disease, it's```cause```, ```symptoms``` and its ```prevention``` in the web site. After developing the models, ```UI``` and every documents, the whole project will be deployed on ```Heroku```
## Clone

```
git clone git@github.com:Nix-code/Onsite-Health-Diagnostic-OHD.git
```
- To run on your local machine, make sure you have installed every requirements.
```
$ export FLASK_APP=app
$ flask run
 * Running on http://127.0.0.1:5000/
 ```
 
## Developers
Rohan Patankar - ```Machine Learning & Deployment```

Apsara Budhathoki - ```Web Design & Development```

Nishant Banjade - ```Machine Learning & Deployment```

## Licence

```MIT```
