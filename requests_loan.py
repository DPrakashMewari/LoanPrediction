# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 13:33:19 2020

@author: hp
"""

import requests
null=None
data = {"Name":"ABC HOBBYCRAFT","City":"EVANSVILLE","State":"IN","Zip":47711,"Bank":"FIFTH THIRD BANK","BankState":"OH","CCSC":451120,"ApprovalDate":"28-Feb-97","ApprovalFY":1997,"Term":84,"NoEmp":4,"NewExist":2,"CreateJob":0,"RetainedJob":0,"FranchiseCode":1,"UrbanRural":0,"RevLineCr":"N","LowDoc":"Y","ChgOffDate":null,"DisbursementDate":"28-Feb-99","DisbursementGross":"$60,000.00 ","BalanceGross":"$0.00 ","ChgOffPrinGr":"$0.00 ","GrAppv":"$60,000.00 ","SBA_Appv":"$48,000.00 "}
response = requests.post("{}/".format("http://127.0.0.1:5000"), json =data )
print("The Client's "+ str(response.json()))