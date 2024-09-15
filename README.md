<h1 align="left">MVP API y sistema de recomendación de películas</h1>

###

<p align="left">MVP API y sistema de recomendación de películas<br>Descripción General<br>Este proyecto tiene como objetivo desarrollar un sistema de recomendación de películas personalizado, utilizando técnicas de aprendizaje automático. El sistema se basa en un conjunto de datos de películas y calificaciones de usuarios, y emplea un proceso de ETL (Extracción, Transformación y Carga) para preparar los datos para el análisis.<br><br>Estructura del Proyecto<br><br><br>data: Contiene los datos preprocesados y procesados.<br>notebooks: Jupyter Notebooks con el código para cada etapa del proyecto:<br>ETL_PI01: Limpieza, transformación y carga de los datos en un formato adecuado para el análisis.<br>EDA_PI01: Análisis exploratorio de datos para comprender las características de los datos y encontrar patrones.<br>ML_modelo: Desarrollo y entrenamiento de los modelos de recomendación.<br>MAIN: Código para crear una API RESTful para hacer consultas a los datos y solicitar las recomendaciones.<br>requirements.txt: Lista de las dependencias del proyecto.<br><br>Proceso<br><br>ETL:<br><br>Extracción: A partir de archivos .csv proporcionados para los fines de este proyecto.<br>Transformación: Limpiar los datos, desanidar columnas y manejar valores faltantes, normalizar los datos y crear características relevantes (ej., géneros, actores, directores).<br>Carga: Cargar los datos en un formato adecuado para el análisis en formato parquet.<br><br>EDA:<br><br>Análisis exploratorio: Visualizar la distribución de las calificaciones, la popularidad de las películas, la relación entre géneros y calificaciones, popularidad o el ROI, lo mismo en relación a los lenguajes en que fueron creadas y lanzadas al mercado, la distribución de estrenos a lo largo del tiempo.<br>Ingeniería de características: Se analizó la cantidad de palabras contenidas en una nube de palabras utilizando las sinopsis (overviews) correspondientes a las películas que tenían un promedio de votación de usuarios mayor a 7 .<br><br>Modelado:<br><br>Selección del modelo: Se optó por hacer un filtrado basado en contenido, para lo que se utilizó un modelo basado en la similitud del coseno.<br><br>API:<br><br>Desarrollo: Crear una API RESTful utilizando FastAPI para exponer las funcionalidades del modelo de recomendación.<br>Endpoints: Los endpoints para la API estaban predefinidos dentro de los requerimientos del MVP.<br><br>Tecnologías Utilizadas<br>Python: Lenguaje de programación principal.<br>Pandas: Manipulación y análisis de datos.<br>NumPy: Operaciones numéricas.  <br>Scikit-learn: Modelado de machine learning.<br>FastAPI: Para crear la API RESTful<br>Render: para desplegar la aplicación.<br><br>Cómo Ejecutar el Proyecto<br><br>Clonar el repositorio.<br>Crear un entorno virtual y activarlo.<br>Instalar las dependencias utilizando pip install -r requirements.txt.<br>Ejecutar los Jupyter Notebooks en el orden indicado.<br>Iniciar el servidor de la API.</p>

###

<h2 align="left">API:<br><br>Aplicación desplegada en Render: <br>https://mvp-sistema-recomendacion.onrender.com<br><br><br>Funciones en la APP:<br>cantidad_filmaciones_mes( Mes ): Se ingresa un mes en idioma Español y devuelve la cantidad de películas que fueron estrenadas en el mes consultado en la totalidad del dataset.<br>         <br>cantidad_filmaciones_dia( Dia ): Se ingresa un día en idioma Español. Debe devolver la   cantidad de películas que fueron estrenadas en día consultado en la totalidad del dataset.<br>                   <br>score_titulo( titulo_de_la_pelicula ): Se ingresa el título de una filmación esperando como respuesta el título, el año de estreno y el score.<br>                   <br>votos_titulo( titulo_de_la_pelicula ): Se ingresa el título de una filmación esperando como respuesta el título, la cantidad de votos y el valor promedio de las votaciones. En caso de que la película cuente con menos de 2000 valoración, regresa un texto que informa que la película no cumple con ese requisito.<br><br><br>get_actor( nombre_actor ): Se ingresa el nombre de un actor que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, la cantidad de películas en las que participó y el promedio de ROI de esas películas.<br>                   <br>get_director( nombre_director ): Se ingresa el nombre de un director que se encuentre dentro de un dataset debiendo devolver el éxito del mismo medido a través del retorno. Además, deberá devolver el nombre de cada película con la fecha de lanzamiento, ROI individual, costo y ganancia de la misma.<br><br><br>Recomendacion(titulo_de_la_pelicula): Se ingresa el título de una película contenida dentro de la base de datos, y el algoritmo hace una recomendación de otras 5.</h2>

###

<p align="left"></p>

###

<h2 align="left">Proyecto creado con:</h2>

###

<div align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" height="40" alt="python logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" height="40" alt="pandas logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/visualstudio/visualstudio-plain.svg" height="40" alt="visualstudio logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/git/git-original.svg" height="40" alt="git logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" height="40" alt="github logo"  />
  <img width="12" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/fastapi/fastapi-original.svg" height="40" alt="fastapi logo"  />
</div>

###

<br clear="both">

<div align="center">
  <img height="" src=""  />
</div>

###
