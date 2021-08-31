import pandas as pd
import requests
import json
from pandas import json_normalize

def api(url,años):
    '''
    Esta función trnasforma una url a la cual le especifico el intervalo de años, en un dataframe.
    Hace una request a la API, la pone en formato json, genera una nueva columna a partir de otra, pero tansformando, de una
    lista a un float.
    Hace drop de 3 columnas que no necesitamos y por último hace un groupby por el intervalo de los años agregando la media de los
    datos de 'Annual_Data'
    Recibe: url y años(intervalo)
    Return: dataframe
    
    '''
    df = pd.DataFrame(requests.get(url).json())
    df['Interval_Years'] = años
    df['Annual_Data'] = [i[0] for i in df['annualData']]
    df.drop(['fromYear', 'toYear', 'annualData'], axis=1, inplace=True)
    df = df.groupby(['Interval_Years'],as_index=False).agg({'Annual_Data':'mean'})

    return df

def limpio(df):
    '''
    Esta función coge el dataframe creado anteriormente, el cual ha sido iterado en el for loop y lo limpia para la visualización.
    Lo primero que hace es resetear el index del df que entra, hace drop de una columna llamda 'index' que no sirve, 
    genera una nueva columna de paises y por ultimo hace un drop de los intervalos de los años (ya que todos los datos de ese df son 
    de los mismo años)
    Recibe : dataframe
    Return: dataframe limpio
    
    '''
    df.reset_index(inplace=True)
    df.drop(['index'], axis=1, inplace=True)
    df['Country'] = 'USA', 'Germany', 'China', 'UK', 'India', 'Rusia'
    df.drop(['Interval_Years'], axis = 1, inplace=True)
    
    return df
