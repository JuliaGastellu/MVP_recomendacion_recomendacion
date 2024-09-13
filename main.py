import uvicorn
from fastapi import FastAPI, HTTPException, Depends
import os
import pandas as pd
from fastapi.responses import HTMLResponse
from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import unicodedata


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
    
df_peliculas = pd.read_parquet("proyecto/data/info_peliculas.parquet")
df_reparto = pd.read_parquet("proyecto/data/data_actor.parquet")
df_equipo = pd.read_parquet("proyecto/data/data_director.parquet")
        

#Instancio la clase 
app = FastAPI(
    title="API de Películas",
    description="Realiza consultas sobre tu película favorita.",
    docs_url="/docs"
)

# Obtener configuraciones desde variables de entorno
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
PORT = int(os.getenv("PORT", 8000))

def get_data_manager():
    return DataManager()

# Función para obtener la cantidad de películas en un mes
@app.get('/cantidad_filmaciones_mes/{mes}')
def cantidad_filmaciones_mes(mes: str):
    meses = {
        'enero': 1, 'febrero': 2, 'marzo': 3, 'abril': 4,
        'mayo': 5, 'junio': 6, 'julio': 7, 'agosto': 8,
        'septiembre': 9, 'octubre': 10, 'noviembre': 11, 'diciembre': 12
    }
    mes = mes.lower()
    if mes in meses:
        mes_numero = meses[mes]
        df_peliculas['release_date'] = pd.to_datetime(df_peliculas['release_date'], errors='coerce')
        count = df_peliculas[df_peliculas['release_date'].dt.month == mes_numero].shape[0]
        return {"mensaje": f"{count} cantidad de películas fueron estrenadas en el mes de {mes.capitalize()}"}
    else:
        return {"mensaje": "Mes inválido"}
    # Filtrar el DataFrame y contar las películas
    cantidad = df_peliculas[df_peliculas['release_date'].dt.month == num_mes].shape[0]

    return f"En el mes de {mes} se estrenaron {cantidad} películas"


@app.get('/cantidad_filmaciones_dia_semana/{dia_semana}')
def cantidad_filmaciones_dia_semana(dia_semana: str):
    """
    Obtiene la cantidad de películas estrenadas en un día de la semana específico """

    dias_semana = {
        'lunes': 0, 'martes': 1, 'miércoles': 2, 'jueves': 3,
        'viernes': 4, 'sábado': 5, 'domingo': 6
    }
    dia_semana = dia_semana.lower()

    if dia_semana in dias_semana:
        dia_numero = dias_semana[dia_semana]
        df_peliculas['release_date'] = pd.to_datetime(df_peliculas['release_date'], errors='coerce')
        count = df_peliculas[df_peliculas['release_date'].dt.dayofweek == dia_numero].shape[0]
        return {"mensaje": f"{count} películas se estrenaron los {dia_semana.capitalize()}."}
    else:
        return {"mensaje": "Día de la semana inválido."}

#3 Ruta de score por título
@app.get("/score_titulo/{titulo}", name="Score por título de película")
async def score_titulo(titulo: str):
    '''Se ingresa el título de una película, por ejemplo "Titanic", y se retorna el título, el año de estreno y el score.'''
    pelicula = df_peliculas[df_peliculas['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado.")
    resultado = pelicula[['title', 'release_year', 'vote_average']].to_dict(orient='records')[0]
    return {"Título de la película": resultado['title'], "Año": resultado['release_year'], "Puntaje": resultado['vote_average']}

#4 Ruta de votos por título
@app.get("/votos_titulo/{titulo}", name="Votos por título de película")
async def votos_titulo(titulo: str):
    '''Se ingresa el título de una película, por ejemplo "The Terminator", y se retorna el título, la cantidad de votos y el promedio de votaciones.'''
    pelicula = df_peliculas[df_peliculas['title'].str.contains(titulo, case=False, na=False)]
    if pelicula.empty:
        raise HTTPException(status_code=404, detail="Título no encontrado.")
    else:
        year_es = int(pelicula["release_year"].iloc[0])
        voto_tot = int(pelicula["vote_count"].iloc[0])
        voto_prom = pelicula["vote_average"].iloc[0]
        # Retornar el nombre del titulo ubicado en la columna title
        titulo = pelicula["title"].iloc[0]
        if voto_tot >= 2000:
            # muestra los datos
            return {
                'Título de la película': titulo, 
                 'Año': year_es, 
                 'Voto total': voto_tot, 
                 'Voto promedio': voto_prom
            }
        else:
            # En caso de que la cantidad de votos sea menor a 2000
            return f"La película {titulo} no cumple con la condición de tener al menos 2000 valoraciones"
        


#5 Ruta para obtener información de un actor

@app.get("/get_actor/{nombre_actor}", name="Información de actor")
async def get_actor(nombre_actor: str):
    '''Se ingresa el nombre de un actor, por ejemplo "Joe Roberts" y se retorna su éxito medido a través del retorno, cantidad de películas y promedio de retorno.'''

    
    actor = df_reparto[df_reparto['name'] == nombre_actor]

    if actor.empty:
        raise HTTPException(status_code=404, detail="Actor no encontrado.")

    # Calcular métricas solo para el actor encontrado
    total_retorno = actor['return'].sum()
    cantidad_peliculas = actor.shape[0]
    promedio_retorno = actor['return'].mean()

    return {
        "Actor/Actriz": nombre_actor,
        "Cantidad de películas": cantidad_peliculas,
        "Retorno Total": total_retorno,
        "Retorno Promedio": promedio_retorno
    }

#6 Ruta para obtener información de un director

import unicodedata
import pandas as pd

@app.get("/get_director/{nombre_director}", name="Información de director")
async def get_director(nombre_director: str):
    """Se ingresa el nombre de un director y se retorna su éxito medido a través del retorno, nombre de cada película, fecha de lanzamiento, retorno individual, costo y ganancia."""

    # Normalizar ambos nombres a una forma canónica
    def normalize_name(name):
        if pd.isna(name):
            return None  # Manejar valores nulos
        return unicodedata.normalize('NFKD', name).encode('ascii', 'ignore').decode('utf-8').lower()

    nombre_director_normalizado = normalize_name(nombre_director)

    try:
        # Filtrar y eliminar duplicados, manejando posibles errores
        director = df_equipo[df_equipo['name'].apply(normalize_name) == nombre_director_normalizado]
        director = director.dropna(subset=['name', 'title']).drop_duplicates(subset=['name', 'title'])

        if director.empty:
            raise HTTPException(status_code=404, detail="Director no encontrado.")

        # Crear una lista con la información de cada película
        resultados = []
        for _, row in director.iterrows():
            resultados.append({
                "Título de la película": row['title'],
                "Fecha de lanzamiento": row['release_date'],
                "Retorno": row['return'],
                "Presupuesto": row['budget'],
                "Ganancia": row['revenue']
            })

        # Calcular el retorno total
        total_retorno = director['return'].sum()

        # Retornar la información
        return {
            "Director": nombre_director,
            "Retorno Total": total_retorno,
            "Películas": resultados
        }
    except Exception as e:
        # Capturar todas las excepciones para un manejo más general
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")
   

