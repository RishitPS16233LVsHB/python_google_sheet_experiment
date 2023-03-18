#from statistics import LinearRegression
#from tkinter import PhotoImage
import pandas as pd
#import numpy as np
#import matplotlib.pyplot as mtplt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


#from flask import Blueprint,render_template,request


#NData = request.form['ndata']
#PData = request.form['pdata']
#KData = request.form['kdata']

UpdatedCropData = pd.read_csv('ds1.csv')
UpdatedCropData['SumNPK'] = UpdatedCropData['N'] + UpdatedCropData['P'] + UpdatedCropData['K']
UpdatedCropData['PerOfN'] = (UpdatedCropData['N'] * 100)/UpdatedCropData['SumNPK']
UpdatedCropData['PerOfP'] = (UpdatedCropData['P'] * 100)/UpdatedCropData['SumNPK']
UpdatedCropData['PerOfK'] = (UpdatedCropData['K'] * 100)/UpdatedCropData['SumNPK']

UpdatedCropData['NStatus'] = 0
UpdatedCropData['PStatus'] = 0
UpdatedCropData['KStatus'] = 0

NList = list(UpdatedCropData.loc[(UpdatedCropData['PerOfN'] >= 55) & (UpdatedCropData['PerOfN'] <= 65)].index)
for i in NList:
    UpdatedCropData.at[i,'NStatus'] = 1
PList = list(UpdatedCropData.loc[(UpdatedCropData['PerOfP'] >= 16) & (UpdatedCropData['PerOfP'] <= 24)].index)
for i in PList:
    UpdatedCropData.at[i,'PStatus'] = 1
KList = list(UpdatedCropData.loc[(UpdatedCropData['PerOfK'] >= 16) & (UpdatedCropData['PerOfK'] <= 24)].index)
for i in KList:
    UpdatedCropData.at[i,'KStatus'] = 1



#actual training starts from here
# x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfN']],UpdatedCropData['NStatus'],test_size=0.2)
# Mdl = LogisticRegression()
# Mdl.fit(x_train,y_train)


# print("="*50)
# print(Mdl.score(x_test,y_test))
# print("="*50)
# Predicted_Values = Mdl.predict(x_test)
# print(Predicted_Values)
# print("="*50)

# DataFrameNew = pd.DataFrame()
# DataFrameNew['PerOfN'] = x_test['PerOfN']
# DataFrameNew['Prediction'] = Predicted_Values
# print(DataFrameNew[DataFrameNew['Prediction'] == 1])

# mtplt.scatter(list(x_test['PerOfN']),list(Predicted_Values))
# mtplt.show()

# # UpdatedCropData.to_csv('NewUpdatedData.csv')
# x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfP']],UpdatedCropData['PStatus'],test_size=0.2)
# Mdl1 = LogisticRegression()
# Mdl1.fit(x_train,y_train)
# Prediction = Mdl1.predict(x_test)
# print("="*50)
# print(Prediction)
# print("="*50)



# DataFrameNew = pd.DataFrame()
# DataFrameNew['PerOfP'] = x_test['PerOfP']
# DataFrameNew['Prediction'] = Prediction
# print(DataFrameNew[DataFrameNew['Prediction'] == 1])
# mtplt.scatter(x_test['PerOfP'],Prediction)
# mtplt.show()


#getting the training and testing data frames here

x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfK']],UpdatedCropData['KStatus'],test_size=0.2)
Mdl1 = LogisticRegression()
# fitting model with the training data
Mdl1.fit(x_train,y_train)   


# DataFrameNew = pd.DataFrame()
# DataFrameNew['PerOfK'] = x_test['PerOfK']
# DataFrameNew['Prediction'] = Prediction

NewTest = pd.DataFrame()
NewTest['PerOfK'] = [25]
Prediction = Mdl1.predict(NewTest)
PredictionProba = Mdl1.predict_proba(NewTest)
NProba = list(PredictionProba)[0]
NPredictionValue = list(Prediction)[0]
print(NPredictionValue)

print(x_test)
print(Mdl1.predict(x_test))

NewDataFrame = pd.DataFrame()
NewDataFrame['PerOfK'] = x_test['PerOfK']
NewDataFrame['Prediction'] = Mdl1.predict(x_test)
print(NewDataFrame[NewDataFrame['Prediction'] == 1])





# x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfP']],UpdatedCropData['PStatus'],test_size=0.2)
# Mdl1 = LogisticRegression()
# # fitting model with the training data
# Mdl1.fit(x_train,y_train)   


# DataFrameNew = pd.DataFrame()
# DataFrameNew['PerOfP'] = x_test['PerOfP']
# DataFrameNew['Prediction'] = Mdl1.predict(x_test)

# # NewTest = pd.DataFrame()
# # NewTest['PerOfP'] = [25]
# # Prediction = Mdl1.predict(NewTest)

# PPredictionValue = list(Prediction)[0]
# print(PPredictionValue)




# x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfK']],UpdatedCropData['KStatus'],test_size=0.2)
# Mdl1 = LogisticRegression()
# # fitting model with the training data
# Mdl1.fit(x_train,y_train)   


# DataFrameNew = pd.DataFrame()
# DataFrameNew['PerOfK'] = x_test['PerOfK']
# DataFrameNew['Prediction'] = Prediction

# # NewTest = pd.DataFrame()
# # NewTest['PerOfK'] = [25]
# # Prediction = Mdl1.predict(NewTest)

# KPredictionValue = list(Prediction)[0]
# print(KPredictionValue)

# #return redirect('<yoursiteURLHere>?NPredictionValue={NPredictionValue}&PPredictionValue={PPredictionValue}&KPredictionValue={KPredictionValue}')

# print(float(list(NProba)[0]))
