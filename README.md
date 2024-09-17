
# MVP API y sistema de recomendación de películas

Descripción General

Este proyecto es parte de una instancia evaluativa que tiene como objetivo desarrollar un MVP basado en una FastApi de consulta, que incluye endpoints para consultar datos específicos de una base de datos de películas y un sistema de recomendación de películas personalizado, utilizando técnicas de aprendizaje automático. 

Estructura del Proyecto

data: Contiene los datos preprocesados y procesados, en formato parquet.

notebooks (Jupyter Notebooks con el código para cada etapa del proyecto):

ETL_PI01.ipynb: Limpieza, transformación y carga de los datos en un formato adecuado para el análisis.
EDA_PI01.ipynb: Análisis exploratorio de datos para comprender las características de los datos y encontrar patrones.
ML_modelo.ipynb: Desarrollo y entrenamiento de los modelos de recomendación.

main.py: Código para crear fastapi para hacer consultas a los datos y solicitar las recomendaciones.

requirements.txt: Lista de las dependencias del proyecto.

Proceso

ETL:

En esta instancia hice el desanidado de las columnas y las transformaciones que se habían propuesto en la consigna, además de desanidar las columnas necesarias en el dataset de credits, hice transformaciones necesarias de datos y eliminé algunas columnas que me resultaban irrelevantes, dejando un solo dataset preliminar concatenando lo que me interesaba de cada uno de los dos archivos csv originales aportados para el proyecto.  

EDA:

En el EDA (Análisis exploratorio de datos) comencé inspeccionando los atributos básicos de mi dataset (un dataframe producto de las transformaciones hechas anteriormente en el proceso de ETL incluido en este proyecto) tales como información, tipos de datos, cantidad de valores nulos por columna.
Decidí eliminar las películas cuyo runtime fuera menor a 50 minutos y mayor a 330 (ya que la columna contenía outliers de duración correspondientes a miniseries y mi sistema de recomendación está basado en películas únicamente).
Hice un conteo de géneros y los grafiqué para verificar todos los contenidos y su distribución.
Hice lo mismo con los idiomas originales de las películas decidiendo quedarme con los 10 más frecuentes. 
Calculé algunas correlaciones pero fueron descartadas por no encontrar nada significativo.
Luego corregí algunos valores que habían quedado como infinitos dentro del cálculo de return (ROI) y que no resutaban significativos de todas maneras. 
Decidí eliminar todas las películas estrenadas antes de 1980 por considerar que no tenía sentido incluir en el análisis la valoración de éstas películas por una cuestión generacional, aunque también tomé la decisión para hacer un recorte que me permitiera subsanar las limitaciones técnicas con las que tuve que lidiar, sobretodo con la capa gratuita de Render.
Eliminé también todas las películas que tuvieran un status diferente a "Released" (es decir, efectivamente estrenadas).
Incluí en mi análisis una nube de palabras que me mostrara las palabras más frecuentes en las Overviews de aquellas películas que tenían un promedio de votación de 7 o más, que son las que consideré que pertenecían a la categoría con mayor aceptación por parte del público. 
Finalicé con la eliminación de las columnas que me parecieron irrelevantes para incluir dentro de mi modelo de recomendación, hice un mapa de calor para verificar las correlaciones del dataframe transformado y lo exporté en formato parquet.



Modelo de Recomendación:

Mi función de recomendación está basada en calcular la similitud del coseno correspondiente a los atributos categóricos tales como el género de las películas y las palabras contenidas en las overviews, y sus títulos, previamente tokenizadas, y devuelve 5 películas "recomendadas" por su similitud en relación a esos atributos.





## API

Desarrollo: Crear una API RESTful utilizando FastAPI para exponer las funcionalidades del modelo de recomendación.
Endpoints: Los endpoints para la API estaban predefinidos dentro de los requerimientos del MVP.


Aplicación desplegada en Render: https://mvp-sistema-recomendacion.onrender.com/docs


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


<h2 align="left">Tecnologías utilizadas:</h2>

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
