import src.cleaning_functions as cl
import pandas as pd

paises_ISO3 = ['USA', 'DEU', 'CHN', 'GBR', 'IND', 'RUS']

finalito =[]
for i in paises_ISO3:
    url = f'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/1980/1999/{i}'
    df = cl.api(url,'1980 1999')
    finalito.append(df)

old_temp = pd.concat(finalito)
old_temp = cl.limpio(old_temp)
old_temp

finalito2 =[]
for i in paises_ISO3:
    url = f'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/pr/1980/1999/{i}'
    df = cl.api(url,'1980 1999')
    finalito2.append(df)

old_prec = pd.concat(finalito2)
old_prec = cl.limpio(old_prec)
old_prec

finalito3 =[]
for i in paises_ISO3:
    url = f'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/tas/2020/2039/{i}'
    df = cl.api(url,'2020 2039')
    finalito3.append(df)

new_temp = pd.concat(finalito3)
new_temp = cl.limpio(new_temp)
new_temp

finalito4 =[]
for i in paises_ISO3:
    url = f'http://climatedataapi.worldbank.org/climateweb/rest/v1/country/annualavg/pr/2020/2039/{i}'
    df = cl.api(url,'2020 2039')
    finalito4.append(df)

new_prec = pd.concat(finalito4)
new_prec = cl.limpio(new_prec)
new_prec

old_temp.to_csv('old_temp.csv')
old_prec.to_csv('old_prec.csv')
new_temp.to_csv('prediction_temp.csv')
new_prec.to_csv('prediction_prec.csv')