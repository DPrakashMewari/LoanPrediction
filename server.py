# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 17:19:54 2020

@author: Prakash
"""
import pickle
from flask import Flask,jsonify,request,render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



@app.route("/predict", methods=['GET','POST'])    
def predict():

    if(request.method == 'POST'):

        
       
        import datetime as dt
            

        
        df_loan=pd.DataFrame(index=[0])
        df_loan['NoEmp']=request.values['NoEmp']
       
        
        df_loan['NewExist']=request.values['NewExist']
        
        df_loan['RetainedJob']=request.values['RetainedJob']
        df_loan['CreateJob']=request.values['CreateJob']
        
        df_loan['FranchiseCode']=request.values['FranchiseCode']
       
        df_loan['UrbanRural']=request.values['UrbanRural']
       
        df_loan['RevLineCr']=request.values['RevLineCr']
        
        df_loan['LowDoc']=request.values['LowDoc']
        
        df_loan['ApprovalDate']=request.values['ApprovalDate']
        print(df_loan['ApprovalDate'])
        df_loan['ApprovalDate']=  pd.to_datetime(df_loan.ApprovalDate, format = '%Y-%m-%d')

      
        df_loan['Term']=request.values['Term']
      
        df_loan['DisbursementGross']=str(request.values['DisbursementGross'])
       
        df_loan['BalanceGross']=str(request.values['BalanceGross'])
      
        df_loan['SBA_Appv']=str(request.values['SbaAppv'])
       
        df_loan['GrAppv']=str(request.values['GrAppv'])
        
        df_loan['ChgOffPrinGr']=request.values['ChgOffPrinGr']
       
        df_loan['DisbursementDate']=request.values['DisbursementDate']
        df_loan['DisbursementDate']=  pd.to_datetime(df_loan.DisbursementDate, format = '%Y-%m-%d')
    
        df_loan['ChgOffDate']=request.values['ChgOffDate']
        df_loan['ChgOffDate']=  pd.to_datetime(df_loan.ChgOffDate, format = '%Y-%m-%d')
        
        
        
        class_map = {'Y': 1, 'N': 0}

        df_loan['RevLineCr'] = df_loan['RevLineCr'].map(class_map)
        class_map1 = {'Y': 1, 'N': 0}
        df_loan['LowDoc'] = df_loan['LowDoc'].map(class_map1) #
        df_loan['DisbursementGross'] = df_loan['DisbursementGross'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
        df_loan['BalanceGross'] = df_loan['BalanceGross'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
        df_loan['SBA_Appv'] = df_loan['SBA_Appv'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
        df_loan['GrAppv'] = df_loan['GrAppv'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
        df_loan['ChgOffPrinGr'] = df_loan['ChgOffPrinGr'].apply(lambda x: x.replace('$','')).apply(lambda x: x.replace(',','')).astype(float)
        df_loan['ChgOffDate']=pd.to_datetime(df_loan['ChgOffDate'])
        df_loan['ApprovalDate']=pd.to_datetime(df_loan['ApprovalDate'])
        df_loan['DisbursementDate']=pd.to_datetime(df_loan['DisbursementDate'])
        df_loan['ChgOffDate']=df_loan['ChgOffDate'].map(dt.datetime.toordinal)
        df_loan['DisbursementDate']=df_loan['DisbursementDate'].map(dt.datetime.toordinal)
        df_loan['ApprovalDate']=df_loan['ApprovalDate'].map(dt.datetime.toordinal)
        df_loan['Portion_Approved']=(df_loan['GrAppv']-df_loan['SBA_Appv'])/df_loan['SBA_Appv']
        df_loan['Time_taken']=df_loan['DisbursementDate']-df_loan['ApprovalDate']
        
        df_loan.drop('GrAppv',axis=1,inplace=True)
        df_loan.drop('SBA_Appv',axis=1,inplace=True)
        df_loan.drop('DisbursementDate',axis=1,inplace=True)
        df_loan.drop('ApprovalDate',axis=1,inplace=True)
        df_loan.columns
        print(df_loan)
        with open('Loanprice_model.pickle', 'rb') as f:
            dt = pickle.load(f)
        print("loading saved artifacts...done")
        value=dt.predict(df_loan)
        print(value)
        if(value==0):
            s=("The Person's defaulting chances are High")
        else:
            s=("The Person's defaulting chances are Low") 
        
        
        print(s)
        return render_template('result.html',s='{}' .format(s))
    else:
        s='Please Try Again Later'
        return render_template('index.html',s='{}' .format(s))
if __name__ == '__main__':
    app.run()
