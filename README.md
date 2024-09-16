
# MVP API y sistema de recomendación de películas

Descripción General

Este proyecto tiene como objetivo desarrollar un sistema de recomendación de películas personalizado, utilizando técnicas de aprendizaje automático. El sistema se basa en un conjunto de datos de películas y calificaciones de usuarios, y emplea un proceso de ETL (Extracción, Transformación y Carga) para preparar los datos para el análisis.

Estructura del Proyecto

data: Contiene los datos preprocesados y procesados, en formato parquet.

notebooks: Jupyter Notebooks con el código para cada etapa del proyecto:
ETL_PI01.ipynb: Limpieza, transformación y carga de los datos en un formato adecuado para el análisis.
EDA_PI01.ipynb: Análisis exploratorio de datos para comprender las características de los datos y encontrar patrones.
ML_modelo.ipynb: Desarrollo y entrenamiento de los modelos de recomendación.

main.py: Código para crear una API RESTful para hacer consultas a los datos y solicitar las recomendaciones.

requirements.txt: Lista de las dependencias del proyecto.

Proceso

ETL:

Extracción: A partir de archivos .csv proporcionados para los fines de este proyecto.
Transformación: Limpiar los datos, desanidar columnas y manejar valores faltantes, normalizar los datos y crear características relevantes (ej., géneros, actores, directores).
Carga: Cargar los datos en un formato adecuado para el análisis en formato parquet.

EDA:

Análisis exploratorio: Visualizar la distribución de las calificaciones, la popularidad de las películas, la relación entre géneros y calificaciones, popularidad o el ROI, lo mismo en relación a los lenguajes en que fueron creadas y lanzadas al mercado, la distribución de estrenos a lo largo del tiempo.
Ingeniería de características: Se analizó la cantidad de palabras contenidas en una nube de palabras utilizando las sinopsis (overviews) correspondientes a las películas que tenían un promedio de votación de usuarios mayor a 7 .

Modelado:

Selección del modelo: Se optó por hacer un filtrado basado en contenido, para lo que se utilizó un modelo basado en la similitud del coseno.





## API

Desarrollo: Crear una API RESTful utilizando FastAPI para exponer las funcionalidades del modelo de recomendación.
Endpoints: Los endpoints para la API estaban predefinidos dentro de los requerimientos del MVP.


Aplicación desplegada en Render: https://mvp-sistema-recomendacion.onrender.com


Funciones en la APP:
cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español y devuelve la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.

cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.

score_titulo( titulo_de_la_pelicula ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.

votos_titulo( titulo_de_la_pelicula ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. En caso de que la película cuente con menos de 2000 valoración, regresa un texto que informa que la película no cumple con ese requisito.


get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas en las que participó y el promedio de ROI de esas películas.

get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, ROI individual, costo y ganancia de la misma.


Recomendacion(titulo_de_la_pelicula): Se ingresa el título de una película contenida dentro de la base de datos, y el algoritmo hace una recomendación de otras 5.

## Autora del Proyecto: Julia Gastellu

juliacgastellu@gmail.com

https://www.linkedin.com/in/julia-gastellu/

<h2 align="left">Tecnologías utilizadas en este proyecto:</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" alt="pandas logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="40" alt="fastapi logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="40" alt="github logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="git logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original.svg" height="40" alt="vscode logo"  />
</div>

###

<p align="left"></p>

###
