#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 08:43:21 2020

@author: Michael
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('salary_data_cleaned.csv')

df.columns

features = ['mean_salary','Rating','Size','ownership', 'Industry', 'Sector', 'Revenue', 'Competitors',
     'job_city', 'isjobinHQ', 'age', 'python', 'html', 'javascript',
       'java', 'cpp', 'sql', 'aws', 'C', 'css', 'scala', 'matlab', 'ML',
       'job_simp', 'desc_len', 'comp_count']

df_model = df[features]


df_dum = pd.get_dummies(df_model)

from sklearn.model_selection import train_test_split
X = df_dum.drop('mean_salary', axis=1)
y = df_dum.mean_salary.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

#Linear regression
lm = LinearRegression()
lm.fit(X_train,y_train)
np.mean(cross_val_score(lm, X_train, y_train,scoring = 'neg_mean_absolute_error', cv= 3))


#Lasso Regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l, X_train, y_train,scoring = 'neg_mean_absolute_error', cv= 3))

alpha =[]
error =[]

for i in range(1,100):
    alpha.append(i/10)
    lml = Lasso(alpha = (i/10))
    error.append(np.mean(cross_val_score(lml, X_train, y_train,scoring = 'neg_mean_absolute_error', cv= 3)))
    
    
plt.plot(alpha, error)    


lm_l = Lasso(alpha =2)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l, X_train, y_train,scoring = 'neg_mean_absolute_error', cv= 3))


#Random Forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor(n_estimators=100)

np.mean(cross_val_score(rf,X_train,y_train,scoring = 'neg_mean_absolute_error', cv= 3))

# tune models GridsearchCV 
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
parameters = {'n_estimators':range(100,200,100), 'criterion':('mse','mae'), 'max_features':('auto','sqrt')}

gs = GridSearchCV(rf,parameters,scoring='neg_mean_absolute_error',cv=3)

gs.fit(X_train,y_train)

gs.best_score_
gs.best_estimator_

# test ensembles 
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

mean_absolute_error(y_test,(tpred_lml+tpred_rf)/2)

import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )


file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']

model.predict(np.array(list(X_test.iloc[1,:])).reshape(1,-1))[0]

list(X_test.iloc[1,:])


