# MLProject

Kaggle competition: Titanic: Machine Learning from Disaster

https://www.kaggle.com/startupsci/titanic-data-science-solutions/data?login=true

https://www.kaggle.com/c/titanic/submit

data sets:
train.csv
test.csv
submission.csv (use this file to submit the results. Template provided on Kaggle)

started on 10/4/2018

completed on 10/9/2018

Variable Notes
pclass: A proxy for socio-economic status (SES)
1st = Upper
2nd = Middle
3rd = Lower

age: Age is fractional if less than 1. If the age is estimated, is it in the form of xx.5

sibsp: The dataset defines family relations in this way...
Sibling = brother, sister, stepbrother, stepsister
Spouse = husband, wife (mistresses and fiancés were ignored)

parch: The dataset defines family relations in this way...
Parent = mother, father
Child = daughter, son, stepdaughter, stepson
Some children travelled only with a nanny, therefore parch=0 for them.

Orginal Model Results
                        Model  Score
3               Random Forest  86.76
8               Decision Tree  86.76
1                         KNN  84.74
0     Support Vector Machines  83.84
2         Logistic Regression  80.36
7                  Linear SVC  79.01
5                  Perceptron  78.00
6  Stochastic Gradient Decent  76.43
4                 Naive Bayes  72.28

Removing Fare Feature Results
                        Model  Score
3               Random Forest  84.29
8               Decision Tree  84.29
0     Support Vector Machines  83.16
1                         KNN  81.93
2         Logistic Regression  80.36
7                  Linear SVC  78.79
5                  Perceptron  75.65
6  Stochastic Gradient Decent  74.64
4                 Naive Bayes  72.17

Removing Fare and IsAlone Features Results
                        Model  Score
3               Random Forest  84.18
8               Decision Tree  84.18
0     Support Vector Machines  83.39
1                         KNN  81.82
2         Logistic Regression  79.57
7                  Linear SVC  79.12
5                  Perceptron  78.56
4                 Naive Bayes  74.97
6  Stochastic Gradient Decent  74.97


DataFrames
X_test -test data used for model
X_train -training data used for model
dataset -used for data manipulation, conversion to ordinals
submission -two column submission file
models -ranked df of model results
test_df -original test data
train_df -original train data
coeff_df -feature correlation from regression

y-train -
y-pred -predicated results "Survived", 0 or 1
