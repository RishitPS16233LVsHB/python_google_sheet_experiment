import pandas as pd
import numpy as np
import math as mt

#important notice there is no time feature with this data set
DataFrame = pd.read_csv("Crop_recommendation.csv")

ListOfCrops = DataFrame['label'].unique()

print("all crops covered in the data set:- ")
for s in ListOfCrops:
    print(s)

# creating separate csv files for the different crops
# Crops = []
# i = 0
# for s in ListOfCrops:    
#     Crops.append(DataFrame.loc[DataFrame['label'] == s ])
#     Crops[i].to_csv('Crop'+str(i)+".csv")
#     i+=1

print("="*50)
print("humidity around 40 %")
print("="*50)
ListOfHUmidity = DataFrame.loc[(DataFrame['humidity'] >= 39)&(DataFrame['humidity'] <= 41)]['label'].unique()
print(DataFrame.loc[(DataFrame['humidity'] >= 39)&(DataFrame['humidity'] <= 41)]['label'].value_counts())
print(ListOfHUmidity)
print("="*50)

print("="*50)
print("ph around 5 to 5.8")
print("="*50)
ListOfPH = DataFrame.loc[(DataFrame['ph'] >= 5)&(DataFrame['ph'] <= 5.8)]['label'].unique()
print(DataFrame.loc[(DataFrame['ph'] >= 5)&(DataFrame['ph'] <= 5.8)]['label'].value_counts())
print(ListOfPH)
print("="*50)

print("="*50)
print("temperature around 30 to 35")
print("="*50)
ListOfTemperature = DataFrame.loc[(DataFrame['temperature'] >= 30)&(DataFrame['temperature'] <= 35)]['label'].unique()
print(DataFrame.loc[(DataFrame['temperature'] >= 30)&(DataFrame['temperature'] <= 35)]['label'].value_counts())
print(ListOfPH)
print("="*50)

print(list(set(ListOfHUmidity) & set(ListOfTemperature) & set(ListOfPH)))


DataFrame['NPKSum'] = DataFrame['N'] + DataFrame['P'] + DataFrame['K']
DataFrame['N_Proportion'] = (DataFrame['N']/DataFrame['NPKSum'])*100
DataFrame['P_Proportion'] = (DataFrame['P']/DataFrame['NPKSum'])*100
DataFrame['K_Proportion'] = (DataFrame['K']/DataFrame['NPKSum'])*100

print("="*50)

print("="*50)
print(DataFrame.loc[(DataFrame['label'] == 'pigeonpeas')])

NewDataFrame = DataFrame.loc[(DataFrame['label'] == 'pigeonpeas') | (DataFrame['label'] == 'mothbeans')]


MoreNewDataFrame = pd.DataFrame()
MoreNewDataFrame['humidity'] = DataFrame['humidity']
MoreNewDataFrame['rainfall'] = DataFrame['rainfall']
MoreNewDataFrame['temperature'] = DataFrame['temperature']

MoreNewDataFrame.to_csv('Weather_info.csv')


NewDataFrame.to_csv('TargetData.csv')

print("="*50)



print(DataFrame['NPKSum'])
