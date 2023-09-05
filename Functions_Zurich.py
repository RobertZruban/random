#!/usr/bin/env python
# coding: utf-8

# In[ ]:
import pandas as pd
import seaborn as sns
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import math
import os
import sklearn

annual_premium = 3000.00

def claim(x):
    """ Function converts claims above 0 to value 1,in order to creat a 
        class of 1 and 0 for those who claimed and those who did not"""
    if x == 0:
        return 0
    else:
        return 1

def risky(x):
    """ Function converts risky claims to 1 (if customer claim was higher than annual_premium and rest to 0)"""
    if x > annual_premium:
        return 1
    else:
        return 0
         
    
def gender(x):
    """ Function converts male to 1 and female to 0"""
    if x == 'M':
        return 1
    else:
        return 0
    

def missing_value(data):
   
    """ Imputation of missing data. Missing Agegat Class are deduced accordingly based on following  labels 6 = 1900-1949, 5= 1950-159, 4 =1960-1969, 3=1970-1979, 2= 1980-1989, 1=1990-1999"""
   
    data["date_of_birth"] = pd.to_datetime(data['date_of_birth'])
    data["DOB_year"]=data.date_of_birth.dt.year
    labels=[6,5,4,3,2,1]
    data["agecat_reclass"] = pd.cut(data.DOB_year, bins = [1900,1949,1959,1969,1979,1989,1999],labels=labels, include_lowest=True)
    data['credit_score_2'] = data.groupby('agecat_reclass')['credit_score'].transform(lambda val: val.fillna(val.mean()))
    data['veh_value'] = (data['veh_value']+1).apply(np.log)
    data.traffic_index.fillna(data.traffic_index.mean(), inplace=True)
    return(data)

def percent_missing(df):
    percent_nan = 100* df.isnull().sum() / len(df)
    percent_nan = percent_nan[percent_nan>0].sort_values()
    return percent_nan

    percent_missing(df)
    percent_nan = percent_missing(df)
    sns.barplot(x=percent_nan.index,y=percent_nan)
    plt.xticks(rotation=90);
    sns.regplot(x = df['credit_score'],
                y = df['age'],
                ci = None,
                scatter_kws={"color": "blue"},
                line_kws={"color": "red"},
                data = df)


