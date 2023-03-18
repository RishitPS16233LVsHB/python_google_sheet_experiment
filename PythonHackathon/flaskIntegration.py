import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from flask import Blueprint,request,redirect

# you have to paste this into the method that pythonanywhere.com provides what this return is prediction values of NPK in boolean
# you may have to check this before usage because this has not been run on a server environment

def ProcessData():
    # this is the raw sensor data
    NData = request.form['ndata']
    PData = request.form['pdata']
    KData = request.form['kdata']

    #perform percentage on this data
    sum = float(NData) + float(PData) + float(KData);  
    NPercentage = float(float(NData)*100)/float(sum)
    PPercentage = float(float(PData)*100)/float(sum)
    KPercentage = float(float(KData)*100)/float(sum)


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
    #getting the training and testing data frames here

    x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfN']],UpdatedCropData['NStatus'],test_size=0.2)
    Mdl1 = LogisticRegression()
    # fitting model with the training data
    Mdl1.fit(x_train,y_train)   

    # an attempt to get singular boolean value from singular data provided
    NewTest = pd.DataFrame()
    NewTest['PerOfN'] = [NPercentage]
    Prediction = Mdl1.predict(NewTest)

    NPredictionValue = list(Prediction)[0]
    print(NPredictionValue)


    x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfP']],UpdatedCropData['PStatus'],test_size=0.2)
    Mdl1 = LogisticRegression()
    # fitting model with the training data
    Mdl1.fit(x_train,y_train)   

    # an attempt to get singular boolean value from singular data provided
    NewTest = pd.DataFrame()
    NewTest['PerOfP'] = [PPercentage]
    Prediction = Mdl1.predict(NewTest)

    PPredictionValue = list(Prediction)[0]
    print(PPredictionValue)




    x_train,x_test,y_train,y_test = train_test_split(UpdatedCropData[['PerOfK']],UpdatedCropData['KStatus'],test_size=0.2)
    Mdl1 = LogisticRegression()
    # fitting model with the training data
    Mdl1.fit(x_train,y_train)   

    # an attempt to get singular boolean value from singular data provided
    NewTest = pd.DataFrame()
    NewTest['PerOfK'] = [KPercentage]
    Prediction = Mdl1.predict(NewTest)

    KPredictionValue = list(Prediction)[0]
    print(KPredictionValue)

    return redirect('<yoursiteURLHere>?NPredictionValue={NPredictionValue}&PPredictionValue={PPredictionValue}&KPredictionValue={KPredictionValue}')