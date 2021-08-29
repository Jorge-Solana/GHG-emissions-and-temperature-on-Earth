# GHG EMISSIONS AND THE CHANGE IN EARTH'S TEMPERATURE

![portada](https://github.com/Jorge-Solana/GHG-emissions-and-temperature-on-Earth/blob/main/Imagenes/unnamed.jpg)

## ETAPAS DEL TRABAJO

Este proyecto consta de tres estapas:
    
-La primera es una etapa de búsqueda de la idea, la cual se ha hecho en la plataforma de busqueda de datasets [Kaggle](https://www.kaggle.com/datasets) , para buscar un dataset al gusto y posteriormente trabajar con los datos que este mismo proporciona.
    
-La segunda etapa consta, también, de una búsqueda, esta vez de una API con la cual poder trabajar en relación a nuestro dataset previamente seleccionado. La API que se ha elegido para este proyecto es [Climate_Data_API](https://datahelpdesk.worldbank.org/knowledgebase/articles/902061-climate-data-api#:~:text=The%20Climate%20Data%20API%20provides,World%20Bank's%20Terms%20of%20Use) , de 'The Wolrd Bank'.
    
-La tercera y última fase, es propiamente el trabajo con estos datos recogidos, su limpieza, organización y visualización.

## METODOLOGÍA

Para la limpieza del dataset original poco se ha necesitado, tan solo contaba con sus dos útlimas filas (inservibles) de nulos.
La organización y seleciión de los datos que se han querido usar de la API, ha sido algo mas trabajoso, ya que en base a lo que queríamos mostrar, el incremento de temperaturas y cambio en las precipitaciones, se han tenido que realizar diferentes operaciones de combinación de datos.
Destacar que la información obtenida de esta API, se ha utilizado tan solo la de 6 países: EEUU, India, Alemania, China, Rusia y Reino Unido.

A la hora de realizar el trabajo de visualización el trabajo que se ha realizado, utilizando las diferentes librerías (mencionadas al final), ha sido de unificación de los datos para realizar gráficos de barras, los cuales para este caso, son los que más nos ayudan a entender estos datos, y también la realización de un gráfico de líneas, usado para ver la evolución a lo largo de los años.

## OBJETIVOS

Con este proyecto se pretende ilustrar y confirmar el daño causado por la masiva emisión de gases de efecto invernadero, la cual va en aumento.

## Librerías usadas

- [Pandas](https://pandas.pydata.org/)
- [Numpy](https://numpy.org/)
- [Seaborn](https://seaborn.pydata.org/)
- [Json](https://docs.python.org/3/library/json.html)
- [Requests](https://docs.python-requests.org/en/master/)
