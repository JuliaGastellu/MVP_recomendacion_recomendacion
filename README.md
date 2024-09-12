<h1 align="left">MVP API y sistema de recomendación de películas</h1>

###

<p align="left">Descripción General<br>Este proyecto tiene como objetivo desarrollar un sistema de recomendación de películas personalizado, utilizando técnicas de aprendizaje automático. El sistema se basa en un conjunto de datos de películas y calificaciones de usuarios, y emplea un proceso de ETL (Extracción, Transformación y Carga) para preparar los datos para el análisis.<br><br>Estructura del Proyecto<br>data: Contiene los datos crudos y procesados.<br>notebooks: Jupyter Notebooks con el código para cada etapa del proyecto:<br>ETL: Limpieza, transformación y carga de los datos en un formato adecuado para el análisis.<br>EDA: Análisis exploratorio de datos para comprender las características de los datos y encontrar patrones.<br>modelado: Desarrollo y entrenamiento de los modelos de recomendación.<br>MAIN: Código para crear una API RESTful para consultar las recomendaciones.<br>models: Guarda los modelos entrenados.<br>requirements.txt: Lista de las dependencias del proyecto.<br><br>Proceso<br>ETL:<br><br>Extracción: A partir de archivos .csv proporcionados para los fines de este proyecto.<br>Transformación: Limpiar los datos, desanidar columnas y manejar valores faltantes, normalizar los datos y crear características relevantes (e.g., géneros, actores, directores).<br>Carga: Cargar los datos en un formato adecuado para el análisis en formato parquet.<br><br>EDA:<br><br>Análisis exploratorio: Visualizar la distribución de las calificaciones, la popularidad de las películas, la relación entre géneros y calificaciones, popularidad o el ROI, lo mismo en relación a los lenguajes en que fueron creadas y lanzadas al mercado, la distribución de estrenos a lo largo del tiempo.<br>Ingeniería de características: Crear nuevas características que puedan mejorar el rendimiento del modelo (ecomo interacciones entre usuarios y películas).<br><br>Modelado:<br><br>Selección del modelo: Se optó por hacer un filtrado basado en contenido, para lo que se utilizó un modelo basado en la similitud del coseno.<br>Entrenamiento: Entrenar el modelo utilizando los datos procesados.<br>Evaluación: Evaluar el rendimiento del modelo utilizando métricas apropiadas (Recall y RMSE).<br><br>API:<br><br>Desarrollo: Crear una API RESTful utilizando FastAPI para exponer las funcionalidades del modelo de recomendación.<br>Endpoints: Los endpoints para la API estaban predefinidos dentro de los requerimientos del MVP.<br><br>Tecnologías Utilizadas<br>Python: Lenguaje de programación principal.<br>Pandas: Manipulación y análisis de datos.<br>NumPy: Operaciones numéricas.<br>Scikit-learn: Modelado de machine learning.<br>FastAPI: Para crear la API RESTful<br><br>Cómo Ejecutar el Proyecto<br><br>Clonar el repositorio.<br>Crear un entorno virtual y activarlo.<br>Instalar las dependencias utilizando pip install -r requirements.txt.<br>Ejecutar los Jupyter Notebooks en el orden indicado.<br>Iniciar el servidor de la API.<br><br>Próximos Pasos<br><br>Mejora del modelo: Experimentar con diferentes algoritmos y hiperparámetros para mejorar el rendimiento.<br><br>Personalización: Incorporar características adicionales para personalizar las recomendaciones (e.g., historial de visualización, género preferido).<br>Despliegue: Desplegar el modelo en una plataforma en la nube para que sea accesible a los usuarios.</p>

###

<h2 align="left"></h2>

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
