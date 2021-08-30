# GHG EMISSIONS AND THE CHANGE IN EARTH'S TEMPERATURE

![portada](https://github.com/Jorge-Solana/GHG-emissions-and-temperature-on-Earth/blob/main/Imagenes/unnamed.jpg)


## OBJETIVOS

Con este proyecto se pretende ilustrar y confirmar el daño causado por la masiva emisión de gases de efecto invernadero.
Con la ayuda de los datos proporcionados con el dataset elegido y las llamadas a la API selecionada, se busca ver la relación que existe entre el aumento de las emisiones de los gases de efecto invernadero y las temperaturas y las precipitaciones en los 6 países de estudio.


## ETAPAS DEL TRABAJO

Este proyecto consta de tres estapas:
    
-La primera es una etapa de búsqueda de la idea, la cual se ha hecho en la plataforma de busqueda de datasets [Kaggle](https://www.kaggle.com/datasets) , para buscar un dataset al gusto y posteriormente trabajar con los datos que este mismo proporciona. El dataset que se ha escogido nos proporciona información sobre la emisión de gases de efecto invernadero de los países y regiones del mundo desde el 1990 hasta el 2018.
    
-La segunda etapa consta, también, de una búsqueda, esta vez de una API con la cual poder trabajar en relación a nuestro dataset previamente seleccionado. La API que se ha elegido para este proyecto es [Climate_Data_API](https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api#:~:text=The%20Climate%20Data%20API%20provides,World%20Bank's%20Terms%20of%20Use) , de 'The Wolrd Bank'. esta API, lo que nos proporciona las temperaturas y las precipitaciones en los países que pidamos tanto de años pasados como de años venideros, de forma predictiva.
    
-La tercera y última fase, es propiamente el trabajo con estos datos recogidos, su limpieza, organización y visualización.

## METODOLOGÍA

Para la limpieza del dataset original poco se ha necesitado, tan solo contaba con sus dos útlimas filas (inservibles) de nulos.
La organización y seleciión de los datos que se han querido usar de la API, ha sido algo mas trabajoso, ya que en base a lo que queríamos mostrar, el incremento de temperaturas y cambio en las precipitaciones, se han tenido que realizar diferentes operaciones de combinación de datos.
Destacar que la información obtenida de esta API, se ha utilizado tan solo la de 6 países: EEUU, India, Alemania, China, Rusia y Reino Unido.

A la hora de realizar el trabajo de visualización el trabajo que se ha realizado, utilizando las diferentes librerías (mencionadas al final), ha sido de unificación de los datos para realizar gráficos de barras, los cuales para este caso, son los que más nos ayudan a entender estos datos, y también la realización de un gráfico de líneas, usado para ver la evolución a lo largo de los años.

## Organización de carpetas

Para un seguimiento correcto de este proyecto, se pasa a explicar el orden lógico de cada archivo.
    
    - En primer lugar, dentro de testing cleaning, se encuentra la pequeña limpieza del dataset original. Aquí tambien se encuentra una llamada general a la API.

    - Dentro de cleaning_functions.py tenemos las funciones que utilizaremos para llamar a la API, generar los pequeños dataframes y posteriormente limpiarlos.

    - Dentro de la carpeta main.py se encuentran los for loops que utilizamos para que nuestros dataframes de la API se junten (concat) los cuales serán limpiados después con la función que se encuentra en cleaning_functions.py (limpio)

    - Por último, el Jupyter de Visuals es pura visualización con los dataframes generados a partir de las funciones y el dataframe original limpio.

## Librerías usadas

- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Json](https://docs.python.org/3/library/json.html)
- [Requests](https://docs.python-requests.org/en/master/)
- [Plotly](https://plotly.com/)