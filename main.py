import uvicorn
from fastapi import FastAPI, HTTPException, Depends
import os
import pandas as pd
from fastapi.responses import HTMLResponse
from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
    
    
df_peliculas = pd.read_parquet("proyecto/data/info_peliculas.parquet")
df_reparto = pd.read_parquet("proyecto/data/reparto.parquet")
df_equipo = pd.read_parquet("proyecto/data/equipo_produccion.parquet")
        

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
        
#5 Ruta para obtener información de un director
@app.get("/nombre_e_info_director/{nombre_actor}", name="Información de actor")
async def nombre_e_info_actor(nombre_actor: str):
    """
    Se ingresa el nombre de un actor, por ejemplo "Jack Black"
    """

    actor_data = df_reparto[df_reparto['name'].str.contains(nombre_actor, case=False, na=False)]
   

    if actor_data.empty:
        raise HTTPException(status_code=404, detail="Actor/actriz no encontrado.")



    return {
        "Actor/actriz": nombre_actor}



#6 Ruta para obtener información de un director
@app.get("/nombre_e_info_director/{nombre_director}", name="Información de director")
async def nombre_e_info_director(nombre_director: str):
    """
    Se ingresa el nombre de un director, por ejemplo "Quentin Tarantino"
    """

    director_data = df_equipo[df_equipo['name'].str.contains(nombre_director, case=False, na=False)]
   

    if director_data.empty:
        raise HTTPException(status_code=404, detail="Director/a no encontrado.")



    return {
        "Director/a": nombre_director}




